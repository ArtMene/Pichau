import tkinter as tk
from datetime import datetime

# ======================= FUNÇÕES DE CALCULO =======================

def calcular ():

# ======================= INSERÇÃO DE DADOS =======================

data_vencimento = datetime.strptime(input("Data Inicial (dd/mm/aaaa): "), "%d/%m/%Y")
data_atualizacao = datetime.strptime(input("Data de Atualização (dd/mm/aaaa): "), "%d/%m/%Y")


valor = float(input("Saldo do título: ").replace(",","."))
indice_igpm = float(input("Insira o indice IGP-M positivo total do periodo: ").replace(",","."))
juros_mes = float(input("Taxa de juros: ").replace(",","."))
multa = float(input("Multa contratual: ").replace(",","."))

# ======================= IGPM =======================

if indice_igpm > 0:
    atualizacao_igpm = valor * (1 + (indice_igpm/100))
else:
 atualizacao_igpm = valor

atualizacao_igpm_final = atualizacao_igpm - valor

# ======================= DIAS EM ATRASO =======================

dias_atraso = (data_atualizacao - data_vencimento).days

if dias_atraso < 0:
    dias_atraso = 0

# ======================= CALCULO DE JUROS =======================

def juros_dia (a):
   return a/ 30

juros_dia_calculado = juros_dia(juros_mes)

def percentual_juros (a, b):
   return a * b

juros_periodo = percentual_juros (juros_dia_calculado, dias_atraso)

def valor_juros (a, b):
   return a * (b / 100)

juros_mora = valor_juros (atualizacao_igpm, juros_periodo)

# ======================= MULTA =======================

var_multa_sob = tk.IntVar()

tk.label(janela, text = "Calcular Multa Sobre Juros?", variable=var_multa_sob)

if multa_sob in ("s", "sim"):
    valor_multa = (atualizacao_igpm + juros_mora) * (multa / 100)
else:
 valor_multa = atualizacao_igpm * (multa / 100)

def valor_corrigido (a, b, c):
   return a + b + c

valor_final = valor_corrigido (valor_multa, atualizacao_igpm, juros_mora)

def encargos (a, b):
   return a - b

encargos_totais = encargos (valor_final, valor)

def moeda (a):
   return f"R$ {a:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")

def percentual(a):
    return f"{a:.2f}".replace(".", ",") + "%"

print("\n====== DEMONSTRATIVO ======")
print(f"Valor Atualizado: {moeda(valor_final)}")
print(f"\nEncargos Totais: {moeda(encargos_totais)}")
print(f"\nValor Multa: {moeda(valor_multa)}")
print(f"Taxa de Juros do período: {percentual(juros_periodo)}")
print(f"Valor Juros do Período: {moeda(juros_mora)}")
print(f"Dias em atraso: {dias_atraso}")
print(f"Valor IGPM: {moeda(atualizacao_igpm_final)}")
print("\n Resumo de valores inseridos: ")
print(f"Saldo do título: {moeda(valor)}")
print(f"Taxa de juros: {percentual(juros_mes)}")
print(f"Valor da multa: {percentual(multa)}")
print(f"Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
print(f"Data de Atualização: {data_atualizacao.strftime('%d/%m/%Y')}")
