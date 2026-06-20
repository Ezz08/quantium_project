import pandas as pd

#read the 3 files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

#merge the 3 files
df = pd.concat([df1, df2, df3])

#specifying the product
df = df[df["product"] == "pink morsel"]

#remove $ symbol
df["price"] = df["price"].str.replace("$", "", regex = False)
df["price"] = df["price"].astype(float)

#turn quantity into int
df["quantity"] = df["quantity"].astype(int)

# calculating the sale
df["sales"] = df["price"] * df["quantity"]

#save the meta data we want
df = df[["sales", "date", "region"]]

#save the final shape
df.to_csv("formatted_sales_data.csv", index = False)