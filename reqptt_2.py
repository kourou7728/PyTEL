import requests
from bs4 import BeautifulSoup
url ='https://www.ptt.cc/bbs/joke/index.html'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

res = requests.get(url ,headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text,"html.parser")

# print(soup)

logo_tab = soup.select_one('a[id="logo"]')
logo_tab_a = soup.findAll("a",{"id":"logo"})
logo_tab_list = soup.select("a#logo")

print(logo_tab)
print(logo_tab_a)
print(logo_tab_list)
print(logo_tab_list[0])
print(logo_tab_list[0].text)
print("https://www.ptt.cc" + logo_tab_list[0]["href"])
print("===================")
title_tag_list = soup.select('div.title')
print("[tittle_tag_list[0]]",title_tag_list[0].text)
print("[tittle_tag_list[0].find('a')]",title_tag_list[0].find('a'))
print("[tittle_tag_list[0].find('a').text]",title_tag_list[0].find('a').text)
print("[tittle_tag_list[0].find('a')[\"href\"]",title_tag_list[0].find('a')['href'])
