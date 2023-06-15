import requests
import pprint
from bs4 import BeautifulSoup
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

data_str ="""action : csco_ajax_load_more page:2 posts_per_page :　30"""

data = {row.split(": ")[0]: row.split(": ")[1] for row in data_str.split("\n")}

res = requests.post(url,headers=headers,data=data)
json_data = res.json()
# pprint.pprint(res.json())
html_str = json_data["data"]["content"]
soup = BeautifulSoup(html_str, "html.parser")

for title_obj in soup.select('h2[class="cs-entry__title"]'):

    #title_element = soup.find('h2', class_='cs-entry__title')
    title = title_obj.text
    print(title)
    print(title_obj)
    print("==")


