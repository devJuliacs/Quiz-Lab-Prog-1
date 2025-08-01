import random

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
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Pequim", "Seul", "Tóquio", "Bangkok"],
        "correct": 2
    },
    {
        "question": "Quem escreveu 'Dom Quixote'?",
        "options": ["Machado de Assis", "Miguel de Cervantes", "William Shakespeare", "Gabriel García Márquez"],
        "correct": 1
    },
    {
        "question": "Qual é o maior oceano da Terra?",
        "options": ["Atlântico", "Índico", "Ártico", "Pacífico"],
        "correct": 3
    },
    {
        "question": "Quantos planetas há no nosso Sistema Solar?",
        "options": ["7", "8", "9", "10"],
        "correct": 1
    },
    {
        "question": "Em que ano a Segunda Guerra Mundial terminou?",
        "options": ["1942", "1945", "1950", "1939"],
        "correct": 1
    },

    # Perguntas de Ciências
    {
        "question": "Qual é a unidade básica da vida?",
        "options": ["Átomo", "Molécula", "Célula", "Tecido"],
        "correct": 2
    },
    {
        "question": "Qual gás é essencial para a respiração dos seres humanos?",
        "options": ["Nitrogênio", "Oxigênio", "Dióxido de Carbono", "Hidrogênio"],
        "correct": 1
    },
    {
        "question": "Qual é a força que nos puxa para o centro da Terra?",
        "options": ["Força centrífuga", "Força magnética", "Gravidade", "Força de atrito"],
        "correct": 2
    },
    {
        "question": "Qual é o planeta mais próximo do Sol?",
        "options": ["Vênus", "Marte", "Mercúrio", "Júpiter"],
        "correct": 2
    },
    {
        "question": "Qual é o processo pelo qual as plantas produzem seu próprio alimento?",
        "options": ["Respiração", "Transpiração", "Fotossíntese", "Germinação"],
        "correct": 2
    },
    {
        "question": "Qual é o principal componente do ar que respiramos?",
        "options": ["Oxigênio", "Dióxido de Carbono", "Nitrogênio", "Argônio"],
        "correct": 2
    },
    {
        "question": "Qual é a temperatura de congelamento da água em graus Celsius?",
        "options": ["0°C", "100°C", "-10°C", "32°C"],
        "correct": 0
    },
    {
        "question": "Qual é o nome do cientista que formulou a Teoria da Relatividade?",
        "options": ["Isaac Newton", "Galileu Galilei", "Albert Einstein", "Stephen Hawking"],
        "correct": 2
    },
    {
        "question": "Qual é o maior órgão do corpo humano?",
        "options": ["Coração", "Cérebro", "Pele", "Fígado"],
        "correct": 2
    },
    {
        "question": "Qual é o nome do processo em que a água muda de estado líquido para gasoso?",
        "options": ["Condensação", "Solidificação", "Evaporação", "Sublimação"],
        "correct": 2
    },

    # Perguntas de Matemática
    {
        "question": "Quanto é 7 multiplicado por 8?",
        "options": ["49", "56", "64", "72"],
        "correct": 1
    },
    {
        "question": "Qual é o resultado de 120 dividido por 4?",
        "options": ["20", "30", "40", "50"],
        "correct": 1
    },
    {
        "question": "Se um quadrado tem um lado de 5 cm, qual é a sua área?",
        "options": ["10 cm²", "15 cm²", "20 cm²", "25 cm²"],
        "correct": 3
    },
    {
        "question": "Qual é o próximo número na sequência: 2, 4, 6, 8, ...?",
        "options": ["9", "10", "11", "12"],
        "correct": 1
    },
    {
        "question": "Quanto é 15% de 200?",
        "options": ["15", "20", "30", "45"],
        "correct": 2
    },
    {
        "question": "Qual é a raiz quadrada de 81?",
        "options": ["7", "8", "9", "10"],
        "correct": 2
    },
    {
        "question": "Se um triângulo tem base de 6 cm e altura de 4 cm, qual é a sua área?",
        "options": ["10 cm²", "12 cm²", "18 cm²", "24 cm²"],
        "correct": 1
    },
    {
        "question": "Quanto é 3/4 de 100?",
        "options": ["25", "50", "75", "100"],
        "correct": 2
    },
    {
        "question": "Qual é o valor de 'x' na equação: x + 7 = 15?",
        "options": ["6", "7", "8", "9"],
        "correct": 2
    },
    {
        "question": "Se você tem 3 maçãs e come 1, quantas maçãs você tem?",
        "options": ["0", "1", "2", "3"],
        "correct": 2
    },

    # Perguntas de História
    {
        "question": "Em que ano o Brasil foi descoberto?",
        "options": ["1492", "1500", "1520", "1534"],
        "correct": 1
    },
    {
        "question": "Quem foi o primeiro presidente do Brasil?",
        "options": ["Dom Pedro I", "Getúlio Vargas", "Marechal Deodoro da Fonseca", "Juscelino Kubitschek"],
        "correct": 2
    },
    {
        "question": "Qual império foi governado por Júlio César?",
        "options": ["Império Grego", "Império Romano", "Império Egípcio", "Império Persa"],
        "correct": 1
    },
    {
        "question": "Em que ano a Primeira Guerra Mundial começou?",
        "options": ["1905", "1914", "1918", "1939"],
        "correct": 1
    },
    {
        "question": "Qual foi o principal objetivo da Revolução Francesa?",
        "options": ["Restaurar a monarquia", "Estabelecer uma ditadura", "Defender os direitos humanos e a igualdade", "Expandir o território francês"],
        "correct": 2
    },
    {
        "question": "Quem foi o líder da independência da Índia?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose"],
        "correct": 1
    },
    {
        "question": "Qual civilização antiga construiu as pirâmides de Gizé?",
        "options": ["Romanos", "Gregos", "Egípcios", "Maias"],
        "correct": 2
    },
    {
        "question": "Qual evento marcou o fim da Idade Média?",
        "options": ["Queda do Império Romano", "Revolução Francesa", "Descoberta da América", "Reforma Protestante"],
        "correct": 2
    },
    {
        "question": "Quem foi o navegador português que realizou a primeira viagem de circum-navegação?",
        "options": ["Vasco da Gama", "Pedro Álvares Cabral", "Fernão de Magalhães", "Bartolomeu Dias"],
        "correct": 2
    },
    {
        "question": "Qual foi o período da história marcado pelo Renascimento?",
        "options": ["Idade Antiga", "Idade Média", "Idade Moderna", "Idade Contemporânea"],
        "correct": 2
    },

    # Perguntas de Geografia
    {
        "question": "Qual é o maior país do mundo em área territorial?",
        "options": ["China", "Canadá", "Rússia", "Estados Unidos"],
        "correct": 2
    },
    {
        "question": "Qual oceano banha a costa leste do Brasil?",
        "options": ["Oceano Pacífico", "Oceano Índico", "Oceano Atlântico", "Oceano Ártico"],
        "correct": 2
    },
    {
        "question": "Qual é o deserto mais quente do mundo?",
        "options": ["Deserto do Saara", "Deserto do Atacama", "Deserto de Gobi", "Deserto da Arábia"],
        "correct": 0
    },
    {
        "question": "Qual é a capital da França?",
        "options": ["Roma", "Berlim", "Londres", "Paris"],
        "correct": 3
    },
    {
        "question": "Qual é a montanha mais alta do mundo?",
        "options": ["Monte Kilimanjaro", "Monte Everest", "Monte Fuji", "K2"],
        "correct": 1
    },
    {
        "question": "Qual é o rio mais longo do mundo?",
        "options": ["Rio Amazonas", "Rio Nilo", "Rio Yangtzé", "Rio Mississippi"],
        "correct": 1
    },
    {
        "question": "Qual país é conhecido como a 'Terra do Sol Nascente'?",
        "options": ["China", "Coreia do Sul", "Japão", "Vietnã"],
        "correct": 2
    },
    {
        "question": "Qual é o maior continente em área terrestre?",
        "options": ["África", "América do Norte", "Ásia", "Europa"],
        "correct": 2
    },
    {
        "question": "Qual estreito separa a Europa da África?",
        "options": ["Estreito de Bering", "Estreito de Magalhães", "Estreito de Gibraltar", "Estreito de Malaca"],
        "correct": 2
    },
    {
        "question": "Qual é o país com a maior população do mundo?",
        "options": ["Índia", "Estados Unidos", "China", "Indonésia"],
        "correct": 2
    },

    # Perguntas de Língua Portuguesa
    {
        "question": "Qual das palavras abaixo é um substantivo próprio?",
        "options": ["mesa", "cachorro", "Brasil", "flor"],
        "correct": 2
    },
    {
        "question": "Qual é o plural de 'pão'?",
        "options": ["pães", "pãos", "panos", "pões"],
        "correct": 0
    },
    {
        "question": "Qual figura de linguagem é usada quando se diz 'O sol beijou a montanha'?",
        "options": ["Metáfora", "Personificação", "Comparação", "Hipérbole"],
        "correct": 1
    },
    {
        "question": "Qual é a classe gramatical da palavra 'rapidamente'?",
        "options": ["Adjetivo", "Substantivo", "Verbo", "Advérbio"],
        "correct": 3
    },
    {
        "question": "Qual das frases abaixo está no futuro do presente?",
        "options": ["Eu comi bolo.", "Eu como bolo.", "Eu comerei bolo.", "Eu comia bolo."],
        "correct": 2
    },
    {
        "question": "Qual é o antônimo de 'alegria'?",
        "options": ["felicidade", "tristeza", "euforia", "contentamento"],
        "correct": 1
    },
    {
        "question": "Qual o nome do sinal de pontuação usado para indicar uma pausa breve na leitura?",
        "options": ["Ponto final", "Ponto de interrogação", "Vírgula", "Ponto e vírgula"],
        "correct": 2
    },
    {
        "question": "Qual das palavras abaixo é um verbo na terceira pessoa do singular?",
        "options": ["corremos", "correu", "correram", "corro"],
        "correct": 1
    },
    {
        "question": "Qual é o coletivo de 'peixes'?",
        "options": ["cardume", "rebanho", "matilha", "enxame"],
        "correct": 0
    },
    {
        "question": "Qual das opções apresenta apenas palavras paroxítonas?",
        "options": ["café, cipó", "árvore, lâmpada", "mesa, casa", "abadá, sofá"],
        "correct": 2
    },

    # Perguntas de Filosofia
    {
        "question": "Qual filósofo grego é conhecido por sua frase 'Só sei que nada sei'?",
        "options": ["Platão", "Aristóteles", "Sócrates", "Heráclito"],
        "correct": 2
    },
    {
        "question": "Qual corrente filosófica defende que a razão é a principal fonte de conhecimento?",
        "options": ["Empirismo", "Racionalismo", "Existencialismo", "Ceticismo"],
        "correct": 1
    },
    {
        "question": "Quem é o autor da obra 'A República', que discute a ideia de uma sociedade ideal?",
        "options": ["Aristóteles", "Sócrates", "Platão", "Epicuro"],
        "correct": 2
    },
    {
        "question": "Qual conceito filosófico se refere à busca pelo sentido da vida e da existência humana?",
        "options": ["Metafísica", "Epistemologia", "Ética", "Existencialismo"],
        "correct": 3
    },
    {
        "question": "Qual filósofo iluminista defendeu a separação dos poderes (legislativo, executivo, judiciário)?",
        "options": ["Jean-Jacques Rousseau", "Voltaire", "John Locke", "Montesquieu"],
        "correct": 3
    },
    {
        "question": "Qual é a área da filosofia que estuda o conhecimento e como ele é adquirido?",
        "options": ["Ontologia", "Estética", "Epistemologia", "Lógica"],
        "correct": 2
    },
    {
        "question": "Quem foi o filósofo que disse 'Penso, logo existo'?",
        "options": ["Immanuel Kant", "René Descartes", "Baruch Spinoza", "Gottfried Leibniz"],
        "correct": 1
    },
    {
        "question": "Qual dos seguintes conceitos está mais associado ao utilitarismo?",
        "options": ["Dever moral", "Felicidade da maioria", "Livre-arbítrio", "Intuição"],
        "correct": 1
    },
    {
        "question": "Qual filósofo é conhecido por sua teoria das 'Ideias' ou 'Formas'?",
        "options": ["Sócrates", "Aristóteles", "Platão", "Tales de Mileto"],
        "correct": 2
    },
    {
        "question": "Qual ramo da filosofia se preocupa com o estudo da moral e dos valores?",
        "options": ["Política", "Estética", "Lógica", "Ética"],
        "correct": 3
    },

    # Perguntas de Literatura
    {
        "question": "Quem é o autor da obra 'Dom Casmurro'?",
        "options": ["José de Alencar", "Machado de Assis", "Carlos Drummond de Andrade", "Clarice Lispector"],
        "correct": 1
    },
    {
        "question": "Qual gênero literário se caracteriza pela narração de eventos fictícios, com personagens e enredo complexos?",
        "options": ["Poesia", "Teatro", "Romance", "Crônica"],
        "correct": 2
    },
    {
        "question": "Qual é a principal característica do movimento literário Romantismo?",
        "options": ["Valorização da razão", "Objetividade e realismo", "Subjetivismo e emoção", "Crítica social"],
        "correct": 2
    },
    {
        "question": "Quem escreveu 'O Cortiço'?",
        "options": ["Manuel Bandeira", "Álvares de Azevedo", "Aluísio Azevedo", "Graciliano Ramos"],
        "correct": 2
    },
    {
        "question": "Qual é o nome da figura de linguagem que consiste na repetição de sons vocálicos?",
        "options": ["Aliteração", "Assonância", "Onomatopeia", "Paralelismo"],
        "correct": 1
    },
    {
        "question": "Em qual período literário surgiu o Modernismo no Brasil?",
        "options": ["Século XVIII", "Século XIX", "Início do Século XX", "Final do Século XX"],
        "correct": 2
    },
    {
        "question": "Qual é a obra mais famosa de Miguel de Cervantes?",
        "options": ["Romeu e Julieta", "Dom Quixote", "Os Lusíadas", "A Divina Comédia"],
        "correct": 1
    },
    {
        "question": "Qual dos seguintes autores é conhecido por suas peças de teatro trágicas e cômicas?",
        "options": ["William Shakespeare", "Fernando Pessoa", "Jorge Amado", "Gabriel García Márquez"],
        "correct": 0
    },
    {
        "question": "Qual é o nome do movimento literário que valoriza a natureza, a vida no campo e a simplicidade?",
        "options": ["Barroco", "Arcadismo", "Realismo", "Simbolismo"],
        "correct": 1
    },
    {
        "question": "Quem é a autora de 'Vidas Secas'?",
        "options": ["Rachel de Queiroz", "Cecília Meireles", "Clarice Lispector", "Graciliano Ramos"],
        "correct": 3
    }
]
def obter_quiz_dados():
    """Retorna a lista completa de perguntas do quiz"""
    return quiz_dados

def obter_perguntas_aleatorias(num_perguntas=10):
    """Retorna uma lista aleatória de perguntas"""
    random.shuffle(quiz_dados)
    return quiz_dados[:num_perguntas]