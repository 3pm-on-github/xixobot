import discord
import os
import asyncio
import random
import json
import re
from yt_dlp import YoutubeDL

with open('private.json') as f:
    data = json.load(f)
    TOKEN = data['token']
    XIXOBANKSIGNATURE = data['xixobanksig']

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'music',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Downloaded audio from", url, "as music.mp3")

class XixoBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msgcount = 890
        self.defaultmsg = ["so true", "peak", "would YOU do this for 40 yen?", "https://cdn.discordapp.com/attachments/1251355055139852309/1385089077392445551/togif.gif", "and alexander wept, seeing as he had no more worlds to conquer", "eat the rich", "they turned xixo woke!!", "*hic*", "trans rights btw", "3pm's ip address is 104.26.-", "this genuenily seagulls", "this would kill a victorian child", "its beautiful", "i do my best", "86 mahi mahi am i right", "these birds are pissing me off", "im the original                  xixobot", "is that pikachu?", "did u guys hear trump died", "you can leave me a tip right on this laptop!", "bro really wants us to think theyre funny", "brian look out noo", "did you know 90% of my viewers arent subscribed", "no", "yeah", "old", "say cheese", "you can say that again", "should i go visit them? they live 5 mins away from my shoot,", "the glorious german flag: :flag_ge:", "Look ! this man is going for a world record. 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, But Watch out if this guy misses he'll die on the spot. Or he will hurt himself very, very badly. And ALL THIS JUST FOR YOU. Just for your EYES. Just to make this video GOES VIRAL. Will he do it?! WILL HE SUCCEED? That's the question we are asking ourself right now. Look at him ! he's flying he's gliding his flying like a rocket. INCREDIBLE ! This man deserves respect ! You should give him strenght in the comments Check him out ! After nearly breaking his neck, he decided to stop. 😼", 
                          "my sleepy ass could never", "i dont wanna say what im thinking right now", "bro i did not expect that", "shut up and take my money", "they may not be pregnant but they never fail to deliver", "mrrp meoww", "im toby fox creator of undertale", "when you see it youll shit bricks", "heres my amazing protein cupcake recipe! first you take 500 grams of cottage cheese", "you deserve a medal for that one", "alone at the edge of a universe humming a tune", "also try reactbot", "youre bald", "gatorade baby", ":x:", ":white_check_mark:", "i support the death penalty", "what if instead of xixo it was mojo and it was extremely inactive", "i dont believe in magic", "isnt it so funny that a person will eat when theyre hungry but will duck if you throw an apple at their face", f"you rolled a {random.randint(0, 7)}!", "conduite accompagnée :fire:", "crazy? i was crazy once, they locked me in a room. a rubber room with rats. and rats make me crazy", "did you know? R74n moderation is quick, efficient and fair. the french monarchy also said that about themselves and look what happened.", "you won!!!! your new balance is [505](<https://www.youtube.com/watch?v=qU9mHegkTc4>)", "do NOT gamble your xixoyens in evil mode at 3AM :scream:!!!!! (GONE WRONG)", "AND FERRARI DOES NOT WIN THE XIXO GRAND PRIX", "you should watch ratatouille again", "EVIL XIXOBOT SHALL PREVAIL"
                          ]
        self.sillymsg = ["meowwwwww :3", "purr purr :3", "hisssss :3", "nyaaa :3", "rawr :3", "mrrr :3", "paw :3", "scratch scratch :3"]
        self.messages = ["HEEELP HELP MEEE HEEEEEEEEEELP"]
        self.supersilly = False
        self.evilmode = False
        self.tree = discord.app_commands.CommandTree(self)
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        guild = self.get_guild(1409280301666013286)
        if guild:
            channel = guild.get_channel(1409281073174679793)
            if channel:
                await channel.send('haii chat :33')
            else:
                print('Channel not found!')
    async def on_message(self, message):
        if message.author == self.user:
            return
        self.msgcount += 1
        self.messages.append(message.content)
        guild = self.get_guild(1409280301666013286)
        if re.search(r"(paw|me+o+w|mrr+)", message.content) and ("<@&1409284344039870484>" in message.content or f"<@{self.user.id}>" in message.content):
            await message.channel.send(random.choice(self.sillymsg))
        if guild:
            if self.supersilly == True and self.msgcount == 0:
                self.supersilly = False
            if self.supersilly == False and self.msgcount == 1000:
                channel = guild.get_channel(1409280302727303271)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL SUPER SILLY!!!! <a:sillysquishbounce:1409297784615731212> ' + str(self.msgcount) + " MESSAGES!!!!")
                        print("EVIL SUPER SILLY!!!!")
                    else:
                        await channel.send('SUPER SILLY!! <a:sillysquishbounce:1409297784615731212> ' + str(self.msgcount) + " messages!")
                        print("super silly!")
                    self.supersilly = True
                    self.msgcount = 0
            if self.msgcount == 777:
                channel = guild.get_channel(1409280302727303271)
                if channel:
                    await channel.send('JACKPOT HIT!!! <a:sillysquish:1409285183441473647> ' + str(self.msgcount) + " messages!")
                    print("jackpot hit!!!")
            if self.msgcount % 100 == 0:
                channel = guild.get_channel(1409280302727303271)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL SILLY!!!! <a:sillysquish:1409297987928996872> ' + str(self.msgcount) + " MESSAGES!!!!")
                        print("EVIL SILLY!!!!")
                    else:
                        await channel.send('silly <a:sillysquish:1409285183441473647> ' + str(self.msgcount) + " messages!")
                        print("silly!")
            if self.msgcount % 10 == 0:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL PING @everyone ' + str(self.msgcount) + " MESSAGES!!!!!")
                        print("EVIL PING!", self.msgcount, "messages!")
                    else:
                        await channel.send('ping @everyone ' + str(self.msgcount) + " messages!")
                        print("ping!", self.msgcount, "messages!")

class XixoBank:
    def __init__(self, xixobankfile, signature):
        self.xixobankf = open(xixobankfile, "r+")
        self.xixobankdata = json.load(self.xixobankf)
        if self.xixobankdata["signature"] != signature:
            raise ValueError("Invalid Signature in xixobank file")

    def checkBalance(self, userid):
        if str(userid) in self.xixobankdata["balances"]:
            return self.xixobankdata["balances"][str(userid)]
        else:
            return "oopsie woopsie! looks like you don't have an account on the xixobank!"

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

client = XixoBot(intents=intents)
bank = XixoBank("xixobank.json", XIXOBANKSIGNATURE)

async def setup_hook():
    await client.tree.sync()

@client.tree.command(name="haiii", description="haiii!!!!!!")
async def haiii_command(interaction: discord.Interaction):
    await interaction.response.send_message("# haiii <:haiii:1409289771825762365>")

@client.tree.command(name="balance", description="check your xixobank balance")
async def balance_command(interaction: discord.Interaction):
    balance = bank.checkBalance(interaction.user.id)
    embed = discord.Embed(title="XixoBank Balance", color=discord.Color.blue())
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)
    embed.add_field(name="Balance", value=balance, inline=True)
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="randomstr", description="sends a random string from xixobot's code")
async def randomstr_command(interaction: discord.Interaction):
    if client.messages:
        randommessage = random.choice(client.defaultmsg)
        await interaction.response.send_message(randommessage)
    else:
        await interaction.response.send_message("no messages have been recorded yet!")

@client.tree.command(name="randommsg", description="sends a random message from chat")
async def randommsg_command(interaction: discord.Interaction):
    if client.messages:
        randommessage = random.choice(client.messages)
        await interaction.response.send_message(randommessage)
    else:
        await interaction.response.send_message("no messages have been recorded yet!")

@client.tree.command(name='playmp3',description='plays an mp3 in a voice channel')
async def playmp3(interaction: discord.Interaction, file: discord.Attachment):
    if not file.filename.endswith(".mp3"):
        await interaction.response.send_message("please upload a valid .mp3 file")
        return
    user=interaction.user
    filepath = f"./music.mp3"
    await file.save(filepath)
    voice_channel=user.voice.channel
    if voice_channel!= None:
        await interaction.response.send_message(f'playing in {voice_channel.name}')
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(filepath), after=lambda _: print('done'))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
        os.remove(filepath)
    else:
        await interaction.response.send_message('user is not in a channel')

@client.tree.command(name='playyt',description='plays a youtube video in a voice channel')
async def playyt(interaction: discord.Interaction, url: str):
    await interaction.response.defer()
    user=interaction.user
    download_audio(url)
    voice_channel=user.voice.channel
    if voice_channel!= None:
        vc = await voice_channel.connect()
        if url == "https://www.youtube.com/watch?v=DxxLzJDARbo":
            await voice_channel.send(f'EVIL MODE!!!!!!!!!!!!')
            await interaction.guild.me.edit(nick="EVIL XIXOBOT!!!!!")
            client.evilmode = True
            with open("./evil xixobot.png", "rb") as image:
                await client.user.edit(avatar=image.read())
        else:
            await interaction.guild.me.edit(nick="xixobot")
            client.evilmode = False
            with open("./xixobot.jpg", "rb") as image:
                await client.user.edit(avatar=image.read())
        vc.play(discord.FFmpegPCMAudio("./music.mp3"), after=lambda _: print('done'))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
        if url == "https://www.youtube.com/watch?v=DxxLzJDARbo":
            await voice_channel.send(f'no more evil')
            await interaction.guild.me.edit(nick="xixobot")
            client.evilmode = False
            with open("./xixobot.jpg", "rb") as image:
                await client.user.edit(avatar=image.read())
        os.remove("./music.mp3")

@client.tree.command(name='gamble',description='lets go gambling!!!')
async def gamble(interaction: discord.Interaction, amount: int):
    if amount <= 0:
        await interaction.response.send_message("please enter a positive amount")
        return
    balance = bank.checkBalance(interaction.user.id)
    if amount > balance:
        await interaction.response.send_message("you don't have enough xixoyens 3:")
        return
    if client.evilmode:
        outcome = random.choice(["win", "lose", "evil", "evil"])
    else:
        outcome = random.choice(["win", "lose"])
    if outcome == "win":
        new_balance = balance + amount
        bank.xixobankdata["balances"][str(interaction.user.id)] = new_balance
        bank.xixobankf.seek(0)
        json.dump(bank.xixobankdata, bank.xixobankf, indent=4)
        bank.xixobankf.truncate()
        if client.evilmode:
            await interaction.response.send_message(f"EVIL MODE ACTIVATED!!!!! YOU HAVE A 1/4 CHANCE OF WINNING NOW!!!!!\nyou won!!!! are you that lucky?? your new balance is {new_balance}")
        else:
            await interaction.response.send_message(f"you won!!!! your new balance is {new_balance}")
    else:
        new_balance = balance - amount
        bank.xixobankdata["balances"][str(interaction.user.id)] = new_balance
        bank.xixobankf.seek(0)
        json.dump(bank.xixobankdata, bank.xixobankf, indent=4)
        bank.xixobankf.truncate()
        if client.evilmode:
            await interaction.response.send_message(f"EVIL MODE ACTIVATED!!!!! YOU HAVE A 1/4 CHANCE OF WINNING NOW!!!!!\nyou lost 3: your new balance is {new_balance}")
        else:
            await interaction.response.send_message(f"you lost 3: your new balance is {new_balance}")

@client.tree.command(name='transfer',description='transfer xixoyens to another user')
async def transfer(interaction: discord.Interaction, member: discord.Member, amount: int):
    if amount <= 0:
        await interaction.response.send_message("please enter a positive amount")
        return
    if member.bot:
        await interaction.response.send_message("you cannot transfer xixoyens to a bot")
        return
    balance = bank.checkBalance(interaction.user.id)
    if amount > balance:
        await interaction.response.send_message("you don't have enough xixoyens")
        return
    recipient_balance = bank.checkBalance(member.id)
    if isinstance(recipient_balance, str):
        await interaction.response.send_message("the other person doesm't have an account on the xixobank")
        return
    new_balance = balance - amount
    new_recipient_balance = recipient_balance + amount
    bank.xixobankdata["balances"][str(interaction.user.id)] = new_balance
    bank.xixobankdata["balances"][str(member.id)] = new_recipient_balance
    bank.xixobankdata["transactions"].append({
        "type": "tra",
        "from": int(interaction.user.id),
        "to": int(member.id),
        "amount": amount
    })
    await interaction.response.send_message(f"you have transferred {amount} xixoyens to {member.name}. your new balance is {new_balance}")
    bank.xixobankf.seek(0)
    json.dump(bank.xixobankdata, bank.xixobankf, indent=4)
    bank.xixobankf.truncate()

@client.tree.command(name='add',description='add xixoyens to another user (admin only)')
async def transfer(interaction: discord.Interaction, member: discord.Member, amount: int):
    if amount <= 0:
        await interaction.response.send_message("please enter a positive amount")
        return
    if member.bot:
        await interaction.response.send_message("you cannot transfer xixoyens to a bot")
        return
    if (not interaction.user.guild_permissions.administrator) and (not interaction.user.id == 932666698438418522):
        await interaction.response.send_message("you do not have permission to use this command")
        return
    recipient_balance = bank.checkBalance(member.id)
    if isinstance(recipient_balance, str):
        await interaction.response.send_message("the other person doesm't have an account on the xixobank")
        return
    new_recipient_balance = recipient_balance + amount
    bank.xixobankdata["balances"][str(member.id)] = new_recipient_balance
    bank.xixobankdata["transactions"].append({
        "type": "add",
        "who": int(member.id),
        "amount": amount
    })
    await interaction.response.send_message(f"you have added {amount} xixoyens to {member.name}. their new balance is {new_recipient_balance}")
    bank.xixobankf.seek(0)
    json.dump(bank.xixobankdata, bank.xixobankf, indent=4)
    bank.xixobankf.truncate()

@client.tree.command(name='eurtoxyn',description='calculate euros to xixoyens')
async def eurtoxyn(interaction: discord.Interaction, amount: int):
    if amount <= 0:
        await interaction.response.send_message("please enter a positive amount")
        return
    await interaction.response.send_message(f"{amount} euros is equal to {round(amount / 0.015576923)} xixoyens")

@client.tree.command(name='xyntoeur',description='calculate xixoyens to euros')
async def xyntoeur(interaction: discord.Interaction, amount: int):
    if amount <= 0:
        await interaction.response.send_message("please enter a positive amount")
        return
    await interaction.response.send_message(f"{amount} xixoyens is equal to {round(amount * 0.015576923, 2)} euros")

client.setup_hook = setup_hook
client.run(TOKEN)
# ((1÷65)−0.005)×1.5 is the formula for euros to xixoyens btw
