import discord
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import random

from utils.unicode import check_hangul, is_hangul_compat_jamo


last_char_dict = {}


def get_html_soup(url: str):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    soup = bs(html, "html.parser")
    return soup


async def continuation(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    try:
        for char in content:
            check_hangul(char)
            assert not is_hangul_compat_jamo(char)
    except:
        return False

    global last_char_dict

    last_char = last_char_dict.get(f'{message.guild} - {channel}')

    word_exists = _word_exists(content)
    is_continue_word = last_char is None or last_char == content[0]

    if not is_continue_word or not word_exists:
        if not word_exists:
            await message.reply('그런 단어는 없다!')
        elif not is_continue_word:
            await message.reply(f"'{last_char}'(으)로 시작하는 말이 아니다!")
        
        await channel.send('내가 이겼다')

        last_char = None
    else:
        words = _search_answer_words(content)
        word = random.choice(words)

        if word is not None:
            last_char = word[-1]
            await message.reply(word)
        else:
            last_char = None
            await channel.send('내가 졌다')

    last_char_dict.update([(f'{message.guild} - {channel}', last_char)])

    return True


def _word_exists(content): # TODO: 두음 법칙 인정
    url = f"https://kkukowiki.kr/&search={quote_plus(content)}&fulltext=1"
    soup = get_html_soup(url)
    result = soup.find('ul', 'mw-search-results')
    
    if result is None:
        url = f"https://kkukowiki.kr/w/{quote_plus(content)}"
        try:
            from utils.rich_ import print_html
            soup = get_html_soup(url)
            print_html(soup)
        except HTTPError as e:
            if not e.status == 404:
                raise
            return False

    return True


def _search_answer_words(content):
    url_subfix = content[-1]
    url = f"https://kkukowiki.kr/w/{quote_plus(f'역대_단어/한국어/{url_subfix}', safe='/')}"

    try:
        soup = get_html_soup(url)
    except HTTPError as e:
        if not e.status == 404:
            raise
        return None

    tr_tags = soup.find('table', 'sortable').find_all('tr')

    if len(tr_tags) < 3:
        return None

    words = [list(tr_tag.children)[-1].text.strip() for tr_tag in tr_tags[2:]]

    return words
