Chatbot Project by Casey Asselin
December 5th, 2022
Intro to Computer Programming
Professor: Dr. Uzair Ahmed

# General Information
If at any time while running the program, you would like to exit the program, input "goodbye" into the chat box
If at any time while running the program, you would like access the other bot, input the name of the bot you would like to access
You will be unable to perform either of these functions while creating a new user profile
In Kelly, your travel destination is case-sensitive, be sure to input your destination with an uppercase first letter
    eg. Paris, Toronto, Dubai
    If you do not follow this, Kelly will set your destination to whatever you input, then be unable to print your ticket
Chat profiles are not mutually exclusive. If you create a profile with Kelly, Charlie will not be able to access that username
You can have the same username for both bots, but they are not stored in the same file and therefore seperate profiles need to be created
Program will end after a new user profile is created with Kelly or Charlie


# Startup
Upon startup, you will be introduced to the program and the two different bots that you are able to talk with
After the welcome message, you will be asked which bot you would like to start talking to
if you chose to speak with Kelly, She will introduce herself and continue with her conversation
If you chose to speak with Charlie, he will introduce himself and continue with his conversation


# Required Files
In order to run properly, you must have the following files saved in the same folder/directory:
    Chatbot.py - This is where all main code is stored
    long_responses.py - This is where all of Charlie's longer and randomized responses are stored
    user_profiles_talk.txt - This is where all user profiles for Charlie are stored
    user_profiles_airport.txt - This is where all user profiles for Kelly are stored
    readme.txt - This is the file that you are currently reading. it contains information on how to run Chatbot.py


# Kelly Profiles
When you chose to talk with Kelly, she will introduce herself and then ask if you already have a profile
If you do not have a profile, you will be prompted to create a new one.
If you do have a profile, you will be asked to sign in to your profile using the username that you set with Kelly earlier
When creating a new profile, Kelly will ask you to enter a username, this will be how Kelly identifies your profile
Kelly will then ask you to enter some key information that she needs in order to book your airline tickets
You will be unable to access Charlie while creating a profile with Kelly
You will be unable to exit the program while creating a profile with Kelly
Kelly cannot access profiles made with Charlie
Program will end after a new user profile is created


# Charlie Profiles
When you chose to talk with Charlie, he will introduce himself and then ask if you already have a profile
If you do not have a profile, you will be prompted to create a new one.
If you do have a profile, you will be asked to sign in to your profile using the username you set with Charlie earlier
When creating a new profile, Charlie will ask you to enter a username, this will be how Charlie identifies your profile
Charlie will then ask you to enter some key information that he needs in order to answer your questions properly while talking
You will be unable to access Kelly while creating a profile with Charlie
You will be unable to exit the program while creating a profile with Charlie
Charlie cannot access profiles made with Kelly
Program will end after a new user profile is created


#Kelly Main Code
Once you have signed into your profile with Kelly, she will list off some possible destinations, then ask you where you want to go
You will enter the city that you would like to travel to
    *This variable is case-sensitive. Refer to # General Information for proper format*
After you decide where you want to go, Kelly will tell you the price of your ticket based on your airline class preference
You will pay for your ticket with your credit card. If you forget the pin for your credit card, you will be unable to buy your ticket
After you pay for your ticket, Kelly will print your ticket to the screen and the program will end
At any time in Kelly Main Code you are able to access Charlie by saying "Charlie"
At any time in Kelly Main Code you are able to exit the program by saying "goodbye"


#Charlie Main Code
Once you have signed into your profile with Charlie, he will say hi and prompt you to start asking him questions
From here you are able to ask Charlie general questions, or questions about you specifically based on information in your profile
If you need suggestions of things to ask Charlie, I suggest any of the following:
    Hello
    How are you?
    What do you eat?
    Who are you?
    What do you like to do?
    What are your hobbies?
    When were you created?
    Are you real?
    Do you enjoy being a robot?
    What is the weather like today?
    Who do you love?
    I love you
    How old are you?
    What is my name?
    How old am I?
    How many family members do I have?
    How many pets do I have
    What do I like to do?
    Where did I grow up?
    What country am I from?
When you are finished talking to Charlie, say "goodbye" in the chat box

# Nonlocal Variables
The nonlocal keyword is used when accessing a variable inside a nested function where the variable should not
belong to the inner function

# References:
Shaw, Z. (2014) Learn Python The Hard Way (Python Version 2.5.1).
Idently. (2021) text_recognition_chat (Python Version 3) https://github.com/indently/text_recogniton_chat

