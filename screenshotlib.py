import io
import os
from PIL import Image, ImageDraw, ImageFont

def load_font(size=16):
    font_paths = [
        "NotoSans-Regular.ttf",
        "NotoSansCJK-Regular.otf",
        "Segoe UI Emoji.ttf",
        "NotoColorEmoji.ttf",
        "DejaVuSans.ttf",
    ]
    for font_name in font_paths:
        try:
            return ImageFont.truetype(font_name, size)
        except IOError:
            continue
    return ImageFont.load_default()

class ScreenshotLib:
    def __init__(self):
        try:
            self.font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            self.font = ImageFont.load_default()
        self.username_font = load_font(16)
        self.message_font = load_font(14)
        self.avatar_size = 32

    async def take_screenshot(self, last5messages, output="screenshot.png"):
        margin = 10
        padding = 5
        line_height = 20
        max_width = 600
        scale = 4

        prepared = []
        total_height = margin

        for message in last5messages:
            member = message.guild.get_member(message.author.id)

            entry = {
                "author": message.author.display_name,
                "avatar": None,
                "lines": [],
                "images": [],
                "file_names": [],
                "role_color": (114, 137, 218)
            }

            entry["role_color"] = member.color.to_rgb()

            if message.author.avatar:
                try:
                    avatar_bytes = await message.author.avatar.replace(size=512).read()
                    avatar_img = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
                    avatar_img = avatar_img.resize((self.avatar_size, self.avatar_size), Image.LANCZOS)
                    entry["avatar"] = avatar_img
                except Exception as e:
                    await message.channel.send(
                        f"ah you fucking piece of shit <@{message.author.id}> YOU COMMITTED A {e}!!!!!!!!!!"
                    )

            lines = self._wrap_text(message.content, self.message_font, max_width - 60)
            entry["lines"] = lines

            for att in message.attachments:
                try:
                    att_bytes = await att.read()
                    try:
                        im = Image.open(io.BytesIO(att_bytes)).convert("RGB")
                        ratio = min(max_width / im.width, 300 / im.height)
                        new_size = (int(im.width * ratio), int(im.height * ratio))
                        im = im.resize(new_size, Image.LANCZOS)
                        entry["images"].append(im)
                    except Exception:
                        entry["file_names"].append(att.filename)
                except Exception as e:
                    await message.channel.send(
                        f"ah you fucking piece of shit <@{message.author.id}> YOU COMMITTED A {e}!!!!!!!!!!"
                    )

            prepared.append(entry)
            total_height += line_height + line_height * len(lines)
            for im in entry["images"]:
                total_height += im.height + padding
            total_height += len(entry["file_names"]) * line_height
            total_height += padding

        img = Image.new(
            "RGB",
            ((max_width + 2 * margin) * scale, (total_height + margin) * scale),
            color=(54, 57, 63)
        )
        d = ImageDraw.Draw(img)
        y = margin * scale

        for entry in prepared:
            if entry["avatar"]:
                avatar_scaled = entry["avatar"].resize(
                    (self.avatar_size * scale, self.avatar_size * scale), Image.LANCZOS
                )
                mask = Image.new("L", (self.avatar_size * scale, self.avatar_size * scale), 0)
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse(
                    (0, 0, self.avatar_size * scale, self.avatar_size * scale), fill=255
                )
                img.paste(avatar_scaled, (margin * scale, y), mask)

            d.text(
                ((margin + self.avatar_size + 8) * scale, y),
                entry["author"],
                font=self.username_font.font_variant(size=16 * scale),
                fill=entry["role_color"]
            )
            y += line_height * scale

            for line in entry["lines"]:
                d.text(
                    ((margin + self.avatar_size + 8) * scale, y),
                    line,
                    font=self.message_font.font_variant(size=14 * scale),
                    fill=(220, 221, 222)
                )
                y += line_height * scale

            for im in entry["images"]:
                im_scaled = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
                img.paste(im_scaled, ((margin + self.avatar_size + 8) * scale, y))
                y += im_scaled.height + padding * scale

            for fname in entry["file_names"]:
                d.text(
                    ((margin + self.avatar_size + 8) * scale, y),
                    f"[File: {fname}]",
                    font=self.message_font.font_variant(size=14 * scale),
                    fill=(200, 200, 200)
                )
                y += line_height * scale

            y += padding * scale

        img.save(output)


    def _wrap_text(self, text, font, max_width):
        words = text.split()
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            if font.getlength(test_line) <= max_width:
                line = test_line
            else:
                lines.append(line.strip())
                line = word + " "
        if line:
            lines.append(line.strip())
        return lines
        