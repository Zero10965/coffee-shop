

cart=[]
total=0

print("\n\n\nHELLO,welcome to zackcoffe!!!!!!!!!!")

name = input("\nwhat is your name?\n\n")

print("hey, how are you today!!\n")





print("-----------menu-----------\n")

for key, Value in menu.items():
    print(f"{key:19}: ${Value:.2f}")

print("--------------------------\n")

print( name + "\nWhat would you like from our menu today?\n\n")

while True:
    drink = input
    if drink == menu:        
        plus=input("and would you like to add anything to your coffee?\n")
        if plus=="yes":
            add=input("these are the addon's we offer what would you like" + name +" ?")

    

    else:
        repeat=input("sorry but for the moment we dont have that would you like to order something from the menu")
        if repeat=="yes":
        input("thats great! what would you like from the menu?\n ")


amount = int(input("how many coffees would you like?\n"))

total = price * amount + add_ons
 #   print("sorry, for the moment we don't have that here")

print(      "sounds good " + name + ", we'll have your " + str(amount) + order + " ready for you in a moment.")


print(  "And your total is - $" + str(total))

print( "And will that be all " + name)

