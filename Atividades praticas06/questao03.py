import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if 'erro' in dados:
            return "CEP não encontrado."

        logradouro = dados.get('logradouro', 'N/A')
        bairro = dados.get('bairro', 'N/A')
        cidade = dados.get('localidade', 'N/A')
        estado = dados.get('uf', 'N/A')

        return (f"Logradouro: {logradouro}\n"
                f"Bairro: {bairro}\n"
                f"Cidade: {cidade}\n"
                f"Estado: {estado}")
    except requests.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"
    




cep_input = input("Digite o CEP: ")
resultado = consultar_cep(cep_input)
print(resultado)