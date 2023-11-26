str1 = 'hello world uglly'
str2 = 'll'

len1 = len(str1)
len2 = len(str2)

match_pos = -1
for i in range(len1):
    k = i
    match_count = 0

    for j in range(len2):
        if(k < len1 and str1[k] == str2[j]):
            match_count += 1
        k += 1
    
    if(match_count == len2):
        match_pos = i
        break
        
print(match_pos)