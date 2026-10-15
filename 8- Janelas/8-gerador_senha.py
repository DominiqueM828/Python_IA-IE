#Importando a biblioteca e nomeando de 'tk'
import tkinter as tk
#===========================================
#Importando outras bibliotecas 
#===========================================
import random as rd
import string as sg

#===========================================
#Definindo um tamanho e largura fixo
#===========================================
LARGURA = "450"
ALTURA = "430"

#===========================================
#7. Funções do sistema (A Lógica)
#===========================================
def gerar_senha():
    try:
    #Verificando se a quantidade de caracteres definida é menor do que 4
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: minímo de 4 caracteres!",
                fg="#b60707"
            )
            return
        
        caracteres = ""
        
        if var_maiuscula.get():
            caracteres += sg.ascii_uppercase
        if var_minuscula.get():
            caracteres += sg.ascii_lowercase
        if var_numeral.get():
            caracteres += sg.digits
        if var_especial.get():
            caracteres += sg.punctuation

        if not caracteres:
            lbl_resultado.config(
                text="Erro: selecione ao menos uma opção!",
                fg="#b60707"
            )
            return

        psw = "".join(
            rd.choice(caracteres) for i in range(tamanho)
            )

        lbl_resultado.config(
            text= f"Senha: {psw}",
            fg="#07D100"
        )
    except ValueError:
        lbl_resultado.config(
            text = "Erro: Digite um número válido!",
            fg="#b60707"
        )

#===========================================
#8. Botão Área de Transferência
#===========================================
def copiar_pws():
    text_resul = lbl_resultado.cget("text")

    if "Senha: " in text_resul:
        senha_pura = text_resul.replace("Senha: ", "")
        #replace troca a palavra "senha" por "vazio"
        janela.clipboard_clear()
        janela.clipboard_append(senha_pura)
    else:
        lbl_status_copia.config(
            text = "Senha não gerada!",
            fg = "#b60707"
        )

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
#5. Botão de intração (btn: se torta objeto)
#===========================================
btn_gerar = tk.Button(
    janela,
    text="Gerar senha segura",
    command=gerar_senha,
    bg="#002b56",
    fg="#ffffff",
    activebackground="#00bbf0",
    padx=10,
    pady=5
)
btn_gerar.pack(anchor="center", pady=15)

#===========================================
#7. Label que apresenta o resultado 
#===========================================
lbl_resultado = tk.Label(
    janela,
    text = "Senha será exibida aqui: ",
    font=("arial", 11, "italic", "bold"),
    bg="#00f5ff",
    fg="#002b36"
)
lbl_resultado.pack(pady=5)

#===========================================
#8. Botão de cópia senha
#===========================================
btn_copiar = tk.Button(
    janela,
    text= "Copiar",
    command= copiar_pws,
    font=("arial", 10, "bold"),
    bg="#002b56",
    fg="#ffffff",
    padx= 8,
    pady= 3
)
btn_copiar.pack(pady= 5 )

lbl_status_copia = tk.Label(
    janela,
    text = " ",
    font=("arial", 9 , "italic"),
    bg="#00f5ff",
    fg="#002b36"
)
lbl_status_copia.pack(pady=4)

#===========================================
#1. Matém a janela aberta rodando
#===========================================
janela.mainloop()