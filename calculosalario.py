horastrabalhadas = float(input("Quantas horas você trabalha por mês? "))
ganhoporhora     = float(input("Insira quanto você ganha por hora: "))
salariobruto     = ganhoporhora * horastrabalhadas
salariobruto     = salariobruto * 0.89
salariobruto     = salariobruto * 0.92
salariobruto     = salariobruto * 0.95
print("O salário líquido é igual a: ", salariobruto)