#extracting the dataset
x = ""
y = ""
dataset = open('dataset.txt')
for i in dataset:
    x += i.split()[0]
    y += i.split()[1]

print(x[0])
print(y[1])
