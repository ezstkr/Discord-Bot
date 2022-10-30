import discord


# 1단계
async def calculator(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    if '+' in content:
        x, y = content.split('+') # key를 기준으로 문자 쪼개기
        x, y = int(x), int(y) # 문자를 숫자로 변환
        await message.reply(x + y)

    if '-' in content:
        x, y = content.split('-')
        x, y = int(x), int(y)
        await message.reply(x - y)

    if 'x' in content:
        x, y = content.split('x')
        x, y = int(x), int(y)
        await message.reply(x * y)

    if '/' in content:
        x, y = content.split('/')
        x, y = int(x), int(y)
        await message.reply(x / y)

# 2단계
async def calculator(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    for key in ['+', '-', 'x', '/']:
        if key in content:
            x, y = content.split(key)
            x, y = int(x), int(y)

            if key == '+':
                answer = x + y
            elif key == '-':
                answer = x - y
            elif key == 'x':
                answer = x * y
            elif key == '/':
                answer = x / y
            else:
                answer = 'error'

            await message.reply(answer)
            break
        
# 3단계
async def calculator(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    for key in ['+', '-', 'x', '/']:
        if key in content:
            x, y = content.split(key)
            x, y = int(x), int(y)
            await message.reply(
                x + y if key=='+' else \
                x - y if key=='-' else \
                x * y if key=='x' else \
                x / y if key=='/' else 'error'
            )
            break

# 4단계
async def calculator(message: discord.message.Message):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널
    
    keys = ['+', '-', 'x', '/']
    functions = [int.__add__, int.__sub__, int.__mul__, int.__truediv__]

    for key, func in zip(keys, functions):
        if key in content:
            x, y = map(int, content.split(key))
            answer = func(x, y)
            await message.reply(answer)
            break
