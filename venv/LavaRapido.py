from Funcionario import Funcionario
from Cliente import Cliente

class LavaRapido:
    def __init__(self, quantidade):
        self.tempoAberto = 1
        self.funcionario = []
        self.tempoProximoCarro = 15
        self.listaClientes = []
        self.lucro = 0
        self.clientesAtendidos = 0
        self.clientesNaoAtendidos = 0

        for i in range(0, quantidade):
            self.funcionario.append(Funcionario())


    def adicionarCliente(self, tipoCarro):
        self.listaClientes.append(Cliente(tipoCarro))

    def simularDia(self):
        totalClientes = len(self.listaClientes)

        for i in range(1, 480 + 1): #480 minutos = 8 horas
            self.verificarProximoCliente()


            self.tempoAberto += 1
            self.tempoProximoCarro += 1

            self.calculandoTempoOcioso()


        #final da simulação
        self.pagarFuncionarios()
        self.clientesNaoAtendidos = totalClientes - self.clientesAtendidos    #calculando os clientes que não conseguiram ser atendido a tempo da loja fechar

        print("lucro: ", self.lucro)
        print ("quantidade de clientes atendidos: ", self.clientesAtendidos)
        print ("quantidade de clientes não atendidos: ", self.clientesNaoAtendidos)

        print ("tempo ocioso do funcionario:", self.funcionario[0].tempoOcioso)


    def verificarProximoCliente(self):
        if(self.tempoProximoCarro >= 15):   #aparece um novo cliente
            if(len(self.listaClientes) != 0):  #tem algum cliente novo para aparecer

                for i in range(0, len(self.funcionario)):
                    if(self.funcionario[i].ocupadoAte < self.tempoAberto):
                        self.tempoProximoCarro -= 15
                        #funcionario esta desocupado

                        print("cliente sendo atendido no tempo: ",self.tempoAberto)

                        if(self.listaClientes[0].tipoCarro == 1):   #se for automovel pequeno
                            if(self.tempoAberto + 30 > 480):    #se nao tiver tempo para fazer no dia, dispensa cliente
                                self.listaClientes.pop(0)
                                print("nao atendeu, nao atendidos: ",self.clientesNaoAtendidos)
                                return

                            #funcionario pegando o servico do cliente
                            self.funcionario[i].ocupadoAte = self.tempoAberto + 30 -1
                            self.lucro += 25

                        if(self.listaClientes[0].tipoCarro == 2):   #se for automovel médio
                            if(self.tempoAberto + 40 > 480):    #se nao tiver tempo para fazer no dia, dispensa cliente
                                self.listaClientes.pop(0)
                                return

                            #funcionario pegando o servico do cliente
                            self.funcionario[i].ocupadoAte = self.tempoAberto + 40 -1
                            self.lucro += 40

                        if(self.listaClientes[0].tipoCarro == 3):   ##se for automovel grande
                            if(self.tempoAberto + 55 > 480):    #se nao tiver tempo para fazer no dia, dispensa cliente
                                self.listaClientes.pop(0)
                                return

                            #funcionario pegando o servico do cliente
                            self.funcionario[i].ocupadoAte = self.tempoAberto + 55 -1
                            self.lucro += 60

                        self.listaClientes.pop(0)
                        self.clientesAtendidos += 1
                        return


    def pagarFuncionarios(self):
        self.lucro -= 100 * len(self.funcionario)

    def calculandoTempoOcioso(self):
        for i in range(0, len(self.funcionario)):
            if(self.funcionario[i].ocupadoAte+1 < self.tempoAberto):
                self.funcionario[i].tempoOcioso += 1