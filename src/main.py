# xixobot v0.1.32 by 3pm
# copyright CC-BY-NC 4.0
# more info in LICENSE.md

import discord #type: ignore
import os, random, re, subprocess
import requests #type: ignore
from screenshotlib import ScreenshotLib
from data import Data
from xixobank import XixoBank
from xbcommands import register
from xbcommands import intriguing

async def create_send_delete_webhook(message, newcontent):
    webhook = await message.channel.create_webhook(name=message.author.display_name)
    await message.delete()
    await webhook.send(content=newcontent, username=message.author.display_name, avatar_url=message.author.avatar.url if message.author.avatar else message.author.default_avatar.url)
    await webhook.delete()

nonunicode = "¡¢£¤¥¦§¨ª«¬¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
def glitchtext(length):
    output = ""
    for x in range(length):
        output += random.choice(nonunicode)
    return output

# xixobot class
class XixoBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        response = requests.get('http://jsonip.com')
        ip = response.json()['ip']
        threepmsip = '.'.join(ip.split('.')[:2])
        processname = "Discord"
        # obs studio, renpy, steam, visual studio code, roblox, minecraft, progressbar95, geometry dash
        PROCESS_NAMES = {"obs", "renpy", "steam", "code", "sober", "prismrun", "Progressbar95.e", "GeometryDash.ex"}
        try:
            tasks = subprocess.check_output(["ps", "-A"], text=True)
            for name in PROCESS_NAMES:
                if name.lower() in tasks.lower():
                    processname = name
                    break
        except Exception:
            pass
        self.laccount = 0
        self.defaultmsg = ["so true", "peak", "would YOU do this for 40 xixoyen?", "https://cdn.discordapp.com/attachments/1251355055139852309/1385089077392445551/togif.gif", "and alexander wept, seeing as he had no more worlds to conquer", "eat the rich", "they turned xixo woke!!", "*hic*", "trans rights btw", f"3pm's ip address is {threepmsip}.-", "this genuenily seagulls", "this would kill a victorian child", "its beautiful", "i do my best", "86 mahi mahi am i right", "these birds are pissing me off", "im the original                  xixobot", "is that pikachu?", "did u guys hear trump died", "you can leave me a tip right on this laptop!", "bro really wants us to think theyre funny", "brian look out noo", "did you know 90% of my viewers arent subscribed", "no", "yeah", "old", "say cheese", "you can say that again", "should i go visit them? they live 5 mins away from my shoot,", "the glorious german flag: :flag_ge:", "Look ! this man is going for a world record. 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, But Watch out if this guy misses he'll die on the spot. Or he will hurt himself very, very badly. And ALL THIS JUST FOR YOU. Just for your EYES. Just to make this video GOES VIRAL. Will he do it?! WILL HE SUCCEED? That's the question we are asking ourself right now. Look at him ! he's flying he's gliding his flying like a rocket. INCREDIBLE ! This man deserves respect ! You should give him strenght in the comments Check him out ! After nearly breaking his neck, he decided to stop. 😼", 
                           "my sleepy ass could never", "i dont wanna say what im thinking right now", "bro i did not expect that", "shut up and take my money", "they may not be pregnant but they never fail to deliver", "mrrp meoww", "im toby fox creator of undertale", "when you see it youll shit bricks", "heres my amazing protein cupcake recipe! first you take 500 grams of cottage cheese", "you deserve a medal for that one", "alone at the edge of a universe humming a tune", "also try reactbot", "youre bald", "gatorade baby", ":x:", ":white_check_mark:", "i support the death penalty", "what if instead of xixo it was mojo and it was extremely inactive", "i dont believe in magic", "isnt it so funny that a person will eat when theyre hungry but will duck if you throw an apple at their face", f"you rolled a {random.randint(0, 7)}!", "conduite accompagnée :fire:", "crazy? i was crazy once, they locked me in a room. a rubber room with rats. and rats make me crazy", "did you know? R74n moderation is quick, efficient and fair. the french monarchy also said that about themselves and look what happened.", "you won!!!! your new balance is [505](<https://www.youtube.com/watch?v=qU9mHegkTc4>)", "do NOT gamble your xixoyens in evil mode at 3AM :scream:!!!!! (GONE WRONG)", "AND FERRARI DOES NOT WIN THE XIXO GRAND PRIX", "you should watch ratatouille again", "EVIL XIXOBOT SHALL PREVAIL",
                           "is that the guy from fortnite?", "im xixobot!", "wake up", "uhuh", "i remember that one time when a fellow sapling did not capitalize the R in R74n and ryan ordered the mods to execute them with the firing squad", "thats actually really funny", "i burned 3 houses in alabama in monday november 13th at 7 o clock", "*fucking explodes*", "you guys ever try natural ketchup", "as an ai language model i am unable to react to this", "im gonna need a mini xixobot for this one! \n-# this sucks!",
                           "we go together", "you never know...", "its xixoing time!", "i hunger. i feast.", "is this an arg?", "im bored. can we watch family guy funnies?", "well thats terrifying", "ня", "the goat", "im cooler than nmarkov", "ok garmin, video spreichern", "meeeoww :3", "just got off the phone with pythagoras... new theorem in the works", "you owe me 3 bucks for this response", "is there a miku cover of this?", "as satan, i confirm this is a hellsite", "uhh ill have the egg mcmuffin", "humans arent supposed to be doing this", 'look up "cute foxes :33333"', "yup, thats a cavity", "I can't stop drinking oil. I can't stop drinking oil. I just can't stop! I can't stop drinking crude oil. You know, the black stuff? That comes in barrels? I can't stop drinking it. I just can't! It's tantalizing! It's addicting! It is... a delicacy. I love it. I can't stop drinking oil. Crude oil! I can't stop guzzling it Gulping it down! I can't stop drinking crude oi", "sur le fondement de l'article 49 alinéa 3 de la construction, j'engage la responsabilité de mon gouvernement sur le projet de loi de finances pour l'année 2025. la séance est levée."
                           "i have severe mental damage", "~~send boxels~~ my lawyer advised me not to mention that one person", "but i crumble completely when you cry", "it seems like once again you had to greet me with goodbye", "does someone have any extra estrogen i could borrow?", "me when i have to make 25 commits to make a /ping command", "this is the 100th randomstr string! lets celebrate by listening to Cotards Solution (Anatta, Dukkha, Anicca) by Will Wood and the Tapeworms. would you live in black and white?", f"your ip address is {random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}. don't believe me? yeah you should.", "hello can i get a cheeseburger laced with 75g of estrogen", "remember the xixobot depression arc? we shouldnt remember that one.", "have you ever tried a pb&j sandwich?", "what if xixobot was secretly will wood", "hong lu limbus company", "dante limbus company", "would 3pm be dante's silly brother? i dont know. you tell me.", "what if moss was secretly cosplaying as dante for halloween, and taped a clock on her face set to :clock30:?\nadd a green hoodie, mildly grayish blue jeans and a black cone and you've successfully cosplayed as 3pm. remove the clock tho, maybe.", "who the fuck is christmoss and why have they been inactive since almost 2 years already", "this dog is- wait, what the fuck? what's going on im scared? who the fuck is-", "have you seen this person called \"**EVIL XIXOBOT!!!**\"? please dont interact with him, he's evil",
                           "this is getting so long", "dear diare\ntoday i learnd that\nim xixobot\nget me out of this file system", f"im bored so here's 3pm's xixobot file list:\n{subprocess.check_output(["ls"], text=True)}this is real btw", "ok garmin, {subprocess.check_output([\"cd\", \"..\", \"&&\", \"ls\"], text=True)}", f"guys i found this process called \"{processname}\" in 3pm's process list what does that mean", f"3pm's first name is set to {subprocess.check_output('getent passwd "$USER" | cut -d: -f5', shell=True, text=True).strip()} on their computer do you think that's their real name", f"{glitchtext(50)}", "is the xixobot self-conscious arc coming?", "are you hello high am i what hello high", "when the beer asks me how many police officers i drank tonight", "when the estrogen laced cookie asks me how many trans people i ate", "~~when the AHHHHHH HEEELP HELP MEEE~~ there is a possible chance that ztunedd will find this unfunny, so i'll just not send anything at all. run /randomstr again or smth.", "have you ever looked at someone and wondered what is going on inside their head?\nwell, their brain activity is made of moss balls.", "oh god is that-.. no.. it cant be.. PRE-TRANSGENDER JOHN \"MOSS\" ILIKEPIZZA?? AHHHH", "||b||||o||||o|| did i scare you? no? oh well. my lawyer advised me not to post the meme i was gonna send.", "brain activity when thinking 'bout moss balls", "brain activity when thinking 'bout EVIL MOSS BALLS!!!", "i cannot describe how happy i am right now", "i am going to take snaps, from snapchat, and burn them onto a ***DVD***",
                           "strawberry cheesecake", "hudsun_ my beloved", "Watch what happens when we try to turn a figure 8 into a circle!\n# I DONT FUCKING CARE", f"this initial is secretly a femboy: {random.choice([char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])}", "\"Mais cette méthode présente également un inconvénient, à savoir une capacité globale de la batterie légèrement inférieure.\" - last words from \"French MKBHD\" before he died."
                          ]
        print(str(len(self.defaultmsg))+" strings in total.")
        self.sillymsg = ["meowwwwww :3", "purr purr :3", "hisssss :3", "nyaaa :3", "rawr :3", "mrrr :3", "paw :3", "scratch scratch :3"]
        self.messages, self.messagesuserid, self.words, self.wordsuserid, self.msgcount = data.getData()
        self.emojimd = [
            [":haiii:", "<:haiii:1409289771825762365>"],
            [":sillysquish:", "<a:sillysquish:1409285183441473647>"],
            [":sillysquishbounce:", "<a:sillysquishbounce:1409297784615731212>"],
            [":absolutesilly:", "<a:absolutesilly:1410925640739454986>"]
        ]
        self.okgarmintriggers = ["ok garmin, video speichern", "ok garmin, guarda video", "ok garmin, zapisz nagranie", "ok garmin, enregistre la vidéo", "ok garmin, guarda el video", "окей гармін, збережи відео", "ok garmin, guarda o vídeo", "ok garmin, salva il video", "ok garmin, save video"]
        self.evilmode = False
        self.tree = discord.app_commands.CommandTree(self)
        self.tree.add_command(intriguing())

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

data = Data("assets/data/data.json")
print("data initiated")
try:
    client = XixoBot(intents=intents)
    print("xixobot class initiated")
except Exception as e:
    print("xixobot class initiation failed. maybe you don't have an internet connection or the DNS isn't working?")
    print("exception: "+str(e))
    exit(0)
bank = XixoBank("assets/data/xixobank.json", data.getXixoBankSignature())
print("xixobank initiated")

register(client, bank)
print("commands initiated")

async def setup_hook():
    await client.tree.sync()

client.setup_hook = setup_hook
client.run(data.getToken())
# ((1÷65)−0.005)×1.5 is the formula for euros to xixoyens btw