import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.music   

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 0;

for song in songs:
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        rank += 1;
        title = song.select_one('.title').text # img 태그의 alt 속성값을 가져오기
        title = title.strip()
        singer = song.select_one('.artist').text
        print(rank,title,singer)
        doc = {
            'rank' : rank,
            'title' : title,
            'singer' : singer
        }

        db.music.insert(doc);
        
view = list(db.music.find())
print(view)
                   # 'dbsparta'라는 이름의 db를 만듭니다.


