#write a python program to print a smallest vowel which is repeating odd times in the given range?
#to print vowels in string
'''s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":      #sravanthi = a a i
        print(i)'''

#to print odd vowels

'''s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":       # sravanthi= i( i repeats odd no of times),a repeates even no of times so o/p is i
        if s.count(i)%2!=0:
            s1+=i
print(s1)'''

# minimum no of odd vowels
s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":          #voeeiiiouuuuk= o/p is i ( i repests 3, o repeats 2,u repeats 4 so min no of odd letter is i)sss
        if s.count(i)%2!=0:     
            s1+=i
print(min(s1))


