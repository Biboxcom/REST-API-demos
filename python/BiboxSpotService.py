# -*- coding:utf-8 -*-

from bibox.BiboxSpotUtil import http_get_request, api_key_post
import random


class BiboxSpot:
    def __init__(self, url, access_key, secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    '''
    ======================
    Market data API
    ======================
    '''
    # 网络测试
    def get_ping(self):
        """
        :return:
        """
        params = {
                    'cmd':'ping',
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询市场深度
    def get_depth(self, symbol, size):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围         
        symbol      true	string  品种代码            BIX_BTC, ETH_BTC, ...
        size        false   int     数量，     200      1-200
        """
        params = {
                    'cmd':'depth',
                    'pair': symbol,
                  'size': size
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询交易对
    def get_symbols(self,):
        """
        :return:
        """
        params = {
            'cmd': 'pairList',
        }


        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询全币种市场行情
    def get_market_all(self):
        """
        :return:
        """
        params = {
            'cmd': 'marketAll',
        }


        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询单币种市场行情
    def get_market(self, symbol):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围         
        symbol      true	string   交易对            BIX_BTC, ETH_BTC, ...	
        """
        params = {
            'cmd': 'market',
            'pair': symbol
        }


        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 获取KLine
    def get_kline(self, symbol, period, size=1000):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围         
        symbol      true	string   交易对            BIX_BTC, ETH_BTC, ...    
        """
        params = {
            'pair': symbol,
            'period': period,
            'cmd': 'kline',
        }

        if size:
            params['size'] = size


        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询最近成交
    def get_deals(self, symbol, size):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围         
        symbol      true	string   交易对            BIX_BTC, ETH_BTC, ...
        size        false   integer  数量      200      1-200  
        """
        params = {
                    'cmd':'deals',
                    'pair': symbol,
                  'size': size
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询市场ticker
    def get_ticker(self, symbol):
        """
        参数名称     是否必须  类型     描述	  默认值   取值范围         
        symbol      true	string   交易对            BIX_BTC, ETH_BTC, ...
        """
        params = {
                    'cmd':'ticker',
                    'pair': symbol,
                  }

        url = self.__url + '/v1/mdata?'
        return http_get_request(url, params)

    # 查询下单限制信息
    def get_trade_limit(self):
        """
        :return:
        """
        params = {
            'cmd': 'traderLimit',
        }

        url = self.__url + '/v1/orderpending?'
        return http_get_request(url, params)


    '''
    ======================
    Trade/Account API
    ======================
    '''

    # 获取用户账户信息
    def get_account_info(self, select=1):
        """
        参数名称     是否必须  类型     描述	         默认值       取值范围         
        select      false	integer  是否查询资产明细            不传-各币种总资产合计，1-请求所有币种资产明细
        """
        params = [
            {
                'cmd': "transfer/assets",
                'body': {
                    'select': select
                }
            }
        ]

        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取币种配置
    def get_coinConfig(self, coin_symbol=""):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        coin_symbol  false   string  币种	       BIX ETH ...
        """
        params = [
            {
                'cmd': "transfer/coinConfig",
                'body': {
                    'coin_symbol': coin_symbol
                }
            }
        ]

        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 充值 地址
    def get_transfer_in(self, coin_symbol):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        coin_symbol	true	string	充值币种		   BIX, BTC, ...
        """
        params = [
            {
                "cmd": "transfer/transferIn",
                "body": {
                    "coin_symbol": coin_symbol,
                }
            }
        ]
        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 提现 地址
    def get_transfer_out(self, coin_symbol, amount, addr, addr_remark, totp_code=None, trade_pwd=None, memo=None):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        coin_symbol	true	string	提现币种		BIX, BTC, ...
        amount	    true	double	提现数量		需大于各币种最小提现数量
        addr	    true	string	提现地址		币种合法地址
        addr_remark	true	string	提现地址备注名称		
        totp_code	false	integer	google验证码		新地址需要,旧地址不需要
        trade_pwd	false	string	资金密码		新地址需要,旧地址不需要
        memo	    false	string	提现标签		一些币种提现必须指定标签，与地址组合标识唯一性，比如EOS
        """
        params = [
            {
                "cmd": "transfer/transferOut",
                "body":{
                    "coin_symbol":coin_symbol,
                    "amount":amount,
                    "totp_code":totp_code,
                    "trade_pwd":trade_pwd,
                    "addr":addr,
                    "addr_remark":addr_remark,
                    "memo":memo,
                }
            }
        ]
        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 查询充值记录
    def get_transfer_in_detail_list(self, page, size, filter_type="",coin_symbol=""):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        filter_type	false	integer	充值记录筛选	0	0-全部，1-充值进行中，2-充值到账，3-充值失败
        coin_symbol	false	string	充值币种		BIX, ETH, ...
        page	     true	integer	第几页		从1开始
        size	     true	integer	每页数量		1-50
        """
        params = [
            {
                "cmd": "transfer/transferInList",
                "body": {
                            "filter_type": filter_type,
                            "page": page,
                            "size": size,
                            "coin_symbol": coin_symbol
                }
            }
        ]
        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 查询提现记录
    def get_transfer_out_detail_list(self, page, size, filter_type="",coin_symbol=""):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        filter_type	false	integer	充值记录筛选	0	0-全部，1-充值进行中，2-充值到账，3-充值失败
        coin_symbol	false	string	充值币种		BIX, ETH, ...
        page	     true	integer	第几页		从1开始
        size	     true	integer	每页数量		1-50
        """
        params = [
            {
                "cmd": "transfer/transferOutList",
                "body": {
                            "filter_type": filter_type,
                            "page": page,
                            "size": size,
                            "coin_symbol": coin_symbol
                }
            }
        ]
        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 查询某一条提现记录
    def get_transfer_withdrawInfo(self, id):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        id	true	integer	提现id
        """
        params = [
            {
                "cmd": "transfer/withdrawInfo",
                "body": {
                    "id": id
                }
            }
        ]
        request_path = self.__url + '/v1/transfer?'
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 下单
    def send_order(self, symbol, account_type, tradeType,  order_type, price=0, amount=0):
        """
        参数名称	      是否必须 	类型	  描述	  默认值	   取值范围
        symbol	       true	   string	交易对		BIX_BTC, ETH_BTC, ...
        account_type   true	   integer	账户类型		0-币币账户
        order_type	   true	   integer	交易类型		2-限价单
        order_side	   true	   integer	交易方向		1-买，2-卖
        price	       true	   double	委托价格		最小值 0.00000001
        amount	       true	   double	委托数量		最小值 0.0001
        """

        params = [
            {
                'cmd': "orderpending/trade",
                'body': {
                    'pair': symbol,
                    'account_type': 0,  # 账户类型，0普通账户
                    'order_type': 2,  # 订单类型 1是市价单 2是限价单
                    'order_side': tradeType,  # 下单方向 1是买 2是卖
                    'price': price,  # 下单价格
                    'amount': amount  # 下单数量
                }
            }
        ]


        request_path = self.__url+ "/v2/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 批量下单
    def send_bach_trades(self, orders):
        """
        参数名称	      是否必须 	类型	    描述	     默认值	   取值范围
        orders	      true	   array	订单信息 		       [['BTC_USDT',price,amount,side], [], []..]
        ps: 
        orders[i][0]   代表 交易对     类型 str       取值: 'BTC_USDT'
        orders[i][1]   代表 价格       类型 double    取值: 5000.01
        orders[i][2]   代表 下单数量   类型 double     取值: 最小值 0.0001
        orders[i][3]   代表 交易方向   类型 integer    取值: 1是买 2是卖
        """
        cmds = []
        for i in range(len(orders)):
            cmd = {
                'cmd': "orderpending/trade",
                'body': {
                    'pair': orders[i][0],
                    'account_type': 0,
                    'order_type': 2,
                    'order_side': orders[i][3],
                    'price': orders[i][1],
                    'amount': orders[i][2],
                }
            }
            cmds.append(cmd)

        request_path = self.__url + "/v2/orderpending"
        return api_key_post(request_path, cmds, self.__access_key, self.__secret_key)

    # 撤销订单
    def cancel_order(self, order_id):
        """
        参数名称     是否必须 类型     描述
        orders_id	true	string	委托单id
        """
        params = [
            {
                'cmd': "orderpending/cancelTrade",
                'body': {
                    'orders_id': order_id
                }
            }
        ]

        request_path = self.__url + "/v2/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 批量撤单
    def cancel_all(self, orderIds):
        """
        参数名称     是否必须  类型     描述
        orderIds	true	 list	委托单ids   orderId=['1223456','234542134','3245675']
        """
        cmds = []
        for i in range(len(orderIds)):
            cmd = {
                'cmd': "orderpending/cancelTrade",
                'body': {
                    'orders_id': orderIds[i]
                }
            }
            cmds.append(cmd)
        request_path = self.__url + "/v2/orderpending"
        return api_key_post(request_path, cmds, self.__access_key, self.__secret_key)

    # 获取当前未成交委托
    def get_open_orders(self,  page, size, account_type=0, coin_symbol=None, order_side=None, symbol="",currency_symbol=None):
        """
        参数名称     是否必须  类型   描述
        symbol	     false	string	交易对		BIX_BTC, ETH_BTC, ...
        account_type true	integer	账户类型		0-币币账户
        page	     true	integer	第几页		从1开始
        size	     true	integer	每页数量		1-50
        order_side	 false	integer	交易方向		1-买，2-卖
        coin_symbol	 false	string	交易币种		BIX, EOS, ...
        currency_symbol	false	string	定价币种		BTC, USDT, ...
        """
        if symbol == '':
            params = [
                {
                    'cmd': "orderpending/orderPendingList",
                    'body': {
                        'pair': symbol,
                        'account_type': account_type,  # 账户类型，0普通账户
                        'order_side': order_side, # 1-买，2-卖
                        'size': size,  # 要几条
                        'page': page,  # 第几页
                        'coin_symbol': coin_symbol, # 交易币种
                        'currency_symbol':currency_symbol, # 定价币种
                    }
                }
            ]
        else:
            sy = symbol.split("_")
            sy1 = sy[0]
            sy2 = sy[1]
            params = [
                {
                    'cmd': "orderpending/orderPendingList",
                    'body': {
                        'account_type': 0,  # 账户类型，0普通账户
                        'coin_symbol': sy1,
                        'currency_symbol': sy2,
                        'size': size,  # 要几条
                        'page': page,  # 第几页
                    }
                }
            ]

        request_path = self.__url + "/v1/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取历史委托
    def get_history_open_orders(self, page, size, account_type=0, coin_symbol=None, order_side=None, symbol="",currency_symbol=None, hide_cancel=1):
        """
        参数名称     是否必须  类型   描述
        symbol	false	string	交易对		BIX_BTC, ETH_BTC, ...
        account_type	true	integer	账户类型		0-币币账户
        order_side	false	integer	交易方向		1-买，2-卖
        coin_symbol	false	string	交易币种		BIX, EOS, ...
        currency_symbol	false	string	定价币种		BTC, USDT, ...
        hide_cancel	false	integer	隐藏已撤销订单		0-不隐藏，1-隐藏
        page	true	integer	第几页		从1开始
        size	true	integer	每页数量		1-50
        """
        if symbol == '':
            params = [
                {
                    'cmd': "orderpending/pendingHistoryList",
                    'body': {
                        'pair': symbol,
                        'account_type': account_type,  # 账户类型，0普通账户
                        'order_side': order_side, # 1-买，2-卖
                        'size': size,  # 要几条
                        'page': page,  # 第几页
                        'coin_symbol': coin_symbol, # 交易币种
                        'currency_symbol':currency_symbol, # 定价币种
                        "hide_cancel" : hide_cancel,
                    }
                }
            ]
        else:
            sy = symbol.split("_")
            sy1 = sy[0]
            sy2 = sy[1]
            params = [
                {
                    'cmd': "orderpending/orderPendingList",
                    'body': {
                        'account_type': 0,  # 账户类型，0普通账户
                        'coin_symbol': sy1,
                        'currency_symbol': sy2,
                        'size': size,  # 要几条
                        'page': page,  # 第几页
                    }
                }
            ]

        request_path = self.__url + "/v1/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取成交记录
    def get_history_orders_detail(self,  id, account_type=0):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        id	         true	string	委托单id		
        account_type true	integer	账户类型		0-币币账户
        """
        params = [
            {
                'cmd': "orderpending/orderDetail",
                'body': {
                    "id": id,
                    'account_type': account_type
                }
            }
        ]

        request_path = self.__url + "/v1/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取委托单详情
    def get_open_orders_info(self,  id, account_type= 0):
        """
        参数名称     是否必须  类型     描述  默认值   取值范围         
        id	        true	string	委托单id		
        account_type true	integer	账户类型		0-币币账户
        """
        params = [
            {
                'cmd': "orderpending/order",
                'body': {
                    "id": id,
                    'account_type': account_type
                }
            }
        ]

        request_path = self.__url + "/v1/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 获取历史成交明细
    def get_history_traders(self,  page, size, account_type=0,
                            order_side=2, coin_symbol=None, currency_symbol=None, symbol=None):
        """
        参数名称         是否必须  类型     描述  默认值   取值范围       
        page	        true	integer	第几页		从1开始
        size	        true	integer	每页数量		1-50
        symbol	        false	string	交易对		BIX_BTC, ETH_BTC, ...
        account_type	true	integer	账户类型		0-币币账户
        order_side	    false	integer	交易方向		1-买，2-卖
        coin_symbol	    false	string	交易币种		BIX, EOS, ...
        currency_symbol	false	string	定价币种		BTC, USDT, ...
        """
        params = [
            {
                'cmd': "orderpending/orderHistoryList",
                'body': {
                    "account_type": account_type,
                    "order_side": order_side,
                    "page": page,
                    "size": size,
                    "coin_symbol": coin_symbol,
                    "currency_symbol": currency_symbol,
                    "pair": symbol
                }
            }
        ]

        request_path = self.__url + "/v1/orderpending"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 钱包-币币资产划转
    def user_transfer(self,type,amount,symbol):
        """
        参数名称         是否必须  类型     描述  默认值   取值范围       
        symbol	        true	string	交易对	----	EOS,BTC...
        amount	        true	double	转账金额	----	> 0
        type	        true	integer	转账类型	----	0钱包转币币; 1币币转钱包
        """
        params = [
            {
                'type': type,      # 划转方向
                'amount':amount,   # 划转数量
                'symbol': symbol   # 划转币种

            }
        ]

        request_path = self.__url + "/v2/assets/transfer/spot"
        return api_key_post(request_path, params, self.__access_key, self.__secret_key)

    # 子母账号互转
    def mom_and_son_transfer(self, side, son_id, coin, amount, pwd=None):
        """
        参数名称         是否必须  类型    描述  默认值   取值范围       
        side	        true	str  	划转方向	----	in， out
        son_id	        true	str  	地址 	----	xxxxx
        coin	        true	str 	币种 	----	EOS,BTC...
        amount	        true	double	数量	    ----	1
        pwd	            false	str	    资金密码 	----	
        """
        if side == 'in':
            type = "son/inSon"
        elif side == 'out':
            type = "son/outSon"
        cmds = [
            {
                'cmd': "son/" + side + "Son",
                'body': {
                    'son_id': son_id,
                    'coin_symbol': coin,
                    'amount': amount,
                    'trade_pwd': pwd,
                }
            }
        ]
        request_path = self.__url + "/v1/assets/transfer"
        return api_key_post(request_path, cmds, self.__access_key, self.__secret_key)