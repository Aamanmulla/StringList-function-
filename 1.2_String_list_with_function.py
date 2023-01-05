lst=[]

n=int(input("Enter the numbers in a list: "))
def string_list(lst):
    for i in range(0, n):
        ele = str(input())
  
        lst.append(ele)
    print("\nInput: ",lst)

    sol1=lst[-2]
    sol2=lst[-1]

    if sol1 in sol2:
        print("\nOutput: \nTrue\n")
    else:
        print("\nOutput: \nFalse\n")

string_list(lst)