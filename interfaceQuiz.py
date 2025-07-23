import random
import tkinter as tk
from tkinter import messagebox
import json
import os
import time
from quiz_dados import obter_quiz_dados, obter_perguntas_aleatorias
# --- Dados do Quiz

#--- Classe QuizApp (tela) ---
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Revisão Ensino Médio")
        self.master.configure(bg="#f0f0f0")

        self.window_width = 600
        self.window_height = 400
        self.button_width = 35

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{int(x)}+{int(y)}')
        
        self.perguntas_disponiveis = obter_perguntas_aleatorias()
        random.shuffle(self.perguntas_disponiveis)
        self.pergunta_atual_obj = None
        self.pontuacao = 0
        self.respondidas = 0
        self.total_perguntas = min(10, len(self.perguntas_disponiveis))

        
        self.master.grid_rowconfigure(0, weight=0) 
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(5, weight=1) 
        self.master.grid_columnconfigure(0, weight=1) 

        self.label_pontuacao = tk.Label(self.master, text=f"Pontuação: {self.pontuacao}/{self.respondidas}",
                                    font=("Arial", 12), bg="#f0f0f0")
        self.label_pontuacao.grid(row=0, column=0, pady=(10, 5), sticky="n")

        self.label_titulo = tk.Label(self.master, text="Quiz Revisão Ensino Médio", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.label_titulo.grid(row=1, column=0, pady=10)

        self.label_pergunta = tk.Label(self.master, text="", font=("Arial", 14), wraplength=550, bg="#f0f0f0", justify="center")
        self.label_pergunta.grid(row=2, column=0, pady=20)

        self.frame_opcoes = tk.Frame(self.master, bg="#f0f0f0")
        self.frame_opcoes.grid(row=3, column=0, pady=0)

        self.frame_opcoes.grid_columnconfigure(0, weight=1) 

        self.var_opcao = tk.StringVar()

        self.botoes_opcoes = []
        for i in range(4):
            btn = tk.Radiobutton(self.frame_opcoes, text="", variable=self.var_opcao,
                             value="", font=("Arial", 12), bg="#f0f0f0",
                             command=self.habilitar_proximo,
                             indicatoron=0,
                             width=self.button_width,
                             anchor="center",
                             padx=10,
                             pady=5,
                             relief="raised"
                             )
            btn.grid(row=i, column=0, pady=5)
            self.botoes_opcoes.append(btn)

        self.btn_proximo = tk.Button(self.master, text="Próxima Pergunta", font=("Arial", 12),
                                 command=self.verificar_e_avancar, state=tk.DISABLED,
                                 width=self.button_width)
        self.btn_proximo.grid(row=4, column=0, pady=20)

        self.proxima_pergunta()

    def habilitar_proximo(self):
        self.btn_proximo.config(state=tk.NORMAL)

    def verificar_e_avancar(self):
        if self.pergunta_atual_obj is None:
            return

        self.btn_proximo.config(state=tk.DISABLED)

        resposta_selecionada_texto = self.var_opcao.get()
        indice_correto = self.pergunta_atual_obj["correct"]
        resposta_correta_texto = self.pergunta_atual_obj["options"][indice_correto]

        # Início do código de feedback de cor
        # Verifica qual botão de rádio foi selecionado e muda a cor
        for i, btn in enumerate(self.botoes_opcoes):
            if btn.cget("text") == resposta_selecionada_texto:
                # Resposta selecionada pelo usuário
                if resposta_selecionada_texto == resposta_correta_texto:
                    btn.config(bg="lightgreen") 
                else:
                    btn.config(bg="red")
                
                self.resposta_usuario_btn = btn 
            
            # Garante que a opção correta sempre fique verde
            if btn.cget("text") == resposta_correta_texto and btn.cget("bg") != "red":
                 btn.config(bg="lightgreen")

            btn.config(state=tk.DISABLED) 
    

        #Tratamento da pontuação
        if not hasattr(self, '_answered_current_question') or not self._answered_current_question:
            if resposta_selecionada_texto == resposta_correta_texto:
                self.pontuacao += 1
            self.respondidas += 1
            self._answered_current_question = True

        self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}/{self.respondidas}")

        self.master.after(2000, self._avancar_apos_feedback)

    def _avancar_apos_feedback(self):
        for btn in self.botoes_opcoes:
            btn.config(bg="#f0f0f0")

        self._answered_current_question = False

        self.proxima_pergunta()


    def proxima_pergunta(self):
        if self.respondidas >= self.total_perguntas:
            messagebox.showinfo("Fim do Quiz", f"Quiz concluído!\nSua pontuação final: {self.pontuacao}/{self.total_perguntas}")
            self.master.destroy()
            return

        self.pergunta_atual_obj = self.perguntas_disponiveis.pop(0)

        self.label_pergunta.config(text=self.pergunta_atual_obj["question"])

        opcoes = list(self.pergunta_atual_obj["options"])
        random.shuffle(opcoes)

        for i in range(4):
            if i < len(opcoes):
                self.botoes_opcoes[i].config(text=opcoes[i], value=opcoes[i], state=tk.NORMAL)
            else:
                self.botoes_opcoes[i].config(text="", value="", state=tk.DISABLED)

        self.var_opcao.set("")
        self.btn_proximo.config(state=tk.DISABLED)

# --- Classe TelaInicial 
class StartScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Bem-vindo ao Quiz!")
        self.master.geometry("400x250")
        self.master.configure(bg="#f0f0f0")

        # Centralizar a janela na tela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (400 / 2)
        y = (screen_height / 2) - (250 / 2)
        self.master.geometry(f'400x250+{int(x)}+{int(y)}')

        self.label_welcome = tk.Label(master, 
                                     text="Bem-vindo ao Quiz de Revisão!\n\nTeste seus conhecimentos!", 
                                     font=("Arial", 16, "bold"), 
                                     bg="#f0f0f0",
                                     justify="center")
        self.label_welcome.pack(pady=40)

        self.btn_start = tk.Button(master, 
                                   text="Iniciar Quiz", 
                                   font=("Arial", 14), 
                                   command=self.start_quiz,
                                   padx=20, pady=10)
        self.btn_start.pack(pady=20)

    def start_quiz(self):
        self.master.destroy() # Fecha a tela de início
        quiz_window = tk.Toplevel() # Cria a nova janela para o quiz
        QuizApp(quiz_window) # Inicia o quiz nessa nova janela


# --- Funções de Cadastro/Login
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
        
        if os.path.exists("cadastros.json"):
            with open("cadastros.json", "r") as f:
                try:
                    cadastros = json.load(f)
                except json.JSONDecodeError:
                    cadastros = []
        else:
            cadastros = []
        
        for cadastro in cadastros:
            if cadastro["usuario"] == usuario:
                messagebox.showerror("Erro", "Usuário já cadastrado!")
                return
        
        cadastros.append(dados)
        
        with open("cadastros.json", "w") as f:
            json.dump(cadastros, f, indent=4)
        
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        janela_cadastro.destroy()
    
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
    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("300x150")

    def verificar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        
        if not os.path.exists("cadastros.json"):
            messagebox.showerror("Erro", "Nenhum usuário cadastrado!")
            return
        
        try:
            with open("cadastros.json", "r") as f:
                cadastros = json.load(f)
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao ler arquivo de cadastros!")
            return
        
        for cadastro in cadastros:
            if cadastro["usuario"] == usuario and cadastro["senha"] == senha:
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                login_root.destroy() # Fecha a janela de login
                iniciar_tela_inicial_quiz() # Chama a nova função para a tela de início do quiz
                return
        
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    tk.Label(login_root, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_root)
    entry_usuario.pack()
    
    tk.Label(login_root, text="Senha:").pack()
    entry_senha = tk.Entry(login_root, show="*")
    entry_senha.pack()
    
    tk.Button(login_root, text="Entrar", command=verificar_login).pack(pady=10)
    tk.Button(login_root, text="Cadastrar", command=tela_cadastro).pack()
    
    login_root.mainloop()

# --- Função para iniciar a Tela Inicial do Quiz ---
def iniciar_tela_inicial_quiz():
    start_window = tk.Toplevel()
    StartScreen(start_window)

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    tela_login()