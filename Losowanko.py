import random

database = []

def import_from_txt():
    file = open('Losowanko.txt', "r", encoding="utf-8")
    for peoples in file:
        database.append (peoples.strip())
    return database

def random_use():
    import_from_txt()
    (random.shuffle(database))
    return database

def groups():
    database.clear()
    random_use()
    group_one = []
    group_two = []
    group_three = []
    group_four = []
    group_five = []
    
    for i in range(0,len(database),5):
        group_one.append (database[i])
    print (f"Grupa pierwsza:\n{', '.join(str(i) for i in group_one)}.")
    file = open("Wynik.txt", 'w', encoding="utf-8")
    file.write(f"Grupa pierwsza:\n{', '.join(str(i) for i in group_one)}.\n")
    
    for i in range(1,len(database),5):
        group_two.append (database[i])
    print (f"Grupa druga:\n{', '.join(str(i) for i in group_two)}.")
    file = open("Wynik.txt", 'a', encoding="utf-8")
    file.write(f"Grupa druga:\n{', '.join(str(i) for i in group_two)}.\n")

    for i in range(2,len(database),5):
        group_three.append (database[i])
    print (f"Grupa trzecia:\n{', '.join(str(i) for i in group_three)}.")
    file = open("Wynik.txt", 'a', encoding="utf-8")
    file.write(f"Grupa trzecia:\n{', '.join(str(i) for i in group_three)}.\n")

    for i in range(3,len(database),5):
        group_four.append (database[i])
    print (f"Grupa czwarta:\n{', '.join(str(i) for i in group_four)}.")
    file = open("Wynik.txt", 'a', encoding="utf-8")
    file.write(f"Grupa czwarta:\n{', '.join(str(i) for i in group_four)}.\n")

    for i in range(4,len(database),5):
        group_five.append (database[i])
    print (f"Grupa piąta:\n{', '.join(str(i) for i in group_five)}.")
    file = open("Wynik.txt", 'a', encoding="utf-8")
    file.write(f"Grupa piąta:\n{', '.join(str(i) for i in group_five)}.")


if __name__ == "__main__":
    print("-------------------------------------------------------------------------")
    print ("Wybrano ich za pomocą losów, na równi jednych i drugich.\n1 Krn 24,5")
while True:
    print("\n-------------------------------------------------------------------------")
    print ("MENU:|l = losuj| |w = wyjdź|")
    print("-------------------------------------------------------------------------")
    resp = input("WYBIERZ: ")
    if  resp == "l":
        groups()
        continue
    elif resp == "w":
            print ("Zamykam i zapisuję... Do zobaczenia! ;)")
            break
    else:
        print ("Wybierz poprawną komendę z menu:")
        continue