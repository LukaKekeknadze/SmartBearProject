# **SmartAutomationBearProject By Luka Kekenadze**
___
#**steps**
* go to the [Smartbear website](https://smartbear.com/). 
* click cart icon . 
* Choose QAComplete shop. 
* choose SaaS license .
* check if price is correct. 
* add to cart 
* check license and price valid.

___
`you should install all modules(pytest,allure,selenium,pytest-assume)`
## To Run Report Generator `Manually` with command promt(cmd)
```
python -m pytest -v -s --alluredir="allure-results\reports" .\Tests\Test_SmartBear.py
```
```
allure serve ./reports/allure
```
---
