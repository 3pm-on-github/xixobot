# xixobot DOCUMENTATION
xixobot is a discord bot made for xixo yapyapyap, anyways lets get to programming, because that's what you're here for, probably.

## COMMANDS

making commands depends if you want them to be a **sub-command**, or a **command**.<br>

- a **sub-command** is a command that's part of a **group**, which gives it a space in it's name.<br>
for example, if the command "kick" is part of a **group** called "modcmds", it would be called:
`/modcmds kick`<br>

- a **command** is a command. it's that simple. except, it doesn't allow spaces in it's name.<br>
for example, if i tried making a command called `/modcmds kick`, it would cause an error, because there's a space in it's name.<br>
in this case you would use a **sub-command**. but, if your command is called `/modcmds-kick`, it wouldn't give an error.
### How to make a command
you will mainly use **commands.py** for adding **commands** or **sub-commands**.<br>

- for **sub-commands**, you will need to add:
```py
class yourgroupnamehere(app_commands.Group):
    def __init__(self):
        super().__init__(name="yourgroupnamehere", description="your group description here")
```
inside of the register function, to initiate the **group**. then, to make a **sub-command** in the **group**, you need to add:
```py
    @app_commands.command(name="yourcommandnamehere", description="your command description here")
    async def yourcommandnamehere_command(self, interaction: discord.Interaction):
        pass
```
the **pass** is only for demonstration. in reality, you will need to put something else instead of the **pass**.<br>
now, you need to append the **group** to the **client**'s **tree**. you should only do this for every **group**.<br>
to do that, append this to the end of **main.py**'s **xixobot** class's **__init__** function.<br>
```py
self.tree.add_command(commands.yourgroupnamehere())
```
and now you are done! you've successfully made a **sub-command**. you should continue to the response section.<br>

- for **commands**, you will need to add:
```py
@client.tree.command(name='yourcommandnamehere',description="your command description here")
async def yourcommandnamehere_command(interaction: discord.Interaction):
    pass
```
inside of the register function. the **pass** is only for demonstration. in reality, you will need to put something else instead of the **pass**.<br>
and now you are done! you've successfully made a **command**. you should continue to the response section.

## RESPONSE
after you've made your **(sub-)command**, you should give a **response** to the **interaction**.<br>
the **interaction** is the user who ran the **(sub-)command**. you should always return something to the **interaction**.<br>
to give a **response** to the **interaction**, you will need to append this to your **(sub-)command**:
```py
await interaction.response.send_message("your message here")
```
this will return a message to the **interaction**.