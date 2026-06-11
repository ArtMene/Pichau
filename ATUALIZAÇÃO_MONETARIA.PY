import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ======================= FUNÇÕES DE CALCULO =======================

def calcular ():
   try:
      data_vencimento = datetime.strptime(entry_vencimento.get(), "%d/%m/%Y")
      data_atualizacao = datetime.strptime(entry_atualizacao.get(), "%d/%m/%Y")
      valor = float(entry_valor.get().replace(",","."))
      indice_igpm = float(entry_igpm.get().replace(",","."))
      juros_mes = float(entry_juros.get().replace(",","."))
      multa = float(entry_multa.get().replace(",","."))

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
         return a / 30

      juros_dia_calculado = juros_dia(juros_mes)

      def percentual_juros (a, b):
         return a * b

      juros_periodo = percentual_juros (juros_dia_calculado, dias_atraso)

      def valor_juros (a, b):
         return a * (b / 100)

      juros_mora = valor_juros (atualizacao_igpm, juros_periodo)

      # ======================= MULTA =======================

      if var_multa_sob.get() == 1:
           valor_multa = (atualizacao_igpm + juros_mora) * (multa / 100)
      else:
         valor_multa = atualizacao_igpm * (multa / 100)

      # ======================= TOTAL E ENCARGOS =======================
      def valor_corrigido (a, b, c):
         return a + b + c

      valor_final = valor_corrigido (valor_multa, atualizacao_igpm, juros_mora)

      def encargos (a, b):
         return a - b

      encargos_totais = encargos (valor_final, valor)

      # ======================= FORMATAÇÕES =======================

      def moeda (a):
         return f"R$ {a:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")
      
      def percentual(a):
         return f"{a:.2f}".replace(".", ",") + "%"
      
      # ======================= RESULTADO =======================

      resultado.config(
         text=
         f"Valor Atualizado: {moeda(valor_final)}\n\n"
         f"Encargos Totais: {moeda(encargos_totais)}\n"
         f"Valor Multa: {moeda(valor_multa)}\n"
         f"Taxa de Juros do período: {percentual(juros_periodo)}\n"
         f"Valor Juros do Período: {moeda(juros_mora)}\n"
         f"Dias em atraso: {dias_atraso}\n"
         f"Valor IGPM: {moeda(atualizacao_igpm_final)}\n\n"
         f"Resumo de valores inseridos: \n"
         f"Saldo do título: {moeda(valor)}\n"
         f"Taxa de juros: {percentual(juros_mes)}\n"
         f"Valor da multa: {percentual(multa)}\n"
         f"Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}\n"
         f"Data de Atualização: {data_atualizacao.strftime('%d/%m/%Y')}\n"
         )
   except Exception as erro:
      messagebox.showerror("Erro", f"Verifique os dados inseridos. \n\n{erro}")

#===================== JANELA ====================

janela = tk.Tk()
janela.title ("Calculadora de Atualização Monetária")
janela.geometry("700x400")

label_vencimento = tk.Label(
   janela, 
   text="Data de Vencimento: "
)

label_vencimento.grid(row=0, column=0)
entry_vencimento = tk.Entry(janela)
entry_vencimento.grid(row=0, column=1)

label_atualizacao = tk.Label(
   janela, 
   text="Data de Atualização: "
)

label_atualizacao.grid(row=1, column=0)
entry_atualizacao = tk.Entry(janela)
entry_atualizacao.grid(row=1, column=1)

label_valor = tk.Label(
   janela,
   text= "Digite o Valor a ser Atualizado: "
)

label_valor.grid(row=2, column=0)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=2, column=1)

label_igpm = tk.Label(
   janela,
   text= "Digite a porcentagem de igpm do período: "
)

label_igpm.grid(row=3, column=0)
entry_igpm = tk.Entry(janela)
entry_igpm.grid(row=3, column=1)

label_juros = tk.Label(
   janela,
   text= "Digite a taxa de juros de mora: "
)

label_juros.grid(row=4, column=0)
entry_juros = tk.Entry(janela)
entry_juros.grid(row=4, column=1)

label_multa = tk.Label(
   janela,
   text= "Digite a multa a ser aplicada: "
)

label_multa.grid(row=5, column=0)
entry_multa = tk.Entry(janela)
entry_multa.grid(row=5, column=1)

var_multa_sob = tk.IntVar()

check_multa = tk.Checkbutton(
   janela, 
   text="Calcular multa sob juros",
   variable = var_multa_sob
)

check_multa.grid(row=6, column=0, columnspan=2)

botao_calcular = tk.Button(
   janela,
   text="Calcular",
   command=calcular
)

botao_calcular.gri(row=7, column=0, columnspan=2)

