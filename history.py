import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
import json
import yfinance as yf

def main():
   
   while True: 

    print("****************************************************"+
     "\n"+"          Welcome to Portfolio Analyzer"+
     "\n"+"****************************************************"+"\n\n")
    print("Please select an option:"+"\n"+
          "1. Add a new company"+"\n"+
          "2. Buy or sell stocks"+"\n"+
          "3. View all records"+"\n"+
          "4. Get a briefing"+"\n"+
          "5. Compare elasticity of two companies"+"\n"+
          "6. Predict future performance"+"\n"+
          "7. Exit")
    
    x()

    def x():
      
      try:
            choice = int(input("Enter your choice (1-7): "))

            match choice:

                case 1:

                    print("You selected: Add a new company")
                    addnewstock()

                case 2:

                    print("You selected: Buy or sell stocks")
                    addstock()

                case 3:

                    name=input("Enter the stock name:")
                    filename="/Users/hirdaybhandal/Desktop/Python Projects/portfolio_optimizer.py/stock_history/" + name + ".json"

                    df=pd.read_json(filename)
                    print(df.to_string())

                case 4:

                    print("You selected: Get a briefing")

                    name=input("Enter the stock name:")
                    give_briefing(name)

                case 5:

                    print("You selected: Compare elasticity of two companies")
                    comp_elasticity()

                case 6:

                    print("You selected: Predict future performance")

                case 7:

                    print("Exiting Portfolio Analyzer. Goodbye!")
                    return
                
                case _:

                    print("Invalid choice. Please select a number between 1 and 7.")

      except ValueError:
                 
                 print("Invalid input.")
                 x()
            


def addnewstock():

    try:

        date =str(datetime.datetime.now())
        stock_name = input("Enter Stock Name:")
        value = float(input("Enter Per Unit Value:"))
        buy = float(input("Number Of Shares Bought:"))
        filename = "/Users/hirdaybhandal/Desktop/Python Projects/portfolio_optimizer.py/stock_history/" + stock_name + ".json"


        stock_data= {
            "history":
            {
                "date":date,
                "value":value,
                "sell": 0,
                "total_stocks": buy,
                "holding": value * buy * -1
            }
        }

        file=open(filename,'w')
        json.dump(stock_data,file,indent=4)

        print("Stock file created successfully.")

    except ValueError:

        print("Please enter a numeric value.")
        addnewstock()



def addstock():

    try:

        date =str(datetime.datetime.now())
        stock_name = input("Enter Stock Name:")
        value = float(input("Enter Per Unit Value:"))
        buy = float(input("Number Of Shares Bought:"))
        sell = float(input("Number Of Shares Sold:"))
        filename = "/Users/hirdaybhandal/Desktop/Python Projects/portfolio_optimizer.py/stock_history/" + stock_name + ".json"

        file=open(filename,'r')
        stock_data = json.load(file)

        last_transc=stock_data["history"][-1]
        total_stocks = last_transc["total_stocks"] + buy - sell
        holding = last_transc["holding"] + value * (sell - buy)

        stock_data["history"].append({
            "date": date,
            "value": value,
            "buy": buy,
            "sell": sell,
            "total_stocks": total_stocks,
            "holding": holding
        })

        file=open(filename,'w')
        json.dump(stock_data, file, indent=4)

        if total_stocks < 0:
            print("You do not have enough units!")
            return
        
        print("Transaction added successfully.")

    except ValueError:

        print("Please enter a numeric value such as 4.6, 5.1 & 4.0 .")
        addstock()

    except FileNotFoundError:

        print("Stock file not found.Please create a new stock using the 'addnewstock' function.")

    except IndexError:

        print("Stock history file is incomplete or corrupted. Please check the file.")
    


def give_briefing(stock_name):

    try:
        
        filename = "/Users/hirdaybhandal/Desktop/Python Projects/portfolio_optimizer.py/stock_history/" + stock_name + ".json"
        file=open(filename,'r')
        stock_data = json.load(file)

        history = stock_data["history"]
        if not history:
            print("No data available.")
            return

        high, low, bhighvol, shighvol = None, None, None, None
        dayinc, invest = 0, 0

        for i, entry in enumerate(history):
            if i == 0:
                print("First Exchange On:", entry["date"], "\tNo. of Shares Bought:", entry["buy"], "\tAt Unit Value:", entry["value"])
                high, low = entry, entry
                bhighvol, shighvol = entry, entry

            if entry["value"] > high["value"]:
                high = entry
            if entry["value"] < low["value"]:
                low = entry
            if entry["buy"] > bhighvol["buy"]:
                bhighvol = entry
            if entry["sell"] > shighvol["sell"]:
                shighvol = entry
            invest += entry["buy"] * entry["value"]

            if i > 0 and entry["value"] > history[i - 1]["value"]:
                dayinc += 1

        last_entry = history[-1]
        roi = (invest - (last_entry["total_stocks"] * last_entry["value"])) / invest * 100

        print("Last Exchange On:", last_entry["date"], "\tAt Unit Value:", last_entry["value"], "\tCurrent Holding:", last_entry["total_stocks"])
        print("Highest Value Recorded:", high["value"], "\tDate:", high["date"])
        print("Lowest Value Recorded:", low["value"], "\tDate:", low["date"])
        print("Highest Volume Bought In A Day:", bhighvol["buy"], "\tDate:", bhighvol["date"])
        print("Highest Volume Sold In A Day:", shighvol["sell"], "\tDate:", shighvol["date"])
        print("ROI:", str(roi) + "%\nTotal Days Recorded:", len(history), "\tDays Value Increased:", dayinc)

        graph(history)

    except FileNotFoundError:

        print("Stock file not found. Please check the stock name and try again.")
        name=input("Enter the stock name:")
        give_briefing(name)

    except ValueError:

        print("Invalid data format in the file. Please ensure the stock file has correct data.")



def graph(history):

    dates = []
    values = []

    for entry in history:
        
        dates.append(entry["date"])
        values.append(entry["value"])

    plt.figure(figsize=(9, 9))
    plt.plot(dates, values, marker='o', linestyle='-', color='b', label="Stock Value")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Stock Value Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()



def comp_elasticity():

    try:
           
        print("Enter the ticker names of the companies:-")
        n1=input("Nmae 1:").upper()
        n2=input("Name 2:").upper()

        while True:
            try:
                years = int(input("Enter the number of years to compare (default is 10): ") or 10)
                break
            except ValueError:
                print("Please enter a valid number of years.")

        ticker=[n1,n2]
        et = datetime.datetime.now()
        st = et - timedelta(days=365 * years)
        df = pd.DataFrame()
    
        for tick in ticker:
            data =yf.download(tick,st,et)
            df[ticker] = data['Close']

        correlation = df.corr()
        corr_value = correlation.loc[n1, n2]

        print("The correlation value is:"+str(corr_value))

        if corr_value > 0:
            print(f"The stocks have been showing elasticity from past 10 years.")
            if corr_value > 0.8:
                print(f"The stocks have  been showing high elasticity from past 10 years.")
        if corr_value < 0:
            print(f"The stocks have  been showing corss-elasticity from past 10 years.")
            if corr_value < -0.8:
                print(f"The stocks have  been showing high cross-elasticity from past 10 years.")

        plt.figure(figsize=(10, 6))
        for tick in ticker:
            plt.plot(df.index, df[tick], label=tick)  

        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.title(f"Stock Price Over Time for {n1} and {n2}")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except ValueError as ve:

        print(f"Please enter a valid ticker.")
        comp_elasticity()

    except Exception as e:

        print(f"Please enter a valid ticker.")
        comp_elasticity()



def pred_future():

    try:
        
        ticker = input("Enter the stock ticker: ").upper()

        
        et = datetime.now()
        st = et - timedelta(days=180)  
        data = yf.download(ticker, st, et)

        if data.empty:
            print("No data available for the specified ticker. Please try another ticker.")
            return

        data = data[['Close']].dropna()

        if len(data) < 20:
            print("Not enough data to make a prediction. Please try another stock.")
            return

        data['10_MA'] = data['Close'].rolling(window=10).mean()  
        data['20_MA'] = data['Close'].rolling(window=20).mean()  

        data['EMA'] = data['Close'].ewm(span=10, adjust=False).mean()  

        predicted_price = data['EMA'].iloc[-1]

        plt.figure(figsize=(12, 6))
        plt.plot(data.index[-50:], data['Close'][-50:], label="Closing Prices", color="blue")
        plt.plot(data.index[-50:], data['10_MA'][-50:], label="10-Day Moving Average", color="orange")
        plt.plot(data.index[-50:], data['20_MA'][-50:], label="20-Day Moving Average", color="green")
        plt.axhline(y=predicted_price, color='red', linestyle='--', label="Predicted Price (Next Day)")
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.title(f"Stock Price Prediction for {ticker} using EMA")
        plt.legend()
        plt.grid(True)
        plt.show()

        print(f"The predicted stock price for {ticker} on the next day is approximately: {predicted_price:.2f}")

    except ValueError:

        print("Invalid input. Please ensure you enter the correct ticker symbol.")
        pred_future()

    except Exception as e:

        print(f"An error occurred: {e}")
        pred_future()

