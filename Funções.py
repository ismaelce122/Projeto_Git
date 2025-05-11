# Função Cadastrar




# Função Buscar




# Função Deletar

def deletarClientes(listaClientes, nome):
    for nomeCliente in listaClientes:
        if nomeCliente['nome'].lower() == nome.lower():
            listaClientes.remove(nomeCliente)
            return True