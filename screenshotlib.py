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

    def take_screenshot(self, last5messages):
        margin = 10
        padding = 5
        line_height = 20
        max_width = 600  
        total_height = margin
        for message in last5messages:
            total_height += line_height
            lines = self._wrap_text(message.content, self.message_font, max_width - 60)
            total_height += line_height * len(lines)
            if hasattr(message, "attachments"):
                for att in message.attachments:
                    try:
                        with Image.open(att) as im:
                            ratio = min(max_width / im.width, 300 / im.height)
                            total_height += int(im.height * ratio) + padding
                    except:
                        pass
            total_height += padding

        img = Image.new("RGB", (max_width + 2 * margin, total_height + margin), color=(54, 57, 63))
        d = ImageDraw.Draw(img)

        y = margin
        for message in last5messages:
            d.text((margin + 40, y), message.author.display_name, font=self.username_font, fill=(114, 137, 218))
            y += line_height
            lines = self._wrap_text(message.content, self.message_font, max_width - 60)
            for line in lines:
                d.text((margin + 40, y), line, font=self.message_font, fill=(220, 221, 222))
                y += line_height
            if hasattr(message, "attachments"):
                for att in message.attachments:
                    try:
                        with Image.open(att) as im:
                            ratio = min(max_width / im.width, 300 / im.height)
                            new_size = (int(im.width * ratio), int(im.height * ratio))
                            im = im.resize(new_size, Image.LANCZOS)
                            img.paste(im, (margin + 40, y))
                            y += new_size[1] + padding
                    except:
                        pass

            y += padding
        img.save("screenshot.png")

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
