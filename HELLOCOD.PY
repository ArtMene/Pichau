from datetime import datetime

data_vencimento = datetime.strptime(input("Data Inicial (dd/mm/aaaa): "), "%d/%m/%Y")
data_atualizacao = datetime.strptime(input("Data de Atualização (dd/mm/aaaa): "), "%d/%m/%Y")

valor = float(input("Saldo do título: "))
indice_igpm = float(input("Insira o indice IGP-M positivo total do periodo: "))
juros_mes = float(input("Taxa de juros: "))
multa = float(input("Multa contratual: "))

if indice_igpm > 0:
    atualizacao_igpm = valor * (1 + (indice_igpm/100))
else:
 atualizacao_igpm = valor

while True:
    multa_sob = input("Multa sob juros? (s/n)").strip().lower()
    if multa_sob in ("s", "sim", "n", "nao", "não"):
        break

    print ("Resposta inválida. Utilize apenas S ou N")

dias_atraso = (data_atualizacao - data_vencimento).days

if dias_atraso < 0:
    dias_atraso = 0

juros_dia = juros_mes / 30
percentual_juros = juros_dia * dias_atraso
valor_juros = atualizacao_igpm * (percentual_juros / 100)

if multa_sob in ("s", "sim"):
    valor_multa = (atualizacao_igpm + valor_juros) * (multa / 100)
else:
 valor_multa = atualizacao_igpm * (multa / 100)

valor_corrigido = valor_multa + atualizacao_igpm + valor_juros



print("O valor atualizado do titulo é : ", f"R$ {valor_corrigido:,.2f}")