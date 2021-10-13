#Pattern 1
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
print()
"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
#Pattern 2
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""

#Pattern 3
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()
print()
"""    
* * * * * 
* * * * 
* * * 
* * 
* 
"""

#Pattern 4
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
print()
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
#Pattern 5
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for k in range(5-i):
        print("*",end=" ")
    print()
print()
"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
#Pattern 6 : Diamond Pattern

for i in range(4):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end=" ")
    print()
print()

"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""

#Pattern 7 : Hour Glass Pattern
for i in range(4):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
print()

"""
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""