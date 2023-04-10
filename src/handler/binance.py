import time
import random
from src.core import const
from src.core import utils
from src.core.binance import binance_withdraw

def binance_handler(data):
    # ETH | BSC | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT
    addresses = []
    total_amount = data['amount']
    min_amount = data['min_amount']
    max_amount = data['max_amount']
    min_sleep = data['min_sleep']
    max_sleep = data['max_sleep']

    with open(data['addresses_path'], 'r') as file:
        for line in file.readlines():
            addresses.append(line.strip())

    address_amount_mapping = utils.distribute_funds(addresses, float(total_amount), float(min_amount), float(max_amount))

    print(f'addresses: {addresses}')
    print(f'address_amount_mapping: {address_amount_mapping}')

    for address, amount in address_amount_mapping.items():
        print(f"address: {address}")
        print(f"amount: {amount}")
        print(f"token: {data['token']}")
        print(f"network: {data['network']}")
        print(f"api_key: {data['api_key']}")
        print(f"secret: {data['secret']}")

        binance_withdraw(
            address,
            amount,
            data['token'],
            data['network'],
            data['api_key'],
            data['secret']
        )

        seconds = random.randint(int(min_sleep), int(max_sleep))
        time.sleep(seconds)