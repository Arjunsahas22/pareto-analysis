import pandas as pd
import numpy as np
df1=pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/OnlineRetail/master/order_items.csv")
df2=pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/OnlineRetail/master/products.csv")
df3=pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/OnlineRetail/master/product_category_name.csv")
#print(df1.columns)
#print(df2.columns)
#print(df3.columns)
df1=df1[["order_id","product_id","price"]]
#print(df1.columns)
df2=df2[["product_id","product_category_name"]]
df3=df3.rename(columns={"1 product_category_name":"product_category_name","2 product_category_name_english":"product_category"})
print(df3.columns)
data=pd.merge(df1,df2,on="product_id",how="left")
#print(data.columns)
data=pd.merge(data,df3,on="product_category_name",how="left")
print(data)
#missing data
for col in data.columns:
    pct_mis=np.mean(data[col].isnull())
    print("{} has {}%".format(col,round(pct_mis*100)))

data["product_category"]=data["product_category"].fillna("Unknown")

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

groupby="product_category"
column="price"

data=data[["price","product_category"]]
data.set_index(data["product_category"])
df=data.groupby(groupby)[column].sum().reset_index()
df=df.sort_values(by=column,ascending=False)
df["cummpercent"]=df[column].cumsum()/df[column].sum()*100
print(df)

fig,ax=plt.subplots(figsize=(20,5))
ax.bar(df[groupby],df[column])
ax2=ax.twinx()
ax2.plot(df[groupby],df["cummpercent"],marker="D")
ax.tick_params(axis="x",rotation=90)
plt.show()








