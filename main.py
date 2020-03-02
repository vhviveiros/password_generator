import string, random, os

lenght = letters_len = numbers_len = symbols_len = -1

def clearConsole(): os.system('cls' if os.name=='nt' else 'clear')

def inputWithCheck(msg, check, error_msg):
    try:
        val = int(input(msg))
        clearConsole()
        if check(val):
            print(error_msg)
            return -1
        return val
    except ValueError as error:
        print("Valor inválido!\n\n")
        return -1

def userInput():
    global lenght, letters_len, numbers_len, symbols_len

    while lenght == -1:
        lenght = inputWithCheck("Digite o tamanho da senha:\n", lambda x: x < 6, "Senha muito curta!\n\n")

    while letters_len == -1:
        letters_len = inputWithCheck("Número de letras:\n", lambda x: x < 0 or x > lenght, "Tamanho inválido!\n\n")

    if lenght - letters_len > 0:
        while numbers_len == -1:
            numbers_len = inputWithCheck("Quantidade de números:\n", lambda x: x < 0 or x > lenght - letters_len, "Tamanho inválido!\n\n")

    symbols_len = lenght - letters_len - numbers_len

def pick(list, count):
    list_lenght = list.__len__()
    return_list = ''
    for i in range(0, count):
        pos = random.randint(0, list_lenght - 1)
        return_list += list[pos]
    return return_list

def pickLetters(lenght):
    return pick(string.ascii_letters, lenght)

def pickDigits(lenght):
    return pick(string.digits, lenght)

def pickSymbols(lenght):
    return pick(string.punctuation, lenght)

def generatePassword():
    global letters_len, numbers_len, symbols_len

    letters = pickLetters(letters_len)
    digits = pickDigits(numbers_len)
    symbols = pickSymbols(symbols_len)

    password = random.sample(letters + digits + symbols, letters_len + numbers_len + symbols_len)
    clearConsole()
    print("Senha gerada: " + ''.join(password))

userInput()
generatePassword()