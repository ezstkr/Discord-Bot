import discord


async def pingpong(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    if content == 'ping': # 특정 메세지 감지
        await message.reply('pong') # 답장 보내기
        return True
