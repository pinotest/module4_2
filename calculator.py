def add_numbers(first, second):
    return first + second

def odd_numbers(first,second):
    return first-second

def multiply_numbers(first,second):
    return first*second

def divide_numbers(first, second):
    return first/second

def get_numbers():
    first_number_choice = ''
    while not first_number_choice:
        first_number_choice = float(input("Podaj składnik 1: "))
    second_number_choice = ''
    while not second_number_choice :
        second_number_choice = float(input("Podaj składnik 2: "))
    return first_number_choice,second_number_choice

choice = ''

while not choice:
    choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    if choice == 1:
        first_number, second_number = get_numbers()
        print("Wynik to: ", add_numbers(first_number,second_number))
    elif choice ==2:
        first_number, second_number = get_numbers()
        print("Wynik to: ", odd_numbers(first_number,second_number))
    elif choice ==3:
        first_number, second_number = get_numbers()
        print("Wynik to: ", multiply_numbers(first_number,second_number))
    elif choice ==4:
        first_number, second_number = get_numbers()
        print("Wynik to: ", divide_numbers(first_number,second_number))
    else:
        print("Błędny wybór, podaj liczbę z zakresu 1-4!")