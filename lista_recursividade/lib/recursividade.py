def fatorial(numero : int) -> int: 

    if numero == 1 or numero == 0:
        return 1
    
    else:
        return numero * fatorial (numero - 1)
    
numero = int(input(f"insira um numero que deseja fatorar: "))
print(fatorial(numero))


def sum_list(lista : list) -> float:
   pass 

