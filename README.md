# SL-Text-GAT
Code for paper "Sentence Level Graph Attention Network for Semi-supervised Short Text Classification"
# Require
Python
PyTorch
stanfordcorenlp(choose)
# Reproducing Results
Take the Ohsumed dataset as an example, other datasets are similar.
```bash
cd data/Ohsumed/raw
python data_process.py
cd ../../..
ptrhon data_process.py
pyrhon train.py
# if you want to use self-training
python get_train_vocab.py
```