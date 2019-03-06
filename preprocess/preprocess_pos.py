import os

def preProcessPos(filename):
    fout = open('out_fifth_col.txt', 'a')
    fin = open(filename, 'r')
    #fin = open(filename, 'r', errors='ignore')
    count = 0
    for line in fin:
        count +=1
        line = line.strip().split("\t")
        if len(line) >=3:
            fout.write(line[1] + "\t" + line[5])
            fout.write("\n")
    fin.close()
    fout.close()

def preProcessAll(inputdir):
    for r, d, f in os.walk(inputdir):
        print(f)
        for file in f:
            if "train" in file:
                f = os.path.join(r, file)
                preProcessPos(f)

# inputdir = "E:\\Mani\\2019-master\\2019-master\\task2\\UD_Hindi-HDTB"
# preProcessAll(inputdir)
