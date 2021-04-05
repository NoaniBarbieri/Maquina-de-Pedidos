def tabela(): #Quando for realizar uma nova compra irá mostrar quais produtos tem na loja
    """APENAS CHAMA A TABELA COM OS PRODUTOS"""
    print('-'*30)
    print(" [1]Pizza ->30.00\n [2]Refrigerante ->4.50\n [3]Suco -> 3.50\n [4]Sorvete ->2.50\n [5]Docinho ->1.50")
    print('-'*30)
def caixa (a=5,b=5,c=5,d=5,e=5): #esta funcao irá verificar se tem o produto ou nao na loja, funcao principal
    """ESTA FUNÇAO CONTEM OS CONTADORES PARA VER SE HÁ DISPONBILIDADE OU NAO"""
    tabela()
    pr=int(input("Escolha um produto"))
    if pr==1:
        a-1
        if a>0 and a<=5:
            print("Você escolheu: Pizza")
            print("Preço: {}".format(preco(pr)))
        else:
            print("Produto Indisponível")
    elif pr==2:
        b-1
        if b>0 and b<=5:
            print("Você escolheu: Refrigerante")
            print("Preço: {}".format(preco(pr)))
        else:
            print("Produto Indisponível")
    elif pr==3:
        c-1
        if c>0 and c<=5:
            print("Você escolheu: Suco")
            print("Preço: {}".format(preco(pr)))
        else:
            print("Produto Indisponível")
    elif pr==4:
        d-1
        if d>0 and d<=5:
            print("Você escolheu: Sorvete")
            print("Preço: {}".format(preco(pr)))
        else:
            print("Produto Indisponível")
    elif pr==5:
        e-1
        if e>0 and e<=5:
            print("Você escolheu: Docinho")
            print("Preço: {}".format(preco(pr)))
        else:
            print("Produto Indisponível")
    else:
        print("Número inválido")
        caixa(a,b,c,d,e)
    dinheiro(pr)
def preco(pr): #calcula o preço dos produtos e retorna na função acima, além de ser utilizada na função dinheiro
    """ESTA CALCULA OS PREÇOS"""
    if pr==1:
        return 30.00
    elif pr==2:
        return 4.50
    elif pr==3:
        return 3.50
    elif pr==4:
        return 2.50
    elif pr==5:
        return 1.50
def dinheiro(pr): #funcao para receber o dinheiro e retornar o valor inserido e o troco, chamando a função troco abaixo
    """PEDE PARA INSERIR O DINHEIRO E RETORNA O VALOR"""
    d=float(input("entre com o pagamento"))
    if d<preco(pr):
        print("Valor inválido")
        dinheiro(pr)
    else:
        if(round(d-(preco(pr)),2)==0):
            print("Não há troco")
            print("Obrigada pela preferencia\nVolte Sempre")
        else:
            print("Valor pago:{}".format(d))
            print("Troco:{}".format(round(d-(preco(pr)),2)))
            print("Pegue seu troco:")
            troco(round(d-(preco(pr)),2))
def troco(t): #função troco retorna as notas e moedas para o troco, sendo chamada na função dinheiro e na principal 
    """FUNCAO PARA REALIZAR O TROCO"""
    if t>=100:
        print("R$100.00")
        return troco(t-100)
    elif t<100 and t>=50:
        print("R$50.00")
        return troco(t-50)
    elif t<50 and t>=20:
        print("R$20.00")
        return troco(t-20)
    elif t<20 and t>=10:
        print("R$10.00")
        return troco(t-10)
    elif t<10 and t>=5:
        print("R$5.00")
        return troco(t-5)
    elif t<5 and t>=2:
        print("R$2.00")
        return troco(t-2)
    elif t<2 and t>=1:
        print("R$1.00")
        return troco(t-1)
    elif t<1 and t>=0.50:
        print("R$0.50")
        return troco(t-0.50)
    elif t<0.50 and t>=0.25:
        print("R$0.25")
        return troco(t-0.25)
    elif t<0.25 and t>=0.10:
        print("R$0.10")
        return troco(t-0.10)
    elif t<0.10 and t>=0.05:
        print("R$0.05")
        return troco(t-0.05)
    elif t<0.05 and t>=0.01:
        print("R$0.01")
        return troco(t-0.01)
    else:
        return ("error")
def main(): #função main que tem como intuito deixar uma segunda opção de compra ou terminar a compra do cliente
    """FUNCAO MENU PARA REALIZAR OUTRA COMPRA OU NAO"""
    r=int(input("Deseja obter nova compra? [1]SIM E [2]NAO"))
    if r==2:
        print('Obrigada pela preferencia\nVolte Sempre')
        exit
    elif r==1:
        caixa()
        main()
    else:
        main()
caixa()
main()

