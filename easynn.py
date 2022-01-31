import json
import random

class nn:
    def __init__(self, nodes, layers, outputs):
        self.evaluation = 0
        self.nodes = nodes
        self.layers = layers
        self.outputs = outputs

    def read(self, path):
        with open(path) as f:
            df = json.load(f)
        self.evaluation = df['evaluation']
        self.weightdata = df['weightdata']
        self.biasdata = df['biasdata']

    def relu(v):
        return v if v > 0 else 0

    def step(v):
        return 1 if v > 0 else 0

    def run(self, data, weightdata = None, biasdata = None, activef1 = relu, activef2 = step):
        weightdata = weightdata if weightdata else self.weightdata
        biasdata = biasdata if biasdata else self.biasdata
        for layer in range(self.layers):
            offset = layer * self.nodes
            data = [[datum * weight for datum, weight in zip(data, weightdata[offset * self.nodes + len(data) * node : offset * self.nodes + len(data) * (node + 1)])] for node in range(self.nodes)]
            data = [activef1(sum(datum) + biasdata[offset + node]) for node, datum in enumerate(data)]
        
        offset = self.layers * self.nodes
        data = [[datum * weight for datum, weight in zip(data, weightdata[offset * self.nodes + len(data) * node : offset * self.nodes + len(data) * (node + 1)])] for node in range(self.outputs)]
        data = [activef2(sum(datum) + biasdata[offset + node]) for node, datum in enumerate(data)]
        return data

    def normalize(data):
        m = max([max(datum[0]) for datum in data])
        return [[[d / m for d in datum[0]]] + datum[1:] for datum in data]

    def genweightdata(length):
        return [random.choice(range(-10, 10)) / 10 for i in range(length)]

    def genbiasdata(length):
        return [random.choice(range(-10, 10)) / 10 for i in range(length)]

    def evformula(datum):
        if datum[0] == datum[1]:
            return 1
        else:
            return - 1

    def train(self, cycles, data, genweightdata = genweightdata, genbiasdata = genbiasdata, evformula = evformula, normalize = normalize):
        data = normalize(data) if normalize else data
        for cycle in range(cycles):
            evaluation = 0
            weightdata = genweightdata(max([len(datum[0]) for datum in data]) * self.nodes + self.nodes * self.nodes * (self.layers - 1) + self.nodes * self.outputs)
            biasdata = genbiasdata(self.nodes * self.layers + self.outputs)
            for datum in data:
                datum = [self.run(datum[0], weightdata, biasdata)] + datum[1:]
                evaluation += evformula(datum)
            if evaluation > self.evaluation:
                self.evaluation = evaluation
                self.weightdata = weightdata
                self.biasdata = biasdata

    def write(self, path):
        d = {'evaluation': self.evaluation, 'weightdata': self.weightdata, 'biasdata': self.biasdata}
        with open(path, 'w') as f:
            json.dump(d, f)