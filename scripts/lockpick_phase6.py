import os

a=4
for b in range(1, 7):
    for c in range(1, 7):
        for d in range(1, 7):
            for e in range(1, 7):
                for f in range(1, 7):
                    if (os.system('echo "Public speaking is very easy.\n1 2 6 24 120 720\n1 b 214\n9\nopekmq\n%d %d %d %d %d %d\n" | ./bomb' % (a, b, c, d, e, f)) != 2048):
                        print("Numbers: %d %d %d %d %d %d" % (a, b, c, d, e, f))
