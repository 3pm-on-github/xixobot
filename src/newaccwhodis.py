import random, asyncio
import discord # type:ignore
from discord import app_commands, ui # type:ignore

reply = ""
replies = [
    "who the fuck are you",
    "can you wait a bit i need to finish this game of chess",
    "no thanks i already have enough",
    "how did you get my phone number",
    "why is there a comically large tungsten cube"
]

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
        prompts = [
            "hey, was just wondering if you got the xixo yet",
            "hi this is amazon refund services how may i help you",
            "do you still have your earbuds? the train is noisy"
        ]
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