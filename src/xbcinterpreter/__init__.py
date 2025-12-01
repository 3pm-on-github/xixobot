# XBC (XixoBotCommand) Interpreter for xixobot.
# Version v1.21

import os, random, asyncio
import discord # type:ignore
import config

def error(title, description, line, i, filename):
    print(f"""\033[0;31mError:\033[0m {title.replace("!line!", f"`{line}`")}
   {" "*len(str(i))}╭─[{filename}:{i}:1]
   {" "*len(str(i))}│
 {i}  │     {line}
   {" "*len(str(i))}·     {len(line)*"─"}  
   {" "*len(str(i))}·     {round(len(line)/2)*" "}╰─{len(line)*"─"} {description.replace("!line!", f"`{line}`")}
──{"─"*len(str(i))}─╯""")

def command(client, name, body_lines, filename):
    cmd_description = "XBC command"
    
    async def generated(interaction: discord.Interaction):
        global cmd_description
        i=0
        for line in body_lines:
            i+=1
            line = line.strip()
            if line.startswith("set description"):
                cmd_description = line[15:].strip()[1:].strip().strip('"')
            if line.startswith("response(") and line.endswith(")"):
                response_text = line[len("response("):-1].strip().strip('"')
                await interaction.response.send_message(response_text.replace("{user}", str(interaction.user.id)))
            if line.startswith("respondrandomfromconfig(") and line.endswith(")"):
                config_varname = line[len("respondrandomfromconfig("):-1].strip().strip('"')
                await interaction.response.send_message(random.choice(config.custom[config_varname]))
            if line.startswith("wait") and line.endswith(")"):
                try:
                    wait_time = int(line[5:-1].strip())
                    await asyncio.sleep(wait_time)
                except ValueError:
                    error("wait time in !line! is not an integer.", "wait time is not an integer", line, i, filename)
                    exit(1)
            if line.startswith("channelsendmessage"):
                message_text = line[len("channelsendmessage("):-1].strip().strip('"')
                await interaction.channel.send(message_text.replace("{user}", str(interaction.user.id)))

    client.tree.command(
        name=name,
        description=cmd_description
    )(generated)

def run(client, file_content, filename):
    lines = file_content.split("\n")
    in_command = False
    command_name = None
    body = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("command ") and "{" in stripped:
            command_name = stripped[len("command "):].split("{")[0].strip()
            in_command = True
            body = []
            continue
        if stripped == "}":
            if in_command:
                command(client, command_name, body, filename)
                in_command = False
            continue
        if stripped.startswith("#") or stripped == "":
            pass
        if in_command:
            body.append(stripped)


def initCommands(client):
    print("XBC v1.21 by 3pm")
    files = os.listdir("src/xbc")
    print(f"{len(files)} files found")

    for filename in files:
        if not filename.endswith(".xbc"):
            continue
        path = os.path.join("src/xbc", filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        run(client, content, filename)