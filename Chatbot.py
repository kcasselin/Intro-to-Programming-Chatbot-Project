import re
import long_responses as long
from random import *
# Techniques used to create this program were learned from "Learn to code the hard way" a textbook written by Zed Shaw
# Opening files for Kelly
airport_file = open('user_profiles_airport.txt', 'r+')
airport_user_file = open('user_profiles_airport.txt', 'r+')
# Opening files for Charlie
file = open('user_profiles_talk.txt', 'r+')
user_file = open('user_profiles_talk.txt', 'r+')

# ----------------------------------------------------------------------------------------------------------------------
# Introduction
print(
    '''
    --------------------------------------------------------------------------------------------------------------------
    Welcome to Casey's Chatbot Project! 
    
    In this file you will be able to access Kelly and Charlie
    Kelly works at the Oshawa Airport and will be able to book you a plane ticket to an available destination
    Charlie will be your friend if you're feeling lonely
    If, at any time, you would like to exit the program, please enter "goodbye" to the chat box
    If you would like to switch agents, please enter their name into the chat box 
    --------------------------------------------------------------------------------------------------------------------
    '''
)
# ----------------------------------------------------------------------------------------------------------------------
# Defining f_charlie as a function that holds the code for our talking bot named Charlie


def f_charlie():
    players = {}
    print('Bot: Hello, My name is Charlie! I understand you want someone to talk to.')
    run = True
    print('Bot: Is this correct?')
    # decides to continue conversation with talk bot or not
    while run:
        comment = input('You: ')
        if comment == 'yes':
            run = False
            print('Bot: Fantastic!')
        elif comment == 'no':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif comment.lower() == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif comment.lower() == 'kelly':
            print('Bot: Calling Kelly')
            f_kelly()
        else:
            print('Bot: Please enter yes or no. ')
# ----------------------------------------------------------------------------------------------------------------------
# Checking for existing user profile
    run = True
    print('Bot: Have you created a profile with this chat bot before?')
    print('Bot: Profiles are specific to respective bots')
    # asks for info about user
    while run:
        created_profile = input('You: ')
        # if user already exists, pulls info, continue with program
        if created_profile == 'yes':
            print('Bot: Great! Please enter your username. ')
            username = input('You: ')
            if username in user_file.read():
                run = False
                print('Bot: Login Successful!')
                user_file.seek(0, 0)
                players = eval(user_file.readlines()[0])
                print('Bot: Hello, ' + players[username]['name'] + '! \nBot: We are now in a conversation!')
                print('Bot: You can now start asking me questions!')
            elif username.lower() == 'goodbye':
                print('Bot: Okay, Have a nice day!')
                exit()
            elif username.lower() == 'kelly':
                print('Bot: Calling Kelly')
                f_kelly()
            else:
                print('Bot: Username Invalid.\nBot: Please restart the chat bot')
                exit()
# ----------------------------------------------------------------------------------------------------------------------
# Creates new profile for new user
        elif created_profile == 'no':
            create_new = True
            print('Bot: Okay, Would you like to create a new profile?')
            while create_new:
                create_new = input('You: ')
                if create_new == 'yes':
                    create_new = False
                    run = False
                    print('Bot: To create a new profile I need to ask you a few questions. ')
                    print('Bot: You will be unable to exit the program at this time. ')

                    # asks questions to create new user profile
                    def character():
                        new_username = input('Bot: Please enter a new username for your profile.\nYou: ')
                        if new_username in user_file.read():
                            print('Bot: Username already in use. \nBot: Please restart the chat bot')
                            exit()
                        elif new_username.lower() == 'goodbye':
                            print('Bot: Okay, Have a nice day!')
                            exit()
                        elif new_username.lower() == 'kelly':
                            print('Bot: Calling Kelly')
                            f_kelly()
                        else:
                            name = input('Bot: What is your name?\nYou: ')
                            user = {}
                            print('Bot: nice to meet you, ' + name + '!')
                            age = input('Bot: How old are you?\nYou: ')
                            country = input('Bot: What country did you grow up in? \nYou: ')
                            family = input('Bot: How many people are in your family? \nYou: ')
                            pets = input('Bot: How many pets do you have? \nYou: ')
                            hobby = input('Bot: What is your favourite hobby? \nYou: ')
                            user['name'] = name
                            user['age'] = age
                            user['country'] = country
                            user['family'] = family
                            user['pets'] = pets
                            user['hobby'] = hobby
                            players[new_username] = user

                    print(players)
                    # writes user profile to text file to be accessed later
                    if len(user_file.read()) > 0:
                        user_file.seek(0, 0)
                        players = eval(user_file.readlines()[0])
                    else:
                        players = {}
                    character()
                    file.seek(0, 0)
                    file.write(str(players))
                    file.close()
                    print(
                        'Bot: Congrats! You created a new profile! \nBot: To continue our conversation, the program will have to restart. '
                        'Don\'t worry! I will see you soon after logging back in!')
                    exit()
                elif create_new.lower() == 'goodbye':
                    print('Bot: Okay, Have a nice day!')
                    exit()
                elif create_new.lower() == 'kelly':
                    print('Bot: Calling Kelly')
                    f_kelly()
                elif create_new == 'no':
                    print('Bot: Okay, Have a nice day!')
                    exit()
                else:
                    print('Bot: Please enter yes or no. ')
        elif created_profile == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif created_profile == 'kelly':
            print('Bot: Calling Kelly')
            f_kelly()
        else:
            print('Bot: Please enter yes or no. ')
# ----------------------------------------------------------------------------------------------------------------------
# Start of main code for Charlie
    # function that decides which response to use depending on keywords in user input
    # Lines 162-199 and 230-245 of code is inspired by Idently's educational YouTube video.
    # Source cited at end of program

    def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
        message_certainty = 0
        has_required_words = True

        # Counts how many words are present in each predefined message
        if user_message[-1] in recognised_words:
            message_certainty += 1
        elif user_message[-1].lower() == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif user_message[-1].lower() == 'kelly':
            print('Bot: Calling Kelly')
            f_kelly()

        # Calculates the percent of recognised words in a user message
        percentage = float(message_certainty) / float(len(recognised_words))

        # checks that the required words are in the string
        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break

        # must either have the required words, or be a single response
        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    # function that simplifies and stores responses in a dict and finds the best response for user input
    def check_all_messages(message):
        highest_prob_list = {}

        # simplifies response creation / adds it to the dict
        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response,
                                                                  required_words)

        # Charlie's Responses
        response('Hello!', ['hello', 'hi', 'sup', 'heyo'], single_response=True)
        response('I\'m doing fine, how are you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
        response(long.eat, ['what', 'you', 'eat'], required_words=['you', 'eat'])
        response(long.charlie, ['who', 'are', 'you'], required_words=['who', 'you'])
        response(long.enjoy, ['what', 'you', 'like', 'to', 'do', 'enjoy'])
        response(long.c_hobby, ['what', 'are', 'your', 'hobbies', 'hobby'])
        response(long.why_bot, ['when', 'created', 'birthday', 'why', 'robot', 'bot', 'are', 'real'])
        response(long.like_bot, ['do', 'you', 'like', 'enjoy', 'being', 'robot'], required_words=['you', 'robot'])
        response(long.weather, ['what', 'is', 'weather', 'today', 'like'], required_words=['weather'])
        response(long.love, ['who', 'you', 'love', 'i', 'you'], required_words=['love'])
        response(long.c_age, ['how', 'old', 'are', 'you'], required_words=['old', 'you'])

        # Charlie's response about user profile
        response('Your name is ' + players[username]['name'], ['what', 'is', 'my', 'name', 'who', 'am', 'i'])
        response('You are ' + players[username]['age'] + ' years old',
                 ['how', 'old', 'am', 'i', 'what', 'is', 'my', 'age'])
        response('You have ' + players[username]['family'] + ' family members',
                 ['how', 'many', 'family', 'members', 'do',
                  'i', 'have'])
        response('You have ' + players[username]['pets'] + ' pets', ['how', 'many', 'pets', 'do', 'i', 'have'],
                 required_words=['pets'])
        response('You really enjoy ' + players[username]['hobby'] + ' as a hobby',
                 ['what', 'do', 'i', 'like', 'to', 'do',
                  'what', 'is', 'my', 'favourite', 'hobby'])
        response('You grew up in ' + players[username]['country'],
                 ['where', 'did', 'i', 'grow', 'up', 'what', 'country',
                  'am', 'from'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)

        if highest_prob_list[best_match] < 1:
            return long.unknown()
        else:
            return best_match

    # function that gets input from user and simplifies it
    def get_response(user_input):
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response = check_all_messages(split_message)
        return response

    # testing the response system
    while True:
        print('Bot: ' + get_response(input('You: ')))
# ----------------------------------------------------------------------------------------------------------------------
# Defining f_kelly as a function that holds the code for our airport employee named Kelly


def f_kelly():
    air_players = {}
    print('Bot: Hello, My name is Kelly! I understand you would like to book a flight out of the Oshawa Airport. ')

    run = True
    print('Bot: Is this correct?')
    # decides to continue conversation with airline bot or not
    while run:
        comment = input('You: ')
        if comment == 'yes':
            run = False
            print('Bot: Amazing! ')
        elif comment == 'no':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif comment.lower() == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif comment.lower() == 'charlie':
            print('Bot: Calling Charlie')
            f_charlie()
        else:
            print('Bot: Please enter yes or no')
# ----------------------------------------------------------------------------------------------------------------------
# Checking is user profile already exists
    run = True
    print('Bot: Have you created a profile with this chat bot before?')
    print('Bot: Profiles are specific to respective bots')
    # asks for info about user
    while run:
        created_profile = input('You: ')
        # if user already exists, pulls info, continue with program
        if created_profile == 'yes':
            print('Bot: Great! Please enter your username. ')
            username = input('You: ')
            if username in airport_user_file.read():
                run = False
                print('Bot: Login Successful!')
                airport_user_file.seek(0, 0)
                air_players = eval(airport_user_file.readlines()[0])
                print('Bot: Hello, ' + air_players[username][
                    'first_name'] + '! \nBot: We will now proceed booking a ticket!')
            elif username.lower() == 'goodbye':
                print('Bot: Okay, Have a nice day!')
                exit()
            elif username.lower() == 'charlie':
                print('Bot: Calling Charlie')
                f_charlie()
            else:
                print('Bot: Username Invalid. \nBot: Please restart the airport bot')
                exit()
# ----------------------------------------------------------------------------------------------------------------------
# if user does not exist, creates new profile
        elif created_profile == 'no':
            create_new = True
            print('Bot Okay, Would you like to create a new profile?')
            while create_new:
                create_new = input('You: ')
                if create_new == 'yes':
                    create_new = False
                    run = False
                    print('Bot: To create a new profile I need to ask you a few questions. ')
                    print('Bot: You will be unable to exit the program at this time. ')

                    # asks questions to create new user profile
                    def character():

                        new_username = input('Bot: Please enter a new username for your profile. \nYou: ')
                        if new_username in airport_user_file.read():
                            print('Bot: Username already in use. \nBot: Please restart the chat bot')
                            exit()
                        elif new_username.lower() == 'goodbye':
                            print('Bot: Okay, have a nice day!')
                            exit()
                        elif new_username.lower() == 'charlie':
                            print('Bot: Calling Charlie')
                            f_charlie()
                        else:
                            first_name = input('Bot: What is your first name? \nYou: ')
                            user = {}
                            last_name = input('Bot: What is your last name? \nYou: ')
                            dob = input('Bot: What is your date of birth? \nYou: ')
                            credit_card = input('Bot: What is your 16 digit credit card number? \nYou: ')
                            pref_class = input(
                                'Bot: Would you prefer to fly first class, economy plus, or economy? \nYou:')
                            card_pin = input('Bot: Please enter the 4 digit pin for your credit card. \nYou: ')

                            user['last_name'] = last_name
                            user['first_name'] = first_name
                            user['dob'] = dob
                            user['credit_card'] = credit_card
                            user['pref_class'] = pref_class
                            user['card_pin'] = card_pin
                            air_players[new_username] = user

                    print(air_players)
                    # write user profile to text file to be accessed later
                    if len(airport_user_file.read()) > 0:
                        airport_user_file.seek(0, 0)
                        air_players = eval(airport_user_file.readlines()[0])
                    else:
                        air_players = {}
                    character()
                    airport_file.seek(0, 0)
                    airport_file.write(str(air_players))
                    airport_file.close()
                    print('Bot: Congrats! You created a new profile at the Oshawa Airport!\n'
                          'Bot: To schedule a new flight, the program will have to restart.\n'
                          'Bot: Please run this program again and sign into your account with your username. \n'
                          'Bot: Charlie will not recognize the username that you just created. \n'
                          'Bot: See you soon!\n')
                    exit()
                elif create_new.lower() == 'goodbye':
                    print('Bot: Okay, Have a nice day!')
                    exit()
                elif create_new.lower() == 'charlie':
                    print('Bot: Calling Charlie')
                    f_charlie()
                else:
                    print('Bot: Please enter yes or no. ')
        elif created_profile.lower() == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif created_profile.lower() == 'charlie':
            print('Bot: Calling Charlie')
            f_charlie()
        else:
            print('Bot: Please enter yes or no. ')
# ----------------------------------------------------------------------------------------------------------------------
# Start of main code for Kelly
    print('Bot: With this agent, you are able to buy a ticket to travel to one of the following cities: ')
    print('Bot: Toronto, New York, Paris, Dubai, Tokyo, or Sydney')
    # General variables for kelly
    seat = str(randint(1, 100))
    first = air_players[username]['first_name']
    last = air_players[username]['last_name']
    pref_class = air_players[username]['pref_class']
    credit_card = air_players[username]['credit_card']
    dob = air_players[username]['dob']
    card_pin = air_players[username]['card_pin']
    # determine price on ticket depending on user preferense
    if pref_class == 'economy':
        due = '50'
    elif pref_class == 'economy plus':
        due = '75'
    elif pref_class == 'first class':
        due = '100'
    else:
        due = '0'

    # classes for each ticket to make them easilly accessable
    class Toronto:
        flight = 'Toronto'
        time = '10:00'
        gate = "1"
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

    class NewYork:
        flight = 'New York'
        time = '11:00'
        gate = '2'
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

    class Paris:
        flight = 'Paris'
        time = '12:00'
        gate = '3'
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

    class Dubai:
        flight = 'Dubai'
        time = '13:00'
        gate = '4'
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

    class Tokyo:
        flight = 'Tokyo'
        time = '14:00'
        gate = '5'
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

    class Sydney:
        flight = 'Sydney'
        time = '15:00'
        gate = '6'
        ticket = (
                    '---------------------------------------------------\nBoarding Pass\n---------------------------------------------------\n'
                    'Flight      Boarding Time       Gate        Seat\n' + flight + '     ' + time + '               ' + gate + '           ' + seat + '\n'
                                                                                                                                                       '---------------------------------------------------\nPassenger Name: ' + first + ' ' + last + '\n'
                                                                                                                                                                                                                                                      'Date of Birth: ' + dob + '\nClass: ' + pref_class + '\nPayment: ' + credit_card + '\n'
                                                                                                                                                                                                                                                                                                                                         '---------------------------------------------------\nFrom: Oshawa                    To: ' + flight + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                '---------------------------------------------------\nAmount Due: $' + due + '\n---------------------------------------------------\n')

# ----------------------------------------------------------------------------------------------------------------------
# Execution of Kelly's code
    destination = input('Bot: Where would you like to go?\nBot: Ensure you are using proper capital letters. \nYou: ')
    if destination.lower() == 'goodbye':
        print('Bot: Okay, Have a nice day!')
        exit()
    elif destination.lower() == 'charlie':
        print('Bot: Calling Charlie')
        f_charlie()
    else:
        print('Bot: One ticket to ' + destination + ' in ' + pref_class + ' will be $' + due)
        print('Bot: to process this payment on credit card: ' + credit_card + ' please enter your pin number')
        payment = True
        while payment:
            pin = input('You: ')
            if pin == card_pin:
                payment = False
                print('Bot: Payment Successful!')
            elif pin == 'goodbye':
                print('Bot: Okay, Have a nice day!')
                exit()
            elif pin == 'charlie':
                print('Bot: Calling Charlie')
                f_charlie()
            else:
                print('Bot: You must make a payment to recieve a ticket.')
                print('Bot: If you no longer wish to purchase a ticket, say \"goodbye\"')
                print('Bot: If you wish to talk to Charlie, say \"Charlie\"')

        print('Thank you for your purchase! Here is your ticket:')
        if destination == 'Toronto':
            print(Toronto.ticket)
        elif destination == 'New York':
            print(NewYork.ticket)
        elif destination == 'Paris':
            print(Paris.ticket)
        elif destination == 'Dubai':
            print(Dubai.ticket)
        elif destination == 'Tokyo':
            print(Tokyo.ticket)
        elif destination == 'Sydney':
            print(Sydney.ticket)
        elif destination == 'goodbye':
            print('Bot: Okay, Have a nice day!')
            exit()
        elif destination.lower() == 'charlie':
            print('Bot: Calling Charlie')
            f_charlie()
        else:
            print('Bot: Hmm... That city is not on my list of destinations. Please restart the program and try again')
            exit()

        print('Bot: Thank you for booking with the Oshawa Airport! Hope to see you soon!')
        exit()

# ----------------------------------------------------------------------------------------------------------------------
# Decides which bot to run


start = True

while start:
    bot = input('Which bot would you like to speak with?\nYou:')
    if bot.lower() == 'charlie':
        kelly = False
        charlie = True
        while charlie:
            f_charlie()
            charlie = False

    elif bot.lower() == 'kelly':
        charlie = False
        kelly = True
        while kelly:
            f_kelly()
            kelly = False

    elif bot.lower() == 'goodbye':
        print('Bye!')
        exit()

# References:
# Shaw, Z. (2014) Learn Python The Hard Way (Python Version 2.5.1).
# Idently. (2021) text_recognition_chat (Python Version 3) https://github.com/indently/text_recogniton_chat

