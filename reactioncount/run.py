import aiohttp
import asyncio
import async_timeout
import time

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        postid = ""  #paste the postID here
        accesskey = "" # Paste your facebook accesskey here
        html = await session.get('https://graph.facebook.com/v2.8/{}/?fields=reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry)&access_token={}'.format(postid, accesskey))
        data = await html.json()
        like = open("reactions/like.txt","w+")
        like.write(str(data["reactions_like"]["summary"]["total_count"]))
        like.close()
        love = open("reactions/love.txt","w+")
        love.write(str(data["reactions_love"]["summary"]["total_count"]))
        love.close()
        haha = open("reactions/haha.txt","w+")
        haha.write(str(data["reactions_haha"]["summary"]["total_count"]))
        haha.close()
        wow = open("reactions/wow.txt","w+")
        wow.write(str(data["reactions_wow"]["summary"]["total_count"]))
        wow.close()
        sad = open("reactions/sad.txt","w+")
        sad.write(str(data["reactions_sad"]["summary"]["total_count"]))
        sad.close()
        angry = open("reactions/angry.txt","w+")
        angry.write(str(data["reactions_angry"]["summary"]["total_count"]))
        angry.close()
x = 0
speed = 3 #change to refresh time for count in seconds.
while x < 10:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    x = x + 1
    time.sleep(speed)
    if x == 10:
        x = 0


