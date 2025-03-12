import sys
sys.setrecursionlimit(10**6) # é pra não dar o erro de recursividade infinita


def fatorial(numero : int) -> int: 
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial (numero - 1)
    



def sum_list(lista : list) -> float:
    if not lista:
        return 0
    else:
        return lista [0] + sum_list (lista[1:])




def inverter_string(palavra):
    if len(palavra) <= 1:
        return palavra
    return palavra[-1] + inverter_string(palavra[:-1])



def calcular_poupanca_dolar(mes = 0, saldo = 0, investido = 0, marcos = None): 
    if marcos is None: #não tiver escrito uma meta, vulgo o marco, pré define um
        marcos = {'100k': None, '1M': None}
    
    if all(marcos.values()):
        return marcos
    
    novo_saldo = saldo * 1.0005 + 500
    novo_investido = investido + 500
    
    if novo_saldo >= 100000 and not marcos['100k']:
        marcos['100k'] = (mes + 1, novo_investido)
    if novo_saldo >= 1000000 and not marcos['1M']:
        marcos['1M'] = (mes + 1, novo_investido)
    
    return calcular_poupanca_dolar(mes + 1, novo_saldo, novo_investido, marcos)

#frufruzisse
def formatar_resultado_dolar(resultado_dolar):
    for marco, dados in resultado_dolar.items():
        if dados:
            meses = dados[0]
            anos, meses_resto = divmod(meses, 12)
            print(f"Marco {marco}: {anos} anos e {meses_resto} meses | Total investido: R$ {dados[1]:,.2f}")



def calcular_investimentos_bitcoin(
    mes_atual = 0,
    moeda_atual = 0,
    total_investido = 0,
    dinheiro = {'100k': None,
    '1M': None, 
    '1btc': None},
    preco_btc  =[300000, 310000, 305000, 320000, 315000, 330000, 325000, 340000, 335000, 350000, 345000, 360000]
):

    if all(dinheiro.values()):
        return dinheiro

    valor_bitcoin = preco_btc[mes_atual % 12] if mes_atual < 12 else preco_btc[-1]

    aumento_mensal = 0.01
    moeda_atual *= (1 + aumento_mensal)

    moeda_atual += 250
    total_investido += 250

    meses = mes_atual + 1
    if not dinheiro['100k'] and moeda_atual >= 100000:
        dinheiro['100k'] = {'tempo': meses, 
                        'investido': total_investido}
    
    if not dinheiro['1M'] and moeda_atual >= 1000000:
        dinheiro['1M'] = {'tempo': meses,
                         'investido': total_investido}
    
    btc_amount = moeda_atual / valor_bitcoin
    if not dinheiro['1btc'] and btc_amount >= 1:
        dinheiro['1btc'] = {'tempo': meses, 
                         'investido': total_investido}

    return calcular_investimentos_bitcoin(
        mes_atual + 1,
        moeda_atual,
        total_investido,
        dinheiro,
        preco_btc
    )

#frufruzisse2
def formatar_resultado_bitcoin(bitcoin_resultado):
    for marco, dados in bitcoin_resultado.items():
        if dados:
            anos, meses = divmod(dados['tempo'], 12)
            print(
                f"Marco {marco} alcançado em {anos} anos e {meses} meses. "
                f"Total investido: R$ {dados['investido']:.2f}"
            )




def calcular_investimentos_acoes(
    mes_atual = 0,
    moeda_atual = 0,
    total_investido = 0,
    dinheiro = {'100k': None, 
                '1M': None, 
                '1btc': None},
    preco_btc = [300000, 310000, 305000, 320000, 315000, 330000, 325000, 340000, 335000, 350000, 345000, 360000]
):
    if all(dinheiro.values()):
        return dinheiro

    valor_bitcoin = preco_btc[mes_atual % 12] if mes_atual < 12 else preco_btc[-1]

    aumento_mensal = 0.01
    moeda_atual *= (1 + aumento_mensal)

    moeda_atual += 250
    total_investido += 250

    meses = mes_atual + 1
    if not dinheiro['100k'] and moeda_atual >= 100000:
        dinheiro['100k'] = {'tempo': meses, 
                            'investido': total_investido}
    
    if not dinheiro['1M'] and moeda_atual >= 1000000:
        dinheiro['1M'] = {'tempo': meses, 
                          'investido': total_investido}
    
    btc_amount = moeda_atual / valor_bitcoin
    if not dinheiro['1btc'] and btc_amount >= 1:
        dinheiro['1btc'] = {'tempo': meses, 
                            'investido': total_investido}

    return calcular_investimentos_acoes(
        mes_atual + 1,
        moeda_atual,
        total_investido,
        dinheiro,
        preco_btc
    )

#frufruzisse3
def formatar_resultado_acoes(acoes_resultado):
    for marco, dados in acoes_resultado.items():
        if dados:
            anos, meses = divmod(dados['tempo'], 12)
            print(
                f"Marco {marco} alcançado em {anos} anos e {meses} meses. "
                f"Total investido: R$ {dados['investido']:.2f}"
            )