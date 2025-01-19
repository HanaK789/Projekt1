"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Hana Kadrmanová
email: hkadrmanova&yahoo.com

"""

# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

# Seznam registrovaných uživatelů a jejich hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Hlavní smyčka programu
while True:
    # 1. Přihlášení uživatele
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Ověření přihlašovacích údajů
    if username in users and users[username] == password:
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        print("We have 3 texts available for analysis.")
        print("----------------------------------------")
    else:
        # Upozornění na neúspěšné přihlášení
        print(f"username: {username}")
        print(f"password: {password}")
        print("Unregistered user. Terminating the program.")
        break  # Ukončení smyčky programu pro neregistrované uživatele

    # 2. Výběr textu k analýze
    text_choice = input("Enter a number between 1 and 3 to select a text: ")

    # Ověření, zda byl zadán platný číselný vstup
    if not text_choice.isdigit():
        print("Invalid input. Terminating the program.")
        break

    # Převod textového vstupu na číslo
    text_choice = int(text_choice)

    # Kontrola, zda je číslo v povoleném rozsahu (1–3)
    if text_choice < 1 or text_choice > len(TEXTS):
        print("Invalid selection. Terminating the program.")
        break

    # Výběr textu podle zadaného čísla
    selected_text = TEXTS[text_choice - 1]

    # 3. Analýza textu
    words = selected_text.split()  # Rozdělení textu na jednotlivá slova
    word_count = len(words)  # Počet slov v textu
    title_case_count = sum(1 for word in words if word.istitle())  # Slova začínající velkým písmenem
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())  # Slova velkými písmeny
    lowercase_count = sum(1 for word in words if word.islower())  # Slova malými písmeny
    numeric_count = sum(1 for word in words if word.isdigit())  # Počet čísel v textu
    numeric_sum = sum(int(word) for word in words if word.isdigit())  # Součet všech čísel

    # Vytvoření slovníku pro délky slov a jejich četnosti

    word_lengths = {}
    for word in words:
        # Vyčištění slova od speciálních znaků
        clean_word = ''.join(char for char in word if char.isalnum())
        length = len(clean_word)  # Délka vyčištěného slova
        if length > 0:
            word_lengths[length] = word_lengths.get(length, 0) + 1  # Zvýšení počtu výskytů dané délky

    # 4. Výpis výsledků analýzy
    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {title_case_count} words starting with a capital letter.")
    print(f"There are {uppercase_count} words in uppercase.")
    print(f"There are {lowercase_count} words in lowercase.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all numbers is {numeric_sum}.")
    print("----------------------------------------")

    # Příprava hlavičky tabulky
    max_count = max(word_lengths.values())  # Maximální četnost pro dynamickou šířku sloupce
    column_width = max_count + 2  # +2 pro mezery po stranách
    header = f"LEN|{'OCCURENCES'.center(column_width)}|NR."
    print(header)
    print("----------------------------------------")

    # Výpis statistik délek slov
    for length, count in sorted(word_lengths.items()):
        stars = '*' * count  # Hvězdičky znázorňující počet slov
        occurrences = f"{stars:<{column_width}}"  # Zarovnání hvězdiček doleva
        print(f"{length:>3}|{occurrences}|{count}")

    # 5. Ukončení programu 
    break



