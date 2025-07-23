# for i in range(1,6):
#     for j in range(1,i+1):##i=0,j=1+0=1
#         print(j,end="")
#     print()



# for i in range(1,6):#num of rows _____
#     for j in range(1,6):#colum
#         print(i*j,end="\t")
#     print()

# count=1
# for i in range(1,6):
#     for j in range(i):
#         print(count,end=" ")
#         count+=1
#     print()

# rows = 5
# for i in range(rows):
#     # print spaces
#     for j in range(rows - i - 1):
#         print("- ", end="")
#     # print star
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()

# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

for i in range(5):
    for j in range(2*i+1):
        print("",end="")
    for k in range(9-i):
        print("*",end="")
    print()