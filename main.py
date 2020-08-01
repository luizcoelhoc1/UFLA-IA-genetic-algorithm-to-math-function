import random 

# Argumentos 
txMutation = 1#%
txCrossover = 60#%
txMortalidade = 50#%
qttyGen = 5
qttyPointCrossOver = 1
qttyInit = 5

"""
classe individuo que representa uma solução do problema 
"""
class Individual:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes #chromosomes responsável pelo fenótipo do individuo (cadeia de bool em complemento de 2 no caso)
        self.size = len(self.chromosomes) #tamanho do cromossomo
        self.x = self.toInt() #individuo em si na forma int para não precisar usar a função toInt toda vez que for necessário 
        self.fx = f(self.x)  #o quão bem o inbdividuo se adapta

        #se os cromossomos não são partes do individuo ele precisa mutar pra minimamente fazer sentido
        if not (self.x <= 10 and self.x >= -10):
            self.mutation()

    """
        Metodo que retorna o individuo em int considerando que os cromossomos são vetores binários na forma de complemento de 2
    """
    def toInt(self):
        signal = self.chromosomes[0]
        return ((listToInt([not gene for gene in self.chromosomes]) + 1) * -1) if signal else listToInt(self.chromosomes)

    """
        Método responsável pela mutação de 1 gene aleatorio ou mais caso o gene mutado não faça sentido para o problema
    """
    def mutation(self):
        # Primeira mutação
        i = random.randint(0, self.size-1)
        self.chromosomes[i] = not self.chromosomes[i] 
        self.x = self.toInt()

        # Caso a mutação inicial do individuo deixe-o de continuar a exisitr muta de novo até 
        while (not (self.x <= 10 and self.x >= -10)):
            i = random.randint(0, self.size-1)
            self.chromosomes[i] = not self.chromosomes[i] 
            self.x = self.toInt()

        # Acerta o fx
        self.fx = f(self.x)

    """
        Método de crossover de dois individuos considerando qttyPointCrossOver como quantidade cortes nos cromossomos dos pais
    """
    def crossover(self, anotherParent):
        #pega a lista de cortes aleatorio e as ordena
        listCuts = [0, self.size]
        for i in range(qttyPointCrossOver):
            cut = random.randint(1, self.size-1)
            while cut in listCuts:
                cut = random.randint(1, self.size-1)
            listCuts.append(cut)
        listCuts.sort()

        #corta os cromossomos dos pais 
        piecesOfChromosomes = []
        for i in range(len(listCuts)-1):
            piecesOfChromosomes.append((self.chromosomes[listCuts[i]:listCuts[i+1]], anotherParent.chromosomes[listCuts[i]:listCuts[i+1]]))

        #escolhe os cromossomos do filho
        sonChromosomes = []
        for pieceSelf, pieceAnother in piecesOfChromosomes:
            sonChromosomes += pieceSelf if bool(random.getrandbits(1)) else pieceAnother
        return Individual(sonChromosomes)
     
    def __str__(self):
        r = '"'
        for gene in self.chromosomes:
            r += str(int(gene))
        r += " " + str(self.x)
        return r + '"'

    def __repr__(self):
        return self.__str__()
"""
Função para conversão de cadeia de bool para int
"""
def listToInt(l):
    r = 0
    index = 0
    for item in reversed(l):
        r +=  int(item) * 2 ** index
        index += 1
    return r

"""
Função responsável por gerar chromossomos aleatoriamentes
"""
def randomChromosomes(size):
    chromosomes = []
    for i in range(size):
        chromosomes.append(bool(random.getrandbits(1)))
    return chromosomes

"""
Função objetivo
"""
def f(x):
    return x*x - 3*x + 4

"""
Função responsável por executar uma função lambda em probability vezes
"""
def runOnProbability(probability, fun):
    aux = probability
    while random.randint(1,100) <= aux:
        fun()
        aux -= 100

# Geração da população inicial
population = []
while(len(population) != qttyInit):
    population.append(Individual(randomChromosomes(5)))
totalPopulationSum = sum(i.fx for i in population)

# Passagem do tempo entre as gerações
for gen in range(qttyGen):
    newGen = []
    for individual in population:
        #mutação
        runOnProbability(txMutation, lambda:
            individual.mutation()
        )

        #  Crossover txCrossovervezes
        runOnProbability(txCrossover, lambda:
            # Adiciona a nova geração o filho do individuo com outro parente aleatorio escolhido baseado na força de adaptação dos participantes da população, excluindo o individuo de ser o outro parente
            newGen.append(
                random.choices(
                    population,
                    weights=[i.fx/totalPopulationSum if not i.x==individual.x else 0 for i in population]
                )[0]
            )
        )

        # Adiciona o individuo na nova geração
        newGen.append(individual)

    # Torneio que mata a taxa de mortalidade vezes participantes fazendo-os disputar com outro participante
    qntDeath = int(len(newGen)*(txMortalidade/100))
    for i in range(qntDeath):
        # Escolhe dois participantes aleatorios com peso na fraca força de adaptação dos participantes
        fighter1 = random.choices(newGen, weights=[1-i.fx/totalPopulationSum for i in newGen])[0]
        fighter2 = random.choices(newGen, weights=[1-i.fx/totalPopulationSum if not i.x==fighter1.x else 0 for i in newGen])[0]
        if fighter1.fx > fighter2.fx:
            newGen.remove(fighter2)
        else: 
            newGen.remove(fighter1)

    # Próxima geração
    population = newGen
    totalPopulationSum = sum(i.fx for i in population)

# Rankea os individuos pelos indices
population = sorted(population, key=lambda x: x.fx, reverse=True)

print("População final:")
print(population)
print("Melhor individuo:")
print(population[0])
