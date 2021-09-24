from sys import stdin, stdout

n_lines = int(stdin.readline())
for ln in range(n_lines):
    b = stdin.readline()
    bint = int(b)
    p_flag = False
    m2 = (bint & 1) == 0
    m5 = b[-2] in '05'
    m3 = bint%3 == 0
    m4 = bint%4 == 0 if m2 else 0
    m6 = bint%6 == 0 if m3 else 0
    f_string = ' '.join(f'{n+2}' for n, m in enumerate((m2, m3, m4, m5, m6)) if m)
    stdout.write(f_string + ('-1' * f_string!='') + '\n')
