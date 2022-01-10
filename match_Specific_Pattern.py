def findSpecificPattern(Dict, pattern):
    #Code here
    def patternCreater(string):
        code="1"
        for i in range(len(string)):
        
            if(i>0):
            
                if (string[i]==string[i-1]):
                    code=code+"0"
                else:
                    code=code+"1"
        return code
    #pattern=input()
    pattern_code=patternCreater(pattern)
    #print(pattern_code)
    #string_list=(str(x) for x in input().split())
    similar_string_list=[]
    for i in Dict:
        if(patternCreater(i)==pattern_code):
            similar_string_list.append(i)
    return similar_string_list
