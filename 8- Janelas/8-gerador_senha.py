#Importando a biblioteca e nomeando de 'tk'
import tkinter as tk
#===========================================
#Definindo um tamanho e largura fixo
#===========================================
LARGURA = "450"
ALTURA = "400"

def acao_clique():
    print("O botão foi clicado!")

#===========================================
#1. Configuração a Janela Principal
#===========================================
janela = tk.Tk()
janela.title("Gerador de senhas seguras")
janela.geometry(f"{LARGURA}x{ALTURA}")
#Definindo um tom contrastante ao fundo 
janela.config(bg="#00f5ff") 

#===========================================
#2. Título principal do aplicativo
#===========================================
titulo = tk.Label(
    text = "Gerador de Senhas",
    font=("constantia", 16, "bold"),
    bg="#00f5ff",
    fg="#002b36"
)
titulo.pack(pady=20)

#===========================================
#3. Configutando campo Tamanho da Senha
#===========================================
lbl_tamanho = tk.Label(
    text = "Tamanho da Senha",
    font=("arial", 11, "italic", "bold"),
    bg="#00f5ff",
    fg="#002b36"
)
lbl_tamanho.pack(pady=12)

# Entrada do tamanho da senha
entry_tamanho = tk.Entry(
    janela,
    font=("arial", 12),
    width=10,
    justify="center"
)
entry_tamanho.pack(pady=5)

#===========================================
#4. Checkbuttons: Variáveis de controle
#===========================================
var_maiuscula = tk.BooleanVar(value= False)
var_minuscula = tk.BooleanVar(value=False)
var_numeral = tk.BooleanVar(value=False)
var_especial =  tk.BooleanVar(value=False)

# Craindo as caixas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text= "Maiúsculas (A-Z)",
    variable=var_maiuscula,
    bg= "#00f5ff",
    fg= "#002b56",
    selectcolor= "#ff3d71",
    activebackground="#00bbf0",
    activeforeground="#e6fbff"
)
chk_maiuscula.pack(anchor="w", padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text= "Minúsculas (a-z)",
    variable=var_minuscula,
    bg= "#00f5ff",
    fg= "#002b56",
    selectcolor= "#ff3d71",
    activebackground="#00bbf0",
    activeforeground="#e6fbff"
)
chk_minuscula.pack(anchor="w", padx=60, pady=2)

chk_numeral = tk.Checkbutton(
    janela,
    text= "Numeral (0-9)",
    variable=var_numeral,
    bg= "#00f5ff",
    fg= "#002b56",
    selectcolor= "#ff3d71",
    activebackground="#00bbf0",
    activeforeground="#e6fbff"
)
chk_numeral.pack(anchor="w", padx=60, pady=2)

chk_especial = tk.Checkbutton(
    janela,
    text= "Caracteres especiais (@ # $)",
    variable=var_especial,
    bg= "#00f5ff",
    fg= "#002b56",
    selectcolor= "#ff3d71",
    activebackground="#00bbf0",
    activeforeground="#e6fbff"
)
chk_especial.pack(anchor="w", padx=60, pady=2)

#===========================================
#5. Botão de intração
#===========================================


#===========================================
#1. Matém a janela aberta rodando
#===========================================
janela.mainloop()