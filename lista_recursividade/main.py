from lib.recursividade import fatorial, sum_list, inverter_string,\
calcular_poupanca_dolar, formatar_resultado_dolar,\
calcular_investimentos_bitcoin, formatar_resultado_bitcoin, calcular_investimentos_acoes,\
calcular_investimentos_acoes, formatar_resultado_acoes

print("¨*¨¨*"*30)
print(fatorial(5))

print("¨*¨¨*"*30)
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8]))

print("¨*¨¨*"*30)
print(inverter_string("anna_banana_gigi"))

print("¨*¨¨*"*30)
resultado_dolar = calcular_poupanca_dolar()
print(formatar_resultado_dolar(resultado_dolar)) 

print("¨*¨¨*"*30)
resultado_bitcoin = calcular_investimentos_bitcoin()
print(formatar_resultado_bitcoin(resultado_bitcoin)) #os resultados só estão parecidos por causa da pré definição se não fosse dado um parametro na função

print("¨*¨¨*"*30)
resultado_acoes = calcular_investimentos_acoes()
print(formatar_resultado_acoes(resultado_acoes))
