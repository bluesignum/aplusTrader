# import win32com.client
# client=win32com.client.Dispatch("XA_Session.XASession")
# client.ConnectServer("demo.ebestsec.co.kr", 20001)

# import sys
# num = int(sys.stdin.readline().rstrip())
# for i in range(num):
#     x,y = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #{0}: {1} + {2} = {3}".format(i+1, x, y, x+y))
# num = int(input())
# for i in range(num):
#     x, y = map(int, input().split(","))
#     print(x+y)
import sys 

max_idx=-1
max_num=0
for i in range(9):
    new_num = int(sys.stdin.readline().rstrip())
    print(i)
    if new_num > max_num:
        max_num = new_num
        max_idx = i
print(max_num)
print(max_idx+1)

