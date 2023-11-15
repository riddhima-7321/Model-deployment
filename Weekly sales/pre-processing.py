import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("Weekly sales.Weekly sales.csv")
df
unique_values = {}
for column in df.columns:
    unique_values[column] = df[column].unique()
for column, values in unique_values.items():
    print(column)
    print(values)
# WE CAN INFER we are given the following features!!

# Store:ahows the store number
# Date: shows the date in the format DD/MM/YY
# Weekly Sales: shows total sales in given week.
# Holiday Flag: a categorical feature shows if there was a holiday at that week(0:no holiday, 1:holiday)
# Fuel Price: Cost of fuel in the region
# CPI: Consumer price index (mostly used to measure inflation or deflation)
# Unemployment: unemployment rate
print(df.info())
print(df.isnull().sum())
df.describe()
df.duplicated().sum()
a=df.corr(numeric_only=True)
a
sns.heatmap(a,annot=True)
plt.show()
# OBSERVATIONS TILL NOW:-

# Total records=6435
# Total features=8
# Total Datatypes=8 7-numeric 1-object(data)(#will convert that)
# NULL values=0(all non-null values)
# Corelation between variables- with thh help of heatmap and the coorealtion matrix, we can easily interpret that there is no corelation between any two variables.
df.columns
df['Date'] = pd.to_datetime(df['Date'])
#verifying if datatype is changed!
df.Date.info()
#creating new columns to access month and year indivisually!
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
# df['Week'] = df['Date'].dt.isocalendar().week
df.head(5)
d3=df.groupby('Year',as_index=False)['Weekly_Sales'].mean()
d3
sns.histplot(df['Weekly_Sales']) 
#(distplot is deprecated in the updated version, use histplot or displot)
plt.bar(d3['Year'], d3['Weekly_Sales'])
plt.xlabel('year')
plt.ylabel('Weekly Sales')
plt.title('Bar Graph of weekly sales by year')
plt.show()

sns.scatterplot(x='Year',y='Weekly_Sales',data=df)

d1=df.groupby('Month',as_index=False)['Weekly_Sales'].mean()
d1

sns.lineplot(x='Month',y='Weekly_Sales',data=d1)

plt.bar(df['Month'], df['Weekly_Sales'])
plt.xlabel('Month')
plt.ylabel('Weekly_Sales')
plt.title('Bar Graph of weekly sales by month')

sns.barplot(x='Holiday_Flag', y='Weekly_Sales', hue='Year', data=df)
plt.xlabel('Holiday Flag')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales by Holiday Flag (Grouped by Year)')
plt.show()

sales_by_holiday = df.groupby('Holiday_Flag')['Weekly_Sales'].sum()
plt.pie(sales_by_holiday, labels=['No-Holiday', 'Holiday'])
plt.title('Weekly Sales by Holiday Flag')
plt.show()

d1=df.groupby('Store',as_index=False)['Weekly_Sales'].sum()
d1
sns.lineplot(x='Store',y='Weekly_Sales',data=d1)

sns.lineplot(x='Store',y='Weekly_Sales',data=df)

plt.bar(d1['Store'], d1['Weekly_Sales'])
plt.xlabel('Store')
plt.ylabel('Weekly_Sales')
plt.title('Bar Graph of weekly sales by Store')

sns.barplot(x='Store',y='Weekly_Sales',data=d1)
plt.xticks(rotation=90)
plt.figure(figsize=(20,10))
plt.show()

sns.barplot(x='Year',y='Weekly_Sales',hue='Holiday_Flag',data=df)

# plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Weekly_Sales'])
plt.xticks(rotation=90)
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('WEEKLY SALES')
plt.grid(True)
plt.show()


month_data = df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2010)]
plt.xticks(rotation=45)
plt.plot(month_data['Date'],month_data['Weekly_Sales'])

month_data = df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2011)]
plt.xticks(rotation=45)
plt.plot(month_data['Date'],month_data['Weekly_Sales'])

sns.barplot(x='Year',y='Fuel_Price',hue='Holiday_Flag',data=df)

sns.lineplot(x='Store',y='Unemployment',data=df)

plt.xticks(rotation=90)
sns.barplot(x='Store',y='Unemployment',data=df)

plt.xticks(rotation=90)
sns.barplot(x='Year',y='Unemployment',data=df)
# sns.barplot(df['Year'],df['Unemployment'])

sns.barplot(x='Month',y='Weekly_Sales',hue='Year',data=df)

print(df['Temperature'].unique())
sns.histplot(df['Temperature']) 

sns.scatterplot(x='Temperature',y='Weekly_Sales',data=df)
temperature_ranges = [-20, 20 , 40 ,60 ,80 ,100, 120] 
categories = [1, 2, 3, 4, 5, 6 ]
df['temp_category'] = pd.cut(df['Temperature'], bins=temperature_ranges, labels=categories,include_lowest=True)
df
d6=df.groupby('temp_category',as_index=False)['Weekly_Sales'].sum()
d6
sns.barplot(x='temp_category',y='Weekly_Sales',data=d6)
df['temp_category'].value_counts()

d7=df.groupby('Year',as_index=False)['CPI'].sum()
d7

sns.barplot(x='Year',y='CPI',data=d7)

sns.barplot(x='Month',y='CPI',data=d8)
