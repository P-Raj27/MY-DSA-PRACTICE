#URL Shortner
num=int(input())
string=""
code_string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
while(num>0):
    rem=num%62
    string=string+code_string[rem]
    num=num//62
print(string[::-1])
