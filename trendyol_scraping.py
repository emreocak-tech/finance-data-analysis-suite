from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout, QMessageBox, QComboBox,QCheckBox
from PyQt5.QtGui import QIcon
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from networkx.algorithms.traversal import dfs_predecessors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
from mysql.connector import DatabaseError,Error
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
import requests
from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
from dotenv import load_dotenv
plt.style.use("seaborn-v0_8-darkgrid")
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")
exchange_rate_api=os.getenv("exchange_rate_api")
urls = [url.strip() for url in os.getenv("url_information").split(",") if url.strip()]
api_key=os.getenv("apı_key")
chat_id=os.getenv("chat_id")
password2=os.getenv("password2")
host2=os.getenv("host2")
database2=os.getenv("database2")
user2=os.getenv("user2")
class Product(ABC):
    def __init__(self,name,price,url):
        self._name=name if isinstance(name, list) else [name]
        self._price=price if isinstance(price, list) else [price]
        self.url=url
        self.__df=pd.DataFrame({"Name":self._name,"Price":self._price})
    @abstractmethod
    def show_product(self):
        pass
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def get_df(self):
        return self.__df
    def _update_df(self):
        self.__df=pd.DataFrame({"Name": self._name, "Price": self._price})
class TrendyolScraping(Product):
    def __init__(self,name,price,url):
        super().__init__(name,price,url)
        self.__headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    def show_product(self):
        print(self.get_df())
    def scraping(self):
        for url in urls:
            page=requests.get(url,headers=self.__headers,timeout=10)
            html_page=BeautifulSoup(page.content,"html.parser")
            name=html_page.find("h1",class_="product-title")
            price=html_page.find("div",class_="price-wrapper")
            self._name.append(name.text.strip())
            self._price.append(price.text.strip())
        self._update_df()
class ProductIllustrate(Product):
    def __init__(self,name,price,url):
        super().__init__(name,price,url)
    def show_product(self):
        print(self.get_df())
class MySqlSave(Product):
    def __init__(self,name,price):
        super().__init__(name,price,url=None)
    def show_product(self):
        pass
    def save_data(self):
        conn=mysql.connector.connect(user=user,database=database,password=password,host=host)
        cursor=conn.cursor()
        sql_query="INSERT INTO products(name,price) VALUES (%s,%s)"
        for n, p in zip(self.get_name(), self.get_price()):
            try:
                cursor.execute(sql_query, (n, p))
                conn.commit()
            except DatabaseError as de:
                print(f"Error: {de}")
        cursor.close()
        conn.close()
class MySqlSort(Product):
    #def __init__(self,name,price):
        #super().__init__(name,price,url=None)
    def show_product(self):
        pass
    def sort_data(self):
        conn = mysql.connector.connect(user=user, database=database, password=password, host=host)
        cursor = conn.cursor()
        try:
            sql_query="SELECT * FROM products"
            cursor.execute(sql_query)
            data=cursor.fetchall()
            for data in data:
                print(data)
        except DatabaseError as rty:
            print(f"Error Code : {rty}")
        finally:
            cursor.close()
            conn.close()
class Telegram(Product):
    def show_product(self):
        pass
    def send_messages(self):
        api=f"https://api.telegram.org/bot{api_key}/SendMessage"
        try:
            for n,p in zip(self.get_name(),self.get_price()):
                message="The Product of name : " + n + "\n\n\n" + "The Product of price : " + p
                requests.post(url=api,data={"chat_id":f"{chat_id}","text":message}).json()
        except ConnectionError as ce:
            print(f"Connection Wrong , Error Code : {ce}")
class CreateImage(Product):
    def show_product(self):
        pass
    def create_image(self):
        #plt.plot(self._update_df()["Name"],self._update_df()["Price"],color="Yellow",linewidth=3)
        plt.bar(self.get_df()["Price"],self.get_df()["Name"],color="Blue")
        plt.title("Products of Trendyol",color="Black",fontsize=20)
        plt.grid()
        plt.show()
class ForexforDolar:
    def __init__(self):
        self.__url=f"https://v6.exchangerate-api.com/v6/{exchange_rate_api}/latest/USD"
    def dolar(self):
        response=requests.get(url=self.__url,timeout=10)
        if response.status_code==200:
            data=response.json()
            print(f"1 dolar is {data['conversion_rates']['TRY']} TL!")
        else:
            print("Connection Error , PLease try again later")
    def dolar_to_tl(self):
        response=requests.get(url=self.__url,timeout=10)
        if response.status_code==200:
            amount=float(input("How much money do you want to calculate : "))
            data=response.json()
            result=amount*data['conversion_rates']['TRY']
            print(f"{amount} dolar is {result} TL!")
        else:
            print("Connection Error , PLease try again later")
class ForexforEuro:
    def __init__(self):
        self.__url=f"https://v6.exchangerate-api.com/v6/{exchange_rate_api}/latest/EUR"
    def euro(self):
        response=requests.get(url=self.__url,timeout=10)
        if response.status_code==200:
            data = response.json()
            print(f"1 euro is {data['conversion_rates']['TRY']} TL!")
        else:
            print("Connection Error , PLease try again later")
    def eur_to_tl(self):
        response=requests.get(url=self.__url,timeout=10)
        if response.status_code==200:
            data=response.json()
            amount=float(input("How much money do you want to calculate : "))
            result = amount * data['conversion_rates']['TRY']
            print(f"{amount} euro is {result} TL!")
        else:
            print("Connection Error , PLease try again later")
class BasicApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.user_input = QLineEdit()
        self.user_input2 = QLineEdit()
        self.user_input3 = QLineEdit()
        self.check_box = QCheckBox("I read contract of user")
        self.form_layout = QFormLayout()
        self.form_layout.addRow("You have to give name of company : ", self.user_input)
        self.form_layout.addRow("You have to give code of company : ", self.user_input2)
        self.form_layout.addRow("You have to give price of share : ", self.user_input3)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.form_layout)
        button = QPushButton("Send")
        button.clicked.connect(self.saving_button)  # sadece bağla, çağırma!
        self.vbox.addWidget(button)
        self.vbox.addWidget(self.check_box)
        self.window.setLayout(self.vbox)
        self.window.setWindowTitle("StockMarket App")
        self.window.setWindowIcon(QIcon("Copilot_20250907_153412.png"))
        self.window.showMaximized()
        sys.exit(self.app.exec_())
    def saving_button(self):
        stockmarket_name = self.user_input.text().strip()
        stockmarket_code = self.user_input2.text().strip()
        purchase_price = self.user_input3.text().strip()
        time = datetime.datetime.now()
        if not self.check_box.isChecked():
            QMessageBox.warning(self.window,"Error","You can not log in because You have not accepted contract of user")
            return
        if not stockmarket_name:
            QMessageBox.warning(self.window,"Error","You must give stockmarket's name!")
            return
        elif not stockmarket_code:
            QMessageBox.warning(self.window,"Error","You must give a float data for code!")
            return
        elif not purchase_price:
            QMessageBox.warning(self.window, "Error", "You must give a float data for price!")
            return
        try:
            conn = mysql.connector.connect(user=user2,host=host2,password=password2,database=database2)
            cursor = conn.cursor()
            sql_query = "INSERT INTO new_table(name,code,price,time) VALUES (%s,%s,%s,%s)"
            values = (stockmarket_name, stockmarket_code, purchase_price, time)
            cursor.execute(sql_query, values)
            conn.commit()
            QMessageBox.information(self.window,"Successful","Data saved")
        except Error as error:
            QMessageBox.warning(self.window,"Error",f"Database Error : {error} , Please try again!")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    product = TrendyolScraping([], [], urls)
    product2=MySqlSave(product.get_name(),product.get_price())
    product.scraping()
    #product.show_product()
    #product2.save_data()
    product3=MySqlSort(product.get_name(),product.get_price(),url=None)
    #product3.sort_data()
    product4=Telegram(product.get_name(),product.get_price(),url=None)
    #product4.send_messages()
    #product5=CreateImage(product.get_name(),product.get_price(),url=None)
    #product5.create_image()
    product6=ForexforDolar()
    #product6.dolar()
    #product6.dolar_to_tl()
    product7=ForexforEuro()
    #product7.euro()
    #product7.eur_to_tl()
    #app=BasicApp()
    #app.saving_button()

































































































































































