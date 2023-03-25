def PegaValor():
    try:
        x = float(input("Digite o valor: "))
        return x
    except:
        print("Digite um entrada válida: (Número) ")
        return PegaValor()
    
##def VerificaInteiro(n):
##    if((type(n) is int) or (type(n) is float)):
##        return n
##    else:
##        new = input("Por favor, digite um número válido:\n")
##        return VerificaInteiro(new)

def ConstanteMarinho():
    print("DS  = Dias da semana")
    DS = PegaValor()
    print("JST = Jornada semanal de trabalho (20,30,36,40..)")
    JST = PegaValor()
    print("IST = índice de segurança técnica")
    IST = PegaValor()
    Km = (DS/JST)*IST
    return Km

def THE():
    print("Informe seu PCM:")
    PCM = PegaValor()
    print("Informe seu PCI")
    PCI = PegaValor()
    print("Informe seu PCAD")
    PCAD = PegaValor()
    print("Informe seu PCSI")
    PCSI = PegaValor()
    print("Informe seu PCIt (Caso não tenha, envie 0)")
    PCIt = PegaValor()
    THE = ((PCM*4)+(PCI*6)+(PCAD*10)+(PCSI*10)+(PCIt*18))
    return THE

def  QP():
    print("--------------INFORME OS DADOS PARA O THE-------------------")
    the = THE()
    print("--------------INFORME OS DADOS PARA A CONSTANTE MARINHO--------------")
    km = ConstanteMarinho()
    QP = the*km
    return QP


while True:
    print("Seja bem vindo Ao Cálculo de plantão de enfermagem")
    while True:
        print("\nEscolha abaixo a função que você deseja cálcular\n")
        print("1 - Constante de Marinho")
        print("2 - Tempo de horas de enfermagem")
        print("3 - Quadro de Profissionais\n")
        comando = PegaValor()
        if(comando == 1):
            print("------------- O valor é:", ConstanteMarinho(),"-------------")
            print("Você deseja fazer outro calculo?\n 1 - Sim \n 2 - Não")
            chave = PegaValor()
            if(chave == 1):
                continue
            else:
                break
        if(comando == 2):
            print("------------- O valor é:", THE(),"-------------")
            print("Você deseja fazer outro calculo?\n 1 - Sim \n 2 - Não")
            chave = PegaValor()
            if(chave == 1):
                continue
            else:
                break
        if(comando == 3):
            print("------------- O valor é do quadro é:", QP(),"-------------")
            print("Você deseja fazer outro calculo?\n 1 - Sim \n 2 - Não")
            chave = PegaValor()
            if(chave == 1):
                continue
            else:
                break
        else:
            print("\nDigite uma opção válida\n")
            continue

    break