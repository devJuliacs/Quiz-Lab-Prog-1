import tkinter as tk
from tkinter import messagebox
import json
import os

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
        
        # Verifica se o arquivo já existe
        if os.path.exists("cadastros.json"):
            with open("cadastros.json", "r") as f:
                try:
                    cadastros = json.load(f)
                except json.JSONDecodeError:
                    cadastros = []
        else:
            cadastros = []
        
        # Verifica se usuário já existe
        for cadastro in cadastros:
            if cadastro["usuario"] == usuario:
                messagebox.showerror("Erro", "Usuário já cadastrado!")
                return
        
        cadastros.append(dados)
        
        with open("cadastros.json", "w") as f:
            json.dump(cadastros, f, indent=4)
        
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        janela_cadastro.destroy()
    
    janela_cadastro = tk.Tk()
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
    
    janela_cadastro.mainloop()

def tela_login():
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
                janela_login.destroy()
                iniciar_quiz()
                return
        
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.geometry("300x150")
    
    tk.Label(janela_login, text="Usuário:").pack()
    entry_usuario = tk.Entry(janela_login)
    entry_usuario.pack()
    
    tk.Label(janela_login, text="Senha:").pack()
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.pack()
    
    tk.Button(janela_login, text="Entrar", command=verificar_login).pack(pady=10)
    tk.Button(janela_login, text="Cadastrar", command=tela_cadastro).pack()
    
    janela_login.mainloop()

def iniciar_quiz():
    try:
        # Tenta importar sua interface de quiz existente
        from interfaceQuiz import main as quiz_main
        quiz_main()
    except ImportError:
        # Se não encontrar, cria uma interface simples de exemplo
        messagebox.showinfo("Info", "Conectado à interface do quiz!")
        janela_quiz = tk.Tk()
        janela_quiz.title("Quiz")
        janela_quiz.geometry("400x300")
        
        tk.Label(janela_quiz, 
                text="Bem-vindo ao Quiz!\n\nEsta é uma interface temporária.",
                font=("Arial", 14),
                pady=50).pack()
        
        tk.Button(janela_quiz, 
                text="Iniciar Quiz", 
                command=lambda: messagebox.showinfo("Quiz", "Quiz iniciado!"),
                padx=20, pady=10).pack()
        
        janela_quiz.mainloop()

if __name__ == "__main__":
    tela_login()