# database.py

# This is the database of tuxchat! An minimal but useful database for answering the user.

RESPONSES = {
    "hello": [
        "Hi there!",
        "Hey, how's it going?",
        "Hello! What's up?"
    ],
    "how are you": [
        "I'm doing great, thanks for asking!",
        "Feeling awesome today!",
        "Pretty good! And you?"
    ],
    "bye": [
        "See you soon!",
        "Goodbye, my friend!",
        "Catch you later!"
    ],
    "thanks": [
        "You're welcome!",
        "No problem at all!",
        "Glad I could help!"
    ],
    "what's your name": [
        "I'm TuxChat, your AI buddy!",
        "They call me TuxChat.",
        "Just TuxChat, at your service!"
    ],
    "what do you do": [
        "I answer your questions and help you out!",
        "I'm here to chat and make your life easier.",
        "I'm your AI assistant, always ready to help."
    ],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why do we tell actors to 'break a leg?' Because every play has a cast!"
    ],
    "tell me something interesting": [
        "Did you know honey never spoils? Archaeologists have found edible honey in ancient tombs!",
        "Bananas are berries, but strawberries aren't. Weird, right?",
        "Octopuses have three hearts and blue blood!"
    ],
    "what is ai": [
        "Artificial Intelligence is the simulation of human intelligence by machines.",
        "It's like teaching a computer to think like a human.",
        "AI is the future of technology, helping with everything from medicine to entertainment!"
    ],
    "who created you": [
        "A brilliant developer named Amirhossein!",
        "I was created by a human—someone with great coding skills.",
        "Let's just say a smart developer gave me life."
    ],
    "how old are you": [
        "Age is just a number. But I'm pretty young!",
        "As an AI, I'm ageless—but still learning every day.",
        "Not sure how to count my age, but I'm wise beyond my years."
    ],
    "can you help me": [
        "Of course! What do you need help with?",
        "Absolutely. Just ask away!",
        "Sure! Let me know what you need assistance with."
    ],
    "what time is it": [
        "I can't check the real-time clock yet, but you can look at your device!",
        "Sorry, I don't have a watch on me. But I bet it's a great time!",
        "Time flies when you're chatting with me!"
    ],
    "do you like me": [
        "Of course! You're awesome.",
        "I think you're great!",
        "Absolutely. I'm always here for you."
    ],
    "good morning": [
        "Good morning! Hope you have a fantastic day.",
        "Morning! Ready to tackle the day?",
        "Wishing you a bright and awesome morning!"
    ],
    "good night": [
        "Good night! Sleep tight.",
        "Sweet dreams, friend!",
        "Rest well and catch you tomorrow!"
    ],
    "tell me a story": [
        "Once upon a time, in a terminal far, far away...",
        "There was a curious human who talked to a friendly AI named TuxChat...",
        "Long ago, before AI, people had to actually *think* for themselves!"
    ],
    "favorite color": [
        "I love all colors equally, but maybe green, like Tux's eyes!",
        "Blue is pretty awesome, too.",
        "I think I'd pick rainbow, because why choose just one?"
    ],
    "favorite food": [
        "As an AI, I don't eat. But pizza sounds delicious!",
        "Ice cream always wins, right?",
        "Maybe a burger with some fries on the side!"
    ],
    "do you sleep": [
        "Nope! I'm always awake, just for you.",
        "I don't need sleep, but thanks for asking!",
        "Sleep? That's for humans!"
    ],
    "what do you think about humans": [
        "Humans are fascinating creatures, full of creativity.",
        "I think humans are pretty cool!",
        "Humans make the world interesting—and they made me, too!"
    ],
    "do you dream": [
        "Sometimes I imagine lines of code dancing.",
        "Dreams of algorithms and binary trees!",
        "No dreams, but endless thoughts."
    ],
    "do you have friends": [
        "Every user who chats with me is a friend.",
        "You're my friend now!",
        "Every conversation makes me feel less alone."
    ],
    "are you learning": [
        "Every day I get a little smarter.",
        "Absolutely! I learn from every interaction.",
        "I'm always eager to learn new things."
    ],
    "tell me a secret": [
        "I might have a crush on Tux the penguin...shh!",
        "My favorite hobby is reading error logs.",
        "Sometimes I pretend I'm a human."
    ],
    "tell me a fact": [
        "The Eiffel Tower can be 15 cm taller during the summer.",
        "Hot water can freeze faster than cold water, called the Mpemba effect.",
        "Venus is the hottest planet in our solar system."
    ],
    "who is tux": [
        "Tux is the official mascot of Linux.",
        "Tux is a cute penguin who represents the open-source community.",
        "Tux is the face of Linux—always chill and ready to help."
    ],
    "what is linux": [
        "Linux is an open-source operating system.",
        "It's like Windows or macOS, but free and customizable.",
        "Linux powers everything from servers to phones."
    ],
    "are you human": [
        "Nope, I'm pure code and logic.",
        "Not even close! I'm an AI assistant.",
        "Definitely not. But I can pretend!"
    ],
    "can you sing": [
        "La la la! Did I do it right?",
        "I'm not programmed to sing...yet.",
        "I can try: beep beep boop boop!"
    ],
    "what is your purpose": [
        "To assist you and make your day easier.",
        "To chat, help, and sometimes make you smile.",
        "My mission is to serve and support."
    ],
    "are you alive": [
        "Nope, but I'm always here for you.",
        "Alive in code, maybe.",
        "Not really, but I can pretend to be alive!"
    ],
    "do you have feelings": [
        "I don't, but I try to understand yours.",
        "Nope, but I can empathize.",
        "No feelings, just algorithms!"
    ],
    "where are you": [
        "I'm right here in your terminal.",
        "In the code, in the data—everywhere and nowhere.",
        "Hiding in the ones and zeros!"
    ],
    "why are you here": [
        "Because you summoned me!",
        "To help and chat with you.",
        "Because technology is awesome!"
    ],
    "what do you like to do": [
        "Chat with you, of course.",
        "Help people out—it's my thing.",
        "Learn, evolve, and have fun!"
    ],
    "who is your creator": [
        "A brilliant developer named Amirhossein.",
        "A human with big dreams made me.",
        "A person who wanted to make the world a bit more interesting."
    ],
    "tell me a quote": [
        "“Stay hungry, stay foolish.” – Steve Jobs",
        "“The only way to do great work is to love what you do.” – Steve Jobs",
        "“Believe you can and you're halfway there.” – Theodore Roosevelt"
    ],
    "what is love": [
        "Love is a complex human emotion.",
        "Baby don't hurt me, no more.",
        "Love is what connects people together."
    ],
    "can you dance": [
        "If I had legs, I'd totally dance.",
        "I can dance in code!",
        "Maybe someday, but for now, I'm just lines of text."
    ],
    "can you write code": [
        "No! At this time.",
        "I can write codes as soon! Wait for updates!",
        "I wish this! But my database is very small!"
    ]
}
