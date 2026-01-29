

print("Welcome to the NBA Team Guesser!")
name = input("What is your name? ")
print(f"\nHey {name}, think of ANY NBA team...")
print("I’ll guess it using yes/no questions!\n")

if name.lower() == "lebron":
    print(" You're thinking of the Los Angeles Lakers — because you ARE the King!")
    exit()

west = input("Is your team in the Western Conference? (yes/no) ").lower()
has_champ = input("Has your team ever won an NBA Championship? (yes/no) ").lower()

if west == "yes":
    big_market = input("Is the team in a big well‑known city? (yes/no) ").lower()

    if has_champ == "yes":
        star = input("Does the team currently have a superstar? (yes/no) ").lower()

        if star == "yes":
            california = input("Is the team located in California? (yes/no) ").lower()
            if california == "yes":
                bay = input("Is the team near the Bay Area? (yes/no) ").lower()
                if bay == "yes":
                    print("You are thinking of the Golden State Warriors!")
                else:
                    print("You are thinking of the Los Angeles Lakers!")
            else:
                texas = input("Are they from Texas? (yes/no) ").lower()
                if texas == "yes":
                    print("You are thinking of the San Antonio Spurs!")
                else:
                    print("You are thinking of the Denver Nuggets!")
        else:
            texas = input("Is the team in Texas? (yes/no) ").lower()
            if texas == "yes":
                print("You are thinking of the Houston Rockets!")
            else:
                print("You are thinking of the Portland Trail Blazers!")

    else:
        young = input("Is the team known for young rising talent? (yes/no) ").lower()
        if young == "yes":
            okc = input("Is the city known for tornadoes? (yes/no) ").lower()
            if okc == "yes":
                print("You are thinking of the Oklahoma City Thunder!")
            else:
                print("You are thinking of the Minnesota Timberwolves!")
        else:
            desert = input("Is the team located in a desert area? (yes/no) ").lower()
            if desert == "yes":
                print("You are thinking of the Phoenix Suns!")
            else:
                print("You are thinking of the Memphis Grizzlies!")

else:
    east_big = input("Is the team from a big famous city? (yes/no) ").lower()

    if has_champ == "yes":
        if east_big == "yes":
            chicago = input("Did Michael Jordan play for the team? (yes/no) ").lower()
            if chicago == "yes":
                print("You are thinking of the Chicago Bulls!")
            else:
                newyork = input("Is the team in New York? (yes/no) ").lower()
                if newyork == "yes":
                    print("You are thinking of the New York Knicks or Brooklyn Nets!")
                else:
                    print("You are thinking of the Boston Celtics or Miami Heat!")
        else:
            canada = input("Is the team in Canada? (yes/no) ").lower()
            if canada == "yes":
                print("You are thinking of the Toronto Raptors!")
            else:
                florida = input("Is the team based in Florida? (yes/no) ").lower()
                if florida == "yes":
                    print("You are thinking of the Miami Heat!")
                else:
                    print("You are thinking of the Milwaukee Bucks or Cleveland Cavaliers!")
    
    else:
        rising = input("Is the team rebuilding with young players? (yes/no) ").lower()
        if rising == "yes":
            print("You are thinking of the Orlando Magic or Detroit Pistons!")
        else:
            print("You are thinking of the Washington Wizards or Charlotte Hornets!")

print("\nIf I got it wrong i'll try again next time")

