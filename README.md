import random

print("Probaj da pogodis broj od 1 do 100!")
tezina = input("\nIzaberi: easy mode(easy), hard mode(hard): ").lower()

while True:
    zamisljen_broj = random.randint(1, 100)

    if tezina == "easy":
        broj_pokusaja = 10
        score_easy = 50
        print("\nIMAS 10 POKUSAJA\n")

    elif tezina == "hard":
        broj_pokusaja = 5
        score_hard = 100
        print("IMAS 5 POKUSAJA\n")

    for i in range(1,broj_pokusaja+1):
        broj_pokusaja -= 1
        user_broj = int(input("Unesite broj: "))

        if user_broj > zamisljen_broj:
            print("\tTrazeni broj je manji")

        elif user_broj < zamisljen_broj:
            print("\tTrazeni broj je veci")

        elif user_broj == zamisljen_broj:
            print(f"\nCESTITAM, POGODILI STE BROJ: {zamisljen_broj}")

            if tezina == "easy":
                print(f"Pogodili ste broj u {abs(broj_pokusaja-10)} pokusaja")
                score_easy = score_easy / float(abs(broj_pokusaja-10))
                print(f"Tvoj konacan rezultat je: {round(score_easy,0)}")

            else:
                print(f"Pogodili ste broj u {abs(broj_pokusaja-5)} pokusaja")
                score_hard = score_hard / float(abs(broj_pokusaja - 5))
                print(f"Tvoj konacan rezultat je: {round(score_hard,0)}")

            break
    else:
        print(f"\nIZGUBILI STE, TRAZENI BROJ JE: {zamisljen_broj}")

    nastavak = input("\nAko zelite da nastavite pritisnite Enter, ako zelite da izadjete pritisnite D: ").upper()
    if nastavak == "":
        continue
    else:
        break
