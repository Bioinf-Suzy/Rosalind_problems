#subs 
with open('rosalind_subs.txt') as f:
    list = f.read().split()
string = list[0].strip()
substring = list[1].strip()
count = 0
positions = []
pos = ''
length = len(substring)
#print(length)
#print(substring)
#print(string)
for i in range(0, len(string)):
    #print(string[i:i+length])
    if string[i:(i+length)] == substring:
        count += 1
        positions.append(i)
        pos += str(i+1) + ' '
#print(count)
#print(positions)
print(pos)
