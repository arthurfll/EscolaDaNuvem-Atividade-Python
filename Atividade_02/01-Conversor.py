dolar = 5.6
euro = 6.6
valor = 100.00

conversaoDolar = float(valor/dolar) 
conversaoEuro = float(valor/euro) 


response = f"valor em reais: {valor:.2f} \n valor em dólares: {conversaoDolar:.2f} \n valor em euros: {conversaoEuro:.2f}"

print(response)

