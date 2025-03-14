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




def calcular_poupanca_dolar(mes=0, saldo=0, investido=0, juros_acumulados=0, meta=None):
    if meta is None:
        meta = {'100k': None, '1M': None}
    
    if all(meta.values()):
        return meta, saldo, investido, juros_acumulados

    if mes > 0:
        saldo_anterior = saldo - 500 
        rendimento = saldo_anterior * 0.0005
        saldo += rendimento
        juros_acumulados += rendimento

    saldo += 500
    investido += 500

    if saldo >= 100000 and not meta['100k']:
        meta['100k'] = (mes + 1, investido, juros_acumulados)
    if saldo >= 1000000 and not meta['1M']:
        meta['1M'] = (mes + 1, investido, juros_acumulados)

    return calcular_poupanca_dolar(mes + 1, saldo, investido, juros_acumulados, meta)

def formatar_resultado_dolar(resultado_dolar, saldo_final, investido_final, juros_final):
    for meta, dados in resultado_dolar.items():
        if dados:
            meses = dados[0]
            anos, meses_resto = divmod(meses, 12)
            print(f"meta {meta}: {anos} anos e {meses_resto} meses | "
                  f"Total investido: R$ {dados[1]:,.2f} | "
                  f"Juros acumulados: R$ {dados[2]:,.2f}")

    print(f"\nSaldo final ao atingir R$ 1.000.000,00: R$ {saldo_final:,.2f}")
    print(f"Total investido: R$ {investido_final:,.2f}")
    print(f"Juros compostos ganhos: R$ {juros_final:,.2f}")





def calcular_investimentos_bitcoin(
    mes_atual = 0,
    moeda_atual = 0,
    total_investido = 0,
    dinheiro = {'100k': None, 
                '1M': None, 
                '1btc': None},
    preco_btc = [300000, 310000, 305000, 320000, 315000, 330000, 325000, 340000, 335000, 350000, 345000, 360000],
    taxa_juros = 0.005
):
    if all(dinheiro.values()) or mes_atual >= 12:
        return dinheiro

    valor_bitcoin = preco_btc[mes_atual]
    moeda_atual *= (1 + taxa_juros)
    moeda_atual += 250
    total_investido += 250
    meses = mes_atual + 1

    if not dinheiro['100k'] and moeda_atual >= 100000:
        dinheiro['100k'] = {'tempo': meses, 'investido': total_investido}
    
    if not dinheiro['1M'] and moeda_atual >= 1000000:
        dinheiro['1M'] = {'tempo': meses, 'investido': total_investido}
    
    btc_amount = moeda_atual / valor_bitcoin
    if not dinheiro['1btc'] and btc_amount >= 1:
        dinheiro['1btc'] = {'tempo': meses, 'investido': total_investido}

    return calcular_investimentos_bitcoin(
        mes_atual + 1,
        moeda_atual,
        total_investido,
        dinheiro,
        preco_btc,
        taxa_juros
    )

def formatar_resultado_bitcoin(bitcoin_resultado):
    for marco, dados in bitcoin_resultado.items():
        if dados:
            anos, meses = divmod(dados['tempo'], 12)
            print(
                f"Marco {marco} alcançado em {anos} anos e {meses} meses. "
                f"Total investido: R$ {dados['investido']:.2f}"
            )





#ações que eu vou utilizar, USAR RECURSIVIDADE É LOUCURA
#Petrobras PN (PETR4): Dividend Yield de 21,84% 
#Banco do Brasil (BBAS3): Dividend Yield de 10,8% 
#Itaúsa (ITSA4): Dividend Yield de 7,3% 

def calcular_investimento_acoes():
    investimento_mensal = 80.00
    acoes = {
        'PETR4': {'preco': 27.00, 'dividend_yield': 0.2184, 'quantidade': 0},
        'BBAS3': {'preco': 45.00, 'dividend_yield': 0.108, 'quantidade': 0},
        'ITSA4': {'preco': 10.00, 'dividend_yield': 0.073, 'quantidade': 0}
    }
    valorizacao_anual = 0.05
    valorizacao_mensal = (1 + valorizacao_anual) ** (1/12) - 1

    mes = 0
    total_investido = 0
    marco_100k = None
    marco_1M = None

    while not marco_1M:
        mes += 1
        total_investido += investimento_mensal
        valor_total = 0

        for acao in acoes.values():
            investimento_por_acao = investimento_mensal / len(acoes)
            quantidade_comprada = investimento_por_acao / acao['preco']
            acao['quantidade'] += quantidade_comprada
            dividendos = acao['quantidade'] * (acao['preco'] * acao['dividend_yield'] / 12)
            quantidade_reinvestida = dividendos / acao['preco']
            acao['quantidade'] += quantidade_reinvestida
            acao['preco'] *= (1 + valorizacao_mensal)
            valor_total += acao['quantidade'] * acao['preco']

        if not marco_100k and valor_total >= 100000:
            marco_100k = {
                'tempo': mes,
                'investido': total_investido,
                'valor_total': valor_total
            }
        if not marco_1M and valor_total >= 1000000:
            marco_1M = {
                'tempo': mes,
                'investido': total_investido,
                'valor_total': valor_total
            }

    return marco_100k, marco_1M

def formatar_tempo(meses):
    anos = meses // 12
    meses_restantes = meses % 12
    return f"{anos} anos e {meses_restantes} meses"

marco_100k, marco_1M = calcular_investimento_acoes()

print(f"Tempo para atingir R$ 100.000,00: {formatar_tempo(marco_100k['tempo'])}")
print(f"Total investido até R$ 100.000,00: R$ {marco_100k['investido']:.2f}")
print(f"Valor total ao atingir R$ 100.000,00: R$ {marco_100k['valor_total']:.2f}")
print()
print(f"Tempo para atingir R$ 1.000.000,00: {formatar_tempo(marco_1M['tempo'])}")
print(f"Total investido até R$ 1.000.000,00: R$ {marco_1M['investido']:.2f}")
print(f"Valor total ao atingir R$ 1.000.000,00: R$ {marco_1M['valor_total']:.2f}")
