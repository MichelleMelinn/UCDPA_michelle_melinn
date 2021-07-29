# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#final project
import pandas as pd
df=pd.read_csv("AMZN (1).csv")
print(df.info())
#no missing values
#datatype is a string
#7 columns
#6077 rows

print(df.isnull().sum())
#no true returned therefore no missing values

print(df.head())
#starts in 1997
print(df.tail())
#finishes in 2021 so a 24 year long collection of data
print(df.info())
print(df.describe())

#sorting and subsetting
high_price = df.sort_values("High",ascending=False)
print(high_price.head())
#subset high greater than mean of 488.839034
gtr_mean = df[df["High"] > 488.839034]
print(gtr_mean)

#sort AMZN df by above average high price in descending and year in descending

high_price_yr = df.sort_values(["High","Date"],ascending= [False,False])
high_price_yr = [["High", "Date"]]
print(high_price_yr)

#get volume of stocks traded in decending order with date
volume_des = df.sort_values("Volume",ascending= False,)
print(volume_des)
#Can see that highest volume of stocks traded in 2007 making up 104329200,
print(volume_des.tail())
#Can see that lowest volume of stocks traded in 1997 making up only 487200

#identify min opening price
min_op_price = min("Open")
#identify min opening price index
min_index = "Open".index(min_op_price)
#identify the year with the smallest opening price for amazon stocks
min_yr = "Date"[min_index]
print(min_yr)
#1997 also had lowest opening price for amazon stocks which is consistent as it is first year
#But what about max

#identify max opening price
max_op_price = max("Open")
#identify max opening price index
max_index = "Open".index(max_op_price)
#identify the year with the largest opening price for amazon stocks
max_yr = "Date"[max_index]
print(max_yr)

high_op_price = df.sort_values("Open",ascending=False)
print(high_op_price.head())
#7th July 2021 saw highest opening price
#in 2020 highest opening price was on 2nd of September

#Dropping Duplicates
same_date = df.drop_duplicates(subset = "Date")
print(same_date)



#1. sort AMZN df by date
df = df.sort_values("Date")
#2. Get the cumulative sum of monthly volume

#Use boolean conditions to subset volume of stocks sold for years 2019 and 2020

vol_bool = df[(df["Date"] >= "2019-01-01") & (df["Date"] <= "2020-12-31")]
print(vol_bool)

#Now set date as an index and sort the index

vol_ind = df.set_index("Date").sort_index()


#Now use .loc[] to subset volume for rows in 2019 and 2020
print(vol_ind.loc["2019-01-01":"2020-12-31","Volume"])

#now see if Jan 2020 volume greater than Jan 2019
#using Datetimes
vol_ind_19 = vol_ind.loc["2019-01-01":"2019-12-31","Volume"]
print(vol_ind_19)
vol_ind_20 = vol_ind.loc["2020-01-01":"2020-12-31","Volume"]
print(vol_ind_20)
vol_ind["vol_ind_19"] = vol_ind_19
vol_ind["vol_ind_20"] = vol_ind_20

print(vol_ind["vol_ind_19"].sum())
print(vol_ind["vol_ind_20"].sum())
#sum of volume sold in 2019 is 974,650,100
#sum of volume sold in 2020 is 124,754,0700
#Appears more sold in 2020 than 2019 despite covid breakthrough
#but what about mean for each year

print(vol_ind["vol_ind_19"].mean()) #3867659.126984127
print(vol_ind["vol_ind_20"].mean()) #4930990.909090909
print(vol_ind["vol_ind_19"].median()) #3475800.0
print(vol_ind["vol_ind_20"].median()) #4526600.0
#On March 11 2020 W.H.O declared coronavirus outbreak a global pandemic
#so it may be more useful to compare March 2019/2020 stats for both volume and low

#Is this the case every year?
#It might be easier to depict this graphically

#import matplotlib.pyplot as plt
#df.plot(x="Date", y="Volume", color = 'red',rot=90)
#plt.xlabel("Date"), plt.ylabel("Volume"),
#plt.title("Volume of Amazon stocks sold 1997-2021")
#plt.show()

import matplotlib.pyplot as plt
vol_sold_by_date = df.groupby("Date")["Volume"].sum()
vol_sold_by_date.plot( kind ="line", rot = 45, title = "Daily volume of Amazon Stocks traded by date (1997-2021")
plt.xlabel("Date"),
plt.ylabel("Daily volume of Stocks traded"),
plt.show()


#shows no major surge around 2020
import matplotlib.pyplot as plt
df.plot( x="High", y= "Volume", kind= "scatter",color = "yellowgreen", title = ("Scatterplot of the relationship between daily volume of Amazon stocks traded and daily maximum price of Amazon stocks"))
plt.show()

#or with a pivot table

vol_by_date_tab = df.pivot_table(values="Volume", index = ["Date"])
print(vol_by_date_tab)
print(vol_by_date_tab.loc["2019-03-01":"2019-03-31", "Volume"].min()-
      (vol_by_date_tab.loc["2020-03-01":"2020-03-31", "Volume"].min())) #1,801,600 more AMZN stocks sold in March 2020 than March 2019

print(vol_by_date_tab.loc["2019-02-01":"2019-02-31", "Volume"].min()-
      (vol_by_date_tab.loc["2020-02-01":"2020-02-31", "Volume"].min())) #104,600 more AMZN stocks sold in Feb 2019 than Feb 2020

#Can see that March 2020 saw a huge surge in the vol of stocks sold,
#we would also expect the high price of stocks to rise also:

low_by_date_tab = df.pivot_table(values="High", index = ["Date"])
print(low_by_date_tab)
print(low_by_date_tab.loc["2019-03-01":"2019-03-31", "High"].max()-
      (low_by_date_tab.loc["2020-03-01":"2020-03-31", "High"].max())) #172.57995600000004 in diff

print(low_by_date_tab.loc["2019-02-01":"2019-02-31", "High"].max()-
      (low_by_date_tab.loc["2020-02-01":"2020-02-31", "High"].max())) #512.8898920000001 in diff

#These results are inconsistent as we would expect the High price of stocks
#from March 2019 to March 2020 to be greater than the diff in the high
#price of stocks from feb 2019 to feb 2020 as the volume increased

#Introduce new dataset for Netflix
import pandas as pd
NFLX=pd.read_csv("NFLX (1).csv")
print(NFLX.info())
#no missing values
#datatype is a string
#7 columns same as AMZN

print(NFLX.isnull().sum())
print(NFLX.head())
#starts in 2002
print(NFLX.tail())
#23-May-2002 to 3-Aug-2020
print(NFLX.info())
print(NFLX.describe())

#merge on volume
vol_AMZN_NFLX = df.merge(NFLX, on= 'Volume', suffixes = ('_AMZN','_NFLX'))
print(vol_AMZN_NFLX) #124 rows, 13 columns
print(vol_AMZN_NFLX.shape) #124 rows, 13 columns

print(vol_AMZN_NFLX["Volume"].max()) #40,265,400
print(vol_AMZN_NFLX["Volume"].mean()) #7,198,652.419354838

import matplotlib.pyplot as plt

AMZN_sold_by_date = df.groupby("Date")["Volume"].sum()
NFLX_sold_by_date = NFLX.groupby("Date")["Volume"].sum()

AMZN_sold_by_date.plot(kind = "line", alpha = 1, rot=45, color = "blue")
NFLX_sold_by_date.plot(kind = "line", alpha = 0.5, rot =45, color = "cyan",title= "Volume of Amazon stocks vs. Netflix stocks traded over time"),
plt.xlabel = ("Date")
plt.ylabel = ("Volume")
plt.legend(["Amazon", "Netflix"])
plt.show()



