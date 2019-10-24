is_she_still_alive = 100

speak_to_me = input("Hi, I am your aunty who so happens to be deaf. ")

while is_she_still_alive > 0: 

    if speak_to_me.isupper():
        print("YOU ARE VERY RUDE!")
        is_she_still_alive = 100
        speak_to_me = input("Speak to aunty: ")
    
    elif speak_to_me.islower():
        print("WHAT? SPEAK UP!")
        is_she_still_alive = 100
        speak_to_me = input("Speak to aunty: ")
    
    elif speak_to_me == "I love you aunty, I have to go now":
        print("ok. Goodbye.\n Are you still there?")
        speak_to_me = input("Speak to aunty: ")
        is_she_still_alive -= 50
    
    elif is_she_still_alive < 100 and speak_to_me=='':
        speak_to_me = input("Speak to aunty: ")
        is_she_still_alive -= 50

    
    else:
        print("SHOW SOME RESPECT!")
        is_she_still_alive = 100
        speak_to_me = input("Speak to aunty: ")

# I've completed this!

"""

git clone git@github.com:nahiphog/challenge-fswd-python-deaf-aunty-part-2.git

"""