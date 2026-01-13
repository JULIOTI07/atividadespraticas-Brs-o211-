import tkinter as tk

def verificar_bissexto():
    try:
        ano = int(entry_ano.get())
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            resultado = f"O ano {ano} é bissexto "
        else:
            resultado = f"O ano {ano} NÃO é bissexto "
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Digite um ano válido!")

# Criando janela
janela = tk.Tk()
janela.title("Verificador de Ano Bissexto")

# Entrada de ano
tk.Label(janela, text="Digite um ano:").grid(row=0, column=0, padx=10, pady=10)
entry_ano = tk.Entry(janela)
entry_ano.grid(row=0, column=1, padx=10, pady=10)

# Botão de verificação
btn_verificar = tk.Button(janela, text="Verificar", command=verificar_bissexto)
btn_verificar.grid(row=1, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()
