#!/usr/bin/env python
# coding: utf-8

# In[8]:


row = [[0 for r in range (9)] for c in range (9)]
print(row)


# # Sort It Up 

# In[7]:


def sort_it_up(lst):
    current = 0
    left = 0
    right = len(lst)-1

    while current!=right:
        if lst[current] == 2:
            lst[current] = lst[right]
            lst[right] = 2
            right = right - 1
        
        elif lst[current] == 1:
            current = current + 1
        
        elif lst[current] == 0:
            lst[current] = lst[left]
            lst[left] = 0
            left = left + 1
            current = current + 1
    
    print(lst)
    
lst = [2,0,0,1,1,0,2,2]
sort_it_up(lst)


# In[6]:


lst = input('Enter numbers = ').split(',')
print(lst)


# # Group Elements of Same Indices using Python
# 
# inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]                                                                         
# outputLists = [10, 40, 70] [20, 50, 80] [30, 60, 90]

# In[92]:


def group_elements(inputLists):
    
    #CREATE A LIST IN EACH VALUE OF A DICTIONARY
    
    small_lst = inputLists[0]        
    
    for j in range (len(small_lst)):
        dic[j+1] = []
    print(dic)
    
    for i in range (len(inputLists)):
        small_lst = inputLists[i]
        
        for j in range (len(small_lst)):
            value = small_lst[j]
            dic[j+1].append(small_lst[j])
            
    print(dic)

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]                                                                         
dic = {}    
group_elements(inputLists)


# In[96]:


dic = {1:[10], 2:[20], 3:[30]}
lst = (dic[1])
print(lst, '\n')

lst.append(40)
print(lst, '\n')

lst = [70]
lst.append(20)

print(lst)


# #### Second Method
# inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]                                                                         
# outputLists = [10, 40, 70] [20, 50, 80] [30, 60, 90]

# In[7]:


inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
final_lst = []

for j in range(3):
    initial_lst = []

    for i in range (len(inputLists)):
        initial_lst.append(inputLists[i][j])
    
    print('List at Index', j, 'is', initial_lst)
    final_lst.append(initial_lst)

print('\n', 'The FINAL List is', final_lst)


# # Number Guessing Game using Python
# In the number guessing game, the program selects a random number between two numbers, and the user guesses the correct number. 

# In[21]:


import random
random_num = random.randint(1,10)
#print('A randomly generated number is', random_num)

user_guess = int(input('Hey! Just guess a number = '))

while True:
    if random_num == user_guess:
        print(user_guess, 'FOUND - HURRAH!')
        break

    elif user_guess<random_num:
        print(user_guess, 'is smaller than random number', '\n')
        user_guess = int(input('Once Again, Guess a number = '))

    elif user_guess>random_num:
        print(user_guess, 'is greater than random number', '\n')
        user_guess = int(input('Once Again, Guess a number = '))


# # PRIME or COMPOSITE Number

# In[1]:


def prime_composite(num):
    status = False
    
    if num<2:
        status = 'none'
    
    #A number is already divisible by 1 and itself, so divisior needs to be other than them.
    
    elif num>2:
        for i in range (2, num):
            if num%i==0:
                status = True
    return status

for i in range (0,5):
    
    num = int(input('Enter a number = '))
    status = prime_composite(num)

    if status == True:
        print(num, 'is a COMPOSITE number')
    elif status == False:
        print(num, 'is a PRIME number')
    elif status == 'none':
        print(num, 'is neither prime nor composite number')
    print()


# # Binary Search

# In[3]:


def binary_search(lst, search):
    low = 0 
    up = len(lst)-1
    
    while low<=up:
        mid = (low + up)//2
        
        if search == lst[mid]:
            print('The value', search, 'found at position', mid+1, 'in the list', lst)
            break
            
        elif search>lst[mid]:
            low = mid + 1
        
        elif search<lst[mid]:
            up = mid - 1

lst = [3,1,2,5,4,7,6,9,8]
search = int(input('Enter the value to search in the list of 1-9 = '))
binary_search(lst, search) 


# # Absolute value || Modulus Sign 
# 
# For integers - integer absolute (positive) value is returned                                                                     
# For floating numbers - floating absolute (positive) value is returned                                                          
# For complex numbers - magnitude of the number is returned                                                                       

# In[12]:


abs(1.5)


# In[1]:


abs(-34)


# In[2]:


abs(-1.57)


# In[3]:


abs(6+8j)


# In[12]:


abs(3j+4)


# # SET Mismatch Using Python

# In[13]:


def set_mismatch(sets):
    duplst = []

    for value in sets:
        
        if sets[value-10]<0:
            duplicate = value
            duplst.append(duplicate)

        else:
            sets[value-10] *= -1
            print('', sets[value-10], end = '')

    print(end = '\n')
    print('Duplicate values are', duplst)
    
    i = 0
    for i in range (0, len(sets)):

        if sets[i] > 0:
            print(sets[i], end = '')
            sets[i] = sets[i] + 1 #put 13 in the place of second 12 to maintain the order
            print('', '=>', sets[i])

        else:
            sets[i] *= -1 #value of sets[i] is multiplied by -1 (-10*-1 = 10)
            print(sets[i])

    print('Final arranged list is', sets)

sets = [10, 11, 12, 12, 14, 14, 16]
set_mismatch(sets)


# In[6]:


def findErrorNums(nums): 
    n = len(nums) 
    duplicate = -1 

    for num in nums: 
        if nums[abs(num) - 1] < 0: 
            duplicate = abs(num) 
            print('duplicate = ', duplicate) 
    
        else: 
            nums[abs(num) - 1] *= -1 
            print('if not duplicate', nums[abs(num) - 1]) 
    
    missing = -1 
    for i in range(n): 
        if nums[i] > 0: 
            missing = i + 1 
            print('missing value = ', missing) 
            
    return [duplicate, missing] 

nums = [1,2,2,4] 
print(findErrorNums(nums))


# In[19]:


#Title refers to a word having the first letter in uppercase and the other letters in lowercase. The function then returns True.
lst = ['Title', 'tITLE', 'TITLE']

for title in lst:
    status = title.istitle()
    
    if status==True:
        print(title, 'is a title')
    else:
        print(title, 'is NOT a title')


# In[28]:


#checks lower case => .islower()

print('pappu'.islower())
print('PAPPu'.islower())
print('PAPPU'.islower())


# In[30]:


#checks upper case => .isupper() 

print('PAPPU'.isupper())
print('PaPpU'.isupper())
print('pappu'.isupper())


# # Check PERFECT NUMBER Using Python
# For example, 6 is a perfect number because its divisors (excluding itself) are 1, 2, and 3 & 1 + 2 + 3 = 6.

# In[20]:


lst = [1,2,3,4]
sum(lst)


# In[20]:


def perfectnum(num):
    divisior = []
    
    for i in range (1,num):
        if num%i==0:
            divisior.append(i)
    
    if sum(divisior) == num:
        print(num, 'is a PERFECT Number')
    #else:
    #    print(num, 'is NOT a PERFECT Number')

for num in range (1, 1001):
    perfectnum(num)


# In[35]:


print(sorted([5,3,4,1,2], reverse = False)) #no reverse - ascending
print(sorted([5,3,4,1,2], reverse = True)) #yes reverse - descending


# In[70]:


#Enumerate() method adds a counter [add count] to an iterable and returns it in a form of enumerating object.

lst1 = ['a','b','c'] 
lst2 = ['*','?','$'] 

print(list(enumerate(lst2, 1)), '\n') 

for i in enumerate(lst1, 1): 
    print(i) 


# In[21]:


def repeatedSubstringPattern(s):
    string = (s + s)[1:-1] #excluding the last character (-1)
    print('string =', string)
    print(string.find(s))
    return string.find(s) != -1
    print(string)

print(repeatedSubstringPattern("abcabcabcabc"))


# In[1]:


#print('kathmandu'[1:-1])
text = 'pappupappu'
return text.find('pappu')


# In[31]:


def countBits(num):
    counter = [0]
    if num >= 1:
        
        while len(counter) <= num:
            counter = counter + [i + 1 for i in counter]
        return counter[:num+1]
    
    else:
        return 0
    
print(countBits(5))


# In[32]:


max([2,3])


# # Max Consecutive Ones using Python

# In[33]:


def maxone(lst):
    count = 0
    maxcount = []
    
    for i in lst:
        
        if i==1:
            count = count + 1
            print(count)
        
        else:
            maxcount.append(count)
            print(maxcount)
            count = 0
    
    maxcount.append(count)
    print('List having maximum number of ones is', maxcount)
    print('Maximum consecutive number of Ones is', max(maxcount))

lst = [1,1,0,1,1,1,0]
maxone(lst)


# # Construct the Rectangle using Python
# We need to return the dimensions of a rectangle with its given area such that its width and height differ by the smallest possible number. 

# In[34]:


import math
def constructRectangle(area):
    
    w = int(math.sqrt(area))
    print('w is ', w)
    
    while area % w != 0:
        print(area, '%', w, '=', area % w)
        w -= 1
    
    print(area // w)
    return [area // w, w]

area = 26
print(constructRectangle(area))


# In[36]:


print('Quotient is', 13//2)


# In[1]:


import math 
def rectangle(area): 
    l = int(math.sqrt(area)) 
    
    while area%l != 0:
        l = l - 1
    b = area//l
    
    return (l,b)

area = int(input('Enter an area = '))
rectangle(area)


# # Number of Segments in a String using Python
# You need to find the total number of words in the string, excluding the spaces

# In[38]:


text = input('Enter a text = ')
parts = text.split(' ')
count = 0

for part in parts:
    print(part)
    count += 1
print('Number of segments in the above string =', count)


# # Third Maximum Number using Python
# You need to find the third largest number in the array as an output. 

# In[12]:


lst = [4,5,3,6,2,1,0,7]
maxn = max(lst)
newlst = []

for i in range(2):
    for num in lst:

        if num==maxn:
            lst.remove(num)

    maxn = max(lst)

print('The THIRD largest number in the list = ', maxn)


# In[42]:


#nsl = []
ls = [1,2,3]
nls = ls
print(nls)

nls.remove(2)
print('nls =>', nls, ',', 'ls =>', ls)


# In[45]:


string = "2-4A0r7-4k"
totalpart = 3

length = len(string)
laterpart = length//totalpart
charfirst = length%totalpart
remainchar = length - charfirst
latereachchar = int(remainchar/laterpart)

print(length, laterpart, charfirst, remainchar, latereachchar)

word = ''

i = 0
while len(word)<=charfirst:
    if string[i]!='-':
        word = word + string[i]
    i = i + 1
print(word)

word = word + '-' 

nword = ''
count = 0
j = i+1

while len(nword)<=remainchar:
    if count==latereachchar:
        nword = nword + '-'
    
    elif string[i]!='-' and len(nword)<=latereachchar:
        nword = nword + string[i]
        count = count + 1
    j=j+1

print(word + nword)


# # REVERSE a string using Python
# The string slicing operator “::” reads all the characters of the string, and -1, in the end, reverses the order of the characters.

# In[48]:


word = 'abcde' 
print(word[::-1]) #from beginning to end with step=1 in reverse direction


# In[47]:


string = 'nepal'

print(string[:-1]) #start=beginning, end = -1 exluded
print(string[::2]) #start = beginning, end = last, step = 2
print(string[::-2]) #from beginning to end with step=2 in reverse direction


# # Power of three (^3)
# 3, 9, 27, 81, 243                                                                                                                  
# You will be given an integer. You need to return True if the integer is a power of three; otherwise, return False. 

# In[ ]:


def powerthree(num):
    for i in range (1,num+1):
        if 3**i==num:
            return(num, 'is a power of 3')
        
    return(num, 'is NOT a power of 3')

for i in range (3):
    num = int(input('Enter a number = '))
    print(powerthree(num))


# In[ ]:


def powerthree(num):
    
    if num%3==0:
        print(num, 'is a MULTIPLE of 3')
    else:
        print(num, 'is NOT a MULTIPLE of 3')

for i in range (5):
    num = int(input('Enter a number = '))
    powerthree(num)


# # SINGLE NUMBER IN THE LIST

# In[ ]:


lst = [1,1,2,2,3,5,3]
newlst = []

for num in lst:
    if num not in newlst:
        newlst.append(num)
    else:
        newlst.remove(num)

print('The single number in the list', lst, 'is', newlst[0])


# # Best Time to Buy and Sell Stock using Python
# Here we will be given an array of closing stock prices on different days, and we need to frame a solution by choosing a single day to buy a stock and choosing another day to sell that stock in the future to maximize our profit.

# In[4]:


def stock(lst):
    max_profit = 0
    buy = 0
    sell = 1
    max_profit_day = 1
    
    while sell < len(lst):
        if lst[sell]>lst[buy]:
            profit = lst[sell]-lst[buy]
            max_profit = max(profit, max_profit)
            max_profit_day = lst.index(buy+max_profit) + 1
            
        else:
            buy = sell
        sell = sell + 1

    print('Maximum profit amount is', max_profit)
    print('Best day to sell the stock is', max_profit_day)

lst = [7, 1, 5, 3, 6, 9]
stock(lst)


# # Solving Two Sum using Python
# 
# In the Two Sum problem, you will be given an array of integers and a target value. To solve this problem, you need to return the indices of these two integers from the array whose addition equals the target value. 

# In[3]:


lst = [1, 2, 3, 5]
target = 5
start = 0
end = 1

while end<=len(lst)-1:
    if target == lst[start] + lst[end]:
        print('The values are', lst[start], lst[end])
        print('The index of those values are', start, end)
        break

    elif end==len(lst)-1:
        start+=1
        end = start
    end = end + 1


# # Excel Sheet Column Title using Python
# You will be given an integer, and you need to return the corresponding column title of the integer as displayed in an excel sheet. 

# In[2]:


column_num = int(input('Enter the index of column = '))
quotient = column_num//26
remainder = column_num%26
ascii = 64
column_name = ''

print('Quotient and Remainder are', quotient, remainder)

if quotient==0:
    column_name = chr(ascii + remainder)
    print('The name of column', column_num, 'is', column_name)

elif quotient>0:
    column_name = column_name + chr(ascii + quotient) + chr(ascii + remainder)
    print('The name of column', column_num, 'is', column_name)


# # Find Missing Number using Python
# 
# Finding the missing number in an array means finding the numbers missing from the array according to the range of values inside the array.

# In[1]:


lst = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
output = []
value = 1

index = 0

while index<=len(lst)-1:
    if value==lst[index]:
        value+=1
        index+=1
        continue

    else:
        output.append(value)
        value+=1
        
print(output)


# # Power of Two using Python
# In the problem of the power of two, you will be given an integer. You need to return True if the integer is a power of two; otherwise, return False.
# 
# 8 = q(4) r(0); q(2) r(0); q(1) r(0)  
# 
# 6 = q(3) r(0); q(1) r(1)

# In[47]:


2%2


# In[57]:


def powertwo(num):
    realnum = num
    quot = num
    rem = num
    while quot!=1 and rem!=1:
        quot = num//2
        rem = num%2
        num = quot
        
        print('quot = ', quot, 'rem = ', rem)
        
    if rem==0:
        print(realnum, 'is a power of 2')
    else:
        print(realnum, 'is NOT a power of 2')

powertwo(8)
print('')
powertwo(6)
print('')
powertwo(10)
print('')
powertwo(121)


# In[61]:


def isPowerOfTwo(n):
    while (n != 1):
        print('n is', n)
        
        if (n % 2 != 0):
            print('n%2 is', n%2)
            return False
        
        n = n // 2
        print('n after n//2 is', n)
    
    else:
        print('n in else part is', n)
        return True

print(isPowerOfTwo(8))
print(' ')
print(isPowerOfTwo(6))


# # DIVISIBLE BY 2

# In[60]:


def powertwo():
    num = int(input('Enter a number = '))
    if num%2==0:
        return True
    else:
        return False
print(powertwo())
print(powertwo())


# # Find Duplicate Values from any DATA STRUCTURE using Python

# In[63]:


lst = ["Aman", "Akanksha", "Divyansha", "Devyansh", "Aman", "Diksha", "Akanksha"]
newlst = []
duplicate = []

for name in lst:
    if name not in newlst:
        newlst.append(name)
    else:
        duplicate.append(name)

print(duplicate)


# # Add Digits using Python
# 
# In the problem of adding digits, you will be given an integer of more than one digit. You need to add all the digits of the integer till you get a single-digit value as the sum.
# 
# Input: 38
# Output: 2 (3+8 = 11, 1+1 = 2)

# In[ ]:


def add_digit(num):
    add = 0
    
    for i in range (len(num)):
        char = num[i]
        add = add + int(char)
    return add
    
num = input('Enter a number = ')
add = add_digit(str(num))

while True:
    if len(str(add))==1:
        print('The sum of digits of the number', num, 'is', add)
        break
    else:
        print('The sum of digits of the number', num, 'is', add)
        final_add = add
        add = add_digit(str(add))
        num = final_add


# In[ ]:


num = ''
print(len(num)) #OUTPUT = 0


# # Move Zeroes using Python
# To solve the problem of moving zeroes, you need to move all the zeroes present in the array at the end of the array.             
# Input: [0, 1, 0, 3, 12]                                                                                                    Output: [1, 3, 12, 0, 0]

# In[5]:


lst = [0,1,0,3,12]
newlst = []

for num in lst:
    if num!=0:
        newlst.append(num)

for num in lst:
    if num==0:
        newlst.append(num)
        
print(newlst)


# # Majority Element using Python

# In[13]:


def majorityElement(nums):
    count = 0
    major_element = 0
    
    for i in nums:
        if count == 0:
            major_element = i
            print('major element', major_element)
        
        if major_element == i:
            count = count + 1
            print('count + part', count, '\n')
            
        else:
            count = count - 1
            print('count - part', count, '\n')
            
    return major_element

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


# In[20]:


lst = [2,1,4,2,3,4,3,0,4]
count = 0
max_num = 0

for num in lst:
    if count==0:
        max_num = num
    else:
        if num == max_num:
            count+=1
        else:
            count-=1
print('The MAJORITY value in the list', lst, 'with the HIGHEST COUNT is', max_num)


# # MAXIMUM and MINIMUM element in a LIST

# In[14]:


lst = [2,2,1,2,1,2,1,3]

print('The maximum value in the list', lst, 'is', max(lst))
print('The minimum value in the list', lst, 'is', min(lst))


# In[29]:


count = 4
print(count)

for i in range (4):
    count-=1
    print(count)


# # APPEND values in a List without using In-Built Function

# In[26]:


lst = ['pappu','roshan','bishnu','nabina']
newlst = []

for name in lst:
    newlst += [name]
    print(newlst)


# # DIFFERENCE of two Lists is NOT Possible, so SETS

# In[34]:


sets = set([1,2,3]) - set([1,2])
lst = list(sets)
print('List is', lst, 'AND Set is', sets)


# In[35]:


names1 = ["Alice", "Bob"]
names2 = ["Bob", "Charlie"]
difference = list(set(names1) - set(names2))
print(difference) 


# # Solving the Single Number Problem using Python
# You will be given an array of integers where each item appears twice except for one that we need to find.
# 
# Input: [4,1,2,1,2]   => Output: 4

# In[40]:


lst = [4,1,2,1,2]
newlst = []

for num in lst:
    if num not in newlst:
        newlst.append(num)
        
    else:
        newlst.remove(num)

print(newlst[0])


# # Square Root using Python

# In[52]:


num = int(input('Enter a number = '))
square_root = num**(1/2)
print(int(square_root))


# In[54]:


def mySqrt(x):
    left = 1
    right = x
    mid = 0
    while (left <= right):
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
            sqrt = mid
    return sqrt

print(mySqrt(25))


# In[3]:


import numpy as np
# Set the earth's radius (in kilometers)
r = 6371

# Convert degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi/180)

# Function to calculate the distance between two points 
# using the haversine formula

def distcalculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return r * c

print(distcalculate(22.745049, 75.892471, 22.765049, 75.912471))


# # Finding the INDEX of a MINIMUM VALUE 

# In[6]:


lst = [10,6,8,7,4,2,3,5]
minm = lst[0]
index = 0

for i in range (1,len(lst)):
    if lst[i]<minm:
        minm = lst[i]
        index = i

print('Minimum value is', minm, 'whose index is', index, 'at position', index+1)


# In[8]:


lst = [10,6,8,7,4,2,3,5]
maxm = lst[0]
index = 0

for i in range (1,len(lst)):
    if lst[i]>maxm:
        maxm = lst[i]
        index = i

print('Maximum value is', maxm, 'whose index is', index, 'at position', index+1)


# In[19]:


try:
    f = open('text.txt', 'r') 
    count = 0

    for line in f:
        for i in range (0, len(line)):
            if line[i]>='A' and line[i]<='Z':
                count+=1

    print('Number of upper cases/capital letters is', count)
    
except Exception as ex:
    print(ex)


# # Python Program to Count Most Frequent Words in a File
# # Calculating Execution Time of a Python Program
# Here you will be given a file, and you will be asked to find the most frequent words in that file along with the number of times they are present.

# In[38]:


from time import time
initial_time = time()

sentence = "The lazy brown fox jumps over the lazy fox the" 
lst = sentence.split(' ')
newlst = [] 
counter = {} 

for i in range (0,len(lst)): 
    word = lst[i].lower() 
    
    if word not in newlst: 
        newlst.append(word)
        counter[word] = 1
    
    else:
        counter[word] += 1

print(counter)

maxi = max(counter.values())
print('\n', counter.items(), '\n')

for index, value in counter.items():
    if value==maxi:
        print('The most frequent word in the sentence is', index)
        
final_time = time()
print('\n', 'The execution time of this program is', final_time-initial_time)


# In[9]:


word = ['the','is','the','is','the']
counter = {}

for letter in word: 
    counter[letter] = counter.get(letter,0) + 1

print(counter)


# In[40]:


from datetime import datetime

initial = datetime.now()
final = datetime.now()

print(final - initial)


# #Power of 2 = 2,4,8,16,32,...
# #Square of 2 = 1,2,9,16,25,...
# 
# 2 = 1
# 4 = 2, 1
# 8 = 4, 2, 1
# 16 = 8, 4, 2, 1
# 
# 6 = 3, 1.5
# 10 = 5, 2.5
# 12 = 6, 3, 1.5

# In[54]:


if (type(2)) == int:
    print(True)
else:
    print(False)


# In[83]:


print(int(5/2))
print(5/2)
type(5/2)

print('')

print(int(4/2))
print(4/2)
type(4/2)


# In[77]:


def power_two(num):
    div = num
    
    while div>1:
        div = div/2
        
    if div==1:
        print(num, 'is a power of 2')
    else:
        print(num, 'is NOT a power of 2')

num = int(input('Enter a number = '))
power_two(num)


# # Group Anagrams using Python [Not Solved Yet]
# 
# Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc. Here you will be given a list of words, and you have to write an algorithm to group all the words which are anagrams of each other.

# In[43]:


from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    print('dfdict is', dfdict, '\n')
    
    for i in a:
        sorted_i = " ".join(sorted(i))
        print('sorted_i is', sorted_i, '\n')
        
        dfdict[sorted_i].append(i)
    
    print('dfdict is', dfdict, '\n')
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))


# In[106]:


#words = ["tea", "eat", "bat", "ate", "arc", "car"]

vowels = ["a", "e", "i", "o", "u"]

vowelsCSV = "".join(vowels)

print("Vowels are = ", vowelsCSV)
print(len(vowelsCSV))


# In[34]:


words = ["tea", "eat", "bat", "ate", "arc", "car"]
newlst = []
dic = {}
final_list = [] 

for word in words:
    lst = []
    
    for i in range (len(word)):
        lst.append(word[i])
    
    lst.sort()
    sort_word = ''.join(lst)
    
    print(sort_word)
    
    if sort_word not in newlst: 
        newlst.append(sort_word) 
        dic[sort_word] = 1 
        
    else:
        dic[sort_word]+=1 
    
print(dic)


# In[133]:


dic = {'pappu':1, 'roshan':2, 'nabina':3, 'bishnu':4}
for index, value in dic.items():
    dic[index]+=1
    print(dic[index)


# In[168]:


dic = {}
dic['pappu'] = 1
print(dic)

dic['pappu'] += 1
print(dic)


# In[178]:


words = ["tea", "eat", "bat", "ate", "arc", "car"]
newlst = []
dic = {}

for word in words:
    lst = []
    
    for i in range (len(word)):
        lst.append(word[i])
    
    print('List is', lst) 
    sort_word = ''.join(lst)
     
    newlst.append(sort_word)

start = 0
while start<len(newlst):

    for i in range (1, len(newlst)):
        if newlst[i] == newlst[start]:
            print(lst[i], lst[start])
            
    start+=1


# # Find Missing Number using Python
# 
# Finding the missing number in an array means finding the numbers missing from the array according to the range of values inside the array. Most of the time, the question you get based on this problem is like:
# 
# - Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.

# In[4]:


lst = [1,2,4,5,6,8,9,11]
index = 0
missing_lst = []

for num in lst:
    if index+1 == num:
        index+=1

    else:
        missing_lst.append(index+1)
        index+=2

print('The missing values in the list', lst, 'are', missing_lst)


# # Group Elements of Same Indices using Python

# In[33]:


lst_one = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
index = 0
lst_three = []

while index<=2:
    lst_two = []
    
    for i in range (len(lst_one[0])):    
        lst_two.append(lst_one[i][index])
    
    print('An individual list at index', index, 'is', lst_two)
    
    lst_three.append(lst_two) 
    index+=1 

print('The final list grouped by index wise is', lst_three)


# In[1]:


dic = {'name':'roshan'}

dic['name'].append('pappu')
print(dic) 


# # Remove Duplicates from a Sorted Array using Python
# 
# Input Array: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]                                                                                     
# Output Array: [0, 1, 2, 3, 4]

# In[4]:


input_array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output_array = []

for num in input_array:
    if num in output_array:
        continue
    else:
        output_array.append(num)

print(output_array)


# # Plus One Problem
# 
# Input Array: [1, 2, 3]                                                                                                           
# Output Array: [1, 2, 4]
# 
# Input: [8], Output: [9]                                                                                                                            Input: [9], Output: [1, 0]

# In[ ]:


lst = [10, 9, 99] 

def plus_one(lst):
    index = len(lst)-1

    if lst[index]%9!=0:
        lst[index]+=1
        print('List formed by adding one is', lst)

    else:
        lst[index]+=1
        print('The list formed by adding one is', lst)

        one_lst = [int(x) for x in str(lst[index])]
        print('List after separating the last number with comma', one_lst)

        del lst[index]
        print(lst+ one_lst)
            
        
plus_one(lst)


# In[ ]:


num = 10
a = [int(x) for x in str(num)]
print(a)


# In[ ]:


lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
print(lst1 + lst2)


# # Longest Common Prefix using Python
# [“flower”, “flow”, “flight”] => As the common prefix among all the strings of the array is “fl”, the output should return “fl”.

# In[4]:


#def common_prefix(lst):
#    for word in lst:       


# In[13]:


strs = ["flower", "flow", "flight"]

def longestCommonPrefix(strs):
    l = len(strs[0])
    print('l is', l)
    
    for i in range(1, len(strs)):
        print('abc is', len(strs[i]))
        length = min(l, len(strs[i]))
        
        print('length is', length)
        print('strs[0][0:length]', strs[0][0:length], 'strs[i][0:length]', strs[i][0:length])

        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            print('length in loop', length)
            
            if length == 0:
                print('0 finally')
                return 0
    
    print('strs[0][0:length]', strs[0][0:length])
    return strs[0][0:length]

print(longestCommonPrefix(strs))


# In[11]:


# If the items in an iterable are strings, the smallest item (ordered alphabetically) is returned.
# Example 2: The smallest string in a list
# min() shows the smallest value when arranged in ascending order alphabetically

languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages)


print("The smallest string is:", smallest_string)


# # Majority Element using Python
# 
# Input: [2,2,1,1,1,2,2] => Output: 2

# In[22]:


lst = ['2','2','1','1','1','2','2','3']
dic = {}

for num in lst:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num]+=1
print(dic)

max_num = 1

for index, value in dic.items():
    if dic[index] > max_num:
        max_value = index
        max_num = value

print('Majority Element is', max_value, 'whose maximum count is', max_num)


# In[17]:


dic = {}
if 'pappu' not in dic:
    dic['pappu'] = 1
print(dic)


# # Counting Bits using Python
# In the counting bits problem, you will be given an integer n. To solve this problem, return an array of the length n + 1 where the elements will be the number of 1’s present in the binary representation of the index number of each value in the array.
# 
# For example, look at the input and output of this problem shown below:
# 
# Input: 5                                                                                                                         
# Output: [0, 1, 1, 2, 1, 2]
# 
# [0: 0, 1: 1, 2: 10, 3: 11, 4: 100, 5: 101]

# In[1]:


binary = [0,1,10,11,100,101]
decimal = [0,1,2,3,4,5]

value = int(input('Enter a number = '))

for num in decimal:
    if num==value:
        


# In[10]:


def countBits(num):
    counter = [0]
    if num >= 1:
    
        while len(counter) <= num:
            print('len(counter) is', len(counter), 'num is', num)
            print('initial counter is', counter)
            print('[i + 1 for i in counter]', [i + 1 for i in counter])
            
            counter = counter + [i + 1 for i in counter]

            print('final counter is', counter, '\n')
        
        print('counter[:num+1]', counter[:num+1])
        return counter[:num+1]
    
    else:
        return 0
    
print(countBits(9))


# # Relative Ranks Problem
# Input: [5, 4, 3, 2, 1] | Output: [“Gold Medal”, “Silver Medal”, “Bronze Medal”, “4”, “5”]

# In[15]:


lst = [5,4,3,2,1]
maximum = max(lst)
print(lst.index(maximum)) #index of the value (5)


# In[27]:


lst = [3,4,5,1,2]
lst = (sorted(lst, reverse = True))
print('The SORTED LIST in DESCENDING Order is', lst)

lst[0] = 'Gold Medal'
lst[1] = 'Silver Medal'
lst[2] = 'Bronze Medal'

for i in range (3,len(lst)):
    lst[i] = i+1

print(lst)


# sentence 1 = “the quick brown fox jumps over the lazy dog”                                                                     sentence 2 = “the quick brown dog jumps over the lazy fox”
# Output: [‘fox’, ‘dog’]

# In[14]:


sen1 = 'the quick brown fox jumps over the lazy dog'
sen2 = 'the quick brown dog jumps over the lazy fox'

lst1 = sen1.split()
lst2 = sen2.split()

final_lst = []

for index in range (len(lst1)):
    if lst1[index] == lst2[index]:
        continue
    else:
        if lst1[index] not in final_lst and lst2[index] not in final_lst:
            final_lst.append(lst1[index])
            final_lst.append(lst2[index])

print(final_lst)


# In[4]:


a = [1,2,3]
b = [2,4,6]
for num in a:
    if num not in b:
        print(num)


# # Set Mismatch Problem
# 
# In the Set Mismatch problem, you will be given an array of positive integers with some elements missing or duplicated. You need to identify and return the missing and duplicated numbers to solve this problem.
# 
# Input: [11, 12, 13, 14, 14, 16] => Output: [15, 14]

# In[26]:


lst = [11, 12, 13, 14, 14, 16]
output_lst = []

for i in range (0,len(lst)):
    for j in range (i+1,len(lst)):
        
        if lst[i]==lst[j]:
            output_lst.append(lst[i])
            lst[j] = lst[i] + 1

print('lst is', lst, 'AND output_lst is', output_lst)


# In[25]:


lst = [10,12,14,17,16,18]
diff_lst = []

for i in range (0,len(lst)-1):
    difference = lst[i+1] - lst[i]
    diff_lst.append(difference)

print(diff_lst)
max(diff_lst)


# # Detect Capital Problem (NOT SOLVED)
# 
# In the detect capital problem, you will be given a word as input, and you need to check if:
# 
#     All the letters are uppercase: return True;
#     All the letters are lowercase: return True;
#     Only the first letter is uppercase: return True;
#     Some letters are uppercase, and some are lowercase: return False;
#     The first letter is lowercase with an uppercase letter in the word: return False;
# 
# So in this problem, we need to check if the words containing capital letters are using capital letters correctly or not. For example, look at the input and output values of this problem shown below:
# 
#     Input: “USA” | Output: True
#     Input: “aman” | Output: True
#     Input: “Google” | Output: True
#     Input: “FlaG” | Output: False
# 

# In[19]:


def capital(word):
    status = False
    if word[0]>='a' and word[0]<='z':
        
        for i in range (1,len(word)):
            if word[i]>='a' and word[i]<='z':
                status = True
    
    else:
        for i in range (1,len(word)):
            
            if word[i]>='a' and word[i]<='z':
                status = True
            elif word[i]>='A' and word[i]<='Z':
                status = True
    
    return status

capital('AMAn')


# # Determine a LEAP YEAR
# In the Gregorian calendar, three conditions are used to identify leap years:
# 
#     The year can be evenly divided by 4, is a leap year, unless:
#         The year can be evenly divided by 100, it is NOT a leap year, unless:
#             The year is also evenly divisible by 400. Then it is a leap year.
# 
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source 

# In[22]:


def is_leap(year):
    leap = False
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))


# # The Minion Game
# 
# NOT SOLVED YET FOR ALL CASES
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false
# 

# In[7]:


def minion_game(string):

    staurt = []
    kevin = []
    vowel = ['A','E','I','O','U']
    score = {'staurt' : 0, 'kevin' : 0}

    for length in range (1,len(string)+1):
        
        for i in range (0, len(string)-length+1):
    
            if string[i] not in vowel:
                score['staurt']+=1
                
                if string[i:i+length] not in staurt:
                    staurt.append(string[i:i+length])
        
    print(staurt, score)
    
if __name__ == '__main__':
    minion_game('BANANA')


# # Finding a PERFECT SQUARE Number

# In[1]:


print(16**(1/2))


# In[ ]:


def perfect_square(num):
    
    try:
        quot = num**(1/2)
        quot = str(quot).rstrip('.0')
        
        print('Quotient is', quot)
        print('The data type of Quotient is', type(int(quot))) #EXCEPTION occurs Here
        print(num, 'is a perfect square')
    
    except:
        print(num, 'is NOT a perfect square')
        
num = int(input('Enter a number = '))
perfect_square(num)


# In[2]:


def perfect_square(num):
    i = 1
    while i<=num:
        if i*i==num:
            return (str(num) + ' is a perfect square')
        
        i+=1
    return (str(num) + ' is NOT a perfect square')

num = int(input('Enter a number = '))
print(perfect_square(num))


# # Finding DUPLICATE VALUES
# 
# sets = [10, 11, 12, 12, 14, 14, 16]                                                                                       Duplicate Values = [12,14]

# In[13]:


sets = [10,11,12,12,14,14,16]
dup = []

for value in sets:
    if sets[value-10] > 0:
        sets[value-10]*=-1
    
    else:
        dup.append(sets[value+1-10])

print(sets)
print('The duplicate values are', dup[0], 'and', dup[1], 'of the list', dup)


# # Finding DUPLICATE VALUES
# 
# sets = [10, 11, 12, 12, 14, 14, 16]                                                                                       Duplicate Values = [12,14]

# In[ ]:


lst = [10, 11, 12, 12, 12, 14, 14, 16]
dup = []

for i in range (len(lst)):
    if lst[i] == lst[i+1]:
        dup.append(lst[i])


# In[15]:


sets = [10,11,12,12,14,14,16]

for value in sets:
    if sets[value-10] > 0:
        sets[value-10]*=-1
    else:
        sets[value+1-10]+=1

for i in range (len(sets)):
    if sets[i] < 0:
        sets[i]*=-1
print('The well-arranged set is', sets)


# In[14]:


sets = {10,11,12,12,14,14,16}
print(sets)


# # Number of Segments in a String
# Input: “Hey, my Instagram username is amankharwal.official” | Output: 6

# In[25]:


text = 'Hey, my Instagram username is amankharwal.official'
lst = text.split(' ')

print('Number of Segments in the string -', text, '- is', len(lst), '\n')

count = 0
for word in lst:
    print(word)
    count+=1

print('\n', 'Number of Segments in the string -', text, '- is', count)


# # Move Zeroes using Python
# Input: [0, 1, 0, 3, 12] => 
# Output: [1, 3, 12, 0, 0]

# In[32]:


lst = [0,1,0,3,12]
newlst = []
zero_count = 0

for num in lst:
    if num!=0:
        newlst.append(num)
    else:
        zero_count+=1

for i in range (zero_count):
    newlst.append(0)

print('The modified list after moving zeroes is', newlst)


# In[ ]:




