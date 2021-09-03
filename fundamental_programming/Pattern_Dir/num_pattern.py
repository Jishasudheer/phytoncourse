row=5
# for i in range (row):
#     for j in range (i):
#         print(i,end=" ")
#     print()
#
# for i in range (row):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()
# # star printing
# for i in range (row):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()
# #piramid
# for i in range (row):
#     for j in range (row):
#         print(end=" ")
#     row=row-1
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
#parallel
for i in range (row):
    for j in range (i):
        print(end=" ")
    for k in range(row):
       print("*",end=" ")
    print()



