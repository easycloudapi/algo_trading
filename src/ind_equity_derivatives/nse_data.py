"""nse_data

All NSE data
"""

import requests
import json


class NSEData():
    def __init__(self):
        """NSEIndia, init method
        """
        # nse api header setup
        # session creation from nse home page
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers, timeout=5)
        
        # nse urls dict
        self.nse_urls = dict()
        self.nse_urls["nse_marketStatus_url"] = "https://www.nseindia.com/api/marketStatus"
        self.nse_urls["nse_company_symbol_url"] = "https://www.nseindia.com/api/master-quote"
        self.nse_urls["nse_optionchain_url"] = "https://www.nseindia.com/api/option-chain-indices?symbol="
        self.nse_urls["nse_equitystock_url"] = "https://www.nseindia.com/api/equity-stock?index="
        # self.nse_urls["nse_live_derivatives_url"] = "https://www.nseindia.com/api/liveEquity-derivatives?index=nse50_opt"
        
    def get_nse_company_symbols(self):
        """get_nse_company_symbols
        
        Returns:
            list: nse_company_symbol (returning nse company symbols )
        """
        # symbol.replace(' ', '%20').replace('&', '%26')
        response = self.session.get(url=self.nse_urls["nse_company_symbol_url"], 
                                    headers=self.headers, timeout=10)
        nse_company_symbol = json.loads(response.text)
        return nse_company_symbol
    
    def get_nse_optionchain_symbol(self, symbol: str="NIFTY"):
        """get_nse_optionchain_single_symbol
        
        Args:
            symbol (str, optional): NSE Symbol. Defaults to "NIFTY".
            
        Returns:
            dict: NSE Option Chain
        """
        # "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
        full_nse_optionchai_url = self.nse_urls["nse_optionchain_url"] + symbol.upper()
        
        response = self.session.get(url=full_nse_optionchai_url, 
                                    headers=self.headers, timeout=20)
        return response.json()
        
    def get_nse_equitystock_index(self, index: str="allcontracts"):
        """get_nse_equitystock_single_index

        Args:
            index (str, optional): NSE Index. Defaults to "allcontracts".
        """
        # https://www.nseindia.com/api/equity-stock?index=allcontracts
        full_nse_equitystock_url = self.nse_urls["nse_equitystock_url"] + index.lower()
        
        response = self.session.get(url=full_nse_equitystock_url, 
                                    headers=self.headers, timeout=10)
        return response.json()
    
    
if __name__ == "__main__":
    nsedata = NSEData()
    out1 = nsedata.get_nse_company_symbols()
    print(out1)
    # out2 = nsedata.get_nse_optionchain_symbol(symbol="NIFTY")
    # print(out2)