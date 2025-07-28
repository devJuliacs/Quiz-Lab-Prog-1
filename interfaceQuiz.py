import random
import tkinter as tk
from tkinter import messagebox
import json
import os
import time
from quiz_dados import obter_quiz_dados, obter_perguntas_aleatorias
from quiz_logica import QuizLogica

class QuizApp:
    def __init__(self, master, perguntas):
        self.master = master
        self.master.title("Quiz Revisão Ensino Médio")
        self.master.configure(bg="#f0f0f0")
        
        self.quiz_logica = QuizLogica(perguntas)
        
        # Configurações de janela (Aumentamos)
        self.window_width = 700
        self.window_height = 500
        self.button_width = 35

        self.master.configure(padx=20, pady=20)

        # Configurando pesos das linhas para melhor distribuição
        self.master.grid_rowconfigure(2, weight=1)  # Linha da pergunta
        self.master.grid_rowconfigure(3, weight=2)  # Linha das opções
        
        # Centralizar janela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{int(x)}+{int(y)}')
        
        # Configuração do grid
        self.master.grid_rowconfigure(0, weight=0) 
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Elementos da interface
        pontuacao = self.quiz_logica.obter_pontuacao()
        self.label_pontuacao = tk.Label(
            self.master, 
            text=f"Pontuação: {pontuacao['pontuacao']}/{pontuacao['respondidas']}",
            font=("Arial", 12), 
            bg="#f0f0f0"
        )
        self.label_pontuacao.grid(row=0, column=0, pady=(10, 5), sticky="n")

        self.label_titulo = tk.Label(
            self.master, 
            text="Quiz Revisão Ensino Médio", 
            font=("Arial", 20, "bold"), 
            bg="#f0f0f0"
        )
        self.label_titulo.grid(row=1, column=0, pady=10)

        self.label_pergunta = tk.Label(
            self.master, 
            text="", 
            font=("Arial", 14), 
            wraplength=550, 
            bg="#f0f0f0", 
            justify="center"
        )
        self.label_pergunta.grid(row=2, column=0, pady=20)

        self.frame_opcoes = tk.Frame(self.master, bg="#f0f0f0")
        self.frame_opcoes.grid(row=3, column=0, pady=0)
        self.frame_opcoes.grid_columnconfigure(0, weight=1)

        self.var_opcao = tk.StringVar()
        self.botoes_opcoes = []
        
        for i in range(4):
            btn = tk.Radiobutton(
                self.frame_opcoes, 
                text="", 
                variable=self.var_opcao,
                value="", 
                font=("Arial", 12), 
                bg="white",          # Fundo branco inicial
                fg="black",          # Texto preto inicial
                command=self.habilitar_proximo,
                indicatoron=0,
                width=self.button_width,
                anchor="center",
                padx=10,
                pady=5,
                relief="raised",
                activebackground="#3498db",  # Cor quando pressionado
                activeforeground="white"     # Texto quando pressionado
            )
            btn.grid(row=i, column=0, pady=5)
            self.botoes_opcoes.append(btn)

        self.btn_proximo = tk.Button(
            self.master,
            bg="#22382D",
            fg="white",
            text="Próxima Pergunta", 
            font=("Arial", 12),
            command=self.verificar_e_avancar, 
            state=tk.DISABLED,
            width=self.button_width
        )
        self.btn_proximo.grid(row=4, column=0, pady=20)

        self.proxima_pergunta()

    

    def habilitar_proximo(self):
        self.btn_proximo.config(state=tk.NORMAL)

    def verificar_e_avancar(self):
        self.btn_proximo.config(state=tk.DISABLED)
        resposta_selecionada_texto = self.var_opcao.get()

        if not self.quiz_logica.pergunta_atual_obj:
            return

        # Obter índice e texto da resposta correta
        indice_correto = self.quiz_logica.pergunta_atual_obj["correct"]
        resposta_correta_texto = self.quiz_logica.pergunta_atual_obj["options"][indice_correto]
        
        # Verificar se a resposta está correta
        resposta_correta = (resposta_selecionada_texto == resposta_correta_texto)
        self.quiz_logica.verificar_resposta(resposta_selecionada_texto)

        # Aplicar feedback visual
        for btn in self.botoes_opcoes:
            texto_botao = btn.cget("text")
            
            # Resetar configurações visuais
            btn.config(bg="white", fg="black", relief="raised")
            
            # Se for a resposta selecionada
            if texto_botao == resposta_selecionada_texto:
                btn.config(bg="#2ecc71" if resposta_correta else "#e74c3c", fg="white")
            
            # Se for a resposta correta (diferente da selecionada)
            elif texto_botao == resposta_correta_texto and not resposta_correta:
                btn.config(bg="#2ecc71", fg="white")
            
            # Desativar todos os botões
            btn.config(state=tk.DISABLED)

        # Atualizar pontuação
        pontuacao = self.quiz_logica.obter_pontuacao()
        self.label_pontuacao.config(text=f"Pontuação: {pontuacao['pontuacao']}/{pontuacao['respondidas']}")

        self.master.after(2000, self._avancar_apos_feedback)
               

    def _avancar_apos_feedback(self):
        for btn in self.botoes_opcoes:
            btn.config(
                bg="#f0f0f0",  # Cor de fundo original
                fg="black",    # Adicionado: cor do texto preta
                relief="raised",
                state=tk.NORMAL
            )
        self.proxima_pergunta()

    def proxima_pergunta(self):
        if not self.quiz_logica.proxima_pergunta():
            pontuacao = self.quiz_logica.obter_pontuacao()
            messagebox.showinfo(
                "Fim do Quiz", 
                f"Quiz concluído!\nSua pontuação final: {pontuacao['pontuacao']}/{pontuacao['total_perguntas']}"
            )
            self.master.destroy()
            return

        pergunta_atual = self.quiz_logica.obter_pergunta_atual()
        self.label_pergunta.config(text=pergunta_atual["pergunta"])
        opcoes = pergunta_atual["opcoes"]

        for i in range(4):
            if i < len(opcoes):
                self.botoes_opcoes[i].config(
                    text=opcoes[i], 
                    value=opcoes[i], 
                    state=tk.NORMAL
                )
            else:
                self.botoes_opcoes[i].config(
                    text="", 
                    value="", 
                    state=tk.DISABLED
                )

        self.var_opcao.set("")
        self.btn_proximo.config(state=tk.DISABLED)

class StartScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Bem-vindo ao Quiz!")
        self.master.geometry("400x250")
        self.master.configure(bg="#f0f0f0")

        # Centralizar janela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (400 / 2)
        y = (screen_height / 2) - (250 / 2)
        self.master.geometry(f'400x250+{int(x)}+{int(y)}')

        self.label_welcome = tk.Label(
            self.master, 
            text="Bem-vindo ao Quiz de Revisão!\n\nTeste seus conhecimentos!", 
            font=("Arial", 16, "bold"), 
            bg="#f0f0f0",
            justify="center"
        )
        self.label_welcome.pack(pady=40)

        self.btn_start = tk.Button(
            self.master, 
            text="Iniciar Quiz", 
            font=("Arial", 14), 
            command=self.start_quiz,
            padx=20, 
            pady=10
        )
        self.btn_start.pack(pady=20)

    def start_quiz(self):
        self.master.destroy()
        root = tk.Tk()
        perguntas = obter_perguntas_aleatorias()
        QuizApp(root, perguntas)
        root.mainloop()

def tela_cadastro():
    def salvar_cadastro():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        email = entry_email.get()
        
        if not usuario or not senha or not email:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        dados = {
            "usuario": usuario,
            "senha": senha,
            "email": email
        }
        
        try:
            if os.path.exists("cadastros.json"):
                with open("cadastros.json", "r") as f:
                    cadastros = json.load(f)
            else:
                cadastros = []
            
            if any(cadastro["usuario"] == usuario for cadastro in cadastros):
                messagebox.showerror("Erro", "Usuário já cadastrado!")
                return
            
            cadastros.append(dados)
            
            with open("cadastros.json", "w") as f:
                json.dump(cadastros, f, indent=4)
            
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            janela_cadastro.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("400x350")
    janela_cadastro.configure(bg="#f0f0f0")

    # Definir as fontes antes de usar
    fonte_label = ("Arial", 10)
    fonte_entry = ("Arial", 11)

    frame_principal = tk.Frame(janela_cadastro, bg="white", padx=20, pady=20)
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")

    # Usuário
    tk.Label(frame_principal, 
             text="Usuário:", 
             bg="white",
             font=fonte_label).grid(row=0, column=0, pady=(0,5), sticky="w")
    entry_usuario = tk.Entry(frame_principal, font=fonte_entry, width=25)
    entry_usuario.grid(row=1, column=0, pady=(0,15), ipady=3)

    # Senha
    tk.Label(frame_principal, 
             text="Senha:", 
             bg="white",
             font=fonte_label).grid(row=2, column=0, pady=(0,5), sticky="w")
    entry_senha = tk.Entry(frame_principal, show="*", font=fonte_entry, width=25)
    entry_senha.grid(row=3, column=0, pady=(0,15), ipady=3)

    # Email
    tk.Label(frame_principal, 
             text="Email:", 
             bg="white",
             font=fonte_label).grid(row=4, column=0, pady=(0,5), sticky="w")
    entry_email = tk.Entry(frame_principal, font=fonte_entry, width=25)
    entry_email.grid(row=5, column=0, pady=(0,20), ipady=3)

    # Botão Cadastrar
    btn_cadastrar = tk.Button(frame_principal,
                             text="Cadastrar",
                             command=salvar_cadastro,
                             bg="#4CAF50",
                             fg="white",
                             font=("Arial", 11, "bold"),
                             padx=20,
                             pady=5)
    btn_cadastrar.grid(row=6, column=0, sticky="ew")

    # Centralizar janela
    janela_cadastro.update_idletasks()
    largura = janela_cadastro.winfo_width()
    altura = janela_cadastro.winfo_height()
    x = (janela_cadastro.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela_cadastro.winfo_screenheight() // 2) - (altura // 2)
    janela_cadastro.geometry(f"+{x}+{y}")

def tela_login():
    def verificar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        
        try:
            if not os.path.exists("cadastros.json"):
                messagebox.showerror("Erro", "Nenhum usuário cadastrado!")
                return
            
            with open("cadastros.json", "r") as f:
                cadastros = json.load(f)
            
            for cadastro in cadastros:
                if cadastro["usuario"] == usuario and cadastro["senha"] == senha:
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                    login_root.destroy()
                    iniciar_tela_inicial_quiz()
                    return
            
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("400x300")

    frame_principal = tk.Frame(login_root, bg="#f0f0f0")
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame
    
    tk.Label(frame_principal, text="Usuário:", bg="#f0f0f0").pack(pady=(0,5))
    entry_usuario = tk.Entry(frame_principal)
    entry_usuario.pack(pady=5)
    
    tk.Label(frame_principal, text="Senha:", bg="#f0f0f0").pack(pady=(0,5))
    entry_senha = tk.Entry(frame_principal, show="*")    
    entry_senha.pack(pady=5)

    frame_botoes = tk.Frame(frame_principal, bg="#f0f0f0")
    frame_botoes.pack(pady=15)
    
    tk.Button(frame_botoes, text="Entrar", command=verificar_login).pack(side="left", padx=10)
    tk.Button(frame_botoes, text="Cadastrar", command=tela_cadastro).pack(side="left", padx=10)
    
    login_root.mainloop()

def iniciar_tela_inicial_quiz():
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()

if __name__ == "__main__":
    tela_login()