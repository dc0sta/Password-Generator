import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
# todos os tipos de letras numeros e sinais

    password = ''.join(random.choice(characters) for i in range(length))
# este codigo escolhe caracteres e mete em sitios aleatórios

    return password

while True: #loop
    try:
        lenght  = int(input("Password Size: "))
        # pergunta a pessoa que esta a criar a password qual ira ser o tamanho da mesma
        
        password = generate_password(lenght)
        print(f"Password: {password}")
        #mostra a password
        
    except ValueError:
        # Escrever exit para sair ou então meter um número de tamanho da password
        user_input = input("Input a valid number or type exit: ")
        
        # escrever exit opara sair
        if user_input.lower() == 'exit':
            print("Bye!")
            break
        else:
            print("Input a valid number.")
