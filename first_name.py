# Recebe a entrada do usuário (stdin)
name = input("Digite seu nome completo: ")

# Extrai partes usando o espaço (" ")
pname = name.split(" ")

# Exibe a primeira parte [0] e capitaliza
print(f"Olá {pname[0].capitalize()}!")