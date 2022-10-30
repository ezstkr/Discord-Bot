import discord

from persona.copycat import copycat # 난이도 순 (제일 쉬움)
from persona.pingpong import pingpong
from persona.pingpong2 import pingpong2
from persona.part_timer import part_timer
from persona.calculator import calculator
from persona.wa_sans import wa_sans
from persona.gungye import gwansimbeop
from persona.what_time import what_time
from persona.last_chat_reminder import save_last_chat
from persona.gif_villain import gif_villain
from persona.continuation import continuation


# 페르소나 적용하는 곳 (위에서부터 하나씩 메세지를 보낼 때까지 실행됨)
# 페르소나 함수 규칙: 메세지 보내면 return True
personas = [ 
    pingpong,
    copycat,
]

async def use_persona(message: discord.message.Message):
    message_sended = False
    
    for persona in personas:
        if not message_sended: # 여러 페르소나가 동시에 메세지를 보내지 않게 만들기
            message_sended = await persona(message)
        else:
            break
    
    save_last_chat(message)
