# -*- coding:utf-8 -*-

from BiboxFuturesAPI.BiboxFuturesUtil import http_get_request, api_key_post
import random


class BiboxFutures:
    def __init__(self, url, access_key, secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    '''
    ======================
    Market data API
    ======================
    '''

    # 查询市场深度
    def get_futures_depth(self, pair, size):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围
        pair      true	string  品种代码            BIX_BTC, ETH_BTC, ...
        size        false   int     数量，     200      1-200
        """
        params = {
                    'cmd':'depth',
                    'pair': pair,
                  'size': size
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询合约面值
    def get_futures_contractValue(self,):
        """
        :return:
        """
        params = {
            'cmd': 'contractValue',
        }


        url = self.__url + '/v1/cquery?'
        return http_get_request(url, params)

    # 查询全币种市场行情
    def get_futures_contractConfig(self):
        """
        :return:
        """
        params = {
            'cmd': 'contractConfig',
        }


        url = self.__url + '/v1/cquery?'
        return http_get_request(url, params)

    # 查询全币种市场行情
    def get_futures_openLimit(self):
        """
        :return:
        """
        params = {
            'cmd': 'openLimit',
        }

        url = self.__url + '/v1/cquery?'
        return http_get_request(url, params)

    # 查询全币种市场行情
    def get_futures_lastPremiumIndex(self):
        """
        :return:
        """
        params = {
            'cmd': 'lastPremiumIndex',
        }

        url = self.__url + '/v1/cquery?'
        return http_get_request(url, params)

    # 获取KLine
    def get_futures_kline(self, pair, period, size=1000):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围
        pair	true	string	交易对		4BTC_USDT, 4ETH_USDT, ...
        period	true	string	k线周期		'1min', '3min', '5min', '15min', '30min', '1hour', '2hour', '4hour', '6hour', '12hour', 'day', 'week'
        size	false	integer	数量	1000	1-1000
        """
        params = {
                    "cmd": "kline",
                    "pair": pair,
                    "period": period,
                    "size": size
                }

        if size:
            params['size'] = size

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询最近成交
    def get_futures_deals(self, pair, size):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围
        pair	true	String	合约符号		4BTC_USDT,4ETH_USDT,...
        size	true	integer	返回数量		1,2,...
        """
        params = {
                    'cmd' : 'deals',
                    'pair': pair,
                    'size': size
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)


    '''
    ======================
    Trade/Account API
    ======================
    '''

    # 获取用户账户信息
    def get_futures_account_info(self):
        """
        """
        params = [
            {
                'cmd': "query/assets",
                'body': {
                }
            }
        ]

        request_path = self.__url + '/v1/cquery?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取单个持仓信息
    def get_futures_symbol_orders(self, pair="4BTC_USDT"):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围
        pair        true   string  币种	       4BTC_USDT,4ETH_USDT, ...
        """
        params = [
            {
                'cmd': "query/order",
                'body': {
                    'pair': pair
                }
            }
        ]

        request_path = self.__url + '/v1/cquery?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取所有合约持仓信息
    def get_futures_all_symbol_orders(self):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围
        pair        true   string  币种	       4BTC_USDT,4ETH_USDT, ...
        """
        params = [
            {
                'cmd': "query/orderAll",
                'body': {

                }
            }
        ]

        request_path = self.__url + '/v1/cquery?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取查询合约未成交订单
    def get_futures_order_pending(self, page, size, pair=""):
        """
        参数名称	是否必须	类型	描述	默认值	取值范围
        page	true	integer	第几页		1,2, ...
        size	true	integer	条数		10,20, ...
        pair	false	string	合约符号		4BTC_USDT,4ETH_USDT, ...
        """
        params = [
            { "cmd":"query/orderPending",
            "body":{
                        "page": page,
                        "size": size,
                        "pair": ""
                    }
            }
        ]

        request_path = self.__url + '/v1/cquery?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 下单
    def send_futures_order(self, pair, price, contract, order_side, leverage= 0, cross_leverage=25):
        """
        参数名称	        是否必须	     类型	     描述	       默认值	取值范围
        order_type	    true	     integer	订单类型		            1:市价,2:限价
        leverage	    true	     integer	杠杆倍数		            全仓:0,逐仓:1,2,...
        cross_leverage	false	     integer	全仓杠杆	        25	    leverage=0时且全仓:1,2,...50
        order_side	    true	     integer	挂单方向		            1:开多,2:开空
        price	        true	     string	    委托价格		            大于0的数
        contract	    true	     string	    合约张数		            1,2, ...
        pair	        true	     string	    合约符号		            4BTC_USDT,4ETH_USDT, ...
        order_from	    true	     integer	6		                6
        client_oid	    false	     Long	    自定义标识	            > 0
        """

        params = [
            {
                "cmd":"order/open",
                'body': {
                        "pair": pair,
                        "order_type": 2,
                        "price": price,
                        "contract": contract,
                        "order_from": 6,
                        "leverage": leverage,
                        "cross_leverage": cross_leverage,
                        "order_side": order_side,

                }
            }
        ]


        request_path = self.__url+ "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 批量下单
    def send_futures_bach_trades(self, pair, orders, leverage= 0, cross_leverage=25):
        """
        参数名称        是否必须	类型	描述	默认值	取值范围
        leverage	true	integer	杠杆倍数		全仓:0,逐仓:1,2,...
        cross_leverage	false	integer	全仓杠杆	25	leverage=0时全仓1,2,...50
        pair	true	string	合约符号		4BTC_USDT,4ETH_USDT, ...

        orders 数据结构
                order_side	true	integer	挂单方向		1:开多,2:开空
                price	true	string	委托价格		大于0的数
                contract	true	string	合约张数		1,2, ...
                client_oid	false	Long	自定义标识		> 0
        """
        params = [
        {
            "cmd": "order/openBatch",
            "body": {
                "pair": pair,
                "leverage": leverage,
                "cross_leverage": cross_leverage,
                "arr": orders
            }
        }]

        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 撤销订单
    def cancel_futures_order(self, order_id):
        """
        参数名称     是否必须 类型     描述
        orders_id	true	string	委托单id
        """
        params = [
            {
                'cmd': "order/close",
                'body': {
                    'order_id': order_id
                }
            }
        ]

        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 撤销订单 通过client_oid撤单
    def cancel_futures_order_by_client_oid(self, clientIds):
        """
        参数名称     是否必须 类型     描述
        clientIds	true	string	委托单id
        """
        params = [
            {
                 "cmd":"order/closeBatchClientOid",
                "body":{
                    "clientIds":[
                        clientIds
                    ]
                },
            }
        ]

        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 批量撤单
    def cancel_futures_all(self, orderIds):
        """
        参数名称     是否必须  类型     描述
        orderIds	true	 list	委托单ids   orderId=['1223456','234542134','3245675']
        """

        params = [
            {
                "cmd":"order/closeBatch",
                'body': {
                    'order_ids': orderIds
                },
                "index": 13

            }
        ]
        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 通过订单号查询未成交订单
    def cancel_futures_order_pendingByIDs(self, id_list):
        """
        参数名称     是否必须 类型     描述
        id_list 	true	string array	订单号		最大长度限制50单
        """
        params = [
            {
                "cmd": "query/orderPendingByIDs",
                "body": {
                    "ids": id_list       # ["491168","2"]
                },
                "index": 13
            }
        ]

        request_path = self.__url + "/v1/cquery"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 通过client_oid查询未成交订单
    def cancel_futures_orders_detailByClientIds(self, clientIds_list):
        """
        参数名称     是否必须 类型     描述
        clientIds_list	true	string array	用户client_oid单号		最大长度限制50单
        """
        params = [
            {
                "cmd": "query/ordersDetailByClientIds",
                "body": {
                    "ids": clientIds_list  # ["1588819328619","1588819328619"]
                },
                "index": 13
            }
        ]

        request_path = self.__url + "/v1/cquery"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 通过client_oid查询委托单
    def cancel_futures_order_pendingByClientIds(self, clientIds_list):
        """
        参数名称     是否必须 类型     描述
        clientIds_list	true	string array	用户client_oid单号		最大长度限制50单
        """
        params = [
            {
                "cmd": "query/orderPendingByClientIds",
                "body": {
                    "ids": clientIds_list  # ["1588819328619","1588819328619"]
                },
                "index": 13
            }
        ]

        request_path = self.__url + "/v1/cquery"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 合约调整杠杆倍数
    def get_futures_change_leverage(self,  pair, leverage, cross):
        """
        参数名称     是否必须  类型   描述
        pair	    true	string	合约符号		4BTC_USDT,4ETH_USDT, ...
        leverage	true	integer	杠杆倍数		全仓:0,逐仓:1,2,...
        cross	    true	integer	是否全仓		0逐仓，1全仓
        """

        params = [{
            "cmd": "order/changeLeverage",
            "body": {
                "pair": pair,
                "leverage": leverage,
                "cross": cross
            },
            "index": 13
        }]
        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 合约调整保证金
    def get_futures_change_margin(self, pair, margin):
        """
        参数名称     是否必须  类型   描述
        pair	    true	string	合约符号		4BTC_USDT,4ETH_USDT, ...
        margin	    true	integer	增减保证金		增加margin>=0.5;减少margin<=-0.5
        """

        params = [{
            "cmd": "order/changeMargin",
            "body": {
                "pair": pair,
                "margin": margin

            },
            "index": 13
        }]
        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 主账户资金转入合约账户
    def user_futures_transfer(self, amount):
        """
        参数名称         是否必须  类型     描述  默认值   取值范围
        amount	        true	double	转账金额	----	> 0
        """
        params = [
            {
                "cmd": "transfer/in",
                "body": {
                    "amount": amount
                }
            }
        ]

        request_path = self.__url + "/v1/ctrade"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 查询个人成交记录
    def get_futures_history_order_list(self, pair, page, size, begin_time=None,  end_time=None, type=2):
        """
        参数名称         是否必须  类型     描述  默认值   取值范围
        pair	true	String	合约符号		4BTC_USDT,4ETH_USDT,...
        page	true	integer	第几页		1,2,...
        size	true	integer	多少条		1,2,...
        begin_time	false	integer	开始时间
        end_time	false	integer	结束时间
        type	false	integer	成交类型		1开仓, 2平仓, 3爆仓, 4减仓
        """
        params = [
            {
                "cmd":"query/orderList",
                "body":{
                    "pair": pair,
                    "page": page,
                    "size": size,
                    "begin_time":begin_time,
                    "end_time":end_time,
                    type: type,
                }
            }
        ]

        request_path = self.__url + "/v1/cquery"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 通过订单号查询未成交订单
    def get_futures_order_detail(self, id):
        """
        参数名称     是否必须 类型     描述
        id	true	String	订单号
        """
        params = [
            {
                "cmd": "query/orderDetailByID",
                "body": {
                    "ids": id
                },
            }
        ]

        request_path = self.__url + "/v1/cquery"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)
