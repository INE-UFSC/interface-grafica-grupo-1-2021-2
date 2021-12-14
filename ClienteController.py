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
                    self.adiciona_cliente(self.verifica_valores(values))
                    resultado = 'Cliente cadastrado com sucesso!'
                except:
                    resultado = '"Código" deve ser um inteiro e "Nome" deve conter apenas letras.'
            elif event == 'Consultar':
                try:
                    codigo, nome = self.verifica_valores(*values)
                    try:
                        resultado = self.busca_codigo(codigo)
                    except:
                        try:
                            resultado = self.busca_nome(nome)
                        except:
                            resultado = 'Cliente nao encontrado'
                except:
                    resultado = 'Os valores inseridos estao incorretos'                
            
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
                return key 

        raise LookupError

    def verifica_valores(codigo, nome):
        if codigo != '':
            try: codigo = int(codigo)
            except: raise ValueError
        if nome != '':
            if not nome.isalpha():
                raise ValueError
        return codigo, nome