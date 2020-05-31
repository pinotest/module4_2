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
    while first_number_choice == '':
        try:
            first_number_choice = float(input("Podaj składnik 1: "))
        except ValueError:
            print("Wprowadź poprawną wartość liczbową!")
    second_number_choice = ''
    while second_number_choice =='':
        try:
            second_number_choice = float(input("Podaj składnik 2: "))
        except ValueError:
            print("Wprowadź poprawną wartość liczbową!")
    return first_number_choice,second_number_choice

choice = ''
while not choice:
    try: 
        choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    except ValueError:
        print("Wprowadź poprawną wartość liczbową!")
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