import random

def get_word(prompt=""):
    while True:
        word = input(prompt).strip()
        if word:
            return word
        print("Please, enter (a) word/words")
     
def get_number(prompt=""):
    while True:
        try: 
            inp = input(prompt).strip()
            if inp == "":
                raise ValueError
            number = int(inp)
            return number
        except ValueError:
            print("Please, enter a number.")

def madLibs():
    print("Welcome to the game! Please, choose a template:")

    while True:
        temp_choice = input("1) The Hospital.\n2) The Camping.\n3) The Letter.\n")
        if temp_choice in ['1', '2', '3']:
            break
        else:
            print("No template found. Please, choose 1, 2, or 3.\n")
    
    if temp_choice == '1':
        numbers1 = []
        print("Input 2 numbers: ")
        for i in range(2):
            n = get_number()
            numbers1.append(n)
        measure_of_time = get_word("Input a measure of time: ")
        mode_of_trans = get_word("Input a mode of transportation: ")        
        adjs1 = []
        print("Input 3 adjectives: ")
        for i in range(3):
            a = get_word()
            adjs1.append(a)
        nouns1 = []
        print("Input 4 nouns: ")
        for i in range(4):
            n = get_word()
            nouns1.append(n)
        color = get_word("Input a color: ")
        body_parts = []
        print("Input 2 body parts: ")
        for i in range(2):
            bp = get_word()
            body_parts.append(bp)
        verb1 = get_word("Input a verb: ")
        silly_word = get_word("Input a silly word: ")
        random_num1 = random.choice(numbers1)
        numbers1.remove(random_num1)
        random_num2 = random.choice(numbers1)
        print(f"It was about {random_num1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_trans}. The hospital is a/an {adjs1[0]} place, there are a lot of {adjs1[1]} {nouns1[0]} here. There are nurses here who have {color} {body_parts[1]}. If someone wants to come into my room I told them that they have to {verb1} first. I’ve decorated my room with {random_num2} {nouns1[1]}. Today I talked to a doctor and they were wearing a {nouns1[2]} on their {body_parts[1]}. I heard that all doctors {verb1} {nouns1[3]} every day for breakfast. The most {adjs1[2]} thing about being in the hospital is the {silly_word} {nouns1[0]}!")

    
    elif temp_choice == '2':
        person_name = get_word("Input a person's name: ")
        nouns2 = []
        print("Input 2 nouns: ")
        for i in range(2):
            n = get_word()
            nouns2.append(n)
        adjs2 = []
        print("Input 2 adjectives (feelings): ")
        for i in range(2):
            a = get_word()
            adjs2.append(a)
        animal = get_word("Input an animal: ")        
        verbs2 = []
        print("Input 2 verbs: ")
        for i in range(2):
            v = get_word()
            verbs2.append(v)
        color2 = get_word("Input a color: ")
        verb_ing = get_word("Input a verb (-ing): ")
        adverb = get_word("Input an adverb (-ly): ")
        num2 = get_number("Input a number: ")
        measure_of_time2 = get_word("Input a measure of time: ")
        silly_word2 = get_word("Input a silly word: ")
        random_noun1 = random.choice(nouns2)
        nouns2.remove(random_noun1)
        random_noun2 = random.choice(nouns2)
        print(f"This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {random_noun1}. I am so {adjs2[0]} to {verbs2[0]} in a tent. I am {adjs2[1]} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verbs2[1]}. I have heard that the {color2} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {num2} {measure_of_time2}. If I see a {color2} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {num2} {silly_word2} stories and roast {random_noun2} around the campfire!!")

    elif temp_choice == '3':
        person_name2 = get_word("Input a person's name: ")
        adjs3 = []
        print("Input 5 adjectives: ")
        for i in range(5):
            a = get_word()
            adjs3.append(a)
        color3 = get_word("Input a color: ")
        animal2 = get_word("Input an animal: ")        
        place = get_word("Input a place: ")
        mag_cr = []
        print("Input 2 magical creatures (plural): ")
        for i in range(2):
            mc = get_word()
            mag_cr.append(mc)
        house_room = get_word("Input a room in a house: ")
        nouns3 = []
        print("Input 3 nouns: ")
        for i in range(3):
            n = get_word()
            nouns3.append(n)
        nouns_pl3 = []
        print("Input 2 nouns (plural): ")
        for i in range(2):
            n = get_word()
            nouns_pl3.append(n)
        num3 = get_number("Input a number: ")
        measure_of_time3 = get_word("Input a measure of time: ")
        verb_ing2 = get_word("Input a verb (-ing): ")
        random_mgcr1 = random.choice(mag_cr)
        mag_cr.remove(random_mgcr1)
        random_mgcr2 = random.choice(mag_cr)
        print(f"Dear {person_name2}, I am writing to you from a {adjs3[0]} castle in an enchanted forest. I found myself here one day after going for a ride on a {color3} {animal2} in {place}. There are {adjs3[1]} {random_mgcr1} and {adjs3[2]} {random_mgcr2} here! In the {house_room} there is a pool full of {nouns3[0]}. I fall asleep each night on a {nouns3[1]} of {nouns_pl3[0]} and dream of {adjs3[3]} {nouns_pl3[1]}. It feels as though I have lived here for {num3} {measure_of_time3}. I hope one day you can visit, although the only way to get here now is {verb_ing2} on a {adjs3[4]} {nouns3[2]}!!")

    else:
        print("No template found:( Please, restart the game.")


madLibs()
