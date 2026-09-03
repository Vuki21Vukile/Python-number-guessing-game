import random

broj_pokusaja = 0
lowest_num = 1
highest_num = 100

print("Probaj da pogodis broj od 1 do 100!")
tezina = input("\nIzaberi: easy mode(easy), hard mode(hard): ").lower()

while True: #provera inputa
    if tezina != "easy" and tezina != "hard":
        print("Unesite ispravnu tezinu")
        tezina = input("\nIzaberi: easy mode(easy), hard mode(hard): ").lower()
    else:
        break

while True:
    zamisljen_broj = random.randint(lowest_num, highest_num)

    if tezina == "easy": #za easy mode
        guess = 10
        score_easy = 50
        print("\nIMAS 10 POKUSAJA\n")

    elif tezina == "hard": #za hard mode
        guess = 5
        score_hard = 100
        print("IMAS 5 POKUSAJA\n")

    for i in range(1,guess+1): #for loop u zavisnosti od mode
        user_broj = int(input("Unesite broj: "))

        broj_pokusaja += 1

        if user_broj < lowest_num or user_broj > highest_num:
            print("Taj broj je izvan opsega!")
            print(f"Molim vas izaberite broj izmedju {lowest_num} i {highest_num}\n")

        elif user_broj > zamisljen_broj:
            print("\tTrazeni broj je manji")

        elif user_broj < zamisljen_broj:
            print("\tTrazeni broj je veci")

        elif user_broj == zamisljen_broj:
            print(f"\nCESTITAM, POGODILI STE BROJ: {zamisljen_broj}")

            if tezina == "easy":
                print(f"Pogodili ste broj u {broj_pokusaja} pokusaja")
                score_easy = score_easy / float(broj_pokusaja)
                print(f"Tvoj konacan rezultat je: {round(score_easy,0)}")

            else:
                print(f"Pogodili ste broj u {broj_pokusaja} pokusaja")
                score_hard = score_hard / float(broj_pokusaja)
                print(f"Tvoj konacan rezultat je: {round(score_hard,0)}")

            break
    else:
        print(f"\nIZGUBILI STE, TRAZENI BROJ JE: {zamisljen_broj}")

    nastavak = input("\nAko zelite da nastavite pritisnite Enter, ako zelite da izadjete pritisnite space,enter: ").upper()
    if nastavak == "":
        continue
    else:
        break