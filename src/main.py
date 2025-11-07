# xixobot v0.1.32 by 3pm
# copyright CC-BY-NC 4.0
# more info in LICENSE.md

import discord #type: ignore
import os, random, re
from screenshotlib import ScreenshotLib
from data import Data
from xixobank import XixoBank
from xbcommands import register
from intriguingmg import intriguing
from config import *

async def create_send_delete_webhook(message, newcontent):
    webhook = await message.channel.create_webhook(name=message.author.display_name)
    await message.delete()
    await webhook.send(content=newcontent, username=message.author.display_name, avatar_url=message.author.avatar.url if message.author.avatar else message.author.default_avatar.url)
    await webhook.delete()

# xixobot class
class XixoBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.laccount = 0
        self.defaultmsg = randomstrstrings
        print(str(len(self.defaultmsg))+" strings in total.")
        self.sillymsg = sillymsg
        self.messages, self.messagesuserid, self.words, self.wordsuserid, self.msgcount = data.getData()
        self.emojimd = [
            [":haiii:", "<:haiii:1409289771825762365>"],
            [":sillysquish:", "<a:sillysquish:1409285183441473647>"],
            [":sillysquishbounce:", "<a:sillysquishbounce:1409297784615731212>"],
            [":absolutesilly:", "<a:absolutesilly:1410925640739454986>"]
        ]
        self.evilmode = False
        self.tree = discord.app_commands.CommandTree(self)
        self.tree.add_command(intriguing())
        self.okgarmintriggers = okgarmintriggers
        self.headcanons = headcanons
    async def on_ready(self):
        print(f'logged in as {self.user}')
        guild = self.get_guild(1409280301666013286)
        self.useridlist = [member.id for member in self.get_guild(1409280301666013286).members if not member.bot]
        if guild:
            channel = guild.get_channel(1409281073174679793)
            if channel:
                await channel.send('haiiii chat :333')
            else:
                print('Channel not found!')
        for guild in client.guilds:
            if guild.id != 1409280301666013286:
                print(f"someone invited me in {guild.name} for some reason ({guild.id})")
                await guild.leave()
    
    async def on_guild_join(guild):
        if guild.id != 1409280301666013286:
            print(f"someone invited me in {guild.name} for some reason ({guild.id})")
            await guild.leave()

    async def on_message(self, message):
        if message.author.bot or message.webhook_id is not None:
            return
        self.msgcount += 1
        if "lac" in message.content:
            self.laccount += 1
        replaced = False
        new_content = message.content
        for trigger, emoji in self.emojimd:
            if trigger in new_content:
                new_content = new_content.replace(trigger, emoji)
                replaced = True
        if client.user.mentioned_in(message) and "YOU FUCKING GOPRO" in message.content:
            await message.channel.send("actually im a nikon")
        if replaced:
            await create_send_delete_webhook(message, new_content)
        self.messages.append(message.content)
        self.messagesuserid.append(message.author.id)
        for word in message.content.split(" "):
            self.words.append(word)
            self.wordsuserid.append(message.author.id)
        data.saveData(self.messages, self.messagesuserid, self.words, self.wordsuserid, self.msgcount)
        guild = self.get_guild(1409280301666013286)
        if "()" in message.content and "garmin" in message.content:
            await message.channel.send("do i look like a fucking python interpreter to you???")
        if re.search(r"(paw|me+o+w|mrr+)", message.content) and ("<@&1409284344039870484>" in message.content or f"<@{self.user.id}>" in message.content):
            await message.channel.send(random.choice(self.sillymsg))
        if guild:
            if str(self.msgcount) in "123456789":
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    await channel.send("holy shit is that a NUMBER SERIES?? "+str(self.msgcount)+" messages!")
                    print("le number series")
            if self.msgcount % 10000 == 0:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL ABSOLUTE SILLY!!!! <a:absolutesilly:1410925640739454986> ' + str(self.msgcount) + " MESSAGES!!!!\nThis is absolutely insane. If you don't realize how huge this number already is, i dont understand you.\nIf 50000 messages are hit, we literally already sent more messages here than in the xixo gc. love y'all :3")
                        print("EVIL ABSOLUTE SILLY!!!!")
                    else:
                        await channel.send('ABSOLUTE SILLY!! <a:absolutesilly:1410925640739454986> ' + str(self.msgcount) + " messages!\nThis is absolutely insane. If you don't realize how huge this number already is, i dont understand you.\nIf 50000 messages are hit, we literally already sent more messages here than in the xixo gc. love y'all :3")
                        print("absolute silly!")
            if self.msgcount % 1000 == 0:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL SUPER SILLY!!!! <a:sillysquishbounce:1409297784615731212> ' + str(self.msgcount) + " MESSAGES!!!!")
                        print("EVIL SUPER SILLY!!!!")
                    else:
                        await channel.send('SUPER SILLY!! <a:sillysquishbounce:1409297784615731212> ' + str(self.msgcount) + " messages!")
                        print("super silly!")
            if self.msgcount % 1000 == 777:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    await channel.send('JACKPOT HIT!!! <a:sillysquish:1409285183441473647> ' + str(self.msgcount) + " messages!")
                    print("jackpot hit!!!")
            if self.msgcount % 10000 == 4090:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    await channel.send('<@1008565108542287994> WAKE UP RTX WE GOT THE 4090!!!!!!!! <a:sillysquish:1409285183441473647> ' + str(self.msgcount) + " messages!")
                    print("rtx 4090!!!")
            if self.msgcount % 10000 == 5090:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    await channel.send('rtx 5090 youre not welcome here get the fuck out, YOU\'RE GAY!!!!!!! (insert rtx doing middle finger emoji here) ' + str(self.msgcount) + " messages!")
                    print("rtx 5090 bad bad")
            if self.msgcount % 100 == 0:
                channel = guild.get_channel(1409281073174679793)
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
                        await channel.send('EVIL PING <@&1409927461550166146> ' + str(self.msgcount) + " MESSAGES!!!!!")
                        print("EVIL PING!", self.msgcount, "messages!")
                    else:
                        await channel.send('ping <@&1409927461550166146> ' + str(self.msgcount) + " messages!")
                        print("ping!", self.msgcount, "messages!")
            if self.laccount == 5:
                self.laccount = 0
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    if self.evilmode:
                        await channel.send('EVIL RIVIÈRE!!!!')
                        print("EVIL RIVIÈRE!!!!")
                    else:
                        await channel.send('rivière')
                        print("rivière")
            if message.content.lower() in self.okgarmintriggers:
                last5messages = []
                async for msg in message.channel.history(limit=6):
                    if msg.id != message.id:
                        last5messages.append(msg)
                last5messages = list(reversed(last5messages))[-5:]
                screenshot_lib = ScreenshotLib()
                await screenshot_lib.take_screenshot(last5messages)
                await message.channel.send(file=discord.File('screenshot.png'))
                os.remove('screenshot.png')

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.members = True
intents.message_content = True
intents.reactions = True

data = Data("assets/data/data.json")
print("data initiated")
client = XixoBot(intents=intents)
print("xixobot class initiated")
bank = XixoBank("assets/data/xixobank.json", data.getXixoBankSignature())
print("xixobank initiated")
register(client, bank)
print("commands initiated")

async def setup_hook():
    await client.tree.sync()

client.setup_hook = setup_hook
try:
    client.run(data.getToken())
except:
    print("an error occured while trying to log in. maybe you don't have an internet connection or the token is invalid?")

# ((1÷65)−0.005)×1.5 is the formula for euros to xixoyens btw