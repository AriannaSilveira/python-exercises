usuarios_banidos = ['Maria', 'André', 'Gustavo']
usuario = 'Paulo'

if usuario not in usuarios_banidos:
    print(usuario.title() + ", você pode postar um comentário.")
else:
    print(usuario.title() + ", infelizmente você está banido.")
    