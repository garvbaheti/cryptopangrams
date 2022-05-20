"""
Created on Sun May 8 18:00:10 2022

@author: Garv Baheti
"""
#before running code please install easygui
#please check the image directory >> C:/Users/Garv/OneDrive - JK LAKSHMIPAT UNIVERSITY/Documents/II - Year BTECH/DAA/Projectimg.png <<
# and replace it with yours
#for problem refer to https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#___________________________________________________________________________________________________________________#

import easygui

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cryptopangrams(X,Y):
    N, L = list(map(int, X.strip().split()))
    input_num = list(map(int, Y.strip().split()))
    actual_primes = set()

    for i in range(L-1):
        if input_num[i] == input_num[i+1]:
            continue
        p = gcd(input_num[i], input_num[i+1])
        actual_primes.add(p)
        actual_primes.add(input_num[i]//p)
        actual_primes.add(input_num[i+1]//p)
        
        if len(actual_primes) == 26:
            break
    
    str_array = {}
    sorted_primes = sorted(actual_primes)
    
    for i, p in enumerate(sorted_primes):
        str_array[p] = chr(ord('A')+i)
    
    for p in sorted_primes:
        result = [str_array[p]]
        for i in range(L):
            if input_num[i] % p != 0:
                break
            p = input_num[i]//p
            result.append(str_array[p])
        else:
            return "".join(result)
    return ""

while 1>0:
    msg="Hello Welcome To Decrypting Machine, would you like to Continue ?"
    title="Decrypting Machine - Welcome"
    choices=['Continue','Exit']
    myChoice=easygui.ynbox(msg,title,choices)
    
    if myChoice==1:
        # Welcome Window 
        msg4="Enter number of Encrypted Text You Want to Decrypt: "
        title4="Decrypting Machine - Cases"
        t=easygui.integerbox(msg4,title4,image='C:/Users/Garv/OneDrive - JK LAKSHMIPAT UNIVERSITY/Documents/II - Year BTECH/DAA/Project/img.png')
        
        if t:
            
            for case in range(t):
                # print('Case #%d: %s' % (case+1, cryptopangrams()))
                msg4="Enter Your Prime Number Range and Encrypted Text Set Size Seperated by a SPACE: "
                title4="Decrypting Machine - Range & Size"
                X=easygui.enterbox(msg4,title4,image='C:/Users/Garv/OneDrive - JK LAKSHMIPAT UNIVERSITY/Documents/II - Year BTECH/DAA/Project/img.png')
                
                if X:
                    msg4="Enter All the Numbers seperated by SPACES:"
                    title4="Decrypting Machine - Integers"
                    Y=easygui.enterbox(msg4,title4,image='C:/Users/Garv/OneDrive - JK LAKSHMIPAT UNIVERSITY/Documents/II - Year BTECH/DAA/Project/img.png')
                
                else:
                    msg55="Oops!! Please begin again"
                    title55="Decrypting Machine"
                    easygui.msgbox(msg55,title55,ok_button='OK')
                    break
                    
                if Y:
                    p=case+1        
                    msg2="Your Decrypted Text for Case #"+str(p)+" is: "+ cryptopangrams(X,Y)
                    title2="Decrypting Machine - Exit"
                    easygui.msgbox(msg2,title2,ok_button='OK')
                
                else:
                    msg55="Oops!! Please begin again"
                    title55="Decrypting Machine"
                    easygui.msgbox(msg55,title55,ok_button='OK')
                    break

    else:
        msg2="Thank your for using the program, Have a Good Day!"
        title2="Decrypting Machine - Exit"
        easygui.msgbox(msg2,title2,ok_button='OK')
        break
    