import requests
from bs4 import BeautifulSoup

url = "https://www.8591.com.tw/mallList-list.html?searchGame=859&searchServer=&searchType=&searchKey=33%e6%99%ba%e6%bb%85%e9%be%8d&buyStatus=&childSearchType=&priceSort=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

all_products = []  # 儲存所有商品資訊的串列

for page in range(1, 6):  # 總共有5頁
    # 構造每個頁面的網址
    page_url = url + f"&pageNo={page}"

    # 使用 requests 套件取得網頁原始碼
    response = requests.get(page_url, headers=headers)

    # 將原始碼轉成 BeautifulSoup 物件，方便擷取資訊
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有商品的區塊
    product_divs = soup.find_all("div", class_="goods-list clearfix")
    print(product_divs.text)

    # 讀取每個商品的資訊
#     for product_div in product_divs:
#         product_name = product_div.find("h3").text.strip()
#         product_price = product_div.find("span", class_="price").text.strip()
#         product_link = product_div.find("a", class_="goods_link")["title"]
#         all_products.append({"name": product_name, "price": product_price, "link": product_link})
#
# # 列印所有商品資訊
# for product in all_products:
#     print("商品名稱：", product["name"])
#     print("商品價格：", product["price"])
#     print("商品連結：", product["link"])
#     print()
