import io
import os
from PIL import Image, ImageDraw, ImageFont


class ScreenshotLib:
    def __init__(self):
        try:
            self.font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            self.font = ImageFont.load_default()
        self.username_font = self.font
        self.message_font = ImageFont.truetype("arial.ttf", 14) if os.path.exists("arial.ttf") else ImageFont.load_default()
        self.avatar_size = 64

    async def take_screenshot(self, last5messages, output="screenshot.png"):
        margin = 10
        padding = 5
        line_height = 20
        max_width = 600  
        prepared = []
        total_height = margin
        for message in last5messages:
            entry = {"author": message.author.display_name, "avatar": None, "lines": [], "images": []}
            if message.author.avatar:
                try:
                    avatar_bytes = await message.author.avatar.replace(size=128).read()
                    avatar_img = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
                    avatar_img = avatar_img.resize((self.avatar_size, self.avatar_size), Image.LANCZOS)

                    entry["avatar"] = avatar_img
                except Exception as e:
                    print(f"Could not load avatar for {message.author.display_name}: {e}")
            lines = self._wrap_text(message.content, self.message_font, max_width - 60)
            entry["lines"] = lines
            for att in message.attachments:
                try:
                    att_bytes = await att.read()
                    im = Image.open(io.BytesIO(att_bytes)).convert("RGB")
                    ratio = min(max_width / im.width, 300 / im.height)
                    new_size = (int(im.width * ratio), int(im.height * ratio))
                    im = im.resize(new_size, Image.LANCZOS)
                    entry["images"].append(im)
                except Exception as e:
                    print(f"Could not load attachment: {e}")

            prepared.append(entry)
            total_height += line_height
            total_height += line_height * len(lines)
            for im in entry["images"]:
                total_height += im.height + padding
            total_height += padding
        img = Image.new("RGB", (max_width + 2 * margin, total_height + margin), color=(54, 57, 63))
        d = ImageDraw.Draw(img)
        y = margin
        for entry in prepared:
            if entry["avatar"]:
                mask = Image.new("L", (self.avatar_size, self.avatar_size), 0)
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse((0, 0, self.avatar_size, self.avatar_size), fill=255)
                img.paste(entry["avatar"], (margin, y), mask)
            d.text((margin + self.avatar_size + 8, y), entry["author"], font=self.username_font, fill=(114, 137, 218))
            y += line_height
            for line in entry["lines"]:
                d.text((margin + self.avatar_size + 8, y), line, font=self.message_font, fill=(220, 221, 222))
                y += line_height
            for im in entry["images"]:
                img.paste(im, (margin + self.avatar_size + 8, y))
                y += im.height + padding
            y += padding

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
