import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
a_list = set()
flag = True

if len(num) > 2:
    for i in range(N-2):
        try:
            a_list.add((num[i+2] - num[i+1]) / (num[i+1] - num[i]))
        except:
            pass
else:
    if len(num) > 1 and num[0] == num[1]:
        a_list.add(1)
    else:
        flag = False

if flag:
    if len(a_list) > 1:
        print('B')
    else:
        a = a_list.pop()
        if a % 1:
            print('B')
        else:
            a = int(a)
            print(num[-1]*a+(num[-1]-num[-2]*a))
else:
    print('A')