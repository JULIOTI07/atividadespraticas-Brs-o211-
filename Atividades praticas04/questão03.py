while True:
    try:
        senha = input("Digite a senha: ")

        if senha.lower() == 'sair':
            print("Sair do Programa...")
            break

        
        if len(senha) < 8:
            raise Exception("A senha deve ter pelo menos 8 caracteres")

        
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break
            '''
            if caractere in '0123456789':
                tem_numero = True
                break
            ''' 
        if not tem_numero:
            raise ValueError("A senha deve conter pelo menos um número")

        print("Senha válida")

    except ValueError as e:
        print(f"Erro: {e} tente novamente")
