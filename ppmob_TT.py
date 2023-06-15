import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def load_article(article_url:  str, load_path: str):
    res = requests.get(article_url,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    article_tag = soup.select_one('div[id="main-content"]')
    #print(article_tag)
    print("============")
    article_tag.select_one('div[class="article-metaline"]').extract()
    for tag in article_tag.select('div'):
        tag.extract()
    print(article_tag.text)
    article_content = article_tag.text
    with open(load_path,'w',encoding="utf-8") as f:
        f.write(article_content)


if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/movie/M.1677862363.A.7AE.html"
    load_article(article_url,"./text.txt")