# a=int(input())
# b=int(input())
# d=0
# while True:
#     d+=1
#     if d%a==0 and d%b==0:
#         print(d)
#         break

# n=int(input())
# f=1
# s=0
# for i in range (1, n+1):
#     f=f*i
#     s=f+s
# print(s)

# n=int(input())
# for i in range(1, n+1):
#     for k in range (1, i+1):
#         print (k, sep='', end='')
#     print(end='\n')

# n=int(input())
# s=0
# s = n * (1 + n) / 2
# for i in range(1, n):
#     k=int(input())
#     s=s-k
# print(s)

n=int(input())
i=1
while i**2 <= n:
    print(i**2)
    i=i+1
