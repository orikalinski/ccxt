# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.bitfinex import bitfinex


class ethfinex (bitfinex):

    def describe(self):
        return self.deep_extend(super(ethfinex, self).describe(), {
            'id': 'ethfinex',
            'name': 'Ethfinex',
            'countries': ['VG'],
            'version': 'v1',
            'rateLimit': 1500,
            # new metainfo interface
            'certified': False,
            'has': {
                'CORS': False,
                'createDepositAddress': True,
                'deposit': True,
                'fetchClosedOrders': True,
                'fetchDepositAddress': True,
                'fetchFees': True,
                'fetchFundingFees': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchTickers': True,
                'fetchTradingFees': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1m',
                '5m': '5m',
                '15m': '15m',
                '30m': '30m',
                '1h': '1h',
                '3h': '3h',
                '6h': '6h',
                '12h': '12h',
                '1d': '1D',
                '1w': '7D',
                '2w': '14D',
                '1M': '1M',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/37555526-7018a77c-29f9-11e8-8835-8e415c038a18.jpg',
                'api': 'https://api.ethfinex.com',
                'www': 'https://www.ethfinex.com',
                'doc': [
                    'https://bitfinex.readme.io/v1/docs',
                    'https://github.com/bitfinexcom/bitfinex-api-node',
                    'https://www.ethfinex.com/api_docs',
                ],
            },
        })
