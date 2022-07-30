import kociemba as kc

U = '红橙橙橙橙橙橙红红'
R = '绿蓝蓝蓝蓝蓝蓝蓝蓝'
F = '绿绿白白白白黄白白'
D = '红红红红红红橙橙橙'
L = '黄绿黄绿绿绿绿黄蓝'
B = '黄黄绿黄黄黄白白白'


cubdict = {U[4]: 'U', R[4]: 'R', F[4]: 'F', D[4]: 'D', L[4]: 'L', B[4]: 'B'}
UC = ''
for s in [U, R, F, D, L, B]:
    for i in range(9):
        UC = UC + cubdict[s[i]]
print(UC)
print(kc.solve(UC))
