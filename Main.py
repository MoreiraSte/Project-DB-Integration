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
            
            query = 'Insert into produto values(null,%s,%s)'
            dados = (user,passCripted)
            cursor.execute(query,dados)
            cnx.commit()
            
        if opUserLog == 2:
            
            userUser = input('Digite seu usuario:')
            senhaUser = input('Digite sua senha:') 
            query = 'select * from usuario where user=%s and where senha=%s'
            dados = (userUser,senhaUser)
            cursor.execute(query,dados)
            
            for (id,user,senha) in cursor:
                if userUser == user and senhaUser == senha:
                    Conta()
                else:
                    print('Usuario não cadastrado')
                    print("\033[1;33m CARREGANDO.... \033[0;0m")
                    time.sleep(3)
                    break
                    
def Conta():
    
    print("\033[1;32m =-=" * 8 + "\033[0;0m")
    print("         BEM-VINDO AO ECOMMERCE")
    print("\033[1;32m Já possui Login?" * 8 + "\033[0;0m")
    print("\033[1;32m =-=" * 8 + "\033[0;0m")
    opProduto = int(input("  \033[1;32m[1]\033[0;0m - Exibir Produtos cadastrados"
                                "\n  \033[1;32m[2]\033[0;0m - Cadastrar Produto"
                                "\n  \033[1;32m[3]\033[0;0m - Editar Produto"
                                "\n  \033[1;32m[4]\033[0;0m - Excluir Produto"
                                "\n\n  \033[1;32m-->\033[0;0m "))

    print("\033[1;32m =-=" * 8 + "\033[0;0m")   
    
                 
      
      
