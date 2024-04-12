liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
path=[]
r = 0.997




def change_1(graph, earn, liquidity, t1, t2):
    q1, q2 = liquidity[(t1, t2)]
    q1_ = q1 + earn
    q2_ = q1 * q2 / q1_
    liquidity[(t1, t2)] = (q1_, q2_)
    liquidity[(t2, t1)] = (q2_, q1_)
    earn = q2_ - q2
    return earn

def change_3(graph, earn, base_Token, t1, t2):
    earn = change_1(graph, earn, liquidity, base_Token, t1)
    earn = change_1(graph, earn, liquidity, t1, t2)
    earn = change_1(graph, earn, liquidity, t2, base_Token)
    return earn

def check_if_arbitrage(graph, tokens, base_index, fee, path):
    for i in range(len(graph)):
        if base_index == i:
            continue
        for j in range(len(graph[i])):
            if base_index == j:
                continue
            print(f"graph[{i}][{j}]: {graph[i][j]}")  # Add this line
            r = fee
            R0 = graph[base_index][i][0]
            R1 = graph[base_index][i][1]
            R1_ = graph[i][j][0]
            R2 = graph[i][j][1]
            R2_ = graph[j][base_index][0]
            R0_ = graph[j][base_index][1]
            E0 = R0 * R1_ / (R1_ + R1 * r)
            E1 = r * R1 * R2 / (R1_ + R1 * r)
            Eb = E0 * R2_ / (E1 + R2_)
            Ea = E1 * R0_ / (E1 + R2_)
            delta = ((Eb * Ea * r) ** 0.5 - Eb) / r
            if Ea > Eb:
                return (i, j, delta)
    return -1

base_index = 0
def Arbitrage(graph,fee):
    earn_all = 5
    while earn_all < 20:
        result = check_if_arbitrage(graph, tokens, base_index, fee, path)
        if result == -1:
            print("fail")
            return earn_all, path
        else:
            t1, t2, earn = result
        path.append([t1, t2, earn]) 
        amount = min(earn_all, earn_all)
        earn_all -= amount
        amount = change_3(liquidity, amount, base_index, t1, t2)
        earn_all += amount
    return earn_all, path









def get_reserves_from_pool(liquidity, _in, _out):
    if (_in, _out) in liquidity:
        reserve_in, reserve_out = liquidity[(_in, _out)]
    else:
        reserve_out, reserve_in = liquidity[(_out, _in)]  
    
    return reserve_in, reserve_out




def find_cycles_recursive(liquidity,current_token, path, cycles):
    if len(path) > 2:
        pathB=path+["tokenB"]
        amount_in = 5
        total_out = get_total_out(liquidity, amount_in, pathB)
        final_amount = total_out[-1]
        if final_amount > 20:
            cycles.append((pathB, final_amount))

    for token in tokens:
        if token not in path and ((current_token, token) in liquidity or (token, current_token) in liquidity):
            new_path = path + [token]
            find_cycles_recursive( liquidity,token, new_path, cycles)
def get_total_out(liquidity, amount_in, path):
    if len(path) < 2:
        raise ValueError('Invalid path: Path should contain at least two tokens')

    total = [0] * len(path)
    total[0] = amount_in

    for i in range(len(path) - 1):
        reserve_in, reserve_out = get_reserves_from_pool(liquidity, path[i], path[i + 1])
        total[i + 1] = calculate_output_amount(total[i], reserve_in, reserve_out)

    return total
def calculate_output_amount(amount_in, reserve_in, reserve_out):
    amount_in_with_fee = amount_in * 1000*r 
    amount_out = (amount_in_with_fee * reserve_out) / (reserve_in * 1000 + amount_in_with_fee )
    return amount_out

def find_loop(liquidity,tokens):
    cycles = []
    for token in tokens:
        if token == "tokenB":
            path = ["tokenB"]
            find_cycles_recursive(liquidity,token, path, cycles)
    return cycles



cycles = find_loop(liquidity, tokens)

max_amount = 0
max_cycle = None
for cycle, final_amount in cycles:
    if final_amount > max_amount:
        max_amount = final_amount
        max_cycle = cycle
max_cycle_str = '->'.join(max_cycle) 
print(f"path: {max_cycle_str}, tokenB balance={max_amount:.10f}")

total_out = get_total_out(liquidity,5, max_cycle)
print(total_out)