import random

class QuizLogica:
    def __init__(self, perguntas):
        self.perguntas_disponiveis = perguntas
        self.pergunta_atual_obj = None
        self.pontuacao = 0
        self.respondidas = 0
        self.total_perguntas = min(10, len(self.perguntas_disponiveis))
        self._answered_current_question = False

    def obter_perguntas_aleatorias(self, num_perguntas=10):
        """Retorna uma lista aleatória de perguntas"""
        random.shuffle(self.perguntas_disponiveis)
        return self.perguntas_disponiveis[:num_perguntas]
    
    def obter_resposta_correta(self):
        """Retorna o texto da resposta correta"""
        if not self.pergunta_atual_obj:
            return ""
        return self.pergunta_atual_obj["options"][self.pergunta_atual_obj["correct"]]

    def verificar_resposta(self, resposta_selecionada_texto):
        """Verifica se a resposta selecionada está correta"""
        if self.pergunta_atual_obj is None:
            return False

        indice_correto = self.pergunta_atual_obj["correct"]
        resposta_correta_texto = self.pergunta_atual_obj["options"][indice_correto]

        if not self._answered_current_question:
            if resposta_selecionada_texto == resposta_correta_texto:
                self.pontuacao += 1
            self.respondidas += 1
            self._answered_current_question = True

        return resposta_selecionada_texto == resposta_correta_texto

    def obter_feedback_resposta(self, resposta_selecionada_texto):
        """Retorna a resposta correta para feedback"""
        indice_correto = self.pergunta_atual_obj["correct"]
        return self.pergunta_atual_obj["options"][indice_correto]

    def proxima_pergunta(self):
        """Prepara a próxima pergunta ou retorna False se o quiz terminou"""
        self._answered_current_question = False

        if self.respondidas >= self.total_perguntas:
            return False

        self.pergunta_atual_obj = self.perguntas_disponiveis.pop(0)
        return True

    def obter_pergunta_atual(self):
        """Retorna a pergunta atual e opções embaralhadas"""
        if not self.pergunta_atual_obj:
            return None

        pergunta = self.pergunta_atual_obj["question"]
        opcoes = list(self.pergunta_atual_obj["options"])
        random.shuffle(opcoes)
        
        return {
            "pergunta": pergunta,
            "opcoes": opcoes
        }

    def obter_pontuacao(self):
        """Retorna a pontuação atual"""
        return {
            "pontuacao": self.pontuacao,
            "respondidas": self.respondidas,
            "total_perguntas": self.total_perguntas
        }