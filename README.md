# easynn
The codes used in [this post](https://qiita.com/m-dev672/items/5f388a32d3e301b40abf).

and

A modularized version of it.

## Usage

```python
import easynn

data = [[[1, 1], [0]], [[0, 0], [0]], [[1, 0], [1]], [[0, 1], [1]]]

nn = easynn.nn(1, 2, 1)
nn.train(1000, data)

result = nn.run([0, 1])
print(restlt)

nn.write('traindata.json')
```

```python
import easynn

nn = easynn.nn(1, 2, 1)
nn.read('traindata.json')

data = [[[1, 1], [0]], [[0, 0], [0]], [[1, 0], [1]], [[0, 1], [1]]]

result = nn.run([1, 1])
print(restlt)
```

```python
import easynn

def evformula(datum):
    if datum[0] == datum[1]:
        return 3
    else:
        return - 2

nn = easynn.nn(1, 2, 1)
nn.train(1000, data, evformula=evformula)

result = nn.run([0, 0])
print(restlt)

nn.write('traindata.json')
```