# -*- coding:utf-8 -*-

from BiboxFuturesAPI.BiboxFuturesService import BiboxFutures
from pprint import pprint

URL = 'https://api.bibox.com'

####  input your access_key and secret_key below:
ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

bb = BiboxFutures(URL, ACCESS_KEY, SECRET_KEY)

# --------------------------------------------------------------------

# print (u' 获取合约面值 ')
# pprint (bb.get_futures_contractValue())

# print (u' 获取杠杆信息 ')
# pprint (bb.get_futures_contractConfig())

# print (u' 获取合约下单单笔限制 ')
# pprint (bb.get_futures_openLimit())

# print (u' 获取合约当前资金费率 ')
# pprint (bb.get_futures_lastPremiumIndex())

# print (u' 获取K线数据 ')
# pprint (bb.get_futures_kline(pair='4BTC_USDT', period='1min', size=20))

# print (u' 获取市场深度 ')
# pprint (bb.get_futures_depth(pair='4BTC_USDT', size=20))

# print (u' 获取市场最近成交记录 ')
# pprint (bb.get_futures_deals(pair='4BTC_USDT', size=20))



#%% trade / account api  ===============
#
# print (u' 获取用户合约资产 ')
# pprint (bb.get_futures_account_info())

# print (u' 获取单个持仓信息 ')
# pprint (bb.get_futures_symbol_orders(pair="4BTC_USDT"))

# print (u' 获取所有合约持仓信息 ')
# pprint (bb.get_futures_all_symbol_orders())

# print (u' 获取查询合约未成交订单 ')
# pprint (bb.get_futures_order_pending(page=1,  size=10, pair=''))


# print (u' 下单 ')
# pprint(bb.send_futures_order(pair="4BTC_USDT", price='9100', contract=1, order_side=1, leverage= 0, cross_leverage=25))

# print (u' 批量下单 ')
# pprint(bb.send_futures_bach_trades(pair="4BTC_USDT",leverage= 0, cross_leverage=25,orders=[{
#                 "order_side":1,
#                 "price":9090,
#                 "contract":1,
#                 "client_oid": '123456787'
#             },
#             {
#                 "order_side":1,
#                 "price":9080,
#                 "contract":1,
#                 "client_oid": '123456788'
#             }
#         ])) 48378731852980 48378731852981

# print (u' 撤销订单 ')
# pprint(bb.cancel_futures_order(order_id='48378731852980'))

# print (u' 批量撤销订单 ')
# pprint(bb.cancel_futures_all(orderIds=['1223456','234542134','3245675']))

# print (u' 通过client_oid撤单')
# pprint(bb.cancel_futures_order_by_client_oid(clientIds=''))

# print (u' 通过订单号查询未成交订单')
# pprint(bb.cancel_futures_order_pendingByIDs(id_list=''))

# print (u' 通过client_oid查询未成交订单')
# pprint(bb.cancel_futures_orders_detailByClientIds(clientIds_list=''))

# print (u' 通过client_oid查询委托单')
# pprint(bb.cancel_futures_order_pendingByClientIds(clientIds_list=''))

# print (u' 合约调整杠杆倍数 ')
# pprint(bb.get_futures_change_leverage(pair="4BTC_USDT", leverage=40, cross=0))

# print (u' 合约调整保证金 ')
# pprint(bb.get_futures_change_margin(pair="4BTC_USDT", margin=4))

# print (u' 账户划转 主账户资金转入合约账户')
# pprint(bb.user_futures_transfer(amount=10))

# print (u' 查询个人成交记录 ')
# pprint(bb.get_futures_history_order_list(pair="4BTC_USDT", page=1, size=1))

# print (u' 查询订单详情 ')
# pprint(bb.get_futures_order_detail(id="11"))

