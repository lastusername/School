def Problem_1():
    def is_multiple(n,m):
        try:
            result = input_n % input_m
            if result != 0:
                return print(str(input_n)+" is not a multiple of "+ str(input_m) + " \nFalse")
            else:
                return print(str(input_n)+" is a multiple of "+str(input_m) + " \nTrue")
        except: 
            return print("error with inputs")    
    print("This program will check if one number is a multiple of another. "
        "You will enter two positive integers: n and m. "
        "The program will return True if n is a multiple of m, "
        "and False otherwise")
    input_n = int(input("Please privde the value of n: "))
    input_m = int(input("Please privde the value of m: "))
    is_multiple(input_n, input_m)
 
def Problem_2():
    print("This program has a function called is_even(k). \nJust enter a positive number, and it will tell you if the number is even or odd. \nIf it’s even, it will return True. If it’s odd, it will return False.")
    def is_even(k):
        n=[]
        m=[]
        for x in range (k):
            if x+1 == k and len(n) > len(m):
                m.append(1)
                if len(n) == len(m):
                    print("True! Your number is even!")
                else:
                    print("False! Your number is odd!")
            elif x+1 == k:
                n.append(1)
                if len(n) == len(m):
                    print("True! Your number is even!")
                else:
                    print("False! Your number is odd!")
            elif len(n) > len(m):
                m.append(1)
            else:
                n.append(1)
            
    input_k = int(input("Please privde the value of k: "))
    is_even(input_k)

def Problem_3():
    print("This program has a function called dist(n). \nYou will give it a list of numbers. \nIt will check if all the numbers in the list are different from each other. \nIf they are all distinct, it will return True. If there are duplicates, it will return False.")
    n = []
    loops_4_integers = int(input("How many integers do you want to use: "))
    for x in range (0, loops_4_integers):
        n.append(int(input("please enter your integer: "))) 
    def dist(n):
        for i in range(loops_4_integers):
            for j in range(i + 1, loops_4_integers):
                if n[i] == n[j]:
                    print("There is a duplicate, FALSE")
                    return
                elif j-1 == loops_4_integers:
                    j=0
                else:
                    print("verifying")
        print("There is no duplicate. True")
    dist(n)

while (True): 
    x = int(input("Which Problem would you like to see? \n1, 2, 3? "))
    if x == 1:
        Problem_1()
    elif x == 2:
        Problem_2()
    elif x == 3:
        Problem_3()
    else: 
        print("Choose '1' '2' or '3'")

# [12 pts] What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
# ANSWER: range(50, 90, 10)

# [12 pts] What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, ,2, 0, -2, -4, -6, -8?
# ANSWER: range(8,-10,-2)

# [16 pts] Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before.
# o = [1,2,3,4,5,6]
# p = []
# for x in range (len(o)):
#   p.append(o[-1-x])