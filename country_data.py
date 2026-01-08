import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from abc import ABC,abstractmethod
from sympy.physics.units import years
class CountryData(ABC):
    def __init__(self):
        self._df=pd.read_csv("C:/Users\emre_\Downloads/archive (8)/2020-2025.csv")
    @abstractmethod
    def gdp_analyze(self):
        pass
    @abstractmethod
    def gdp_infographic(self):
        pass
class AnalyzeGdp(CountryData):
    def __init__(self):
        super().__init__()
    def gdp_analyze(self):
        top_gdp_for_2025=self._df.nlargest(10,'2025')[['Country','2025']]
        print(top_gdp_for_2025)
    def gdp_infographic(self):
        top_gdp_for_2025 = self._df.nlargest(10, '2025')[['Country', '2025']]
        common_value=top_gdp_for_2025['2025'].mean(numeric_only=True)
        plt.bar(top_gdp_for_2025['Country'],top_gdp_for_2025['2025'],color="Red")
        plt.axhline(common_value,color="Yellow",linestyle='--',label='Common Value')
        plt.legend()
        plt.grid(True)
        plt.show()
class GdpGrow(CountryData):
    def __init__(self):
        super().__init__()
    def gdp_research(self):
        value=input("Which country are you interested in : ")
        country=self._df['Country']
        control_in_dataframe=(country == value).any().any()
        if control_in_dataframe==True:
            my_country=self._df[self._df['Country']==value].iloc[0,1:]
            print(my_country)
            average_value=(my_country[4]/my_country[3])*100
            print(f"Average value of {value} is {average_value}")
        else:
            print("There is no country")
    def gdp_analyze(self):
        pass
    def gdp_infographic(self):
        pass
class PredictGdp(CountryData):
    def __init__(self):
        super().__init__()
    def make_a_prediction(self):
        years=np.array([2020,2021,2022,2023,2024,2025]).reshape(-1, 1)
        future_years=np.array([2026]).reshape(-1,1)
        country=input("Which country do you choose : ")
        country_data=self._df[self._df['Country']==country]
        if country_data.empty:
            print("This country wasn't fount in DataFrame!")
            return None
        gdp_values = country_data.iloc[0, 1:].values
        model=LinearRegression()
        model.fit(years,gdp_values)
        predictions=model.predict(future_years)
        print(f"{country} will have {predictions}$ in 2026")
    def gdp_analyze(self):
        pass
    def gdp_infographic(self):
        pass
