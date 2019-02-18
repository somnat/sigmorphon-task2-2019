import os
import itertools as it
def preProcess(filename):
    fout = open('seq_train1.txt', 'a')
    fin = open(filename, 'r')
    rl, ll = [], []
    for line in fin:
        line = line.split("\t")
        if line[0].isdigit():
            rl.append(line[1])
            ll.append(line[2])
        else:
            fout.write(" ".join(rl) + "\t" + " ".join(ll))
            fout.write("\n")
            rl, ll = [], []

    fin.close()
    fout.close()

def getLemmaWord(filename):
    fin = open(filename, 'r')
    fout = open('lema_train1.txt', 'a')
    openlist = []
    for line in fin:
        line = line.lower()
        line = line.split("\t")
        inp = line[0].strip().split()
        tar = line[1].strip().split()
        if len(inp) == len(tar):
            for i in range(len(inp)):
                if inp[i] != tar[i]:
                    fout.write(inp[i] + "\t" + tar[i])
                    fout.write("\n")
        else:
            print("error, input and target length are not equal")
    fin.close()
    fout.close()

def preProcessAll(inputdir):
    for r, d, f in os.walk(inputdir):
        for file in f:
            if "train" in file:
                f = os.path.join(r, file)
                preProcess(f)
