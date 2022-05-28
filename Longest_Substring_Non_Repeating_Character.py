#Using kdane's algo for longest substring wwith no repeating character.
string="geeksforgeeks"
#temp_string=""
max_length=0
seen={}
start=0
for end in range(len(string)):
    if string[end] in seen:
        start=max(start,seen[string[end]]+1)
        
    max_length=max(max_length,end-start+1)
    seen[string[end]]=end
print(max_length)
    
    
    
    
