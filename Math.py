#This code will find the  range of a number in a sequence

"""print("Common Difference")
commonDifference = int(input(">> "))
print("Common Difference in the arithmetic sequence is:", commonDifference)

print("First Term")
firstTerm = int(input(">> "))
print("First term in the arithmetic sequence is:", firstTerm)


# calculating 100th term


print("Nth term")
N = int(input(">> "))
print("Nth term is", N)

nthTerm = firstTerm


sum = N/2 * ((2 * firstTerm) + (N-1) * commonDifference)

for i in range(1, N):
    nthTerm = nthTerm + commonDifference

print("The " +str(N) + "th term in the arithmetic sequence is:", nthTerm)
print(sum)
"""

#print("First Term")
#first_Term = int(input(">> "))

#print("Common Difference")
#common_Difference = int(input(">> "))

#print("Final Range Number")
#N = int(input(">> "))

#nth_Term = first_Term

#for num in range(1, N):
 #   nth_Term += common_Difference
  #  print(nth_Term)

"_________________________________________________________________________________"
def someFunction(a, d, n):
    final_num = a + (n-1) * d
    return final_num

def sum(a, d, N):
    sum = N/2 * ((2 * a) + (N-1) * d)
    return sum

print("First Term")
first_Term = int(input(">> "))

print("Common Difference")
common_Difference = int(input(">> "))

print("Final Range Number")
N = int(input(">> "))

print(someFunction(first_Term, common_Difference, N))
print(sum(first_Term, common_Difference, N))







