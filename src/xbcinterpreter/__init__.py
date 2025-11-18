# XBC (XixoBotCommand) Interpreter for xixobot.
# Version v1.1

import os, random
import discord # type:ignore
import config

def command(client, name, body_lines):
    response_text = None
    config_varname = None
    cmd_description = "XBC command"
    for line in body_lines:
        line = line.strip()
        if line.startswith("set description"):
            cmd_description = line[15:].strip()[1:].strip().strip('"')
        if line.startswith("response(") and line.endswith(")"):
            response_text = line[len("response("):-1].strip().strip('"')
        if line.startswith("respondrandomfromconfig(") and line.endswith(")"):
            config_varname = line[len("respondrandomfromconfig("):-1].strip().strip('"')

    if (response_text is None) and (config_varname is None):
        print(f"Error: Command '{name}' has no response.")
        return
    
    async def generated(interaction: discord.Interaction):
        if response_text is not None:
            await interaction.response.send_message(response_text)
        elif config_varname is not None:
            await interaction.response.send_message(random.choice(config.custom[config_varname]))

    client.tree.command(
        name=name,
        description=cmd_description
    )(generated)

def run(client, file_content):
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
                command(client, command_name, body)
                in_command = False
            continue
        if stripped.startswith("#") or stripped == "":
            pass
        if in_command:
            body.append(stripped)


def initCommands(client):
    print("XBC v1.0 by 3pm")
    files = os.listdir("src/xbc")
    print(f"{len(files)} files found")

    for filename in files:
        if not filename.endswith(".xbc"):
            continue
        path = os.path.join("src/xbc", filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        run(client, content)