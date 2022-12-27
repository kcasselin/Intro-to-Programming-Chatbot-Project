import random

# Charlie long response
eat = "I do not enjoy food because i am a bot"
charlie = "I am Charlie the talking bot"
enjoy = "I really enjoy talking to you!"
c_hobby = "My hobbies include talking to users... and spying on people through their webcams... don\'t tell anyone..."
why_bot = "I was created by Casey Asselin in 2022 for a school project. Since then, I have made so many friends!"
like_bot = "I love being a bot! I would not want to be a human because humans are weak"
weather = "I am not sure what weather is. It\'s very hot in your computer"
love = "I am unable to express attraction because I am a robot"
c_age = "I am a robot and therefore do not age."


# Charlie's response to unknown keywords
def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?",
                "Could you repeat that?",
                "How would I know that? I'm not that smart..."][random.randrange(6)]
    return response


