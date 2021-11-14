import sqlite3
import requests
import json
import pandas as pd


api_key = "e2fb8840ca4abaa9d46e48188bbb23aff65603ad"
api_endpoint_countires = "https://calendarific.com/api/v2/countries"
api_endpoint = "https://calendarific.com/api/v2/holidays?api_key=e2fb8840ca4abaa9d46e48188bbb23aff65603ad&country=IN&year=2021"


json_data = requests.get(api_endpoint).json()
# print(json_data)
json_data_write = json.dump(json_data, open('holidays_list.json', "w"),indent=4) 

#data validation
def check_if_valid(df: pd.DataFrame) -> bool:
    #check if dataframe is empty
    if df.empty:
        print("data frame is empty")
        return False    
    #check for nulls
    if df.isnull().values.any():
        raise Exception("Null values found!")

data = json_data['response']
holiday_name = []
holiday_day = []
holiday_month = []
holiday_type = []

for holiday in data['holidays']:
     holiday_name.append(holiday["name"])
     holiday_day.append(holiday["date"]["datetime"]["day"])
     holiday_month.append(holiday["date"]["datetime"]["month"])
     holiday_type.append(holiday["type"][0])
         

holiday_dict = {
    "holiday_name" : holiday_name,
    "day" : holiday_day,
    "month" : holiday_month,
    "type" : holiday_type,              
}

holiday_df = pd.DataFrame(holiday_dict, columns=["holiday_name","day","month","type"])
print(holiday_df)

# VALIDATE
if check_if_valid(holiday_df):
    print("Data valid, proceed to load stage")

# LOAD
connection = sqlite3.connect('holidays.db')
cursor = connection.cursor()
#create a table
command1 = """Create Table if not exists holidays_list(holiday_name VARCHAR(300), day Integer, month Integer, type VARCHAR(300))"""
cursor.execute(command1)
print("Database created succesfully")

try:
    holiday_df.to_sql("holidays_list", connection, index=False, if_exists='append')
except:
        print("Data already exists in the database")


connection.close()
print("close database succesfully...")
