def salvar(usuario, senha):
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f'{usuario},{senha}\n')
    print(f'Usuário {usuario} salvo com sucesso!')  # Para depuração, pode ser removido depois