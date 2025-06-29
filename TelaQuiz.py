import PySimpleGUI as sg

# Dados do quiz - perguntas e respostas
quiz_dados = [
    {
        "question": "Qual é o elemento químico mais abundante da terra?",
        "options": ["Ferro", "Oxigênio", "Silício", "Alumínio"],
        "correct": 1  
    },
    {
        "question": "Qual movimento artístico se caracterizou pela valorização da razão e da ciência, criticando o absolutismo e o Antigo Regime?",
        "options": ["Iluminismo", "Renascimento", "Romantismo", "Barroco"],
        "correct": 0
    },
    {
        "question": "Em uma equação de segundo grau qual o nome do termo que define o número de soluções reais da equação?",
        "options": ["Coeficiente", "Raíz", "Delta(Discriminante)", "Variável"],
        "correct": 2
    },
    {
        "question": "Qual bacia hidrográfica brasileira é a maior do mundo em volume de água e possui a maior biodiversidade?",
        "options": ["Bacia do Paraná", "Bacia do São Francisco", "Bacia Amazônica", "Bacia do Tocantins-Araguaia"],
        "correct": 2
    }, 
    {
        "question": "Qual das seguintes opções é uma característica principal do Neodarwinismo (Teoria Sintética da Evolução)?",
        "options": ["Lamarckismo", "Mutação e seleção natural", "Herança dos caracteres adquiridos", "Geração espontânea"],
        "correct": 1
    },
    {
        "question": "Na Língua Portuguesa, qual figura de linguagem consiste em um exagero intencional para expressar uma ideia?",
        "options": ["Metáfora", "Ironia", "Hipérbole", "Eufemismo"],
        "correct": 2
    },
    {
        "question": "Qual evento histórico marcou o início da Idade Contemporânea?",
        "options": ["Revolução Francesa", "Queda do Império Romano do Ocidente", "Descoberta do Brasil", "Revolução Industrial"],
        "correct": 0
    },
    {
        "question": "Qual é a função do cloroplasto em uma célula vegetal?",
        "options": ["Armazenar água", "Produzir energia através da respiração celular", "Realizar a fotossíntese", "Controlar as atividades da célula"],
        "correct": 2
    },
    {
        "question": "No estudo de vetores em Física, qual operação resulta em um novo vetor perpendicular aos dois vetores originais?",
        "options": ["Soma de vetores", "Subtração de vetores", "Produto escalar", "Produto vetorial"],
        "correct": 3
    },
    {
        "question": "Qual sistema de governo é caracterizado pela centralização do poder nas mãos de um monarca, cuja autoridade é considerada divina?",
        "options": ["Democracia", "República", "Absolutismo", "Feudalismo"],
        "correct": 2
    },

]

question_one = 0
score_user = 0

sg.theme('DarkBlue3')

layout = [
    [sg.Text("", key= "score")],
    [sg.Text("", key= "question")],
    [sg.Button("", key= "op1")],
    [sg.Button("", key= "op2")],
    [sg.Button("", key= "op3")],
    [sg.Button("", key= "op4")],
    [sg.Button("Próxima", key= next)]
]

Janela_Quiz = sg.Window("Quiz", layout)

def update_quiz():
    global question_one
    question_dados = quiz_dados[question_one]

    Janela_Quiz["question"].update(question_dados["question"])
    for i in range(4):
        Janela_Quiz[f"op{i}"].update(question_dados["options"][i]) 

while True:
    events, values = Janela_Quiz.read()
    if events == sg.WIN_CLOSED:
        break
    