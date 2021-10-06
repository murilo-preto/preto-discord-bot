import discord
from discord.ext import commands
from discord.player import FFmpegPCMAudio
import asyncio


client = commands.Bot(command_prefix = '!preto ')

@client.event
async def on_ready():
    print("Bot pronto para uso")
    print("------------------")

@client.command(pass_context = True)
async def pomodoro(ctx):
    
    t = 1500
    while t != 0:
        
        if t == 1500:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                player = voice.play( source = FFmpegPCMAudio("sessao iniciada.mp3"))
 
                await ctx.send("Sessão iniciada, 25 minutos restantes.")
                await ctx.send("Te avisarei faltando 10 e 5 minutos para acabar, bons estudos!!!")
                await asyncio.sleep(5)

                await ctx.guild.voice_client.disconnect()


                await asyncio.sleep(895)
                t -= 900
       
        if t == 600:

                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                player = voice.play(source = FFmpegPCMAudio("10 minutos restantes.mp3"))

                await asyncio.sleep(5)
                await ctx.guild.voice_client.disconnect()

                await asyncio.sleep(295)
                t -= 300
        
        if t == 300:

                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                player = voice.play(source = FFmpegPCMAudio("5 minutos restantes.mp3"))

                await asyncio.sleep(5)
                await ctx.guild.voice_client.disconnect()

                await asyncio.sleep(295)
                t -= 300
    
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source = FFmpegPCMAudio("sessao terminada.mp3"))
    await ctx.send("Sessão de estudos terminada, descanse um pouco!!!")

    await asyncio.sleep(5)
    await ctx.guild.voice_client.disconnect()
        
@client.command(pass_context = True)
async def ping(ctx):
    await ctx.send("Pong!")



client.run("TOKEN")