import os
def preProcess(filename):
    fout = open('out.txt', 'a')
    fin = open(filename, 'r')
    for line in fin:
        line = line.strip().split("\t")
        if len(line) >=3:
            fout.write(line[1] + "\t" + line[2])
            fout.write("\n")
    fin.close()
    fout.close()

def preProcessAll(inputdir):
    for r, d, f in os.walk(inputdir):
        for file in f:
            if "train" in file:
                f = os.path.join(r, file)
                preProcess(f)
