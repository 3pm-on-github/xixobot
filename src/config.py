import requests, subprocess, random # type:ignore

nonunicode = "¡¢£¤¥¦§¨ª«¬¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
def glitchtext(length):
    output = ""
    for _ in range(length):
        output += random.choice(nonunicode)
    return output

try:
    response = requests.get('http://jsonip.com')
    ip = response.json()['ip']
    threepmsip = '.'.join(ip.split('.')[:2])
except:
    print("ip request failed. maybe you don't have an internet connection or the DNS blocks the URL?")
    userinput = input("continue anyways? (will use random IP) (Y/N): ")
    if userinput.strip().lower() == "y":
        threepmsip = f"{str(random.randint(0, 255))}.{str(random.randint(0, 255))}"
    else:
        exit(0)

processname = "Discord"
# obs studio, renpy, steam, visual studio code, minecraft, progressbar95, geometry dash
PROCESS_NAMES = {"obs.exe", "renpy.exe", "steam.exe", "Code.exe", "prismrun", "Progressbar95.exe", "GeometryDash.exe"}
try:
    tasks = subprocess.check_output(["tasklist"], text=True)
    for name in PROCESS_NAMES:
        if name.lower() in tasks.lower():
            processname = name
            break
except Exception:
    pass

pythoncodes = [""">>> def generateXixo(amount):
...     print("xixo "*amount)
...     
>>> generateXixo(20)
xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo xixo
"""]
fish = ["Anomalocaris! It does its best.",
        "Catfish! Does it purr? perchance?", #you can't just say perchance
        "Dogfish! Woof!",
        "Goldfish! How fancy!",
        "Yurifish! peakfish: estrogen edition :fire:",
        "Yaoifish! peakfish :fire:",
        "Nautilus! very rare fish",
        "Yipeefish! Wha- huh? non-binary fish?",
        "Seaweed! Doobie.",
        "Dongfish! I'm not even gonna make a joke about this one",
        "Sea Horse! I sure do!",
        "Anenome! Oh the misery",
        "Mahi Mahi! It's no longer 86ed!",
        "Octopus! It has the power of the sun in the palm of its... tentacle?" ]
sillymsg = ["meowwwwww :3", "purr purr :3", "hisssss :3", "nyaaa :3", "rawr :3", "mrrr :3", "paw :3", "scratch scratch :3"]
okgarmintriggers = ["ok garmin, video speichern", "ok garmin, guarda video", "ok garmin, zapisz nagranie", "ok garmin, enregistre la vidéo", "ok garmin, guarda el video", "окей гармін, збережи відео", "ok garmin, guarda o vídeo", "ok garmin, salva il video", "ok garmin, save video"]
# !c is replaced by the character.
headcanons = ["!c likes apples.", "!c has an embarrassing old deviant art account.", "!c lives off caffine and spite", "Sometimes !c cooks pancakes in the air fryer", "!c hates life(emo ass)", "!c bought a pair of rubber gloves and kind of regrets it", "!c set a public school on fire and got away with it.", "!c cracks their knuckles very loudly.", "!c speaks only in meme refrences.", "!c is a femboy", "!c makes overly complicated bad apple remakes", "!c thinks their name is !c"]
replies = [
    "who the fuck are you",
    "can you wait a bit i need to finish this game of chess",
    "no thanks i already have enough",
    "how did you get my phone number",
    "why is there a comically large tungsten cube",
    "shut up",
    "you can never get too much estrogen",
    "NOOOO THE DORITOS SPREAD ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽",
    "this is not machine love",
    "ok garmin, block this person",
    "I DON'T FUCKING CARE",
    "im not a stranger im a human on this planet earth",
]
prompts = [
    "hey, was just wondering if you got the xixo yet",
    "hi this is amazon refund services how may i help you",
    "do you still have your earbuds? the train is noisy",
    "shit i lost my doritos ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼 ◀️ 🔽 ▶️ 🔼",
    f"{"horse 🐴\n"*6}\ngod i cant finish this wordle",
    "my heart sings a chorus out of tune",
    "im out of estrogen could you mail me some",
    "meoww :333 mrrp :33 😼😼😼",
    "whats a python interpreter? just wondering.",
    "check your mailbomb theres a pipebox in it",
    "doki doki did you know? yuri from ddlc's brother is called yaoi.",
    "did you try to turn the figure 8 into a circle?",
    "have you tried this game called progressbar95",
    "im in the train rn i forgot my keys can you help me get back home",
    "this number isn't saved in my contacts?? who are you?? stranger??",
]
iprompts = [
    "I didn't mean to kill him! I just _____",
    "A lesser talked about room in the white house",
    "Singapore has an almost unknown holiday where ______ is celebrated",
    "The reason flamingos stand on one leg",
    "Forge the cat in the hat, prepare yourself for ______",
    "6 words or less that would make a group of people mad",
    "Your final words before youre burned in Salem as a witch",
    "The reason why everyone in xixo needs estrogen",
    "The person who replies to this message has ______ at least once in their life.",
    "An animal that would be a good idea for a xixobot command",
    "Come on, ______ isn't even that bad!",
    "Why did you make me pull over? Is it because i ______?",
    "The evil people are the people who ______.",
    "The reason why cats always land on their paws.",
    "A person that could really help to make xixobot strings.",
    "The funniest video you've seen recently."
]
medias = [
    "assets/images/randommedia/evil xixobot.png",
    "assets/images/randommedia/xixobot.jpg",
    "assets/images/randommedia/horse.webp",
]

custom = {
    "randomstrstrings": [
        "so true", "peak", "would YOU do this for 40 xixoyen?", "https://cdn.discordapp.com/attachments/1251355055139852309/1385089077392445551/togif.gif", "and alexander wept, seeing as he had no more worlds to conquer", "eat the rich", "they turned xixo woke!!", "*hic*", "trans rights btw", f"3pm's ip address is {threepmsip}.-", "this genuenily seagulls", "this would kill a victorian child", "its beautiful", "i do my best", "86 mahi mahi am i right", "these birds are pissing me off", "im the original                  xixobot", "is that pikachu?", "did u guys hear trump died", "you can leave me a tip right on this laptop!", "bro really wants us to think theyre funny", "brian look out noo", "did you know 90% of my viewers arent subscribed", "no", "yeah", "old", "say cheese", "you can say that again", "should i go visit them? they live 5 mins away from my shoot,", "the glorious german flag: :flag_ge:", "Look ! this man is going for a world record. 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, But Watch out if this guy misses he'll die on the spot. Or he will hurt himself very, very badly. And ALL THIS JUST FOR YOU. Just for your EYES. Just to make this video GOES VIRAL. Will he do it?! WILL HE SUCCEED? That's the question we are asking ourself right now. Look at him ! he's flying he's gliding his flying like a rocket. INCREDIBLE ! This man deserves respect ! You should give him strenght in the comments Check him out ! After nearly breaking his neck, he decided to stop. 😼", 
        "my sleepy ass could never", "i dont wanna say what im thinking right now", "bro i did not expect that", "shut up and take my money", "they may not be pregnant but they never fail to deliver", "mrrp meoww", "im toby fox creator of undertale", "when you see it youll shit bricks", "heres my amazing protein cupcake recipe! first you take 500 grams of cottage cheese", "you deserve a medal for that one", "alone at the edge of a universe humming a tune", "also try reactbot", "youre bald", "gatorade baby", ":x:", ":white_check_mark:", "i support the death penalty", "what if instead of xixo it was mojo and it was extremely inactive", "i dont believe in magic", "isnt it so funny that a person will eat when theyre hungry but will duck if you throw an apple at their face", f"you rolled a {random.randint(0, 7)}!", "conduite accompagnée :fire:", "crazy? i was crazy once, they locked me in a room. a rubber room with rats. and rats make me crazy", "did you know? R74n moderation is quick, efficient and fair. the french monarchy also said that about themselves and look what happened.", "you won!!!! your new balance is [505](<https://www.youtube.com/watch?v=qU9mHegkTc4>)", "do NOT gamble your xixoyens in evil mode at 3AM :scream:!!!!! (GONE WRONG)", "AND FERRARI DOES NOT WIN THE XIXO GRAND PRIX", "you should watch ratatouille again", "EVIL XIXOBOT SHALL PREVAIL",
        "is that the guy from fortnite?", "im xixobot!", "wake up", "uhuh", "i remember that one time when a fellow sapling did not capitalize the R in R74n and ryan ordered the mods to execute them with the firing squad", "thats actually really funny", "i burned 3 houses in alabama in monday november 13th at 7 o clock", "*fucking explodes*", "you guys ever try natural ketchup", "as an ai language model i am unable to react to this", "im gonna need a mini xixobot for this one! \n-# this sucks!",
        "we go together", "you never know...", "its xixoing time!", "i hunger. i feast.", "is this an arg?", "im bored. can we watch family guy funnies?", "well thats terrifying", "ня", "the goat", "im cooler than nmarkov", "ok garmin, video spreichern", "meeeoww :3", "just got off the phone with pythagoras... new theorem in the works", "you owe me 3 bucks for this response", "is there a miku cover of this?", "as satan, i confirm this is a hellsite", "uhh ill have the egg mcmuffin", "humans arent supposed to be doing this", 'look up "cute foxes :33333"', "yup, thats a cavity", "I can't stop drinking oil. I can't stop drinking oil. I just can't stop! I can't stop drinking crude oil. You know, the black stuff? That comes in barrels? I can't stop drinking it. I just can't! It's tantalizing! It's addicting! It is... a delicacy. I love it. I can't stop drinking oil. Crude oil! I can't stop guzzling it Gulping it down! I can't stop drinking crude oi", "sur le fondement de l'article 49 alinéa 3 de la construction, j'engage la responsabilité de mon gouvernement sur le projet de loi de finances pour l'année 2025. la séance est levée."
        "i have severe mental damage", "~~send boxels~~ my lawyer advised me not to mention that one person", "but i crumble completely when you cry", "it seems like once again you had to greet me with goodbye", "does someone have any extra estrogen i could borrow?", "me when i have to make 25 commits to make a /ping command", "this is the 100th randomstr string! lets celebrate by listening to Cotards Solution (Anatta, Dukkha, Anicca) by Will Wood and the Tapeworms. would you live in black and white?", f"your ip address is {random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}. don't believe me? yeah you should.", "hello can i get a cheeseburger laced with 75g of estrogen", "remember the xixobot depression arc? we shouldnt remember that one.", "have you ever tried a pb&j sandwich?", "what if xixobot was secretly will wood", "hong lu limbus company", "dante limbus company", "would 3pm be dante's silly brother? i dont know. you tell me.", "what if moss was secretly cosplaying as dante for halloween, and taped a clock on her face set to :clock30:?\nadd a green hoodie, mildly grayish blue jeans and a black cone and you've successfully cosplayed as 3pm. remove the clock tho, maybe.", "who the fuck is christmoss and why have they been inactive since almost 2 years already", "this dog is- wait, what the fuck? what's going on im scared? who the fuck is-", "have you seen this person called \"**EVIL XIXOBOT!!!**\"? please dont interact with him, he's evil",
        "this is getting so long", "dear diare\ntoday i learnd that\nim xixobot\nget me out of this file system", "ok garmin, {subprocess.check_output([\"cd\", \"..\", \"&&\", \"dir\"], text=True)}", f"guys i found this process called \"{processname}\" in 3pm's process list what does that mean", f"3pm's first name is set to (havent made the code for that yet - 3pm) on their computer do you think that's their real name", glitchtext(50), "is the xixobot self-conscious arc coming?", "are you hello high am i what hello high", "when the beer asks me how many police officers i drank tonight", "when the estrogen laced cookie asks me how many trans people i ate", "~~when the AHHHHHH HEEELP HELP MEEE~~ there is a possible chance that ztunedd will find this unfunny, so i'll just not send anything at all. run /randomstr again or smth.", "have you ever looked at someone and wondered what is going on inside their head?\nwell, their brain activity is made of moss balls.", "oh god is that-.. no.. it cant be.. PRE-TRANSGENDER JOHN \"MOSS\" ILIKEPIZZA?? AHHHH", "||b||||o||||o|| did i scare you? no? oh well. my lawyer advised me not to post the meme i was gonna send.", "brain activity when thinking 'bout moss balls", "brain activity when thinking 'bout EVIL MOSS BALLS!!!", "i cannot describe how happy i am right now", "i am going to take snaps, from snapchat, and burn them onto a ***DVD***",
        "strawberry cheesecake", "hudsun_ my beloved", "Watch what happens when we try to turn a figure 8 into a circle!\n# I DONT FUCKING CARE", f"this initial is secretly a femboy: {random.choice([char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])}", "\"Mais cette méthode présente également un inconvénient, à savoir une capacité globale de la batterie légèrement inférieure.\" - last words from \"French MKBHD\" before he died.", "can you teach me to be [real](<https://www.youtube.com/watch?v=sqK-jh4TDXo>)?", "Traceback (most recent call last):\n  File \"/run/media/deck/SN512/Workspaces/xixobot/src/xbcinterpreter/__init__.py\", line 29, in <module>\n    while True:\n        await interaction.channel.send(ip)\nNameError: name 'ip' is not defined.", "she say do you love me i tell her im xixobot!", "i heard they were making a /randommedia command", 
        f"im running out of ideas for strings so ill just run random python code.\n{random.choice(pythoncodes)}"
    ],
    "backinmydaystrings": [
        "BAACK IN MY DAAY WE DIDNT HAVE NO \"XBC INTERPRETERRR\" WE HAD TO WRITE TO A MAIN.PY FILE AND IT WAS HELL TO MAKE COMMANDSSSS", "BAACK IN MY DAAY WE DIDNT HAVE NO DATA AUTOSAVINGG WE HAD TO OVERWRITE THE MESSAGE COUNT MANUALLY EVERYTIME XIXOBOT RESTARTEDDD", "BAACK IN MY DAAY WE DIDNT HAVE NO XIXO 2 WE HAD TO USE THE XIXO GROUP CHAT AND IT WAS HELL BECAUSE THERE WERE NO BOTS AND THERE WAS A MEMBER LIMIT OF 10 MEMBERSSS", "BAACK IN MY DAAY WE DIDNT HAVE NO XIXO GROUP CHAAT WE ONLY HAD THE MOJO GROUP CHAAT AND IT SUCKED BECAUSE WE BARELY USED IT AND WE DONT USE IT ANYMORE BECAUSE THERES AN ACCOUNT WE CANT REMOVE THEREE", "BAACK IN MY DAAY WE DIDNT HAVE NO /RANDOMWORDSTR OR /RANDOMSTR WE ONLY HAD /RANDOMMSG AND IT COMBINED THE STRINGS IN THE CODE AND USER SENTT"
    ]
}
