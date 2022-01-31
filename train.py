import random

correctdata = [[0, 1], [1, 0]]
incorrectdata = [[1, 1], [0, 0]]

nodes = 2 #中間層のノード数
layers = 1 #中間層の層数

outputs = 1 #出力層のノード数

best = {'evaluation': 0, 'weightdata': [], 'biasdata': []} #評価が一番高い重み・バイアスの値を格納する辞書

for cycle in range(300):
    evaluation = 0 #評価値
    weightdata = [random.choice(range(-10, 10)) / 10 for i in range(len(correctdata[0]) * nodes + nodes * nodes * (layers - 1) + nodes * outputs)]
    biasdata = [random.choice(range(-10, 10)) / 10 for i in range(nodes * layers + outputs)]
    for data in correctdata + incorrectdata:
        initialdata = data
        for layer in range(layers):
            offset = layer * nodes
            data = [[datum * weight for datum, weight in zip(data, weightdata[offset * nodes + len(data) * node : offset * nodes + len(data) * (node + 1)])] for node in range(nodes)]
            data = [sum(datum) + biasdata[offset + node] if sum(datum) + biasdata[offset + node] > 0 else 0 for node, datum in enumerate(data)]

        offset = layers * nodes
        data = [[datum * weight for datum, weight in zip(data, weightdata[offset * nodes + len(data) * node : offset * nodes + len(data) * (node + 1)])] for node in range(outputs)]
        data = [1 if sum(datum) + biasdata[offset + node] > 0 else 0 for node, datum in enumerate(data)]

        if initialdata in correctdata and data[0] == 1:
            evaluation += 1
        elif initialdata in incorrectdata and data[0] == 0:
            evaluation += 1
        else:
            evaluation -= 1

    if evaluation > best['evaluation']:
        best = {'evaluation': evaluation, 'weightdata': weightdata, 'biasdata': biasdata}

print(best)