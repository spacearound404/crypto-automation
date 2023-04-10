# Crypto Automation
[![pypi: package](https://img.shields.io/badge/pypi-0.0.4-blue)](https://pypi.org/project/bufflogin/)
[![Python: versions](
https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)]()

Crypto Automation project contains several modules for interaction with crypto.

## Features

- binance: withdrawal from binance to wallets via api key;
- okx: withdrawal from okx to wallets via api key;
- transfer: withdrawal from wallets to other wallets (okx sub-accounts);
- bridge: bridge from any network to any network via Orbiter;

## Requirements
- Python 3.x.x

## Setup
Setup project, follow these steps:
1. `pip install -r requirements.txt`
2. setup `config.py`
3. setup `actions.json`

### Setup `config.py`
| Param           |                                                               Desc                                                                |
|-----------------|:---------------------------------------------------------------------------------------------------------------------------------:|
| `ERC20_ABI_PATH`  |                                                    path to ERC20 ABI json file                                                    |
| `ACTIONS_PATH`    |                                                    path to actions, json file                                                     |
| `RPCS`            |                                   RPC. To add a new network, follow the general json structure                                    |
| `ORBITER_AMOUNT`  | The code of the network to which Orbiter transfers. Make sure that the code is the same as those described on the Orbiter website | 

### Setup `actions.json`
You can combine these actions, building them into a chain of actions to automate the process. Use the templates below.

> ⚠️ **Warnning!**
>
> 1. Name of network corresponds to name of `chain` field in `RPCS` constant, in file `config.py`.
> 2. `token_contract` must be taken from scan site of your network/chain
> 3. `bridge_contract` must be taken from the Orbiter site.
> 4. When using token name in Orbiter and when transfer token from wallet, you must first add ABI of that token to `abi` folder with name of that token, i.e. the name of token in your `actions.json` is the name of ABI file.
> 5. Note that amount specified for Orbiter is `amount` + `X` to compensate for gas in various networks, `X` can be viewed on Orbiter website.
> 6. Note that your API tokens for Binance and OKX, must have permission to withdraw funds.

### Binance templates
```json
  {
    "type": "binance-withdraw",
    "data": {
      "api_key": "",
      "secret": "",
      "token": "USDT",
      "amount": 3,
      "network": "MATIC",
      "address": ""
    }
  }
```
### OKX templates
```json
  {
    "type": "okx-withdraw",
    "data": {
      "api_key": "",
      "secret": "",
      "password": "",
      "token": "USDT",
      "amount": "2",
      "network": "MATIC",
      "fee": "1",
      "address": "",
      "proxies": {
            "http": "http://ip:port",
            "https": "http://username:password@ip:port/"
        }
    }
  }
```
### Metamask transfer templates
```json
  {
    "type": "mm-withdraw",
    "data": {
      "token": "USDT",
      "amount": "2",
      "network": "MATIC",
      "private_key": "",
      "token_contract": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
      "address": ""
    }
  }
```
### Orbiter bridge templates
```json
  {
    "type": "orbiter-bridging",
    "data": {
      "private_key": "",
      "from_chain": "MATIC",
      "to_chain": "ARBITRUM",
      "amount": "4.5",
      "token": "USDT",
      "token_contract": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
      "bridge_contract": "0xd7aa9ba6caac7b0436c91396f22ca5a7f31664fc"
    }
  }
```

## Run
To run the project, use the command:
`python main.py`
