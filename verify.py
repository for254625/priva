import discord
from bs4 import BeautifulSoup
import requests
import urllib
import discord
from discord.ext import commands
import os
import asyncio
import random
from bs4 import BeautifulSoup
from urllib.request import Request
import parse
import time


client = discord.Client()

owner = ['765425379065331793']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["코로나 의심시 1339", "x.priva.cf" , " 🌸 : 안녕하세요 " , str(user) + "분이 평점해주셨어요.! ", str(server) + "개의 서버에서 열심히 말 하는중"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)



@client.event
async def on_message(message):
    if message.content.startswith('<코로나'):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        #print(f'기준일: {datecr.string}')

        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        #print(f'누적 확진자: {totalcovid} 명')

        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        #print(f'확진자 소계: {todaytotalcovid} 명')

        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        #print(f'국내발생: {todaydomecovid} 명')

        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        #print(f'해외유입: {todayforecovid} 명')

        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        #print(f'누적 격리해제: {totalca} 명')

        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        #print(f'격리해제: {todayca} 명')

        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        #print(f'누적 격리중: {totalcaing}')

        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        #print(f'격리중: {todaycaing} 명')

        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        #print(f'누적 사망자: {totaldead} 명')

        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        #print(f'사망자: {todaydead} 명')

        covidembed = discord.Embed(title='코로나19정보 Corona 19 information', description="Imininingwane yeCorona 19 , कोरोना १ information जानकारी , Informacije o Coroni 19", color=0xFF0F13, url='http://ncov.mohw.go.kr/')
        covidembed.add_field(name='모든 나라 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                f'\n\n국내발생환자: {todaydomecovid} 명\n해외에서 온 사람: {todayforecovid} 명', inline=False)
        covidembed.add_field(name='격리자', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        covidembed.add_field(name='격리가 끝난사람', value=f'{totalca}({todayca}) 명', inline=False)
        covidembed.add_field(name='사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        covidembed.set_footer(text=datecr.string)
        await message.channel.send(embed=covidembed)
        
    if (message.content.split(" ")[0] == "<아이피밴"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title=" 안녕안녕.. 안녕... ", description=f'아쉽게도 **{message.guild.name}** 서버에서 차단당했습니다. 밴 이유 ```{reason}```', color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Ban Success", description=f"{message.author.mention} 님, 성공적으로 차단시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러코드", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한에러", description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.", color=0xff0000))
            return

    if message.content.startswith('<위성검색'):
        url = 'https://www.weather.go.kr/weather/images/satellite_service.jsp'
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, 'html.parser')
        soup = soup.find("div", class_="image-player-slide")
        imgUrl = 'https://www.weather.go.kr' + soup.find("img")["src"]

        typoonEmbed = discord.Embed(title='천리안 2A호 위성으로 촬영한 사진', description='출처:[기상청]에서 parsing한 사진입니다.', colour=discord.Colour.dark_grey())
        typoonEmbed.set_image(url=imgUrl)
        await message.channel.send(embed=typoonEmbed)

    if message.content.startswith('>nuke'):
        if message.author.guild_permissions.ban_members:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='펑!', colour=discord.Colour.red())
            embed.set_image(url='https://i.kym-cdn.com/photos/images/original/000/914/350/d2c.gif')
            await new.send(embed=embed)
        else:
            await message.channel.send('권한을 확인하곧 다시해봐요.')
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
