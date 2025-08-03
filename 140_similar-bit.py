def solurion(n, l, r):
    bit = '1'
    
    cnt = 0
    while cnt < n:
        new_bit = ''
        for i in range(len(bit)):
            if bit[i] == '1':
                new_bit += '11011'
            else:
                new_bit += '00000'
        bit = new_bit
        cnt += 1
        
    return bit[l-1:r].count('1')
        