import requests # type:ignore
import random, os, asyncio, json
import discord # type:ignore
from yt_dlp import YoutubeDL #type: ignore
from config import prompts, iprompts, replies, fish, medias

VERSION = "0.2.2"

async def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'music',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl: # type:ignore
        ydl.download([url])
        print("Downloaded audio from", url, "as music.mp3")

def register(client, bank):
    @client.tree.command(name="balance", description="check your xixobank balance")
    async def balance_command(interaction: discord.Interaction):
        balance = bank.checkBalance(interaction.user.id)
        embed = discord.Embed(title="XixoBank Balance", color=discord.Color.blue())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)
        embed.add_field(name="Balance", value=balance, inline=True)
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name='fishing',description="let's go fishing!!!")
    async def fishing(interaction: discord.Interaction):
        await interaction.response.send_message("You fish..")
        await asyncio.sleep(random.randint(1, 10))
        xynamount = random.randint(1, 10)
        await interaction.edit_original_response(content=f"You caught a {random.choice(fish)}\nYou won {xynamount}XYN.")
        recipient_balance = bank.checkBalance(interaction.user.id)
        if isinstance(recipient_balance, str):
            await interaction.channel.send("You don't have an account on the xixobank!")
            return
        new_recipient_balance = recipient_balance + xynamount
        bank.xixobankdata["balances"][str(interaction.user.id)] = new_recipient_balance
        bank.xixobankdata["transactions"].append({
            "type": "add",
            "who": int(interaction.user.id),
            "amount": xynamount
        })
        bank.xixobankf.seek(0)
        json.dump(bank.xixobankdata, bank.xixobankf, indent=4)
        bank.xixobankf.truncate()

    @client.tree.command(name="characterheadcanon", description="sends a character headcanon")
    async def headcanon_command(interaction: discord.Interaction, character:str):
        await interaction.response.send_message(random.choice(client.headcanons).replace("!c", character))

    @client.tree.command(name="randomwordstr", description="sends a random string of words sent in xixo")
    async def randomwordstr_command(interaction: discord.Interaction, wordcount:int):
        if interaction.channel.id in [1438628843857645638, 1438899970907308103, 1438899992134946848, 1438900011466358804, 1438900042957193266, 1438900067095417024, 1438900085801877614]:
            await interaction.response.send_message("/randomwordstr isn't allowed in visitor channels!")
        else:
            string = []
            for _ in range(wordcount):
                string.append(random.choice(client.words)+" ")
            await interaction.response.send_message(f"generated string: ``{"".join(string)}``")

    @client.tree.command(name="removemydata", description="removes your data from xixobot")
    async def removemydata_command(interaction: discord.Interaction):
        i=-1
        for userid in client.messagesuserid:
            i+=1
            if userid == interaction.user.id:
                del client.messages[i]
                del client.messagesuserid[i]
        i=-1
        for userid in client.wordsuserid:
            i+=1
            if userid == interaction.user.id:
                del client.words[i]
                del client.wordsuserid[i]
        await interaction.response.send_message("your data has been removed from xixobot.")

    @client.tree.command(name="randommsg", description="sends a random message from chat")
    async def randommsg_command(interaction: discord.Interaction):
        if interaction.channel.id in [1438628843857645638, 1438899970907308103, 1438899992134946848, 1438900011466358804, 1438900042957193266, 1438900067095417024, 1438900085801877614]:
            await interaction.response.send_message("/randommsg isn't allowed in visitor channels!")
        else:
            if client.messages:
                randommessage = random.choice(client.messages)
                await interaction.response.send_message(randommessage)
            else:
                await interaction.response.send_message("no messages have been recorded yet!")

    @client.tree.command(name="randommedia", description="sends a random media")
    async def randommedia_command(interaction: discord.Interaction):
        if interaction.channel.id in [1438628843857645638, 1438899970907308103, 1438899992134946848, 1438900011466358804, 1438900042957193266, 1438900067095417024, 1438900085801877614]:
            await interaction.response.send_message("/randommedia isn't allowed in visitor channels!")
        else:
            randommedia = random.choice(medias)
            await interaction.response.send_message(file=discord.File(randommedia))

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
            await interaction.response.send_message("please wait..")
            await interaction.edit_original_response(content=f'playing in {voice_channel.name}')
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(filepath), after=lambda _: print("done"))
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
        await download_audio(url)
        voice_channel=user.voice.channel
        if voice_channel!= None:
            vc = await voice_channel.connect()
            if url == "https://www.youtube.com/watch?v=DxxLzJDARbo":
                await voice_channel.send(f'EVIL MODE!!!!!!!!!!!!')
                await interaction.guild.me.edit(nick="EVIL XIXOBOT!!!!!")
                client.evilmode = True
                with open("assets/images/evil xixobot.png", "rb") as image:
                    await client.user.edit(avatar=image.read())
            else:
                await interaction.guild.me.edit(nick="xixobot")
                client.evilmode = False
                with open("assets/images/xixobot.jpg", "rb") as image:
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
    async def transfer_command(interaction: discord.Interaction, member: discord.Member, amount: int):
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
            await interaction.response.send_message("the other person doesn't have an account on the xixobank")
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
            await interaction.response.send_message("the other person doesn't have an account on the xixobank")
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

    @client.tree.command(name='cat',description='sends a random cat')
    async def cat(interaction: discord.Interaction):
        r = requests.get("https://api.thecatapi.com/v1/images/search?limit=1")
        jsondata = r.json()
        await interaction.response.send_message(jsondata[0]['url'])

    @client.tree.command(name='fox',description='sends a random fox')
    async def fox(interaction: discord.Interaction):
        r = requests.get("https://randomfox.ca/floof/")
        jsondata = r.json()
        await interaction.response.send_message(jsondata['image'])

    @client.tree.command(name='eurtoxyn',description='calculate euros to xixoyens')
    async def eurtoxyn(interaction: discord.Interaction, amount: float):
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

    @client.tree.command(name='surprise',description="a surprise")
    async def flashbang(interaction: discord.Interaction):
        await interaction.response.send_message("THINK FAST CHUCKLENUTS")
        await interaction.edit_original_response(content="", attachments=[discord.File("assets/images/flashbang.png")])

    @client.tree.command(name='horse',description="horse")
    async def h(interaction: discord.Interaction):
        embed = discord.Embed(
            title="horse",
            color=int("a35b17", 16),
            description=f"{"horse\n"*6}"
        )
        embed.set_author(name="horse", icon_url="https://raw.githubusercontent.com/3pm-on-github/xixobot/refs/heads/main/assets/images/horse.webp")
        embed.set_image(url="https://raw.githubusercontent.com/3pm-on-github/xixobot/refs/heads/main/assets/images/horse.webp")
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name='stats',description='xixobot string stats')
    async def stats_command(interaction: discord.Interaction):
        embed = discord.Embed(
            title="xixobot string stats",
            color=int("EED7A6", 16),
            description=f"these are the stats for the number of strings in xixobot's code."
        )
        embed.add_field(name="randomstr strings", value=str(len(client.defaultmsg)), inline=True)
        embed.add_field(name="randommsg strings", value=str(len(client.messages)), inline=True)
        embed.add_field(name="randomwordstr words", value=str(len(client.words)), inline=True)
        embed.add_field(name="headcanon strings", value=str(len(client.headcanons)), inline=True)
        embed.add_field(name="schmitlash prompts", value=str(len(iprompts)), inline=True)
        embed.add_field(name="newaccwhodis prompts", value=str(len(prompts)), inline=True)
        embed.add_field(name="newaccwhodis replies", value=str(len(replies)), inline=True)
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name='membercount',description="the member count (not including alts and bots)")
    async def membercount(interaction: discord.Interaction):
        members = interaction.channel.members
        membercount = 0
        for member in members:
            if member.bot:pass
            else:membercount += 1
        membercount -= 14 # not including alts btw!!
        await interaction.response.send_message(f"there are {str(membercount)} members")

    @client.tree.command(name='info',description='more info about xixobot')
    async def info_command(interaction: discord.Interaction):
        await interaction.response.send_message(f"""xixobot v{VERSION} is a discord bot made for the xixo discord server.
xixobot collects the following data about you:
- your discord avatar
- your server name
- your role color
- your user id
- messages you sent
this data is only used for commands such as:
- every xixobank command
- /randommsg and /randomwordstr
- /removemydata
- \"ok garmin, save video\"
you can request a data removal with the /removemydata command.
xixobot is not intended for use outside of xixo.""")