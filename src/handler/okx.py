import time
import random
from src.core import utils
from src.core.okx import okx_withdraw


def okx_handler(data):
    # ETH | BSC | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT
    addresses = []
    total_amount = data['amount']
    min_amount = data['min_amount']
    max_amount = data['max_amount']
    min_fee = data['min_fee']
    max_fee = data['max_fee']
    min_sleep = data['min_sleep']
    max_sleep = data['max_sleep']

    with open(data['addresses_path'], 'r') as file:
        for line in file.readlines():
            addresses.append(line.strip())

    print(f'addresses: {addresses}')

    address_amount_mapping = utils.distribute_funds(addresses, total_amount, min_amount, max_amount)

    print(f'address_amount_mapping: {address_amount_mapping}')

    for address, amount in address_amount_mapping.items():
        fee = random.randint(int(min_fee), int(max_fee))
        seconds = random.randint(int(min_sleep), int(max_sleep))

        print(f'address: {address}')
        print(f'fee: {fee}')
        print(f'seconds: {seconds}')
        print(f"token: {data['token']}")
        print(f"network: {data['network']}")
        print(f"api_key: {data['api_key']}")
        print(f"secret: {data['secret']}")
        print(f"password: {data['password']}")
        print(f"proxies: {data['proxies']}")

        okx_withdraw(
            address,
            amount,
            fee,
            data['token'],
            data['network'],
            data['api_key'],
            data['secret'],
            data['password'],
            data['proxies']
        )

        time.sleep(seconds)