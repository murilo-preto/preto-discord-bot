import discord
from discord.ext import commands
from discord.player import FFmpegPCMAudio
import asyncio
import pandas as pd
import os

client = commands.Bot(command_prefix = '!preto ')

@client.event
async def on_ready():
    print("Bot pronto para uso")
    print("------------------")

@client.command(pass_context = True)
async def v_pomodoro(ctx):
    """
    [!preto v_pomodoro]: Inicia uma sessão de estudos de 25 minutos.\
    Será notificado por voz o início, restando 10 e 5 minutos, o fim.
    """
    
    t = 0
    while t != 0:
        
        try:
            if t == 1500:
                    channel = ctx.message.author.voice.channel
                    voice = await channel.connect()
                    player = voice.play( source = FFmpegPCMAudio("sessao iniciada.mp3"))
    
                    await ctx.send("Sessão iniciada, 25 minutos restantes. Te avisarei faltando 10 e 5 minutos para acabar, bons estudos!!!")
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
        except:
            await ctx.send("Ocorreu um erro, verifique se você está em um chat de voz, e tente novamente.\
            \nCaso persista, reporte-o para @Preto#4988.")
        

    #Importa dataframe
    df = pd.read_csv("pomodoro.csv")
    autor = f"{ctx.author}"

    #Verifica se o autor já foi registrado, caso não -> Registra. Caso sim, soma 1 ao seu valor.
    if df['Nome'].str.contains(autor).any():
        await ctx.send(f"{autor} já registrado no ranking, atualizando valor:")
        df.loc[(df.Nome == autor),'Pomodoros realizados'] += 1
    else:
        await ctx.send(f"Adicionando {autor} ao ranking de usuários:")
        df_temp = pd.DataFrame({"Nome":[autor],"|":["|"],"Pomodoros realizados":[1]})
        df = df.append(df_temp, ignore_index=True)

    #Atualiza dataframe
    df.sort_values("Pomodoros realizados", ascending=False, inplace=True)
    await ctx.send(df.to_string(index=False))
    os.remove("pomodoro.csv")
    df.to_csv(path_or_buf="pomodoro.csv", index=False)

    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source = FFmpegPCMAudio("sessao terminada.mp3"))
    await ctx.send("Sessão de estudos terminada, descanse um pouco!!!")

    await asyncio.sleep(5)
    await ctx.guild.voice_client.disconnect()

        
        
@client.command(pass_context = True)
async def ping(ctx):
    """
    [!preto ping]: Verifica o tempo de resposta do bot.
    """
    await ctx.send(f"{ctx.author} requested ping!")

@client.command(pass_context = True)
async def comandos(ctx):
    await ctx.send("Comandos disponíveis:\
        \n\
        \n [!preto help]: Explica os principais comandos.\
        \n [!preto ping]: Verifica o tempo de resposta do bot.\
        \n [!preto v_pomodoro]: Inicia uma sessão de estudos de 25 minutos. Será notificado por voz o início, restando 10 e 5 minutos, o fim.")

client.run("TOKEN")