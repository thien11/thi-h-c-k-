name = input("Tên em là: ")
n=int(input("Nhập số nguyên dương: "))
S=0
temp=n
while(n>0):
    S=S+n%10
    n=n//10
print('Tổng các chữ số trong',temp,'là:',S)