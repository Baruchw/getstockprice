from yahoo_fin import stock_info as si
msft = si.get_live_price("msft")
print (msft)
