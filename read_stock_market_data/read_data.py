import yfinance as yf
import os

class readdata:
    def __init__(self):
        pass
    def read_live_data_store(self,stock_name,period,interval):
        stock = yf.Ticker(stock_name)
        live_data = stock.history(period=period, interval=interval)
        os.makedirs('data', exist_ok=True)
        file_path = os.path.join('data', 'live_data.csv')
        live_data.to_csv(file_path)
        return file_path
        
    def read_past_data_store(self,stock_name,period):
        stock = yf.Ticker(stock_name)
        past_data = stock.history(period=period)
        os.makedirs('data',exist_ok=True)
        file_path = os.path.join('data','past_data.csv')
        past_data.to_csv(file_path)
        return file_path
obj = readdata()
obj.read_live_data_store('RELIANCE.NS','1d','1m')
obj.read_past_data_store('RELIANCE.NS','5y')
