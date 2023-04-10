import time
import json
import random
import decimal
import requests
from config import *
from web3 import Web3
from tqdm import tqdm
from decimal import Decimal
from src.core import utils
from termcolor import cprint
from tabulate import tabulate


table = []

def transfer_token(private_key, token, amount_to_transfer, to_address, chain_id, scan, rpc_chain, address_contract):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_chain))

        token_contract = web3.eth.contract(
            address=Web3.to_checksum_address(address_contract),
            abi=utils.get_abi(token)
        )
        account = web3.eth.account.from_key(private_key)
        address = account.address
        print(f'from address: {address}')
        print(f'to address: {to_address}')

        nonce = web3.eth.get_transaction_count(address)

        amount = round(decimal.Decimal(amount_to_transfer), 6)
        amount = int(amount * pow(10, 6))

        print(f'amount to withdraw: {amount}')

        gasLimit = web3.eth.estimate_gas({
            'to': Web3.to_checksum_address(address),
            'from': Web3.to_checksum_address(to_address),
            'value': 0
        })
        gasPrice = web3.eth.gas_price

        print(f'gasLimit: {gasLimit}')
        print(f'gasPrice: {gasPrice}')

        # if chain_id == 1:
        #     contract_txn = token_contract\
        #         .functions.transfer(Web3.to_checksum_address(to_address), int(amount))\
        #         .build_transaction({
        #             'type': '0x2',
        #             'chainId': chain_id,
        #             # 'gas': gasLimit,
        #             'maxFeePerGas': random.randrange(20000000000, 25000000000, 9),
        #             # 'maxFeePerGas': web3.to_wei('25', 'gwei'),
        #             'maxPriorityFeePerGas': web3.to_wei('1.5', 'gwei'),
        #             'nonce': nonce,
        #         })
        # else:
        #     contract_txn = token_contract\
        #         .functions\
        #         .transfer(Web3.to_checksum_address(to_address), amount)\
        #         .build_transaction({
        #             'chainId': chain_id,
        #             'from': address,
        #             'gasPrice': gasPrice,
        #             'value': 0,
        #             # 'gas': gasLimit,
        #             'nonce': nonce,
        #         })
        #
        # tx_signed = web3.eth.account.sign_transaction(contract_txn, private_key)
        # tx_hash = web3.eth.send_raw_transaction(tx_signed.rawTransaction)
        #
        # print(f'tx_hash: {tx_hash}')
        #
        # cprint(f'\n>>> transfer : {decimal.Decimal(str(amount_to_transfer))} | {address} => {to_address} | {scan}/{web3.to_hex(tx_hash)}', 'green')

    except Exception as error:
        cprint(f'\n>>> transfer : {private_key} | {error}', 'red')


def transfer_eth(privatekey, amount_to_transfer, to_address, chain_id, scan, rpc_chain, symbol):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_chain))

        account = web3.eth.account.privateKeyToAccount(privatekey)
        address = account.address
        nonce = web3.eth.get_transaction_count(address)

        amount = utils.int_to_decimal(amount_to_transfer, 18)

        gasLimit = web3.eth.estimate_gas({'to': Web3.toChecksumAddress(address), 'from': Web3.toChecksumAddress(address),'value': amount}) 
        gasPrice = web3.eth.gas_price
        
        if chain_id == 1:
            contract_txn = {
                'type': '0x2',
                'chainId': chain_id,
                'gas': gasLimit,
                'maxFeePerGas': random.randrange(20000000000, 25000000000, 9), 
                # 'maxFeePerGas': web3.to_wei('25', 'gwei'),
                'maxPriorityFeePerGas': web3.to_wei('1.5', 'gwei'),
                'nonce': nonce,
                'to': Web3.toChecksumAddress(to_address),
                'value': int(amount)
            }
        else:
            contract_txn = {
                'chainId': chain_id,
                'gasPrice': gasPrice,
                'gas': gasLimit,
                'nonce': nonce,
                'to': Web3.toChecksumAddress(to_address),
                'value': int(amount)
            }

        tx_signed = web3.eth.account.signTransaction(contract_txn, privatekey)
        tx_hash = web3.eth.sendRawTransaction(tx_signed.rawTransaction)

        cprint(f'\n>>> transfer : {decimal.Decimal(str(amount_to_transfer))} {symbol} | {address} => {to_address} | {scan}/{web3.toHex(tx_hash)}', 'green')
        table.append([f'{decimal.Decimal(str(amount_to_transfer))} {symbol}', address, to_address, '\u001b[32msend\u001b[0m'])

    except Exception as error:
        cprint(f'\n>>> transfer : {privatekey} | {error}', 'red')
        try:
            table.append([f'{decimal.Decimal(str(amount_to_transfer))} {symbol}', address, to_address, '\u001b[31merror\u001b[0m'])
        except:
            table.append([f'{symbol}', address, to_address, '\u001b[31merror\u001b[0m'])


def transfer(private_key, token, to_address, chain, amount, token_contract):
    data = utils.check_rpc(chain)
    rpc_chain = data['rpc']
    chain_id = data['chain_id']
    scan = data['scan']

    print(f'rpc_chain: {rpc_chain}')
    print(f'chain_id: {chain_id}')
    print(f'scan: {scan}')

    # symbol_chain = data['token']

    # if token_contract == '':
    #     if amount == 'all_balance':
    #         amount = utils.check_balance(private_key, rpc_chain, symbol_chain, MIN_BALANCE)
    #
    #     if amount > MIN_AMOUNT:
    #         transfer_eth(
    #             private_key,
    #             token,
    #             amount,
    #             to_address,
    #             chain_id,
    #             scan,
    #             rpc_chain,
    #             symbol_chain
    #         )
    # else:
    # if amount == 'all_balance':
    #     amount = utils.check_token_balance(private_key, rpc_chain, token_contract, MIN_BALANCE)

    transfer_token(
        private_key,
        token,
        amount,
        to_address,
        chain_id,
        scan,
        rpc_chain,
        token_contract
    )

