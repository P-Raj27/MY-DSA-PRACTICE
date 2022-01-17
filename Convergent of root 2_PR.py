numerator=3
denominator=2
count=0
for i in range(2,1001):
    temp_numerator=numerator+2*denominator
    denominator=numerator+denominator
    if(len(str(temp_numerator))>len(str(denominator))):
        count=count+1
    numerator=temp_numerator
    #print("Numerator is=",numerator," and denominator is",denominator)
print(count)
