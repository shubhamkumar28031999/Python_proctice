import pandas as pd
# import workbook
df = pd.read_csv("reading_writing_csv\stock_data.csv")
df.to_csv("new2.csv",index=False,columns=['tickers','eps'],header=False)
print(df)
print("-----------====================----------------------")
df1 = pd.read_csv("new2.csv")
print(df1)
print("-----------====================----------------------")
# df2 = pd.read_excel("reading_writing_csv\stock_data.xlsx")
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})
# with pd.ExcelWriter('stocks_weather.xlsx') as writer:
#     df_stocks.to_excel(writer, sheet_name="stocks")
#     df_weather.to_excel(writer, sheet_name="weather")

def convert_cell(cell):
    if cell=='n.a.':
        return 'sam walton'
    else:
        return cell
df = pd.read_csv('reading_writing_csv\stock_data.csv',converters={'people':convert_cell})
print(df)