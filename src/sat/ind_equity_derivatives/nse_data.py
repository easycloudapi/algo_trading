"""nse_data

All NSE data
"""

import requests
import json
from io import BytesIO
import pandas as pd
from zipfile import ZipFile


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
        self.nse_urls["nse_fo_bhavcopy"] = "https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22F%26O%20-%20Bhavcopy(csv)%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22derivatives%22%2C%22section%22%3A%22equity%22%7D%5D&date=<date_place_holder>&type=equity&mode=single"
        
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
    
    def get_nse_optionchain_data(self, symbol: str="NIFTY"):
        """get_nse_optionchain_data
        
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
        
    def get_nse_equitystock_data(self, index: str="allcontracts"):
        """get_nse_equitystock_data

        Args:
            index (str, optional): NSE Index. Defaults to "allcontracts".
        """
        # https://www.nseindia.com/api/equity-stock?index=allcontracts
        full_nse_equitystock_url = self.nse_urls["nse_equitystock_url"] + index.lower()
        
        response = self.session.get(url=full_nse_equitystock_url, 
                                    headers=self.headers, timeout=10)
        return response.json()
    
    def get_nse_data_from_raw_api(self, nse_complete_api_url: str, timeout: int=10):
        """get_nse_data_from_raw_api
        Generic function to get the data from NSE API

        Args:
            nse_complete_api_url (str): _description_
            timeout (int, optional): _description_. Defaults to 10.

        Returns:
            json: _description_
        """
        response = self.session.get(url=nse_complete_api_url, headers=self.headers, timeout=timeout)
        return response.json()
    
    def get_nse_future_option_bhavcopy(self, date: str=None):
        """_summary_

        Args:
            date (str): _description_
        """
        updated_nse_fo_bhavcopy_url = self.nse_urls["nse_fo_bhavcopy"]
        updated_nse_fo_bhavcopy_url = "https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22F%26O%20-%20Bhavcopy(csv)%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22derivatives%22%2C%22section%22%3A%22equity%22%7D%5D&date=23-Nov-2023&type=equity&mode=single"
        
        # 1st way, to read zip file from response into pandas dataframe
        response = self.session.get(url=updated_nse_fo_bhavcopy_url, headers=self.headers, timeout=10)
        df = pd.read_csv(BytesIO(response.content), compression='zip', header=0, sep=",")
        print(f"bhavcopy loaded into dataframe, {df.shape}")
        
        # # 2nd way, to read zip file from response into pandas dataframe
        # bavcopy_file_name = "fo23NOV2023bhav.csv"
        # with ZipFile(BytesIO(self.session.get(url=updated_nse_fo_bhavcopy_url, headers=self.headers, timeout=10).content)) as zip_archive:
        #     with zip_archive.open(bavcopy_file_name) as f:
        #         df = pd.read_csv(f)
        #         print(f"bhavcopy loaded into dataframe, {df.shape}")
        return df
        
    
    
if __name__ == "__main__":
    nsedata = NSEData()
    # out1 = nsedata.get_nse_company_symbols()
    # print(out1)
    # out2 = nsedata.get_nse_equitystock_data(symbol="NIFTY")
    # print(out2)
    
    # nifty50_ohlc = nsedata(nse_complete_api_url="")
    
    out = nsedata.get_nse_future_option_bhavcopy()