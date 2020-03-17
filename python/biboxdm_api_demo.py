# -*- coding:utf-8 -*-

from bibox.BiboxSpotService import BiboxSpot
from pprint import pprint

URL = 'https://api.bibox.com'

####  input your access_key and secret_key below:
ACCESS_KEY = 'xxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxx'

bb = BiboxSpot(URL, ACCESS_KEY, SECRET_KEY)

# --------------------------------------------------------------------
# print (u' 网络测试 ')
# pprint (bb.get_ping())

# print (u' 获取交易对 ')
# pprint (bb.get_symbols())

# print (u' 获取全币种市场行情 ')
# pprint (bb.get_market_all())

# print (u' 获取单币种市场行情 ')
# pprint (bb.get_market(symbol='BIX_BTC'))

# print (u' 获取K线数据 ')
# pprint (bb.get_kline(symbol='BIX_BTC', period='1min', size=20))

# print (u' 获取市场深度 ')
# pprint (bb.get_depth('BIX_BTC', size=20))

# print (u' 获取市场最近成交记录 ')
# pprint (bb.get_deals(symbol='BIX_BTC', size=20))

# print (u' 获取ticker数据 ')
# pprint (bb.get_ticker(symbol='BIX_BTC'))


#%% trade / account api  ===============
#
# print (u' 获取用户账户信息 ')
# pprint (bb.get_account_info())

# print (u' 获取查询充值记录 ')
# pprint (bb.get_transfer_in(coin_symbol="BTC"))

# print (u' 获取查询提现记录 ')
# pprint (bb.get_transfer_out(coin_symbol="BTC", amount=0.02, addr="xxxxxxx", addr_remark="备注"))

# print (u' 获取查询充值记录 ')
# pprint (bb.get_transfer_in_detail_list(page=1,  size=10))

# print (u' 获取查询提现记录 ')
# pprint (bb.get_transfer_out_detail_list(page=1, size= 10))

# print (u' 获取币种配置 ')
# pprint (bb.get_coinConfig())

# print (u' 获取某一条的提现记录')
# pprint (bb.get_transfer_withdrawInfo(id=3))


# print (u' 下单 ')
# pprint(bb.send_order(symbol="BIX_BTC", account_type= 0,
#                      tradeType= 2,
#                      order_type= 2,
#                      price=0.00001416,
#                      amount=20))

# print (u' 批量下单 ')
# pprint(bb.send_bach_trades(orders=[['BTC_USDT',100000,0.001,2],['ETC_USDT',1500,0.001,2]]))

# print (u' 撤销订单 ')
# pprint(bb.cancel_order(order_id='12488253125370673'))

# print (u' 批量撤销订单 ')
# pprint(bb.cancel_all(orderIds=['1223456','234542134','3245675']))


# print (u' 查看当前委托 ')
# pprint(bb.get_open_orders(page=1, size=10))

# print (u' 查看历史委托 ')
# pprint(bb.get_history_open_orders(page=1, size=10))

# print (u' 查看委托详情 ')
# pprint(bb.get_orders_pending_info(id="))

# print (u' 查看历史成交明细 ')
# pprint(bb.get_history_traders(page=1, size=1))

# print (u' 账户划转 ')
# pprint(bb.user_transfer(type=1, amount=1 , symbol="USDT" ))

# print (u' 母子之间账户划转 ')
# pprint(bb.mom_and_son_transfer(side="in", son_id="XXXXXXX", coin="BTC", amount=0.001))
