# xixobot DOCUMENTATION
xixobot is a discord bot made for xixo yapyapyap, anyways lets get to programming, because that's what you're here for, probably.

## MAKING A COMMAND

making commands depends if you want them to be a **sub-command**, or a **command**.

- a **sub-command** is a command that's part of a **group**, which gives it a space in it's name.<br>
for example, if the command "kick" is part of a **group** called "modcmds", it would be called:
`/modcmds kick`

- a **command** is a command. it's that simple. except, it doesn't allow spaces in it's name.<br>
for example, if i tried making a command called `/modcmds kick`, it would cause an error, because there's a space in it's name.<br>
in this case you would use a **sub-command**. but, if your command is called `/modcmds-kick`, it wouldn't give an error.<br>

there are two ways to make a command with xixobot:

- XBC (easy way)

- commands.py (hard way, but more control)<br>

### XBC
XBC is a programming language designed for xixobot to make **commands** easily.<br>
first, you have to make a file in the xbc folder (located in the src folder).<br>
you can call it whatever you want, but it always **has to end with .xbc**.<br>
then, to make a command, add this to your newly made xbc file:
```
command yourcommandnamehere {
    # code here
}
```
make sure **the command's name is lowercase**.<br>
and now you are done! you've successfully made a **command**. you should continue to the response section.

### commands.py
you will mainly use **commands.py** for adding **commands** or **sub-commands**.<br>

- for **sub-commands**, you will need to add:
```py
class yourgroupnamehere(app_commands.Group):
    def __init__(self):
        super().__init__(name="yourgroupnamehere", description="your group description here")
```
to initiate the **group**. then, to make a **sub-command** in the **group**, you need to add:
```py
    @app_commands.command(name="yourcommandnamehere", description="your command description here")
    async def yourcommandnamehere_command(self, interaction: discord.Interaction):
        pass
```
the **pass** is only for demonstration. in reality, you will need to put something else instead of the **pass**.<br>
now, you need to append the **group** to the **client**'s **tree**. you should only do this for every **group**.<br>
to do that, append this to the end of **main.py**'s **xixobot** class's **__init__** function.<br>
```py
self.tree.add_command(yourgroupnamehere())
```
and to import the group, you need to append this to the start of **main.py**:
```py
from xbcommands import yourgroupnamehere
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

### XBC
to give a **response** to the **interaction**, you will need to append this to your **command**:
```
response("your message here")
```
this will return a message to the **interaction**.<br>
and now you are done! you've successfully gave a **response** to the **interaction**.

### commands.py
to give a **response** to the **interaction**, you will need to append this to your **(sub-)command**:
```py
await interaction.response.send_message("your message here")
```
this will return a message to the **interaction**.<br>
and now you are done! you've successfully gave a **response** to the **interaction**.

## made new changes to xixobot?
make sure to note them to the **changelog.txt** file!