import time
import random
from src.core.bridges import orbiter_bridge

def bridge_orbiter_handler(data):
    # ETH | OPTIMISM | BNB | MATIC | FTM | ARBITRUM | NOVA | AVAXC
    # AMOUNT_TO_BRIDGE = 'all_balance'
    # AMOUNT_TO_BRIDGE = 10
    private_keys = []
    min_sleep = data['min_sleep']
    max_sleep = data['max_sleep']
    MIN_BALANCE = 0  # останется токенов на балансе после бриджа

    with open(data['private_keys_path'], 'r') as file:
        for line in file.readlines():
            private_keys.append(line.strip())

    print(f'private_keys: {private_keys}')

    for private_key in private_keys:
        print(f"private_key: {private_key}")
        print(f"from_chain: {data['from_chain']}")
        print(f"to_chain: {data['to_chain']}")
        print(f"amount: {data['amount']}")
        print(f"token: {data['token']}")
        print(f"token_contract: {data['token_contract']}")
        print(f"bridge_contract: {data['bridge_contract']}")
        print(f"MIN_BALANCE: {MIN_BALANCE}")

        orbiter_bridge(
            private_key,
            data['from_chain'],
            data['to_chain'],
            data['amount'],
            data['token'],
            data['token_contract'],
            data['bridge_contract'],
            MIN_BALANCE
        )

        seconds = random.randint(int(min_sleep), int(max_sleep))
        time.sleep(seconds)