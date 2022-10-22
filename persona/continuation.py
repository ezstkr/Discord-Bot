import discord
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
import random


def get_html_soup(url: str):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    soup = bs(html, "html.parser")
    return soup


async def continuation(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    url_subfix = content[-1]
    url = f'https://kkukowiki.kr/w/%EC%97%AD%EB%8C%80_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/{quote_plus(url_subfix)}'
    
    try:
        soup = get_html_soup(url)

        tr_tags = soup.find('table', 'sortable').find_all('tr')
        words = [list(tr_tag.children)[-1].text for tr_tag in tr_tags[1:]]
        word = random.choice(words)
        print(word)
        await message.reply(word) # 채널에 메세지 보내기
    except:
        await channel.send('내가 졌다') # 채널에 메세지 보내기
    return True
