import time
import random
from src.core.transfer import transfer
from src.core import utils

def transfer_tokens_handler(data):
    # ETH | OPTIMISM | BNB | MATIC | FTM | ARBITRUM | NOVA | AVAXC
    addresses = []
    min_amount = data['min_amount']
    max_amount = data['max_amount']
    min_sleep = data['min_sleep']
    max_sleep = data['max_sleep']
    total_amount = data['amount']
    ADDRESS_CONTRACT = ''  # пусто если eth
    # AMOUNT_TO_TRANSFER = 'all_balance'

    with open(data['addresses_path'], 'r') as file:
        for line in file.readlines():
            addresses.append(line.strip())

    address_amount_mapping = utils.distribute_funds(
        addresses,
        float(total_amount),
        float(min_amount),
        float(max_amount)
    )

    print(f'total_amount: {total_amount}')
    print(f'min_amount: {min_amount}')
    print(f'max_amount: {max_amount}')
    print(f'addresses: {addresses}')
    print(f'address_amount_mapping: {address_amount_mapping}')

    for address, amount in address_amount_mapping.items():
        print(f'address: {address}')
        print(f'amount: {amount}')

        print(f"private_key: {data['private_key']}")
        print(f"token: {data['token']}")
        print(f"address: {address}")
        print(f"network: {data['network']}")
        print(f"amount: {float(amount)}")
        print(f"token_contract: {data['token_contract']}")

        transfer(
            data['private_key'],
            data['token'],
            address,
            data['network'],
            float(amount),
            data['token_contract']
        )

        seconds = random.randint(int(min_sleep), int(max_sleep))
        print(f'seconds: {seconds}\n')
        time.sleep(seconds)