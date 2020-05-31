import logging
logging.basicConfig(level=logging.INFO)#,format='%(asctime)s %(message)s')

def add_numbers(user_list_numbers):
    user_numbers_sum = 0
    for i, num_to_add in enumerate(user_list_numbers):
        if i > 0:
            logging.info("Dodaję %s + %s" %(user_numbers_sum, user_list_numbers[i]))
        user_numbers_sum += num_to_add
    return user_numbers_sum

def odd_numbers(first,second):
    logging.info("Odejmuję %s - %s" %(first, second))
    return first-second

def multiply_numbers(user_list_numbers):
    user_numbers_multi = 1
    for i, num_to_multi in enumerate(user_list_numbers):
        if i > 0:
            logging.info("Mnożę %s * %s" %(user_numbers_multi , user_list_numbers[i]))
        user_numbers_multi *= num_to_multi
    return user_numbers_multi
 
def divide_numbers(first, second):
    logging.info("Dzielę  %s / %s" %(first, second))
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
def get_list_numbers():
    user_list_numbers = []
    while not user_list_numbers:
        try:
            user_list_numbers = (input("Podaj listę liczb oddzielając je przecinkiem ").split(","))
            user_list_numbers = [float(i) for i in user_list_numbers]
        except:
            print("Wprowadź poprawne wartość liczbową!")
        return user_list_numbers
    
choice = ''
while not choice:
    try: 
        choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    except ValueError:
        print("Wprowadź poprawną wartość liczbową!")
    if choice == 1:
        user_numbers = get_list_numbers()
        print("Wynik to: ", add_numbers(user_numbers))
    elif choice ==2:
        first_number, second_number = get_numbers()
        print("Wynik to: ", odd_numbers(first_number,second_number))
    elif choice ==3:
        user_numbers = get_list_numbers()
        print("Wynik to: ", multiply_numbers(user_numbers))
    elif choice ==4:
        first_number, second_number = get_numbers()
        while second_number == 0:
            print("Niestety nie możesz dzielić przez 0")
            first_number, second_number = get_numbers()
        print("Wynik to: ", divide_numbers(first_number,second_number))
    else:
        print("Błędny wybór, podaj liczbę z zakresu 1-4!")