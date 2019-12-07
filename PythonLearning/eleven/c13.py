

def stepCnt():
    a = 0
    def addStep(x):
        a += x
        return a
    return addStep

f = stepCnt()

print(f(2))
