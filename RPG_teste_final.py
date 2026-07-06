nome_personagem = input("Digite o nome do personagem: ")
nivel_personagem = int(input("Digite o nível do personagem: (1-20) "))
if nivel_personagem < 1 or nivel_personagem > 20:
 print("O nível do personagem deve estar entre 1 e 20.")
forca = float(input("Digite o estatus de força: "))
agilidade = float(input("Digite o estatus de agilidade: "))
constituicao = float(input("Digite o estatus de constituição: "))
inteligencia = float(input("Digite o estatus de inteligência: "))
vigor = float(input("Digite o estatus de vigor: "))
energia = float(input("Digite o estatus de energia: "))

soma_estatus = forca + agilidade + constituicao + inteligencia + vigor + energia

if forca < 0 or agilidade < 0 or constituicao < 0 or inteligencia < 0 or vigor < 0 or energia < 0:
    print("Os valores não podem ser negativos.")

    if nivel_personagem == 1:
     soma_estatus_maxima = 11
    elif nivel_personagem == 2:
     soma_estatus_maxima = 14
    elif nivel_personagem == 3:
     soma_estatus_maxima = 17
    elif nivel_personagem == 4:
     soma_estatus_maxima = 20
    elif nivel_personagem == 5:
     soma_estatus_maxima = 23
    elif nivel_personagem == 6:
     soma_estatus_maxima = 26
    elif nivel_personagem == 7:
     soma_estatus_maxima = 29
    elif nivel_personagem == 8:
     soma_estatus_maxima = 32
    elif nivel_personagem == 9:
     soma_estatus_maxima = 35
    elif nivel_personagem == 10:
     soma_estatus_maxima = 38
    elif nivel_personagem == 11:
     soma_estatus_maxima = 41
    elif nivel_personagem == 12:
     soma_estatus_maxima = 44
    elif nivel_personagem == 13:
     soma_estatus_maxima = 47
    elif nivel_personagem == 14:
     soma_estatus_maxima = 50
    elif nivel_personagem == 15:
     soma_estatus_maxima = 53
    elif nivel_personagem == 16:
     soma_estatus_maxima = 56
    elif nivel_personagem == 17:
     soma_estatus_maxima = 59
    elif nivel_personagem == 18:
     soma_estatus_maxima = 62
    elif nivel_personagem == 19:
     soma_estatus_maxima = 65
    elif nivel_personagem == 20:
     soma_estatus_maxima = 68

else:
    print("\nEstatus do personagem:", nome_personagem)
    print("Força:", forca)
    print("Agilidade:", agilidade)
    print("Constituição:", constituicao)
    print("Inteligência:", inteligencia)
    print("Vigor:", vigor)
    print("Energia:", energia)

    if forca >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Golpe extremo!")
    if agilidade >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Esquiva perfeita!")
    if constituicao >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Resistência inabalável!")
    if inteligencia >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Conhecimento avançado!")
    if vigor >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Energia vital!")
    if energia >= 15:
        print("O ", nome_personagem, "desbloqueou a habilidade: Magia poderosa!")

numero_pericias = 5

pericias_lista = ["Percepção", "Investigação", "Investigação", "Fortitude", "Cura", "Luta", "Reflexos", "Iniciativa", "Misticismo", "Pontaria", "Atletismo", "Acrobacia", "História", "Enganação", "Prestidigitação", "Sobrevivência", "Intimidação", "Diplomacia", "Vontade", "Ciências", "Religião"]

print("\nPerícias disponíveis:")
print("1. Percepção")
print("2. Investigação")
print("3. Fortitude")
print("4. Cura")
print("5. Luta")
print("6. Reflexos")
print("7. Iniciativa")
print("8. Misticismo")
print("9. Pontaria")
print("10. Atletismo")
print("11. Acrobacia")
print("12. História")
print("13. Enganação")
print("14. Prestidigitação")
print("15. Sobrevivência")
print("16. Intimidação")
print("17. Diplomacia")
print("18. Vontade")
print("19. Ciências")
print("20. Religião")

pericias = input("Selecione as perícias do personagem (1-20): ")
pericias_selecionadas = [int(x) for x in pericias.split(",") if x.isdigit() and 1 <= int(x) <= 20]
pericias_lista = [pericias_lista[i - 1] for i in pericias_selecionadas]


n_treinado = "+0"
treinado = "+5"
veterano = "+10"
expert = "+20"

pericias_bonus = {}
for pericia in pericias_lista:
    nivel = input(f"Digite o nível da perícia {pericia} (n_treinado(n), treinado(t), veterano(v), expert(e)): ").lower()
    if nivel == "n":
        pericias_bonus[pericia] = n_treinado
    elif nivel == "t":
        pericias_bonus[pericia] = treinado
    elif nivel == "v":
        pericias_bonus[pericia] = veterano
    elif nivel == "e":
        pericias_bonus[pericia] = expert
    else:
        print(f"Nível inválido para a perícia {pericia}. Nenhum bônus será aplicado.")

print("Perícias do personagem:", pericias_lista)
print("Bônus das perícias:", pericias_bonus)

origens = ["cientista", "marinheiro", "psicologo", "professor", "militar", "paramedico", "agiota", "duble", "ex-presidiario", "historiador", "famoso", "cacador", "engenheiro"]

print("\nOrigens disponíveis:")
print("1. Cientista")
print("2. Marinheiro")
print("3. Psicólogo")
print("4. Professor")
print("5. Militar")
print("6. Paramédico")
print("7. Agiota")
print("8. Duble")
print("9. Ex-Presidiário")
print("10. Historiador")
print("11. Famoso")
print("12. Caçador")
print("13. Engenheiro")

escolha_origem = int(input("Escolha a origem do personagem (1-13): ")) - 1
if 0 <= escolha_origem < len(origens):
    print(f"Origem selecionada: {origens[escolha_origem]}")
else:
    print("Origem inválida.")

selecao_energia = ["Ki", "Mana", "Chakara", "Reiatsu", "Enargia Amaldiçoada"]

descricao_energia = {
    "Ki": "Estatos bonus:[+1(VIG), +1(ENE)]: Ki é a energia vital do corpo. Vem do treino, da respiração e da força de vontade. Serve para fortalecer o corpo, deixar golpes mais fortes e melhorar o físico. Usar demais cansa o corpo.",
    "Mana": "Estatos bonus: [+1(INT), +1(ENE)] Mana é a energia mágica. Vem do espírito, do ambiente ou de fontes místicas. Serve para feitiços e poderes sobrenaturais. Usar demais esgota a mente.",
    "Chakara": "Estatos bonus: [+1(AGI), +1(ENE)] Chakra é a energia que surge da combinação da força física com a espiritual. Ela circula pelo corpo através dos canais de chakra e pode ser moldada para realizar técnicas especiais. Quem treina o chakra aprende a controlar seu fluxo, usando-o para aumentar força, velocidade, cura ou executar jutsus. Sem controle, ele se desperdiça e cansa o usuário rapidamente.",
    "Reiatsu": "Estatos bonus: [+1(CON), +1(ENE)] Reiatsu é a pressão espiritual liberada por alguém com grande energia espiritual. Ela pode ser sentida pelos outros como um peso opressor, capaz até de imobilizar, intimidar ou ferir quem é fraco demais para suportar. Quanto maior a reiatsu, maior a presença e o poder espiritual do usuário.",
    "Energia Amaldiçoada": "Estatos bonus: [+1(FOR), +1(ENE)] Energia Amaldiçoada é a força que nasce de emoções negativas, como ódio, medo e rancor. Ela é usada para técnicas amaldiçoadas e pode ferir espíritos e humanos. Quem controla essa energia transforma sentimentos ruins em poder — mas, sem controle, ela pode escapar e causar destruição." }

print("\nTipos de energia disponíveis:")
print("1. Ki")
print("2. Mana")
print("3. Chakara")
print("4. Reiatsu")
print("5. Energia Amaldiçoada")

selecionar_energia = int(input("Escolha o tipo de energia do personagem (1-5): ")) - 1
if 0 <= selecionar_energia < len(selecao_energia):
    energia_escolhida = selecao_energia[selecionar_energia]
    print(f"Tipo de energia selecionado: {energia_escolhida}")
    print("Descrição:", descricao_energia[energia_escolhida])  
else:
    print("Tipo de energia inválido.")

if energia_escolhida == "Ki":
    forca += 1
    energia += 1
elif energia_escolhida == "Mana":
    inteligencia += 1
    energia += 1
elif energia_escolhida == "Chakara":
    agilidade += 1
    energia += 1
elif energia_escolhida == "Reiatsu":
    constituicao += 1
    energia += 1
elif energia_escolhida == "Energia Amaldiçoada":
    forca += 1
    energia += 1

print("\nEstatus do personagem após bônus de energia:", nome_personagem)
print("Força:", forca)
print("Agilidade:", agilidade)
print("Constituição:", constituicao)
print("Inteligência:", inteligencia)
print("Vigor:", vigor)
print("Energia:", energia)

raças = ["Humanos", "Sayajin", "Meio Demônio", "Ghoul", "Oni", "Elfo", "Tritão", "Ciborgue", "Vampiro", "Hollow"]

descricao_raca = {
   "Humanos": "Vantagens: [Duas pericias treinadas, pericia percepção treinada, +1 ponto em um estatus a escolha do jogador]: Humanos são adaptáveis, aprendem rápido e servem pra qualquer classe. Não são extremos, mas evoluem bem e se viram em qualquer situação.",
   "Sayajin": "Vantagens: [Treinado nas pericias (Fortitude), (Luta) e (Reflexos) {Abilidades de raça: (Transformação: Super Sayajin: estatos bonus: [+5(FOR), +5(VIG), +5(CON)]) (Transformação: Super Sayajin 2: estatos bonus: [+10(FOR), +7(VIG), +7(CON) e +5(ENE)])(Transformação: Super Sayajin 3: estatos bonus: [+15(FOR), +10(VIG), +10(CON) e +7(ENE)])}] Sayajin é uma raça guerreira obcecada por luta. Ficam mais fortes após quase morrer, têm cauda, se transformam e escalam poder absurdamente conforme enfrentam inimigos mais fortes. Brutais e resistentes.",
   "Meio Demônio": "Vantagens: [Treinado nas pericias (Percepção), (Luta) e (Iniciativa) {Abilidades de raça: (Transformação: Incorporação Demoniaca: estatos bonus: [+5(FOR), +5(CON) e +5(AGI)} Arma Matadora de Inimigos: Quando chega no nível 10 e está incorporado, o jogador poderá escolher uma arma do seu gosto dentre a lista que o Mestre fazer, que será indestrutível.])  híbrido instável. Mistura humanidade com poder demoníaco, ganhando força, resistência e habilidades sobrenaturais, mas lutando contra impulsos violentos e perda de controle. Quanto mais poder usa, maior o risco de se perder para a escuridão.",
   "Ghoal": "Vantagens: [Treinado nas pericias (Furtividade),  (Percepção) e (Reflexos) {Abilidades de reça: (Trasformação: Kagune:  Kagune é um órgão predatório dos Ghouls, manifestado a partir das células RC (células especiais do universo de Tokyo Ghoul), que se projeta do corpo como uma arma viva(a partir do LV 5) . Saber mais na Página 5., Armadura de Células: Podem endurecer as células RC para formar uma cobertura corporal resistente, como armaduras. Quando ativada por três turno o usuário tomara -1d10 de dano podendo aumentar ou diminuir dependendo de sua Kagune.]) Ghouls são humanos corrompidos por energia sombria. Precisam se alimentar de carne humana, possuem força e regeneração acima do normal e vivem à margem da sociedade, sempre lutando contra a própria fome.", 
   "Oni": "Vantagens: [Treinado nas pericias (Fortitude), (Reflexos) e (Iniciativa).(Abilidades de raça: Demon Art: Demon Art é uma técnica demoníaca que usa energia sombria para criar habilidades sobrenaturais. Saber mais na Página 5., Regeneração de Sangue: O jogador pode regenerar seu CON com isso, porém ficará mais fraco, porém só pode usar 3 vezes na batalha.Recupera 20 de vida, perdendo -2(FOR) e -2(VIG) sempre que usar. )] Onis são demônios de força bruta. Corpos monstruosos, resistência absurda e poder físico esmagador. Vivem para o combate e destruição, confiando mais na força do que em estratégia.",
   "Elfo": "Vantagens: [Treinado nas pericias (Misticismo), (Percepção) e (Cura) {Abilidades de raça: Talento Mágico: Facilidade em aprender magias e usar magias, deixando o testes que envolvem magias mais fáceis.+2 em testes que envolvem magias e +1(ENE)., Longevidade: Elfos tem uma expectativa de 1 milênio de vida, então o jogador poderá ter mais de 100 anos fácil., Afinidade com Espirito: Por terem crescido em um ambiente espiritual tem maior facilidade em fazer contrato com espíritos.}] Elfos são ágeis e longevos. Especialistas em magia, precisão e furtividade. Corpo frágil, mas sentidos aguçados e grande controle espiritual.",
   "Tritão": "Vantagens: [Treinado nas pericias (Luta), (Iniciativa) e (Fortitude) {Abilidades de raça: Postura Imóvel: Tritões tem uma base firme e controle de corpo, então será difícil de deslocar ele do lugar e difícil de desarmar.Para desarmar tem que fazer um teste 3d20 e tem que tirar 17+ e para conseguir deslocar ele do lugar será um 3d20 tendo que tirar 19+., Pele Impenetrável: Sua pele fica mais forte e reduz o dano levado.Quando ativo -50 porcento de dano no ataque e só pode ativar a cada 4 turnos de ação., Brânquias: Permite respirar o oxigênio dissolvido na água.}] Tritões são humanoides aquáticos endurecidos por sofrimento físico e mental. Têm Fortitude alta, resistência absurda e excelente combate na água. Usam pouca magia e são fracos nesse aspecto, confiando mais no corpo e na disciplina.",
   "Ciborgue": "Vantagens: [Treinado nas pericias (Luta), (Percepção) e (Pontaria) {Abilidades de raça: Scanner: Os olhos emitem um feixe azul que varre o local, coletando vestígios físicos e energéticos como sangue, digitais, impactos, calor e objetos fora do lugar. O sistema analisa os dados e projeta um holograma que reconstrói o que aconteceu, identificando quem esteve ali e mostrando suas ações., Raio Ômega: um feixe de energia disparado pela mão, em linha reta, com alto dano, consome muita energia.2d14 de dano e -25 porcento da sua energia.}] Ciborgues são humanos aprimorados por tecnologia. Corpo reforçado, sentidos ampliados e habilidades mecânicas únicas. Dependem de manutenção e energia, mas compensam com força, resistência e precisão sobre-humanas.",
   "Vampiro": "Vantagens: [Treinado nas pericias (Furtividade), (Reflexos) e (Iniciativa) {Abilidades de raça: Vampirismo: Quando o Vampiro ataca um ser vivo com armas de corte de curto alcance, ele pode recupera sua energia vital, podendo recuperar 1d6 de vida ou 1d10 de energia., Mestre do sangue: Vampiros podem controlar sangue podendo usa-lo para cura de si próprio ou de aliados 2d8 de cura ou usando em forma de ataque em forma de balas de sangue 2d10 de dano}] Vampiros são predadores noturnos. Força, velocidade e regeneração elevadas, sentidos aguçados e poderes sombrios. Dependem de sangue para sobreviver e sofrem com luz solar e fogo.",
   "Hollow": "Vantagens: [Treinado nas pericias (Fortitude), (Misticismo) e (Luta) {Abilidades de raça: Cero: Cero é um raio de energia espiritual dos Hollows, eles juntam reiatsu e disparam um feixe vermelho super destrutivo com 2d15 de dano (a partir do LV 5) . Só os fortes usam., Evolução: Os Hollows começam como Gillian, gigantes e quase sem consciência. Alguns evoluem para Adjuchas, menores, inteligentes e bem mais fortes. Pouquíssimos chegam a Vasto Lorde, que são raros, com forma quase humana e poder extremo — o topo da hierarquia (Saiba mais na página 3).}] Hollow são criaturas espirituais corrompidas pelo vazio. Extremamente agressivos, possuem alto poder espiritual, máscaras que amplificam habilidades e fome constante por almas. Quanto mais consomem, mais fortes (e menos conscientes) se tornam."}
   
print("\nRaças disponíveis:")
print("1. Humanos")
print("2. Sayajin")
print("3. Meio Demônio")
print("4. Ghoul")
print("5. Oni")
print("6. Elfo")
print("7. Tritão")
print("8. Ciborgue")
print("9. Vampiro")
print("10. Hollow")

escolha_raca = int(input("Escolha a raça do personagem (1-10): ")) - 1
if 0 <= escolha_raca < len(raças):
    print(f"Raça selecionada: {raças[escolha_raca]}")
    print("Descrição:", descricao_raca[raças[escolha_raca]])
else:
    print("Raça inválida.")

bonus_raca = {
    "Humanos": {
        "pericias_bonus": ["Perícia1", "Perícia2"],  # adjust as needed
        "pericia_percepcao_bonus": 1,
        "estatus_bonus": 1
    },
    "Sayajin": {
        "pericias_bonus": ["Fortitude", "Luta", "Reflexos"],
        "habilidades_raca": [
            "Transformação: Super Sayajin",
            "Transformação: Super Sayajin 2",
            "Transformação: Super Sayajin 3"
        ]
    },
    "Meio Demônio": {
        "pericias_bonus": ["Percepção", "Luta", "Iniciativa"],
        "habilidades_raca": [
            "Transformação: Incorporação Demoniaca",
            "Arma Matadora de Inimigos"
        ]
    },
    "Ghoul": {
        "pericias_bonus": ["Furtividade", "Percepção", "Reflexos"],
        "habilidades_raca": ["Trasformação: Kagune", "Armadura de Células"]
    },
    "Oni": {
        "pericias_bonus": ["Fortitude", "Reflexos", "Iniciativa"],
        "habilidades_raca": ["Demon Art", "Regeneração de Sangue"]
    },
    "Elfo": {
        "pericias_bonus": ["Misticismo", "Percepção", "Cura"],
        "habilidades_raca": ["Talento Mágico", "Longevidade", "Afinidade com Espirito"]
    },
    "Tritão": {
        "pericias_bonus": ["Luta", "Iniciativa", "Fortitude"],
        "habilidades_raca": ["Postura Imóvel", "Pele Impenetrável", "Brânquias"]
    },
    "Ciborgue": {
        "pericias_bonus": ["Luta", "Percepção", "Pontaria"],
        "habilidades_raca": ["Scanner", "Raio Ômega"]
    },
    "Vampiro": {
        "pericias_bonus": ["Furtividade", "Reflexos", "Iniciativa"],
        "habilidades_raca": ["Vampirismo", "Mestre do sangue"]
    },
    "Hollow": {
        "pericias_bonus": ["Fortitude", "Misticismo", "Luta"],
        "habilidades_raca": ["Cero", "Evolução"]
    }
}

pericia_bonus_raca = bonus_raca[raças[escolha_raca]]["pericias_bonus"]
pericia_final = list(set(pericias_lista + pericia_bonus_raca))
print("\nPerícias finais do personagem:", pericia_final)

classes = ["Pirata", "Guerreiro", "Ninja", "Cavaleiro Magico", "Herói", "Caçador", "Cienceiro", "Fenticeiro", "Ceifador", "Assassino", "Mago", "Lutador de artes marciais", "Shinigami", "Quincy", "Mentalista", "Sacerdote", "Mestre de Barreiras", "Invocador"]
   
if escolha_raca == 9:
   
  evolucao_hollow = ["Gillian", "Menos Grande", "Adjuchas", "Vasto Lorde"]
  
  print("\nEvoluções disponíveis para Hollow:")
  print("1. Gillian")
  print("2. Menos Grande")
  print("3. Adjuchas")
  print("4. Vasto Lorde")
  
  escolha_evolucao_hollow = int(input("Escolha a etapa da evolução do hollow: (1-4) ")) - 1
  if 0 <= escolha_evolucao_hollow < len(evolucao_hollow):
    print(f"A evolução wollow swlwcionada: {evolucao_hollow[escolha_evolucao_hollow]}")
  else:
    print("Evolução Hollow invalida.")

  print("\nClasses disponiveis para Hollows:")
  print("1. Pirata")
  print("2. Guerreiro")

  escolha_classe = int(input("Escolha a classe do personagem. (1-2): ")) - 1
  if 0 <= escolha_classe < len(classes):
    print(f"A classe selecionada: {classes[escolha_classe]}")
  else:
    print("Classe invalida.")

else:
 print("\nNenhuma evolução disponível para a raça selecionada.")

 print("\nClasses disponíveis:")
 print("1. Pirata")
 print("2. Guerreiro")
 print("3. Ninja")
 print("4. Cavaleiro Mágico")
 print("5. Herói")
 print("6. Caçador")
 print("7. Cientista")
 print("8. Feiticeiro")
 print("9. Ceifador")
 print("10. Assassino")
 print("11. Mago")
 print("12. Lutador de Artes Marciais")
 print("13. Shinigami")
 print("14. Quincy")
 print("15. Mentalista")
 print("16. Sacerdote")
 print("17. Mestre de Barreiras")
 print("18. Invocador")

 escolha_classe = int(input("Escolha a classe do personagem. (1-18): ")) - 1
 if 0 <= escolha_classe < len(classes):
    print(f"A classe selecionada: {classes[escolha_classe]}")
 else:
    print("Classe invalida.")

if escolha_raca == 9:
   
   print("\nficha_final:")
   print("Nome: ", nome_personagem, " Rassa: ", {raças[escolha_raca]}, " ", {evolucao_hollow[escolha_evolucao_hollow]}, " Classe: ", {classes[escolha_classe]})
   print ("\nEstatos do Personagem:")
   print("Força:", forca)
   print("Agilidade:", agilidade)
   print("Constituição:", constituicao)
   print("Inteligência:", inteligencia)
   print("Vigor:", vigor)
   print("Energia:", energia)
   print("\nPericias do Personagem:")
   print(pericia_final)
else:
   print("\nficha_final:")
   print("Nome: ", nome_personagem, " Rassa: ", {raças[escolha_raca]}, " Classe: ", {classes[escolha_classe]})
   print ("\nEstatos do Personagem:")
   print("Força:", forca)
   print("Agilidade:", agilidade)
   print("Constituição:", constituicao)
   print("Inteligência:", inteligencia)
   print("Vigor:", vigor)
   print("Energia:", energia)
   print("\nPericias do Personagem:")
   print(pericia_final)