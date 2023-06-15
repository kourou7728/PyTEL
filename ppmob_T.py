import requests
from bs4 import BeautifulSoup
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
            print(title_name)
            print('https://www.ptt.cc'+title_href)
        else:
            print("Title is empty")
        print("=======")

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]