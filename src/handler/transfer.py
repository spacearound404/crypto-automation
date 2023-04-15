import time
import random
from src.core.transfer import transfer
from src.core import utils

def transfer_tokens_handler(data):
    # ETH | OPTIMISM | BNB | MATIC | FTM | ARBITRUM | NOVA | AVAXC
    addresses = []
    pk_amnt_addr_list = []
    min_sleep = data['min_sleep']
    max_sleep = data['max_sleep']
    total_amount = data['amount']
    ADDRESS_CONTRACT = ''  # пусто если eth
    # AMOUNT_TO_TRANSFER = 'all_balance'

    with open(data['addresses_path'], 'r') as file:
        for line in file.readlines():
            addresses.append(line.strip())

    with open(data['private_keys_amount_path'], 'r') as file:
        for line in file.readlines():
            pk, amount = line.strip().split(' ')
            pk_amnt_addr_list.append({
                'pk': pk,
                'amnt': float(amount),
                'addr': ''
            })

    for i, address in enumerate(addresses):
        pk_amnt_addr_list[i]['addr'] = address

    for pk_amnt_addr in pk_amnt_addr_list:
        pk = pk_amnt_addr['pk']
        amount = pk_amnt_addr['amnt']
        to_address = pk_amnt_addr['addr']

        print(f"private_key: {pk}")
        print(f"token: {data['token']}")
        print(f"to_address: {to_address}")
        print(f"network: {data['network']}")
        print(f"amount: {float(amount)}")
        print(f"token_contract: {data['token_contract']}")

        transfer(
            pk,
            data['token'],
            to_address,
            data['network'],
            amount,
            data['token_contract']
        )

        seconds = random.randint(int(min_sleep), int(max_sleep))
        print(f'seconds: {seconds}\n')
        time.sleep(seconds)