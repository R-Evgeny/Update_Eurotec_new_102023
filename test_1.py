import pandas as pd
import re


file_path = "Остатки.xls"

df = pd.read_excel(file_path)

df = df.rename(columns={
        "Unnamed: 0": "name",
        "Unnamed: 2": "order",
        "Unnamed: 3": "quantity"
    })
df = df[['name', 'order', 'quantity']]
df = df.loc[7:]
df["sku"] = df["name"].apply(lambda x: re.search(r"арт\. (.*?)( \(шт\.\))", x).group(1) if re.search(r"арт\. (.*?)( \(шт\.\))", x) else "")


df.to_csv('ostatki_1c.csv')



# df = pd.read_csv('ostatki_1c.csv')
# df["code"] = df["name"].str.extract("(?<=арт. )(.*?)(?= (шт.))")
#
# print(df)

# import pandas as pd
# import re
#
# df = pd.DataFrame({
#     "name": ["Franke TURBO ELITE TE-50 (134.0535.229), арт. 134.0535.229 (шт.)",
#              "Franke TURBO ELITE TE-75 (134.0535.241), арт. 134.0535.241 (шт.)",
#              "In Sink Erator Evolution 250, арт. Evolution 250 (шт.)",
#              "Teka TR 750 (115890014), арт. 115890014 (шт.)"],
# })
#
# # Використовуємо .apply для вибірки значень та запису у стовпчик "articul"
# df["articul"] = df["name"].apply(lambda x: re.search(r"арт\. (.*?)( \(шт\.\))", x).group(1) if re.search(r"арт\. (.*?)( \(шт\.\))", x) else "")
#
print(df)