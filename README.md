# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.1298889441
5, 5.655321988655322, 2.4587813170979333, 5.088927293301516, 20.12988894407745

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual executed price due to market volatility or trade size. It's a common issue in decentralized exchanges where liquidity is provided by liquidity providers rather than traditional order books.

Uniswap V2 addresses the slippage issue through a mechanism called the constant product market maker model(x*y = k). In this model, trades are executed based on a constant product formula, where the product of the quantities of two tokens in a liquidity pool remains constant. This means that as one token is bought, the quantity of the other token in the pool adjusts to maintain the product.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
The UniswapV2Pair contract imposes a minimum liquidity requirement during initial liquidity minting to prevent users from exploiting the system by minting LP tokens with minimal liquidity contributions. This ensures that LP tokens are only issued in exchange for meaningful liquidity contributions, safeguarding the stability and integrity of the liquidity pool and protecting the interests of existing liquidity providers.
## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
The UniswapV2Pair contract utilizes a specific formula for obtaining liquidity when depositing tokens, particularly after the initial deposit. This formula ensures fairness and balance in the liquidity pool by proportionately rewarding liquidity providers based on their contributions. It also helps prevent manipulation or abuse of the system by discouraging malicious behaviors. Overall, the formula aims to maintain stability, efficiency, and integrity in Uniswap V2 liquidity pools while incentivizing participation from liquidity providers.
## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack is a form of market manipulation in decentralized exchanges where an attacker exploits the predictable price impact of large trades to profit. They do this by front-running transactions and strategically placing their own trades to capitalize on the price movement caused by the target transaction. As an initiator of a swap, you might unwittingly fall victim to such attacks, resulting in receiving less of the desired token than expected or paying a higher price for it. To mitigate this risk, users can use limit orders, monitor trading activity, and choose exchanges with built-in protections.






