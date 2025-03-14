from lib.recursividade import fatorial, sum_list, inverter_string,\
calcular_poupanca_dolar, formatar_resultado_dolar,\
calcular_investimentos_bitcoin, formatar_resultado_bitcoin

print("¨*¨¨*"*30)
print(fatorial(5))

print("¨*¨¨*"*30)
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8]))

print("¨*¨¨*"*30)
print(inverter_string("anna_banana_gigi"))

print("¨*¨¨*"*30)
metas, saldo_final, investido_final, juros_final = calcular_poupanca_dolar()
formatar_resultado_dolar(metas, saldo_final, investido_final, juros_final)

print("¨*¨¨*"*30)
resultado = calcular_investimentos_bitcoin()
print(formatar_resultado_bitcoin(resultado))

#a questão 6 esta no recursividade.py