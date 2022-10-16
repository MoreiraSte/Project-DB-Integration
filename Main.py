from xmlrpc.client import boolean
import bcrypt
import mysql.connector
import time

cnx = mysql.connector.connect(user='root',password='user123',host='127.0.0.1',database='ecommercev2')

def Usuario():
    while True: 
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        print("         BEM-VINDO AO ECOMMERCE")
        print("\033[1;32m Já possui Login?" * 8 + "\033[0;0m")
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        opUserLog = int(input("  \033[1;32m[1]\033[0;0m - Criar conta"
                                "\n  \033[1;32m[2]\033[0;0m - Entrar com login"
                                "\n\n  \033[1;32m-->\033[0;0m "))

        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        
        if opUserLog == 1:
            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)
            
            print('Digite seu usuario:\n')
            user = input('--> ')
            
            time.sleep(2)
            print('Digite sua senha com no máximo 8 caracteres:\n') 
            password = input('-->')     
            passCripted = bcrypt.hashpw(password,bcrypt.gensalt())
            
            query = 'Insert into usuario values(null,%s,%s)'
            dados = (user,passCripted)
            cursor.execute(query,dados)
            cnx.commit()
            
        if opUserLog == 2:
            
            userUser = input('Digite seu usuario:')
            senhaUser = input('Digite sua senha:') 
            query = 'select * from usuario where user=%s and where senha=%s'
            dados = (userUser,senhaUser)
            cursor.execute(query,dados)
            
            for (user,senha) in cursor:
                if userUser == user and senhaUser == senha:
                    Conta()
                else:
                    print('Usuario não cadastrado')
                    print("\033[1;33m CARREGANDO.... \033[0;0m")
                    time.sleep(3)
                    break
                    
def Conta():
     while True: 
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        print("         BEM-VINDO AO ECOMMERCE")
        print("\033[1;32m Já possui Login?" * 8 + "\033[0;0m")
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        opProdutoPedido = int(input("  \033[1;32m[1]\033[0;0m - Inserir Produtos"
                                    "\n  \033[1;32m[2]\033[0;0m - Exibir Produtos cadastrados"
                                    "\n  \033[1;32m[3]\033[0;0m - Editar Produto"
                                    "\n  \033[1;32m[4]\033[0;0m - Excluir Produto"
                                    "\n  \033[1;32m[5]\033[0;0m - Inserir Pedido"
                                    "\n  \033[1;32m[6]\033[0;0m - Exibir Pedidos cadastrados"
                                    "\n  \033[1;32m[3]\033[0;0m - Editar Pedido"
                                    "\n  \033[1;32m[4]\033[0;0m - Excluir Pedido"

                                    
                                    "\n\n  \033[1;32m-->\033[0;0m "))

        print("\033[1;32m =-=" * 8 + "\033[0;0m")  

        if opProdutoPedido == 1:

            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)
            
            print('Nome do novo produto:\n')
            nomeProd = input('--> ')
            time.sleep(2)

            print('Quantidade de estoque:\n')
            qtdProd = int(input('--> '))
            time.sleep(2)

            print('Preço do produto:\n')
            precoProd = int(input('--> '))
            time.sleep(2)

            query = "INSERT INTO produto (null, nome,qtd_estoque,preco) VALUES ('%s', '%d','%d')"
            dados = (nomeProd,qtdProd,precoProd)
            cursor.execute(query,dados)
            cnx.commit()

            print('Produto adicionado com sucesso!')
            time.sleep(3)
        
        if opProdutoPedido == 2:

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)
            
            cursor = cnx.cursor()
            cursor.execute('SELECT * FROM produto')

        if opProdutoPedido == 3:

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)

            print('Preço do produto:\n')
            precoProd = int(input('--> '))
            time.sleep(2)
             
            query ="UPDATE carros SET nome_dono = 'Joaquim' WHERE placa = 'ABC-1234'"
            cnx.commit()

                 
        if opProdutoPedido == 4:

            cursor.execute("DELETE FROM carros WHERE placa = 'ABC-1234'")
            cnx.commit()

        if opProdutoPedido == 5:
            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)
            
            print('Nome do cliente:\n')
            nomeCliente = input('--> ')
            time.sleep(2)

            print('valor total do pedido:\n')
            valorTotal = int(input('--> '))
            time.sleep(2)

            print('status do pedido:\n')
            statusPedido = boolean(input('--> '))
            time.sleep(2)

            query = "INSERT INTO produto (null, nome_cliente,valor_total,statusPe) VALUES ('%s', '%d','%b')"
            dados = (nomeCliente,valorTotal,statusPedido)
            cursor.execute(query,dados)
            cnx.commit()

            print('Pedido adicionado com sucesso!')
            time.sleep(3)
      
        if opProdutoPedido == 6:

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)
            
            cursor = cnx.cursor()
            cursor.execute('SELECT * FROM pedido')

        if opProdutoPedido == 7:

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(6)

            print('Preço do produto:\n')
            precoProd = int(input('--> '))
            time.sleep(2)
             
            query ="UPDATE carros SET nome_dono = 'Joaquim' WHERE placa = 'ABC-1234'"
            cnx.commit()

        if opProdutoPedido == 8:

            cursor.execute("DELETE FROM carros WHERE placa = 'ABC-1234'")
            cnx.commit()