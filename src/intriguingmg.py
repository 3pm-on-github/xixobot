import random, asyncio
import discord # type:ignore
from discord import app_commands, ui # type:ignore
from config import *

ireplies = 0
intriguingreplies = []
intriguingrepliesuserid = []
votes = []
votesuserids = []

class intriguingmodal(ui.Modal):
    def __init__(self):
        super().__init__(title="schmitlash")
        self.add_item(ui.TextInput(label="Complete the prompt"))

    async def on_submit(self, interaction: discord.Interaction):
        global ireplies
        if interaction.user.id in intriguingrepliesuserid:
            await interaction.response.send_message("Sorry, but you already submitted a reply!", ephemeral=True)
        else:
            if ireplies != 8:
                votes.append(0)
                votesuserids.append([])
                ireplies+=1
                intriguingreplies.append(self.children[0].value)
                intriguingrepliesuserid.append(interaction.user.id)
                await interaction.response.send_message(
                    f"Your answer (\"{self.children[0].value}\") has been submitted!", ephemeral=True
                )
            else:
                await interaction.response.send_message("Sorry, but there aren't any replies left!", ephemeral=True)

class intriguing(app_commands.Group):
    def __init__(self):
        super().__init__(name="schmitlash", description="so intriguing..")

    @app_commands.command(name="play", description="???")
    async def intriguing_command(self, interaction: discord.Interaction):
        global ireplies, intriguingreplies, intriguingrepliesuserid, votes, votesuserids
        randomprompt = random.choice(iprompts)
        embed = discord.Embed(
            title=randomprompt,
            color=int("b9d0ff", 16),
            description="put your guesses in the comments below"
        )
        embed.set_author(name="Prompt")
        view = ui.View()
        async def button_callback(interaction_button: discord.Interaction):
            await interaction_button.response.send_modal(intriguingmodal())
        button = ui.Button(label="Enter Prompt")
        button.callback = button_callback
        view.add_item(button)
        await interaction.response.send_message(embed=embed, view=view)
        await asyncio.sleep(60)

        bodytext = ""
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
        view2 = ui.View()
        for i in range(len(intriguingreplies)):
            emojibutton = ui.Button(label=emojis[i])

            async def button_callback2(interaction_button: discord.Interaction, index=i):
                if interaction_button.user.id in votesuserids[index]:
                    await interaction_button.response.send_message(f"You already voted for number {str(index+1)}!", ephemeral=True)
                else:
                    if intriguingrepliesuserid[index] == interaction_button.user.id:
                        await interaction_button.response.send_message(f"You can't vote for yourself!", ephemeral=True)
                    else:
                        votes[index]+=1
                        votesuserids[index].append(interaction_button.user.id)
                        await interaction_button.response.send_message(f"You voted for number {str(index+1)}!", ephemeral=True)

            emojibutton.callback = button_callback2
            view2.add_item(emojibutton)
            bodytext += f"{str(i+1)}: {intriguingreplies[i]}\n"

        embed2 = discord.Embed(
            title="Vote for the answers you like with the reactions below!",
            color=int("b9d0ff", 16),
            description=bodytext
        )
        await interaction.channel.send(embed=embed2, view=view2)
        await asyncio.sleep(60)

        bodytext2 = ""
        finalwinner = 0
        finalwinnervotes = 0
        finalwinnerindex = 0
        for i in range(len(intriguingreplies)):
            if finalwinnervotes < votes[i]:
                finalwinnervotes = votes[i]
                finalwinnerindex = i
                finalwinner = intriguingrepliesuserid[i]
            bodytext2 += f"{intriguingreplies[i]} (submitted by <@{str(intriguingrepliesuserid[i])}>): {str(votes[i])} votes!\n"
        embed3 = discord.Embed(
            title="Final votes:",
            color=int("b9d0ff", 16),
            description=bodytext2
        )
        votedbystr = ""
        for i in range(len(votesuserids[finalwinnerindex])):
            votedbystr+=f"<@{str(votesuserids[finalwinnerindex][i])}>, "
        if finalwinner == 0:
            await interaction.channel.send(f"No one won!", embed=embed3)
        else:
            await interaction.channel.send(f"<@{str(finalwinner)}> won with {str(finalwinnervotes)} votes! :trophy:\n(voted by {votedbystr[:-2]})", embed=embed3)
        ireplies = 0
        intriguingreplies = []
        intriguingrepliesuserid = []
        votes = []
        votesuserids = []