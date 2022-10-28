from xmlrpc.client import boolean
import bcrypt
import mysql.connector
import time

cnx = mysql.connector.connect(user='root',password='root',host='10.109.71.19',database='stephany_moreira')

def Conta():
     while True: 
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        print("         BEM-VINDO AO ECOMMERCE")
        print("\033[1;32m" * 8 + "\033[0;0m")
        print("\033[1;32m =-=" * 8 + "\033[0;0m")
        opProdutoPedido = int(input("  \033[1;32m[1]\033[0;0m - Inserir Produtos"
                                    "\n  \033[1;32m[2]\033[0;0m - Exibir Produtos cadastrados"
                                    "\n  \033[1;32m[3]\033[0;0m - Editar Produto"
                                    "\n  \033[1;32m[4]\033[0;0m - Excluir Produto"
                                    "\n  \033[1;32m[5]\033[0;0m - Inserir Pedido"
                                    "\n  \033[1;32m[6]\033[0;0m - Exibir Pedidos cadastrados"
                                    "\n  \033[1;32m[7]\033[0;0m - Editar Pedido"
                                    "\n  \033[1;32m[8]\033[0;0m - Excluir Pedido"
                                    "\n  \033[1;32m[9]\033[0;0m - Aumentar o preço dos produtos"
                                    "\n  \033[1;32m[10]\033[0;0m - Diminuir o preço dos produtos"
                                    "\n  \033[1;32m[11]\033[0;0m - Valor total dos pedidos"
                                    

                                    
                                    "\n\n  \033[1;32m-->\033[0;0m "))

        print("\033[1;32m =-=" * 8 + "\033[0;0m")  

        if opProdutoPedido == 1:

            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)
            
            print('Nome do novo produto:\n')
            nomeProd = input('--> ')
            time.sleep(2)

            print('Quantidade de estoque:\n')
            qtdProd = int(input('--> '))
            time.sleep(2)

            print('Preço do produto:\n')
            precoProd = int(input('--> '))
            time.sleep(2)

            query = "INSERT INTO produto (idP,nome,qtd_estoque,preco) VALUES (null,%s, %s,%s)"
            dados = (nomeProd,qtdProd,precoProd)
            cursor.execute(query,dados)
            cnx.commit()

            print('Produto adicionado com sucesso!')
            time.sleep(3)
        
        if opProdutoPedido == 2:
            
            cursor = cnx.cursor()
            cursor.execute('SELECT * FROM produto')
            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)
            
            for (idP,nome,qtd_estoque,preco) in cursor:
                print(f'{idP} - {nome} - {qtd_estoque} - {preco}')
            

        if opProdutoPedido == 3:
            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)

            print('O que você deseja alterar?\n'
                  +'1- nome do produto'
                  +'2- quntidade de estoque'
                  +'3- preço do produto')
            opAlterProduto = int(input('--> '))
            time.sleep(2)

            if opAlterProduto == 1:
                cursor = cnx.cursor()

                upName = input('Digite o nome:')
                time.sleep(2)
                upId = int(input('Informe o id do produto:'))

                query ="UPDATE produto SET nome = %s WHERE idP = %s"
                dados = (upName,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Nome editado com sucesso! \033[0;0m")
                time.sleep(2)

            if opAlterProduto == 2:
                cursor = cnx.cursor()

                upEstoque = int(input('Digite a quantidade de estoque:'))
                time.sleep(2)
                upId = int(input('Informe o id do produto:'))

                query ="UPDATE produto SET qtd_estoque = %s WHERE idP = %s"
                dados = (upEstoque,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Quantidade de estoque editado com sucesso! \033[0;0m")
                time.sleep(2)
             
            if opAlterProduto == 3:
                cursor = cnx.cursor()

                upPreco = int(input('Digite o preço:'))
                time.sleep(2)
                upId = int(input('Informe o id do produto:'))

                query ="UPDATE produto SET preco = %s WHERE idP = %s"
                dados = (upPreco,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Preço editado com sucesso! \033[0;0m")
                time.sleep(2)

        if opProdutoPedido == 4:
            cursor = cnx.cursor()

            delProd = input('Digite o id do produto que deseja deletar: ')

            query = "DELETE FROM produto WHERE idP = %s"
            dados = (delProd, )
            cursor.execute(query,dados)
            cnx.commit()
            
            print("\033[1;33m Produto deletado com sucesso! \033[0;0m")
            time.sleep(2)

        if opProdutoPedido == 5:
            cursor = cnx.cursor()

            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)
            
            print('Nome do cliente:\n')
            nomeCliente = input('--> ')
            time.sleep(2)

            print('valor total do pedido:\n')
            valorTotal = int(input('--> '))
            time.sleep(2)

            print('status do pedido:\n')
            statusPedido = boolean(input('--> '))
            time.sleep(2)

            query = "INSERT INTO produto (idPe, nome_cliente,valor_total,statusPe) VALUES (null,%s, %s,%s)"
            dados = (nomeCliente,valorTotal,statusPedido)
            cursor.execute(query,dados)
            cnx.commit()

            print('Pedido adicionado com sucesso!')
            time.sleep(3)
      
        if opProdutoPedido == 6:
            cursor = cnx.cursor()
            cursor.execute('SELECT * FROM pedido')
            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)
            
            for (idPe,nome_cliente,valor_total,statusPe) in cursor:
                print(f'{idPe} - {nome_cliente} - {valor_total} - {statusPe}')

        if opProdutoPedido == 7:
            cursor = cnx.cursor()
            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)

            print('O que você deseja alterar?\n'
                  +'1- nome do produto'
                  +'2- quntidade de estoque'
                  +'3- preço do produto')
            opAlterProduto = int(input('--> '))
            time.sleep(2)

            if opAlterProduto == 1:
                cursor = cnx.cursor()
                upCliente = input('Digite o nome do cliente:')
                time.sleep(2)
                upId = int(input('Informe o id do pedido:'))

                query ="UPDATE produto SET nome_cliente =%s WHERE idPe = %s"
                dados = (upCliente,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Nome do cliente editado com sucesso! \033[0;0m")
                time.sleep(2)


            if opAlterProduto == 2:
                cursor = cnx.cursor()
                upValor = int(input('Digite o valor total:'))
                time.sleep(2)
                upId = int(input('Informe o id do pedido:'))

                query ="UPDATE produto SET valor_total = %s WHERE idPe = %s"
                dados = (upValor,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Valor total editado com sucesso! \033[0;0m")
                time.sleep(2)

             
            if opAlterProduto == 3:
                cursor = cnx.cursor()
                upstatus = int(input('Digite true ou false para o status:'))
                time.sleep(2)
                upId = int(input('Informe o id do pedido:'))

                query ="UPDATE produto SET statusPe = %b WHERE idPe = %s"
                dados = (upstatus,upId)
                cursor.execute(query,dados)
                cnx.commit()
                
                print("\033[1;33m Status editado com sucesso! \033[0;0m")
                time.sleep(2)



        if opProdutoPedido == 8:

            cursor = cnx.cursor()
            delPedido = int(input('Digite o id do pedido que deseja deletar: '))

            query ="DELETE FROM pedido WHERE idPe = %s"
            dados = (delPedido)
            cursor.execute(query,dados)
            cnx.commit()
            
            print("\033[1;33m Pedido excluido com sucesso! \033[0;0m")
            time.sleep(2)
               
            
        # if opProdutoPedido == 9:

        #     cursor = cnx.cursor()
        #     print("\033[1;33m CARREGANDO.... \033[0;0m")
        #     time.sleep(3)

        #     print('Quantos porcento os preços irão aumentar?')
        #     aumento= input('--> ')
            
        #     query ="Update FROM produto WHERE idPe = %s"
        #     dados = (delPedido)
        #     cursor.execute(query,dados)
        #     cnx.commit()
        
        # if opProdutoPedido == 10:
        
        if opProdutoPedido == 11:
            
            cursor = cnx.cursor()
            cursor.execute('SELECT SUM(valor_total) FROM pedido')
            print("\033[1;33m CARREGANDO.... \033[0;0m")
            time.sleep(3)
            
            for (valor_total) in cursor:
                print(f'{valor_total}')
            
        



# def Usuario():
#     while True: 
#         print("\033[1;32m =-=" * 8 + "\033[0;0m")
#         print("         BEM-VINDO AO ECOMMERCE")
#         print("\033[1;32m Já possui Login?" * 8 + "\033[0;0m")
#         print("\033[1;32m =-=" * 8 + "\033[0;0m")
#         opUserLog = int(input("  \033[1;32m[1]\033[0;0m - Criar conta"
#                                 "\n  \033[1;32m[2]\033[0;0m - Entrar com login"
#                                 "\n\n  \033[1;32m-->\033[0;0m "))

#         print("\033[1;32m =-=" * 8 + "\033[0;0m")
        
#         if opUserLog == 1:
#             cursor = cnx.cursor()

#             print("\033[1;33m CARREGANDO.... \033[0;0m")
#             time.sleep(6)
            
#             print('Digite seu usuario:\n')
#             user = input('--> ')
            
#             time.sleep(2)
#             print('Digite sua senha com no máximo 8 caracteres:\n') 
#             password = input('-->')     
#             password = password.encode()
#             passCripted = bcrypt.hashpw(password,bcrypt.gensalt())
            
#             query = 'Insert into usuario values(null,%s,%s)'
#             dados = (user,passCripted)
#             cursor.execute(query,dados)
#             cnx.commit()
#             continue
            
#         if opUserLog == 2:
#             cursor = cnx.cursor()
#             userUser = input('Digite seu usuario:')
#             cursor.execute('select * from usuario')
            
            
#             for (id,user,senha) in cursor.fetchall():
#                 hashed = senha
            
#                 if userUser == user :
#                     senhaUser = input('Senha: ')
#                     if bcrypt.checkpw(senhaUser.encode(), hashed.encode()):
                    
#                      Conta()
#                 else:
#                     print('Usuario não cadastrado')
#                     print("\033[1;33m CARREGANDO.... \033[0;0m")
#                     time.sleep(3)
#                     break
                    

        
        
Conta()