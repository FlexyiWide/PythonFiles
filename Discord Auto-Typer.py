import os, discord
from discord.ext import commands

token = input("Enter Token: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')
os.system(f'autotyper')
os.system(f'mode 100,25')




@client.event
async def on_ready():
  print(f"nugget boi")
  
  print(f""" \u001b[31m

  type "nr" (numbers) in chat to start auto typing
""")


@client.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith('nr'):

        await message.channel.send('1')
        await message.channel.send('2')
        await message.channel.send('3')
        await message.channel.send('4')
        await message.channel.send('5')
        await message.channel.send('6')
        await message.channel.send('7')
        await message.channel.send('8')
        await message.channel.send('9')
        await message.channel.send('10')
        await message.channel.send('11')
        await message.channel.send('12')
        await message.channel.send('13')
        await message.channel.send('14')
        await message.channel.send('15')
        await message.channel.send('16')
        await message.channel.send('17')
        await message.channel.send('18')
        await message.channel.send('19')
        await message.channel.send('20')
        await message.channel.send('21')
        await message.channel.send('22')
        await message.channel.send('23')
        await message.channel.send('24')
        await message.channel.send('25')
        await message.channel.send('26')
        await message.channel.send('27')
        await message.channel.send('28')
        await message.channel.send('29')
        await message.channel.send('30')
        await message.channel.send('31')
        await message.channel.send('32')
        await message.channel.send('33')
        await message.channel.send('34')
        await message.channel.send('35')
        await message.channel.send('36')
        await message.channel.send('37')
        await message.channel.send('38')
        await message.channel.send('39')
        await message.channel.send('40')
        await message.channel.send('41')
        await message.channel.send('42')
        await message.channel.send('43')
        await message.channel.send('44')
        await message.channel.send('45')
        await message.channel.send('46')
        await message.channel.send('47')
        await message.channel.send('48')
        await message.channel.send('49')
        await message.channel.send('50')
        await message.channel.send('51')
        await message.channel.send('52')
        await message.channel.send('53')
        await message.channel.send('54')
        await message.channel.send('55')
        await message.channel.send('56')
        await message.channel.send('57')
        await message.channel.send('58')
        await message.channel.send('59')
        await message.channel.send('60')
        await message.channel.send('61')
        await message.channel.send('62')
        await message.channel.send('63')
        await message.channel.send('64')
        await message.channel.send('65')
        await message.channel.send('66')
        await message.channel.send('67')
        await message.channel.send('68')
        await message.channel.send('69')
        await message.channel.send('70')
        await message.channel.send('71')
        await message.channel.send('72')
        await message.channel.send('73')
        await message.channel.send('74')
        await message.channel.send('75')
        await message.channel.send('76')
        await message.channel.send('77')
        await message.channel.send('78')
        await message.channel.send('79')
        await message.channel.send('80')
        await message.channel.send('81')
        await message.channel.send('82')
        await message.channel.send('83')
        await message.channel.send('84')
        await message.channel.send('85')
        await message.channel.send('86')
        await message.channel.send('87')
        await message.channel.send('88')
        await message.channel.send('89')
        await message.channel.send('90')
        await message.channel.send('91')
        await message.channel.send('92')
        await message.channel.send('93')
        await message.channel.send('94')
        await message.channel.send('95')
        await message.channel.send('96')
        await message.channel.send('97')
        await message.channel.send('98')
        await message.channel.send('99')
        await message.channel.send('100')











client.run(token, bot=False)