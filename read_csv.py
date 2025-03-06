import pandas as pd  # pandasライブラリを使う
import matplotlib.pyplot as plt  # 既に書いてあるなら追加しなくてOK

# 日本語表示用フォントの設定
plt.rcParams["font.family"] = "MS Gothic"

# CSVファイルを読み込む
df = pd.read_csv("sales_data.csv", encoding="utf-8")

# 読み込んだデータを表示
print(df)
import pandas as pd  # pandasライブラリを使う
import matplotlib.pyplot as plt  # matplotlibを使ってグラフを作成

# CSVファイルを読み込む
df = pd.read_csv("sales_data.csv", encoding="utf-8")

# 商品ごとの売上金額を集計
product_sales = df.groupby("商品名")["売上金額"].sum()

# 商品ごとの売上金額を棒グラフで表示
product_sales.plot(kind='bar', color='skyblue')

# グラフのタイトルを設定
plt.title("商品別売上金額")

# x軸のラベルを設定
plt.xlabel("商品名")

# y軸のラベルを設定
plt.ylabel("売上金額")

# グラフを表示
plt.show()
