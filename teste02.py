# Recebe a idade do usuário como string
age = input("Digite sua idade: ")

# Faz "cast" da idade para inteiro e calcula
age = int(age) + 10

# Exibe tudo "interpolando" → f
print (f"Daqui a 10 anos você terá {age} anos!")