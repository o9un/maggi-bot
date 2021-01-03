import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Minecraft")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("매기야 찍먹"):
        await message.channel.send("찍먹이 답이지")
    if message.content.startswith("매기야 부먹"):
        await message.channel.send("개새끼야 ㅄ같네")
    if message.content.startswith("매기야 안녕"):
        await message.channel.send("안녕")
    if message.content.startswith("매기야 똥"):
        await message.channel.send("가서 싸")
    if message.content.startswith("매기야 잘가"):
        await message.channel.send("너밴")
    if message.content.startswith("매기야 시발"):
        await message.channel.send("너밴")
    if message.content.startswith("매기야 씨발"):
        await message.channel.send("너밴")
    if message.content.startswith("매기야 병신"):
        await message.channel.send("무지개 반사")


@client.event
async def on_message(message):
    if message.content.startswith("매기야 투표"):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, vote[i])
            await client.add_reaction(choose, '👍')


access_token = os.environ
client.run(acces_tokken)
