# TD Sequential Calculator
A library to calculating td sequental.
# Install
```
pip3 install td-sequential-calculator
```
# Using
## In another script
```python
from td_sequential_calculator import TDS
for i in range(13):
  buy_setup, sell_setup, buy, sell = TDS.price_update(i)
  print(f"Buy setup: {buy_setup}")
  print(f"Sell setup: {sell_setup}")
  if buy:
    print("BUY")
  elif sell:
    print("SELL")
```