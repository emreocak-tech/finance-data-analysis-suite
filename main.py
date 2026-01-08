import time
from stockmarket import Analyze
from stockmarket import MakePredict
from country_data import AnalyzeGdp
from country_data import GdpGrow
from country_data import PredictGdp
from cars import AnalyzeCars
from cars import SimulationCars
from cars import MakePredictCars
from trendyol_scraping import TrendyolScraping
from trendyol_scraping import MySqlSave
from trendyol_scraping import MySqlSort
from trendyol_scraping import Telegram
from trendyol_scraping import CreateImage
from trendyol_scraping import ForexforDolar
from trendyol_scraping import ForexforEuro
from trendyol_scraping import BasicApp
import os
from dotenv import  load_dotenv
load_dotenv()
urls = [url.strip() for url in os.getenv("url_information").split(",") if url.strip()]
def main():
    while True:
        print("Welcome")
        print("You can:\n1=StockMarket Analyze\n2=Make a Predict about StockMarket\n3=Analyze GDP\n4=Research GDP for per country\n5=Make a Predict about GDP\n6=Cars Analyze\n7=Read information about Cars""\n8=Make a Predict about price of cars\n9=Show Product\n10=Record your products due to MySql\n11=Get Your products due to MySql\n12=Send a message for Telegram""\n13=Create A Image about price pf products\n14=Dolar\n15=Euro\n16=App\n17=Quit on system")
        decision=int(input("Choose a operation : "))
        if decision==1:
            stockmarket=Analyze()
            print("1=Analyze StockMarket\n2=Show Image\n3=Select Title")
            karar=int(input("Choose a operation : "))
            if karar==1:
                stockmarket.analyzestockmarket()
            elif karar==2:
                stockmarket.show_infoghrapic()
            elif karar==3:
                stockmarket.select_title()
            else:
                print("Try Again!")
        elif decision==2:
            stockmarket=MakePredict()
            print("1=Analyze StockMarket\n2=Show Image\n3=Select Title")
            karar = int(input("Choose a operation : "))
            if karar == 1:
                stockmarket.analyzestockmarket()
            elif karar == 2:
                stockmarket.show_infoghrapic()
            elif karar == 3:
                stockmarket.select_title()
            else:
                print("Try Again!")
        elif decision==3:
            gdp=AnalyzeGdp()
            print("1=Analyze GDP\n2=Show Image")
            karar = int(input("Choose a operation : "))
            if karar == 1:
                gdp.gdp_analyze()
            elif karar == 2:
                gdp.gdp_infographic()
        elif decision==4:
            gdp=GdpGrow()
            gdp.gdp_research()
        elif decision==5:
            gdp=PredictGdp()
            gdp.make_a_prediction()
        elif decision==6:
            cars=AnalyzeCars()
            print("1=Select a car\n2=Show Image\n3=Analyze Cars")
            karar=int(input("Choose a operation : "))
            if karar==1:
                cars.select_car()
            elif karar==2:
                cars.show_infographic()
            elif karar==3:
                cars.analyze_cars()
            else:
                print("Try Again!")
        elif decision==7:
            cars=SimulationCars()
            print("1=Select a car\n2=Show Image\n3=Analyze Cars")
            karar = int(input("Choose a operation : "))
            if karar == 1:
                cars.select_car()
            elif karar == 2:
                cars.show_infographic()
            elif karar == 3:
                cars.analyze_cars()
            else:
                print("Try Again!")
        elif decision==8:
            cars=MakePredictCars()
            cars.select_car()
        elif decision==9:
            trendyol=TrendyolScraping([], [], urls)
            print("1=Show Product\n2=Scraping")
            karar = int(input("Choose an operation : "))
            if karar == 1:
                trendyol.show_product()
            elif karar == 2:
                trendyol.scraping()
        elif decision==10:
            trendyol = TrendyolScraping([], [], urls)
            my_sql=MySqlSave(trendyol.get_name(),trendyol.get_price())
            my_sql.save_data()
        elif decision==11:
            trendyol = TrendyolScraping([], [], urls)
            my_sql=MySqlSort(trendyol.get_name(),trendyol.get_price(),url=None)
            my_sql.sort_data()
        elif decision==12:
            trendyol = TrendyolScraping([], [], urls)
            telegram=Telegram(trendyol.get_name(),trendyol.get_price(),url=None)
            telegram.send_messages()
        elif decision==13:
            trendyol = TrendyolScraping([], [], urls)
            image=CreateImage(trendyol.get_name(),trendyol.get_price(),url=None)
            image.create_image()
        elif decision==14:
            dolar=ForexforDolar()
            print("1=Price of Dolar\n2=Dolar to Turkish Lira")
            karar = int(input("Choose an operation : "))
            if karar==1:
                dolar.dolar()
            elif karar==2:
                dolar.dolar_to_tl()
        elif decision==15:
            euro=ForexforEuro()
            print("1=Price of Euro\n2=Euro to Turkish Lira")
            karar = int(input("Choose an operation : "))
            if karar==1:
                euro.euro()
            elif karar==2:
                euro.eur_to_tl()
        elif decision==16:
            app=BasicApp()
            app.saving_button()
        elif decision==17:
            print("You are quiting...")
            time.sleep(3)
            print("The operation is successful!")
            quit()
        else:
            print("Try Again!")
if __name__ == "__main__":
    main()






































