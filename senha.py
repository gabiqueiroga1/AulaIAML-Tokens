def validar_senha(senha:str)->bool:
    """Verifica se uma senha cumpre os requisitos minimos de comprimento e caracteres"""
    tamanho_minimo = len(senha)>=8

    maiscula =any(char.isupper() for char in senha)

    numero = any(char.isdigit() for char in senha)

    return tamanho_minimo and maiscula and numero

print("Senha", validar_senha("Senha123"))
print("Senha", validar_senha("senhaalterada"))
print("Senha", validar_senha("minhasenha12345"))


