values = [100,150,180]#[int(i) for i in input('please enter positive comma separated values\n').split(',')]
C = 50
H = 30
for D in values:
    Q = [round(((2*C*D)/H)**0.5)]
print(Q,sep=',')
