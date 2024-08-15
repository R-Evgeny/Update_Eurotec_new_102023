import pandas as pd
import re


file_path = "Остатки.xlsx"


df = pd.read_excel(file_path,)

df = df.rename(columns={
        "Unnamed: 0": "name_uk",
        "Unnamed: 3": "quantity"
    })
df = df[['name_uk', 'quantity']]
df = df.loc[10:]
df["sku"] = df["name_uk"].apply(lambda x: re.search(r"арт\. (.*?)( \(шт\.\))", x).group(1) if re.search(r"арт\. (.*?)( \(шт\.\))", x) else "")
df = df.query('sku != ""')

print(df)

#df.to_csv('ostatki_1c.csv')
df.to_excel('local_stock.xlsx', index=False)
