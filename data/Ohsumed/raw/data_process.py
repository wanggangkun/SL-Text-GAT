#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
from random import shuffle

text = []
labels = []
vocab = {}
min_fre = 5

for i in range(9):
    for _, _, doc in os.walk("training/C0{}".format(i+1)):
        for d in doc:
            with open("training/C0{}/{}".format(i+1, d), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                sen = ""
                for line in lines:
                    sen += line.strip()
                    break
                text.append(sen)
                labels.append(str(i))
for i in range(9, 23):
    for _, _, doc in os.walk("training/C{}".format(i+1)):
        for d in doc:
            with open("training/C{}/{}".format(i+1, d), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                sen = ""
                for line in lines:
                    sen += line.strip()
                    break
                text.append(sen)
                labels.append(str(i))
for i in range(9):
    for _, _, doc in os.walk("test/C0{}".format(i+1)):
        for d in doc:
            with open("test/C0{}/{}".format(i+1, d), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                sen = ""
                for line in lines:
                    sen += line.strip()
                    break
                text.append(sen)
                labels.append(str(i))
for i in range(9, 23):
    for _, _, doc in os.walk("test/C{}".format(i+1)):
        for d in doc:
            with open("test/C{}/{}".format(i+1, d), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                sen = ""
                for line in lines:
                    sen += line.strip()
                    break
                text.append(sen)
                labels.append(str(i))
index = []
for i in range(len(text)):
    index.append(i)
shuffle(index)
dataset_number = len(index)
train_size = int(dataset_number * 0.8)
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
        if value > min_fre:
            f.writelines(key + '\n')
with open("../Ohsumed-all-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(dataset_number):
        f.writelines(labels[index[i]]+"\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_fre:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../Ohsumed-train-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_fre:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../Ohsumed-dev-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size, real_train_size+dev_size):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_fre:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
with open("../Ohsumed-test-stemmed.txt", 'w', encoding='utf-8') as f:
    for i in range(real_train_size+dev_size, dataset_number):
        f.writelines(labels[index[i]] + "\t")
        t = []
        for j in text[index[i]].split():
            if vocab[j] > min_fre:
                t.append(j)
        f.writelines(" ".join(t) + '\n')
