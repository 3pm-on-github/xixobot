import discord # type:ignore
from discord import app_commands, ui # type:ignore
from data import Data

mood = "Happy"
data = Data("assets/data/data.json")
food = 0
happy = 0

class setnamemodal(ui.Modal):
    def __init__(self):
        super().__init__(title="Set Anomalocaris Name")
        self.add_item(ui.TextInput(label="Set the name of your Anomalocaris"))

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Name set successfully!", ephemeral=True)
        print(str(interaction.user.id)+" set the anomalocaris's name to "+self.children[0].value)
        data.saveAnomalocarisInfo(self.children[0].value)

class raiseananomalocaris(app_commands.Group):
    def __init__(self):
        super().__init__(name="raisean", description="raise an anomalocaris")

    @app_commands.command(name="anomalocaris", description="raise an anomalocaris")
    async def anomalocaris_command(self, interaction: discord.Interaction):
        global mood, food, happy
        happy -= 1
        food -= 2
        if happy > 75:
            mood = "im so happy!!1! :D"
        elif happy > 55:
            mood = "im happy :D"
        elif happy > 45:
            mood = "im okay :3"
        elif happy > 30:
            mood = "im kinda sad 3:"
        elif happy > 15:
            mood = "im very sad 3:"
        elif happy > 5:
            mood = "miserable"
        elif happy < 5:
            mood = "depression"

        if (food >= 10) and (food < 25):
            mood = "i hunger. i feast."
        elif food >= 5 and (food < 10):
            mood = "father i am in desperate need of food. please feed me."
        elif food == 0:
            mood = "im literally dead"

        name, dateofcreation = data.getAnomalocarisInfo()
        embed = discord.Embed(
            title=f"{name}",
            color=int("FF6347", 16),
            description=f"{mood} | Full: {food}% | Happiness: {happy}%",
        )
        embed.set_author(name=f"Anomalocaris - Since {dateofcreation}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1409280302727303271/1455138846793666562/thumbnail.jpg?ex=6953a328&is=695251a8&hm=26a088f9617ca8488e624fb1b5dd19560ec5d5ea7830bfdf4d24b4adde5478ed&")
        view = ui.View()

        async def button_callback(interaction_button: discord.Interaction):
            global food
            await interaction_button.response.send_message("You feed the Anomalocaris. It seems satisfied.")
            food += 25
            if food > 100:
                food = 100

        async def button2_callback(interaction_button: discord.Interaction):
            global happy
            await interaction_button.response.send_message("You pet the Anomalocaris. It.. purrs?")
            happy += 10
            if happy > 100:
                happy = 100

        async def button3_callback(interaction_button: discord.Interaction):
            await interaction_button.response.send_modal(setnamemodal())

        button = ui.Button(label="Feed")
        button2 = ui.Button(label="Pet")
        button3 = ui.Button(label="Set Name")
        button.callback = button_callback
        button2.callback = button2_callback
        button3.callback = button3_callback
        view.add_item(button)
        view.add_item(button2)
        view.add_item(button3)
        await interaction.response.send_message(embed=embed, view=view)