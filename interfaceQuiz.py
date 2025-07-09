import random
from tkinter import *
from tkinter import messagebox
from TelaQuiz import perguntas  # Importa as perguntas do arquivo Telaquiz.py

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Revisão ensino médio")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        # Variáveis de controle
        self.perguntas_disponiveis = perguntas.copy()
        self.pergunta_atual = None
        self.pontuacao = 0
        self.respondidas = 0
        self.total_perguntas = 5  # Número de perguntas do quiz
        
        # Elementos da interface
        self.label_titulo = Label(root, text="Quiz Revisão ensino médio", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.label_titulo.pack(pady=10)
        
        self.label_pergunta = Label(root, text="", font=("Arial", 14), wraplength=550, bg="#f0f0f0", justify="left")
        self.label_pergunta.pack(pady=20)
        
        self.frame_opcoes = Frame(root, bg="#f0f0f0")
        self.frame_opcoes.pack()
        
        self.var_opcao = StringVar()
        self.var_opcao.set(None)
        
        self.botoes_opcoes = []
        for i in range(4):
            btn = Radiobutton(self.frame_opcoes, text="", variable=self.var_opcao, 
                             value="", font=("Arial", 12), bg="#f0f0f0", 
                             command=self.verificar_resposta)
            btn.pack(anchor="w", pady=5)
            self.botoes_opcoes.append(btn)
        
        self.btn_proximo = Button(root, text="Próxima Pergunta", font=("Arial", 12), 
                                 command=self.proxima_pergunta, state=DISABLED)
        self.btn_proximo.pack(pady=20)
        
        self.label_pontuacao = Label(root, text=f"Pontuação: {self.pontuacao}/{self.respondidas}", 
                                    font=("Arial", 12), bg="#f0f0f0")
        self.label_pontuacao.pack()
        
        # Iniciar o quiz
        self.proxima_pergunta()
    
    def proxima_pergunta(self):
        if self.respondidas >= self.total_perguntas or not self.perguntas_disponiveis:
            messagebox.showinfo("Fim do Quiz", f"Quiz concluído!\nSua pontuação final: {self.pontuacao}/{self.total_perguntas}")
            self.root.destroy()
            return
        
        # Seleciona uma pergunta aleatória
        self.pergunta_atual = random.choice(self.perguntas_disponiveis)
        self.perguntas_disponiveis.remove(self.pergunta_atual)
        
        # Atualiza a interface com a nova pergunta
        self.label_pergunta.config(text=self.pergunta_atual["pergunta"])
        
        # Embaralha as opções
        opcoes = self.pergunta_atual["opcoes"]
        random.shuffle(opcoes)
        
        # Atualiza os botões de opção
        for i in range(4):
            if i < len(opcoes):
                self.botoes_opcoes[i].config(text=opcoes[i], value=opcoes[i], state=NORMAL)
            else:
                self.botoes_opcoes[i].config(text="", value="", state=DISABLED)
        
        self.var_opcao.set(None)
        self.btn_proximo.config(state=DISABLED)
    
    def verificar_resposta(self):
        resposta_selecionada = self.var_opcao.get()
        if resposta_selecionada == self.pergunta_atual["resposta"]:
            self.pontuacao += 1
        
        self.respondidas += 1
        self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}/{self.respondidas}")
        
        # Desabilita os botões de opção após responder
        for btn in self.botoes_opcoes:
            btn.config(state=DISABLED)
        
        # Habilita o botão de próxima pergunta
        self.btn_proximo.config(state=NORMAL)

if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.interfaceQuizloop()