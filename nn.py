import random

data = [0, 1, 0]

nodes = 3 #中間層のノード数
layers = 1 #中間層の層数

outputs = 3 #出力層のノード数

weightdata = [random.choice(range(-10, 10)) / 10 for i in range(len(data) * nodes + nodes * nodes * (layers - 1) + nodes * outputs)]
biasdata = [random.choice(range(-10, 10)) / 10 for i in range(nodes * layers + outputs)]

print(weightdata, biasdata)

for layer in range(layers):
    offset = layer * nodes
    data = [[datum * weight for datum, weight in zip(data, weightdata[offset * nodes + len(data) * node : offset * nodes + len(data) * (node + 1)])] for node in range(nodes)]
    data = [sum(datum) + biasdata[offset + node] if sum(datum) + biasdata[offset + node] > 0 else 0 for node, datum in enumerate(data)]
    print(data)

offset = layers * nodes
data = [[datum * weight for datum, weight in zip(data, weightdata[offset * nodes + len(data) * node : offset * nodes + len(data) * (node + 1)])] for node in range(outputs)]
data = [1 if sum(datum) + biasdata[offset + node] > 0 else 0 for node, datum in enumerate(data)]

print(data)