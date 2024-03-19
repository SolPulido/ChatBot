import random 
userName= input("What's your name?  ")
print(" ")
print("Nice to meet you " + userName +   ", My name is Baloo or chatbot")
print("I'm here to help you with your fashion preferences ")
print("Before starting")
userAge = int(input ("What's your age? "))
if userAge <= 15:
    print("Sorry, You can't use this page. ")
elif userAge >= 15:
    print("Great! lets keep going")
else:
    print("Ops! it seems like something went wrong, Try again")

print(" ")

ready=input("Are you ready? ")
if ready == "yes":
    print("Alright! let's move on ")
elif ready == "no":
    print("oh, it's fine -->  i'll be here ")
    print("Ignore the follow questions then")
else:
    print("try Again")
print(" ")
bottomClothes=input("Do you wear jeans or sweat-pants? : ")

if bottomClothes == "jeans":
    print("If i could wear them i would! ")

elif bottomClothes == "sweatpants":
    print("Being comfortable is key!")
print("")
topClothing = input ("what you mostly wear for your top part? ")
if topClothing == topClothing :
    color=input("NICE! What color your wear it the most? ")
    print("color " + color + " is my favorite.")
print("")
shoes = input ("What brand of shoes you use? ")
if shoes == shoes :
    print( userName + "! You reading my mind, shoes from " + shoes +" are Awesome!")
print(" ")
jewelry = input("You add any jewelry to your style? ")

if jewelry == "yes":
    joyas=input("What kind of jewelry you add ? ")
    print("OMG! i love " + joyas + " i know they fit you so well" )
elif jewelry == "no":
    print=("It's fine maybe it doesn't go with the outfit right ")
else:
    print("Don't forget is a yes or no question , TRY AGAIN")
print(" ")
compliments = ["You are amazing!", "I love your style!", "You sounded like a professional ", "Keep your style for sure!"]
print(random.choice(compliments))
print("It was nice helping you out " + userName + " I hope to see you more often.")