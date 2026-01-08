import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from abc import ABC,abstractmethod
import logging
from dotenv import load_dotenv
import os
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
load_dotenv()
csv_path =os.getenv("my_csv_path")
plt.style.use("seaborn-v0_8-darkgrid")
class Cars(ABC):
    def __init__(self):
        self._df=pd.read_csv(csv_path)
    @abstractmethod
    def select_car(self):
        pass
    @abstractmethod
    def show_infographic(self):
        pass
    @abstractmethod
    def analyze_cars(self):
        pass
class AnalyzeCars(Cars):
    def __init__(self):
        super().__init__()
    def select_car(self):
        print(self._df.columns)
        manufacturer=input("Which manfacturer do you want to research : ")
        data_manufacturer=self._df['Manufacturer']
        model=input("Which model do you like : ")
        control_in_manufacturer=(manufacturer==data_manufacturer).any().any()
        data_model=self._df['Model']
        control_in_model=(data_model==model).any().any()
        if (control_in_model==True) and (control_in_manufacturer==True):
            my_car=self._df[self._df['Manufacturer']==manufacturer].iloc[0,1:]
            print(my_car)
        else:
            print("There are no cars")
        print(self._df['Manufacturer'].unique())
    def show_infographic(self):
        bmw_cars=len(self._df[self._df['Manufacturer']=='BMW'])
        print(f"There are {bmw_cars} cars of BMW in the Dataframe")
        ford_cars=len(self._df[self._df['Manufacturer']=='Ford'])
        print(f"There are {ford_cars} cars of Ford in the Dataframe")
        porshe_cars=len(self._df[self._df['Manufacturer']=='Porsche'])
        print(f"There are {porshe_cars} cars of Porsche in the Dataframe")
        toyota_cars=len(self._df[self._df['Manufacturer']=='Toyota'])
        print(f"There are {toyota_cars} cars of Toyota in the DataFrame")
        volkwagen_cars=len(self._df[self._df['Manufacturer']=='VW'])
        print(f"There are {volkwagen_cars} cars of Volkswagen in the DataFrame")
        plt.plot(self._df['Manufacturer'].unique(),[ford_cars,porshe_cars,toyota_cars,volkwagen_cars,bmw_cars],color='Red',linewidth=3)
        plt.axhline(12500,linestyle='--',linewidth=5,color="Blue",label="Average Value")
        plt.legend()
        plt.grid()
        plt.show()
    def analyze_cars(self):
        common_value = self._df['Mileage'].mean()
        print(f"Average mileage is {common_value} in the DataFrame")
        average_value=self._df['Price'].mean()
        print(f"Average price is {average_value} in the DataFrame")
class SimulationCars(AnalyzeCars):
    def __init__(self):
        super().__init__()
    def select_car(self):
        selection=self._df.nlargest(10,['Price'])[['Manufacturer','Price']]
        print(selection)
    def show_infographic(self):
        plt.scatter(self._df['Engine size'],self._df['Price'])
        plt.xlabel("Engine Size",color="Black",fontsize=20)
        plt.ylabel("Price",color="Black",fontsize=20)
        plt.title("Relationship of Motor Size and Price",color="Black",fontsize=20)
        plt.grid()
        plt.show()
    def analyze_cars(self):
        plt.scatter(self._df['Mileage'].head(100),self._df['Price'].head(100))
        plt.xlabel("Mileage",color="Black",fontsize=20)
        plt.ylabel("Price",color="Black",fontsize=20)
        plt.title("Relationship of Mileage and Price",color="Black",fontsize=25)
        plt.grid()
        plt.show()
class MakePredictCars(Cars):
    def __init__(self):
        super().__init__()
    def select_car(self):
        x = input("Which car do you want to analyze : ")
        filtered_data = self._df[self._df['Model'] == x]
        if filtered_data.empty:
            print(f"Model '{x}' not found in dataset!")
            return
        X = np.array([filtered_data['Year of manufacture'],filtered_data['Mileage']]).T
        Y = np.array(filtered_data['Price'])
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
        model=LinearRegression()
        model.fit(X_train,Y_train)
        year=int(input("Which year do want to analyze : "))
        mileage=int(input("How much kilometres the car go : "))
        prediction=model.predict([[year,mileage]])
        prediction2=int(prediction[0])
        test_predictions = model.predict(X_test)
        mse = mean_squared_error(Y_test, test_predictions)
        r2 = r2_score(Y_test, test_predictions)
        print(f"This car will become {prediction2} $ in {year}!")
        print(f"Common error : {np.sqrt(mse)}")
        print(f"Score of the model is {r2}")
    def show_infographic(self):
        pass
    def analyze_cars(self):
        pass