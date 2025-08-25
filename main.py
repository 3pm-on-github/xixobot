import discord
import asyncio
import random
import json

with open('private.json') as f:
    data = json.load(f)
    TOKEN = data['token']
    XIXOBANKSIGNATURE = data['xixobanksig']

class XixoBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msgcount = 0
        self.messages = []
        self.supersilly = False
        self.tree = discord.app_commands.CommandTree(self)
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        guild = self.get_guild(1409280301666013286)
        if guild:
            channel = guild.get_channel(1409281073174679793)
            if channel:
                await channel.send('haii chat')
            else:
                print('Channel not found!')
    async def on_message(self, message):
        if message.author == self.user:
            return
        self.msgcount += 1
        self.messages.append(message.content)
        guild = self.get_guild(1409280301666013286)
        if guild:
            if self.supersilly == True and self.msgcount == 0:
                self.supersilly = False
            if self.msgcount % 10 == 0:
                channel = guild.get_channel(1409281073174679793)
                if channel:
                    await channel.send('ping @everyone')
                    print("ping!", self.msgcount, "messages!")
            if self.msgcount == 100:
                channel = guild.get_channel(1409280302727303271)
                if channel:
                    await channel.send('silly <a:sillysquish:1409285183441473647>')
                    print("silly!")
                    self.msgcount = 0
            if self.supersilly == False and self.msgcount == 1000:
                channel = guild.get_channel(1409280302727303271)
                if channel:
                    await channel.send('SUPER SILLY!! <a:sillysquishbounce:1409297784615731212>')
                    self.supersilly = True
                    print("super silly!")
                    self.msgcount = 0

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

@client.tree.command(name="randommsg", description="sends a random message from chat")
async def randommsg_command(interaction: discord.Interaction):
    if client.messages:
        randommessage = random.choice(client.messages)
        await interaction.response.send_message(randommessage)
    else:
        await interaction.response.send_message("no messages have been recorded yet!")

@client.tree.command(name='playmp3',description='plays an mp3 in a voice channel')
async def playmp3(interaction: discord.Interaction):
    user=interaction.user
    voice_channel=user.voice.channel
    if voice_channel!= None:
        await interaction.response.send_message(f'Playing in {voice_channel.name}')
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('music.mp3'), after=lambda _: print('done'))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    else:
        await interaction.response.send_message('User is not in a channel.')

client.setup_hook = setup_hook
client.run(TOKEN)