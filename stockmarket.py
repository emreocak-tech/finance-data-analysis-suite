import logging
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
import requests
from abc import ABC,abstractmethod
from dotenv import load_dotenv
plt.style.use("seaborn-v0_8-darkgrid")
load_dotenv()
from prophet import Prophet
import datetime
class DatasforStockMarket(ABC):
    def __init__(self):
        self._endtime=datetime.datetime(year=2025, month=9, day=21)
        self._starttime=datetime.datetime(year=2020,month=3,day=13)
    @abstractmethod
    def analyzestockmarket(self):
        pass
    @abstractmethod
    def show_infoghrapic(self):
        pass
    @abstractmethod
    def select_title(self):
        pass
class Analyze(DatasforStockMarket):
    def __init__(self):
        super().__init__()
    def analyzestockmarket(self):
        tickers=input("Which company are you interested in ? : ")
        df_multi=yf.download(tickers=tickers,start=self._starttime,end=self._endtime,interval="1d",group_by="ticker")
        common_value_open=df_multi[tickers]['Close'].mean(numeric_only=True)
        print(f"Open price of common value is {common_value_open}")
        common_value_close=df_multi[tickers]['Open'].mean(numeric_only=True)
        print(f"Close price of common value is {common_value_close}")
    def show_infoghrapic(self):
        tickers=input("Which company are you interested in : ")
        try:
            df_single = yf.download(tickers=tickers, start=self._starttime, end=self._endtime, interval="1d",group_by="ticker")
            value_of_volume = df_single[tickers]['Volume']
            plt.plot(value_of_volume, color="Red")
            plt.xlabel("Time", color="Black", fontsize=20)
            plt.ylabel("Volume", color="Black", fontsize=20)
            plt.title(f"Volume of {tickers}", color="Black", fontsize=25)
            plt.axhline(df_single[tickers]['Volume'].mean(), label="Average value of Volume", color="Blue",linestyle="--")
            plt.legend()
            plt.grid(True)
            plt.show()
        except ConnectionError as ec:
            print(f"Warning Code : {ec} , Connection Error , Please Try Again Later")
    def select_title(self):
        title=input("Which company are you interested in : ")
        df_single=yf.download(tickers=title,start=self._starttime,end=self._endtime,group_by="ticker",interval="1d")
        df_single.info()
class MakePredict(DatasforStockMarket):
    def __init__(self):
        super().__init__()
    def analyzestockmarket(self):
        title = input("Which company are you interested in : ")
        df = yf.download(tickers=title, start=self._starttime, end=self._endtime, interval="1d")
        df = df[['Close']].reset_index()
        df.columns = ['ds', 'y']
        df = df.dropna()
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=360)
        predict= model.predict(future)
        print(predict)
        model.plot(predict)
        plt.show()
    def select_title(self):
        title=[]
        for i in range(3):
            stock_code=input("Which company are you interested in : ")
            title.append(stock_code)
        try:
            data = yf.download(tickers=title, period="1y")['Close']
            data.dropna()
            if data.empty:
                print("No data found for the given tickers!")
                return
            for ticker in title:
                plt.plot(data.index, data[ticker], label=ticker)
            plt.grid(True)
            plt.title(f"{title[0]} , {title[1]} , {title[2]} Comparasion",fontsize=20,color="Black")
            plt.legend()
            plt.show()
        except KeyboardInterrupt as ki:
            print(f"Error Code : {ki} , Keybord Warning!")
    def show_infoghrapic(self):
        ticker=input("Which company are you interested in : ")
        data=yf.download(tickers=ticker,start=self._starttime,end=self._endtime,interval="1d")
        data=data[['Volume']].reset_index()
        data.columns=['ds','y']
        data.dropna()
        model=Prophet()
        model.fit(data)
        future=model.make_future_dataframe(periods=360)
        predict=model.predict(future)
        model.plot(predict)
        plt.show()
        print(predict)













































































