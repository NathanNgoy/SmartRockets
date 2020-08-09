import random

class DNA:
    def __init__(self, genes = [], lifespan = 200):
        if genes:
            self.genes = genes
        else:
            self.genes = []
            # give random direction
            for i in range(lifespan):
                self.genes.append([random.randint(-1, 1), -random.randint(-1, 1)])
        
        # prevent out of range error
        self.genes.append([0,0])

    def crossover(self, partner):
        newdna = []
        mid = float(random.uniform(0, len(self.genes)))
        for i in range(len(self.genes)):
            if i > mid:
                newdna.append(self.genes[i])
            else:
                newdna.append(partner.genes[i])
        return DNA(newdna)

    def mutation(self):
        for i in range(len(self.genes)):
            if random.random() < 0.01:
                self.genes[i] = [random.randint(-1, 1), -random.randint(-1, 1)]