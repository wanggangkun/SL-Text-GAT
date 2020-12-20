#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from random import shuffle

text = []
labels = []
vocab = {}
min_freq = 5

with open("rt-polarity.neg", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text.append(line.strip())
        labels.append(str(0))
with open("rt-polarity.pos", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text.append(line.strip())
        labels.append(str(1))
index = []
for i in range(len(text)):
    index.append(i)
shuffle(index)
dataset_number = len(index)
train_size = int(dataset_number * 0.1)
dev_size = int(train_size * 0.1)
real_train_size = train_size - dev_size
print(real_train_size)
print(dev_size)
print(dataset_number)

for i in range(dataset_number):
    words = text[index[i]].split()
    for word in words:
        if word in vocab:
            count = vocab[word]
            vocab[word] = count+1
        else:
            vocab[word] = 1
with open("../vocab-5.txt", 'w', encoding='utf-8') as f:
    for key, value in vocab.items():
        if value > min_freq:
            f.writelines(key + '\n')
with open("../mr-all-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(dataset_number):
        f.writelines(labels[index[i]]+"\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_freq:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../mr-train-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_freq:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../mr-dev-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size, real_train_size+dev_size):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_freq:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../mr-test-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size+dev_size, dataset_number):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_freq:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
