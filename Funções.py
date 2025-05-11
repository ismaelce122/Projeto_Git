# Função Cadastrar




# Função Buscar




# Função Deletar

def deletarClientes(listaClientes, nome):
    for i in range(len(listaClientes)):
        if listaClientes[i]['nome'].lower() == nome.lower():
            listaClientes.pop(i)
            return True