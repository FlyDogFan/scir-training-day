#!/usr/bin/env python
import sys

def read_instance(fp):
    sentence = []
    while True:
        line = fp.readline()
        if not line:
            yield sentence
            break

        line = line.strip()

        if len(line) == 0:
            yield sentence
            sentence = []
        else:
            sentence.append( line.split() )


def bi2words(chars,fpo):
    # insert your code here
    biSeq = []
    ans = ''
    for elem in chars:
        if elem[1] == 'B':
            if ans != '':
                biSeq.append(ans)
            ans = ''
            ans = ans + elem[0]
        elif elem[1] == 'I':
            ans = ans + elem[0]
    if ans != '':
        biSeq.append(ans)
    lenth = len(biSeq)
    i = 0
    for elem in biSeq:
        i = i+1
        if i == lenth:
            fpo.write(elem)
        else:
            fpo.write(elem + " ")
    fpo.write("\n")

if  __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    try:
        fpo = open(sys.argv[2], "w")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    for sentence in read_instance(fpi):
        bi2words(sentence,fpo)
