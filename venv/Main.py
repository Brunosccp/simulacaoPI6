from LavaRapido import LavaRapido

def Main():


    lavaRapido = LavaRapido(1)

    #print("tempo do lava rapido: ", lavaRapido.funcionario[2].ocupadoAte)

    lavaRapido.adicionarCliente(1)
    lavaRapido.adicionarCliente(2)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(2)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(1)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(3)
    lavaRapido.adicionarCliente(2)
    lavaRapido.adicionarCliente(1)
    lavaRapido.adicionarCliente(1)

    print("teste: ", lavaRapido.listaClientes[3].tipoCarro)

    lavaRapido.simularDia()


Main()



