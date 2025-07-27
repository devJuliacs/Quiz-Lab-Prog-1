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

        # Configurar pesos das linhas para melhor distribuição
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
                bg="#f0f0f0",
                fg="black",
                command=self.habilitar_proximo,
                indicatoron=0,
                width=self.button_width,
                anchor="center",
                padx=10,
                pady=5,
                relief="raised",
                activebackground="#3498db",  # Cor quando mouse está sobre
                activeforeground="white"     # cor do texto quando o mouse está sobre
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

        resposta_correta = self.quiz_logica.verificar_resposta(resposta_selecionada_texto)
        resposta_correta_texto = self.quiz_logica.pergunta_atual_obj["options"][self.quiz_logica.pergunta_atual_obj["correct"]]

        for btn in self.botoes_opcoes:
            if btn.cget("text") == resposta_selecionada_texto:
                btn.config(bg="#e74c3c" if not resposta_correta else "#2ecc71")  # Vermelho/Verde
                btn.config(fg="white")
        
            if btn.cget("text") == resposta_correta_texto:
                btn.config(bg="#2ecc71", fg="white")  # Verde para resposta correta
            
            btn.config(state=tk.DISABLED)

        pontuacao = self.quiz_logica.obter_pontuacao()
        self.label_pontuacao.config(text=f"Pontuação: {pontuacao['pontuacao']}/{pontuacao['respondidas']}")

        self.master.after(2000, self._avancar_apos_feedback)

    def _avancar_apos_feedback(self):
        for btn in self.botoes_opcoes:
            btn.config(
                bg="#f0f0f0",  # Cor de fundo original
                fg="black",    # Adicionado: cor do texto preta
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
    janela_cadastro.geometry("300x200")
    
    tk.Label(janela_cadastro, text="Usuário:").pack()
    entry_usuario = tk.Entry(janela_cadastro)
    entry_usuario.pack()
    
    tk.Label(janela_cadastro, text="Senha:").pack()
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.pack()
    
    tk.Label(janela_cadastro, text="Email:").pack()
    entry_email = tk.Entry(janela_cadastro)
    entry_email.pack()
    
    tk.Button(janela_cadastro, text="Cadastrar", command=salvar_cadastro).pack(pady=10)

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
    login_root.geometry("300x150")
    
    tk.Label(login_root, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_root)
    entry_usuario.pack()
    
    tk.Label(login_root, text="Senha:").pack()
    entry_senha = tk.Entry(login_root, show="*")
    entry_senha.pack()
    
    tk.Button(login_root, text="Entrar", command=verificar_login).pack(pady=10)
    tk.Button(login_root, text="Cadastrar", command=tela_cadastro).pack()
    
    login_root.mainloop()

def iniciar_tela_inicial_quiz():
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()

if __name__ == "__main__":
    tela_login()