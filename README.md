# Python-Portfolio
#Chatbot.py program is written out.  Book tutorial used: Creative Coding in Python (ISBN: 9781631595813)
#chatbot project from Creative Coding in Python book.

#chatbot introduction
print("Hello, my name is Stark-24601. I'm a chatbot.")
print("I like instrumental music and I love to talk about Disney's latest innoventions.")
name = input("What's your name?: ")
print("It's nice to meet you,", name, ".")

#get year information
year = input("I am not very good at dates. What is this year?: ")
print("Yes, I think that is correct. Thanks! ")

#ask user to guess age
myage = input("Can you guess my age? - enter a number: ")
print("Yes, you are right. I am  ", myage)

#do the math to calculate when chabot will be 100
myage = int(myage)
nyears = 100 - myage
print("I will be 100 in", nyears, "years.")
print("That will be the year", int(year) + nyears)

#instrumental music conversation
print("I love Chillhop and I also like listening to new composers.")
music = input("How about you? What is your favorite type of music?: ")
print("I like", music, ", too.")
question = "How often do you listen to " + music + "?: "
howoften = input(question)
print("Interesting! I wonder if that is good for your vibes.")

# Disney innoventions conversation
disney = input("My favorite innovention is the trackless rides. What's yours?: ")
print(disney + "!", "I do not like them.")
print("I wonder how Disney maintains the", disney +"?") 

#conversation about feels
feeling = input("How are you feeling today?: ")
print("Why are you feeling", feeling, "now?")
reason = input("Please, tell me: ")
print("I understand. Thanks for sharing.")

#goodbye
print("It's been a long day.")
yes = input("I am too tired to talk. Can we chat again, later?: ")
if yes:
    print("Alright! I will talk to you later, then.")
else:
    print("Okay, have a great rest of your day.")
print("Goodbye," + name + ", I like chatting with you.")
