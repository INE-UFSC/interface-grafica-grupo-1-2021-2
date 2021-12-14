from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                try:
                    codigo, nome = self.verifica_valores(values)
                    if nome == '' or codigo == '': raise ValueError                
                    for key in self.__clientes.keys():
                        if codigo == key:
                            print('codigo ja existe')
                            raise ValueError
                    self.adiciona_cliente(codigo, nome)
                    resultado = 'Cliente cadastrado com sucesso!'
                except:
                    resultado = '"Código" deve ser único e um inteiro, e "Nome" deve conter apenas letras.'
            elif event == 'Consultar':
                try:
                    codigo, nome = self.verifica_valores(values)
                    try:
                        resultado = self.busca_codigo(codigo)
                    except:
                        try:
                            resultado = self.busca_nome(nome)
                        except:
                            resultado = 'Cliente nao encontrado'
                except:
                    resultado = '"Código" deve ser um inteiro, e "Nome" deve conter apenas letras.'            
            
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return self.__clientes[key]

        raise LookupError

    def verifica_valores(self, valores):
        nome, codigo = valores['Nome'], valores['Código']
        if codigo != '':
            try: codigo = int(codigo)
            except:
                print('erro codigo nao int')
                raise ValueError
        return codigo, nome