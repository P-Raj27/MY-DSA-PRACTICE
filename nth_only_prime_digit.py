def code_converter(num):
    string=""
    while(num>0):
        rem=num%4
        string=string+str(rem)
        if(rem==0):
            num=num-1
        num=num//4
    return string[::-1]
if __name__=="__main__":
    number=int(input())
    final_number=""
    dic={"1":"2","2":"3","3":"5","0":"7"}
    code=code_generator(number)
    for i in code:
        final_number=final_number+dic[i]
    print(final_number)
        
