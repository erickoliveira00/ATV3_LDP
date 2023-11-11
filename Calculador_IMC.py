import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100
        peso = float(entry_peso.get())

        imc = peso / (altura ** 2)
        resultado = f"Seu IMC é: {imc:.2f}\n\nClassificação:\n"

        if imc < 17:
            resultado += "Muito abaixo do peso"
        elif 17 <= imc < 18.5:
            resultado += "Abaixo do peso"
        elif 18.5 <= imc < 25:
            resultado += "Peso normal"
        elif 25 <= imc < 30:
            resultado += "Acima do peso"
        elif 30 <= imc < 35:
            resultado += "Obesidade I"
        elif 35 <= imc < 40:
            resultado += "Obesidade II (severa)"
        else:
            resultado += "Obesidade III (mórbida)"

        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, resultado)
        texto_resultado.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")


def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.config(state=tk.DISABLED)


def sair():
    janela.destroy()



janela = tk.Tk()
janela.title("Calculadora de IMC")


tk.Label(janela, text="Nome completo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(janela, text="Endereço:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(janela, text="Altura (cm):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_altura = tk.Entry(janela)
entry_altura.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(janela, text="Peso (kg):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_peso = tk.Entry(janela)
entry_peso.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=4, column=0, pady=10, sticky="ew")

btn_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar)
btn_reiniciar.grid(row=5, column=0, pady=10, sticky="ew")

btn_sair = tk.Button(janela, text="Sair", command=sair)
btn_sair.grid(row=6, column=0, pady=10, sticky="ew")

texto_resultado = tk.Text(janela, height=10, width=40, state=tk.DISABLED)
texto_resultado.grid(row=4, column=1, rowspan=3, pady=10, padx=10, sticky="nsew")


janela.columnconfigure(1, weight=1)
janela.rowconfigure(4, weight=1)


janela.mainloop()
