from subprocess import Popen, PIPE
from time import time

def refine(strs):
    replaces = ['\t', '\n']
    for i in replaces:
        strs = strs.replace(i,' ')

    escapes = ''.join([chr(char) for char in range(1, 32)])
    strs = strs.translate(None, escapes)

    return strs

finp = open('input.txt', 'r')
fout = open('output.txt', 'r')

inp = finp.read()
exout = fout.read()

pipes = Popen([r"C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\g++", "-o", "test", "test.c"], stdout=PIPE, stderr=PIPE, shell=True)
out,err = pipes.communicate()

if not err:
    pipes = Popen("test", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    start = time()
    out, err = pipes.communicate(input=inp)
    end = time() - start

    if not err:
        out = out[:-1]
        out = refine(out)
        exout = refine(exout)

        if out == exout:
            print "Your program gives correct output."
            print "The time taken is approx",round(end, 3),"sec."
        else:
            print "Your program does not give desired output."

    else:
        print "ERROR !!"
        print err
    
else:
    print "ERROR !!"
    print err
