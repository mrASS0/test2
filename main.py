import discord
from bot_logic import *

# la variabile indents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Abbiamo fatto l'accesso come {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$testa o croce'):
        await message.channel.send(testa_o_croce())
    elif message.content.startswith('$emoji casuale'):
        await message.channel.send(emoji_casuale())
    else:
        await message.channel.send("La tua password " + gen_pass(10))

client.run("TOKEN_SEGRETO")
