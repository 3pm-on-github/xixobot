import random, asyncio
import discord # type:ignore
from discord import app_commands, ui # type:ignore
from config import *

reply = ""

class newaccwhodisview(ui.View):
    def __init__(self):
        super().__init__()
        for _ in range(3):
            label = random.choice(replies)
            button = ui.Button(label=label)

            async def callback(interaction: discord.Interaction, label=label):
                await interaction.channel.send(f'<@{interaction.user.id}> replied with "{label}"')

            button.callback = callback
            self.add_item(button)

class newaccwhodis(app_commands.Group):
    def __init__(self):
        super().__init__(name="newaccwhodis", description="new acc, who dis?")

    @app_commands.command(name="play", description="new acc, who dis?")
    async def intriguing_command(self, interaction: discord.Interaction):
        global replies, intriguingreplies, intriguingrepliesuserid, votes, votesuserids
        embed = discord.Embed(
            title=random.choice(prompts),
            color=int("b9d0ff", 16),
            description="Enter a Reply"
        )
        embed.set_author(name="New Message")
        view = ui.View()
        async def button_callback(interaction_button: discord.Interaction):
            await interaction_button.response.send_message("Choose a reply", view=newaccwhodisview(), ephemeral=True)
        button = ui.Button(label="Reply")
        button.callback = button_callback
        view.add_item(button)
        await interaction.response.send_message(embed=embed, view=view)