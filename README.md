# Smart Algo Trading
> Simple and smart Algo Trading module to build robust and scalable application

> Help Coders and Traders to build own strategies and earn 

## Info:
1. Version: 1.0.0
2. Test Pypi Link: https://test.pypi.org/project/smart-algo-trading
3. Pypi Link: https://pypi.org/project/smart-algo-trading
4. Bug/Issue Tracker (GitHub): https://github.com/easycloudapi/smart_algo_trading/issues
5. Discussion (GitHub): https://github.com/easycloudapi/smart_algo_trading/discussions
6. Repository (GitHub): https://github.com/easycloudapi/smart_algo_trading

## Module Details:

| ID | Package Name | Module Name | Import The Module | Description
| --- | --- | --- | --- | --- |
| 1. | ind_equity_derivatives | nse_data | from ind_equity_derivatives.nse_data import NSEData | Fetch equity and options data |
| | | | | |


## Sample Code (`NSE Company Symbols`):
```shell
from ind_equity_derivatives.nse_data import NSEData

nsedata = NSEData()
out1 = nsedata.get_nse_company_symbols()
print(out1)
```

## How to contribute:
Follow [Developer Guide](Developer_Guide.md)