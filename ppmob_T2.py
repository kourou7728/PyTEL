import os.path

import requests
from bs4 import BeautifulSoup
from ppmob_TT import load_article

load_folder = "articles"
if not os.path.exists("./articles"):
    os.mkdir("./articles")

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
for i in range (0,5):
    res = requests.get(url ,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    title_tag_list = soup.select('div.title')
    #print(title_tag_list)

    for TTG in title_tag_list:

        if TTG.select_one('a'):
            title_name = title_name = TTG.select_one('a').text
            title_href = TTG.find('a')['href']
            article_url = "https://www.ptt.cc" + TTG.select_one('a')["href"]
            try:
                load_article(
                article_url=article_url,
                load_path = f"./{load_folder}/{title_name}.txt"
                             )
            except FileExistsError:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_floder}/{title_name.replace('/', '-')}.txt"
                             )
            except OSError:
                pass
            
            print(title_name)
            print('https://www.ptt.cc'+title_href)
        else:
            print("Title is empty")
        print("=======")

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]