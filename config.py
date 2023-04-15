import json

ERC20_ABI_PATH = './abi/erc20.json'
ACTIONS_PATH = './actions.json'

with open(ERC20_ABI_PATH, 'r') as file:
    ERC20_ABI = json.load(file)

with open(ACTIONS_PATH, 'r') as f:
    ACTIONS = json.load(f)

RPCS = [
    {
        'chain': 'ETH',
        'chain_id': 1,
        'rpc': 'https://rpc.ankr.com/eth',
        'scan': 'https://etherscan.io/tx',
        'token': 'ETH'
    },
    {
        'chain': 'OPTIMISM',
        'chain_id': 10,
        'rpc': 'https://rpc.ankr.com/optimism',
        'scan': 'https://optimistic.etherscan.io/tx',
        'token': 'ETH'
    },
    {
        'chain': 'BNB',
        'chain_id': 56,
        'rpc': 'https://bsc-dataseed.binance.org',
        'scan': 'https://bscscan.com/tx',
        'token': 'BNB'
    },
    {
        'chain': 'MATIC',
        'chain_id': 137,
        'rpc': 'https://polygon-rpc.com',
        'scan': 'https://polygonscan.com/tx',
        'token': 'MATIC'
    },
    {
        'chain': 'ARBITRUM',
        'chain_id': 42161,
        'rpc': 'https://arb1.arbitrum.io/rpc',
        'scan': 'https://arbiscan.io/tx',
        'token': 'ETH'
    },
    {
        'chain': 'AVAXC',
        'chain_id': 43114,
        'rpc': 'https://api.avax.network/ext/bc/C/rpc',
        'scan': 'https://snowtrace.io/tx',
        'token': 'AVAX'
    },
    {
        'chain': 'NOVA',
        'chain_id': 42170,
        'rpc': 'https://nova.arbitrum.io/rpc',
        'scan': 'https://nova.arbiscan.io/tx',
        'token': 'ETH'
    },
    {
        'chain': 'FTM',
        'chain_id': 250,
        'rpc': 'https://rpc.ankr.com/fantom',
        'scan': 'https://ftmscan.com/tx',
        'token': 'FTM'
    },
]

ORBITER_AMOUNT = {
    'ETH': 0.009001,
    'BNB': 0.009015,
    'NOVA': 0.009016,
    'MATIC': 0.009006,
    'ZKSYNC': 0.009003,
    'ARBITRUM': 0.009002,
    'OPTIMISM': 0.009007,
    'STARKNET': 0.009004,
}


