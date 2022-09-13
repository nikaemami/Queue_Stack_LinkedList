n = int(input())
address = []
pattern = []
for r in range(2*n):
    if (r % 2 == 0):
        address.append(input())
    else:
        pattern.append(input())

def check_pattern(address, pattern, char_dict, i, j):
 
    if i == len(address) and j == len(pattern):
        return True

    if (len(address) < len(pattern)) or (i == len(address) or j == len(pattern)):
        return False
 
    current_char = pattern[j]
 
    if current_char in char_dict:
 
        str1 = char_dict[current_char]
        k = len(str1)
 
        if i + k >= len(address):
            str2 = address[i:]
        else:
            str2 = address[i:i + k]
            

        if str2 != str1:
            return False

        return check_pattern(address, pattern, char_dict, i + k, j + 1)

    k = 1
    while (k < len(address) - i + 1):
        char_dict[current_char] = address[i:i + k]
 
        if check_pattern(address, pattern, char_dict, i + k, j + 1):
            return True

        char_dict.pop(current_char)
        k+=1 
 
    return False
 

for q in range (n):
    char_dict = {}
    i = j = 0

    if check_pattern(address[q], pattern[q], char_dict,i,j):
        print("Yes")
    else:
        print("No")