logo = f"""
  \033[35m░██████╗██╗░░██╗░█████╗░███╗░░██╗████████╗░██████╗
  ██╔════╝██║░░██║██╔══██╗████╗░██║╚══██╔══╝██╔════╝
  ╚█████╗░███████║██║░░██║██╔██╗██║░░░██║░░░╚█████╗░
  ░╚═══██╗██╔══██║██║░░██║██║╚████║░░░██║░░░░╚═══██╗
  ██████╔╝██║░░██║╚█████╔╝██║░╚███║░░░██║░░░██████╔╝
  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░\033[0m
   +-+-+-+-+  \033[1;36mP\033[1;94mH\033[1;36mA\033[1;94mN\033[1;36mT\033[1;94mO\033[1;36mM \033[1;94mS\033[1;36mT\033[1;94mO\033[1;36mC\033[1;94mK\033[0m  +-+-+-+-+
    \033[1;37m(👻)\033[0m   O estoque que nunca morre.
  
  \033[1;31m>>> Desenvolvido por [NIGHTPRZ] <<<\033[0m
"""

print(logo)

itensGR=[] #itensGR = itens em  geral 
def incluir_itens(): #adiciona algum item 
    nome= input('digite o nome do para se incluido ')
    quantidade= int(input('digite a quantidade comprada '))
    valor= float(input('digite o valor pago '))
    total_pago= quantidade*valor

    payload = {
        "nome": nome,
        "quantidade": quantidade,
        "valor": valor,
        "total": f"R$ {total_pago:.2f}" 
    }

    itensGR.append(payload)
    listar_itens()

def listar_itens(): #lista todos os itens
    print("***************************************************************")
    for item in itensGR: 
        print(f"O item {item['nome']} na quantidade {item['quantidade']} com o valor de {item['valor']} deu o valor total de {item['total']}")
    print("***************************************************************")
    

def excluir_item(item_nome):#exclui algum item
    for i,item in enumerate(itensGR):
        if item['nome'].lower() == item_nome.lower():
            itensGR.pop(i)
            print(f"O item '{item_nome}' foi excluído com sucesso.")
            listar_itens()#mostra qual item foi excluido 
            return
    print(f"O item '{item_nome}' não foi encontrado na cesta.")       
    
while True:#menu 
    print('\n')
    print(" ----MENU PRINCIPAL---- ")
    print("1. Incluir itens    ➔ Adiciona novos itens")
    print("2. Listar itens     ➔ Mostra todos os itens adicionado")
    print("3. Excluir itens    ➔ Remove um item")
    print("4. Sair             ➔ Encerra o programa")
    print("\n")
    opçoes=input('digite a opção desejada! ')


    if opçoes =='1':
        incluir_itens()
    elif opçoes =='2':
        listar_itens()
    elif opçoes == '3':
        itens_para_excluir=input("Digite o item para exluir!  ")
        excluir_item(itens_para_excluir)
    else :
        print('voce saiu do sistema :(  ')
    break
