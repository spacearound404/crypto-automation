import re
import time
import json
import random
import math
import decimal
from config import *
from web3 import Web3
from tqdm import tqdm
from src.core import utils
from termcolor import cprint


def bridge(private_key, token, amount, amount_to_chain, token_contract, bridge_contract, rpc_chain, chain_id, scan):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_chain))
        account = web3.eth.account.from_key(private_key)
        address_wallet = account.address

        nonce = web3.eth.get_transaction_count(address_wallet)

        token_contract = web3.eth.contract(
            address=Web3.to_checksum_address(token_contract),
            abi=utils.get_abi(token)
        )

        print(f'amount_to_chain: {amount_to_chain}')

        if '%' in str(amount):
            percentage = float(re.findall(r'\b\d+(?:,\d+)?(?:\.\d+)?\b', amount.replace(',', '.'))[0])
            print(f'percentage: {percentage}')
            token_amount = token_contract.functions.balanceOf(address_wallet).call() / pow(10, 6)
            print(f'wallet balance: {token_amount}')
            amount = token_amount * (percentage / 100)
            amount = "{:.2f}".format(amount)
            amount = float(amount)
            print(f'amount without code: {amount}')

        amount = round(decimal.Decimal(amount) + decimal.Decimal(amount_to_chain), 6)

        amount = int(amount * pow(10, 6))

        print(f'withdraw amount with code: {amount}')
        print(f'address_wallet: {address_wallet}\n')

        tx_hash = token_contract\
            .functions\
            .transfer(Web3.to_checksum_address(bridge_contract), amount)\
            .build_transaction({
                'chainId': chain_id,
                'from': address_wallet,
                'nonce': nonce,
                'value': 0,
                'gasPrice': web3.eth.gas_price
            })

        signed_txn = web3.eth.account.sign_transaction(tx_hash, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> bridge | {scan}/{web3.to_hex(tx_hash)}', 'green')
    except Exception as error:
        cprint(f'\n>>> bridge | {error}', 'red')

def orbiter_bridge(private_key, from_chain, to_chain, amount_to_bridge, token, token_contract, bridge_contract, MIN_BALANCE):

    cprint(f'\nstart : orbiter bridge {from_chain} => {to_chain}', 'yellow')

    amount_to_chain = ORBITER_AMOUNT[to_chain]

    data = utils.check_rpc(from_chain)
    rpc_chain = data['rpc']
    chain_id = data['chain_id']
    scan = data['scan']

    print(f'amount_to_chain: {amount_to_chain}')
    print(f'rpc_chain: {rpc_chain}')
    print(f'chain_id: {chain_id}')
    print(f'scan: {scan}')

    bridge(private_key, token, amount_to_bridge, amount_to_chain,  token_contract, bridge_contract, rpc_chain, chain_id, scan)