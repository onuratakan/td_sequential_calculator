# TD Sequential
A library to calculating td sequental.
# Install
```
pip3 install td-sequential
```
# Using
## In another script
```python
from td_sequential import TDS
for i in range(13):
  buy_setup, sell_setup, buy, sell = TDS.price_update(i)
  print(f"Buy setup: {buy_setup}")
  print(f"Sell setup: {sell_setup}")
  if buy:
    print("BUY")
  elif sell:
    print("SELL")
```