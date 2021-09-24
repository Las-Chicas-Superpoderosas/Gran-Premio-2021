from sys import stdin, stdout


class Sub_Time:
    def __init__(self, time):
        h, m, s = time.split(':')
        self.time = float(s.replace(',', '.')) + (int(m) * 60) + (int(h) * 3600)

    def __str__(self):
        h = str(int(self.time // 36000)).zfill(2)
        m = str(int((self.time % 3600) // 60)).zfill(2)
        s = '%0.3f' % (self.time % 60)
        t_string = '%s:%s:%s' % (h, m, s.zfill(6))
        return t_string.replace('.', ',')


l1 = stdin.readline().split(" ")
n = int(l1[0])
time_2_add = float(l1[1].replace(',', '.'))
while True:
    line = stdin.readline()
    if not line:
       break
    if '-->' in line:
        beg, end = map(Sub_Time, line.split(' --> '))
        beg.time += time_2_add
        end.time += time_2_add
        stdout.write(f'{beg} --> {end}\n')
    else:
        stdout.write(line) 
