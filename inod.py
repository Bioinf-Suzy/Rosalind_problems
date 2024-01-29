#inod                   
with open('rosalind_inod.txt', 'r') as f:
    leaves = int(f.readline().replace('\n', '').strip())
    
print(leaves - 2)  
