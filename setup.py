from setuptools import setup


setup(name='td_sequential',
version='0.1.0',
description="""A library to calculating td sequental.""",
long_description="""
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
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/td_sequential',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["td_sequential"],
package_dir={'':'src'},
python_requires=">= 3",
zip_safe=False)