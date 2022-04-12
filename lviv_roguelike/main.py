from lviv_game import *

kozelnytska = Street("Kozelnytska")
kozelnytska.set_description("UCU collegium is here")

stryiska = Street("Stryiska")
stryiska.set_description("Katya lives here")

franka = Street("Franka")
franka.set_description("53 is here")

shevckenka = Street("Shevckenka")
shevckenka.set_description("Go to ksienga skotska")

krakivska = Street("Krakivska")
krakivska.set_description("Krakiv to ukrainske misto")

kozelnytska.link_room(stryiska, 'west')
stryiska.link_room(kozelnytska, 'east')
kozelnytska.link_room(franka, 'north')
franka.link_room(kozelnytska, 'south')
franka.link_room(stryiska, 'west')
stryiska.link_room(franka, 'north')
stryiska.link_room(shevckenka, 'west')
shevckenka.link_room(stryiska, 'east')
shevckenka.link_room(krakivska, 'north')
krakivska.link_room(shevckenka, 'east')

lotr = Enemy("Yurii Dovhorukyi", "V livii ruci vin trymaje nozha (lotr)")
lotr.set_conversation("Zroby tylko krok!")
lotr.set_weakness("makivka")
stryiska.set_character(lotr)

student = Comrade("Ostap", "Poyasnue divchatam matan (student)")
student.set_conversation("Yak kr?")
kozelnytska.set_character(student)

kavaler = Comrade("Chel", "You see a guy stopping his car nearby (kavaler)")
kavaler.set_conversation("Poznayomymos`? Dai Instagram")
shevckenka.set_character(kavaler)

zbui = Enemy("OPZG did", "Vata (zbui)")
zbui.set_conversation("rosiane - nashi brattia!")
zbui.set_weakness("kobzar")
krakivska.set_character(zbui)

batyar = Comrade("Volodya", " Hodyt` do tserkvy, shanuye bat`kiv, tryndyt` nevpynno (batyar)")
batyar.set_conversation("Olimpiaka chorna, shody v optyku!!!")
franka.set_character(batyar)

kobzar = Item("kobzar")
kobzar.set_description("Ukrainian bible")
shevckenka.set_item(kobzar)

makivka = Item("makivka")
makivka.set_description("U shpytz mozna nabraty sok")
franka.set_item(makivka)

visited = []
to_visit = {"Kozelnytska", "Stryiska", "Franka", "Shevckenka", "Krakivska"}
current_street = kozelnytska
backpack = []

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street = current_street.move(command)
        visited.append(current_street.name)
        if visited[-1] == kozelnytska.name and set(visited) == to_visit:
            print("Congratulations, you've walked sucessfully!")
            dead = True
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_street.character = None
                    # if inhabitant.get_defeated() == 2:
                    #     print("Congratulations, you have vanquished the enemy horde!")
                    #     dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with or the one you see is not enemy")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)