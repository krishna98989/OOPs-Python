jk = []
List1 = [1,2,3,4]
arr_size = len(List1)
for i in range(len(List1)):
    for j in range(i,arr_size+1):
        kl = [List1[i]:List1[j]]
        print(kl)
        # print(list(i,j))
        # for k in range(i,j):
        #     print(k)
        #     jj = list[i:j]
        #     print(jj)

# for start_point in range(arr_size):
#         # group sizes
#         for grps in range(start_point, arr_size + 1):
#             # if start point = 1 then
#             # group size = 1, print 1
#             # group size = 2, print 1 2
#             # group size = 3, print 1 2 3 and so on
#             for j in range(start_point, grps):
#                 print(List1[j], end=" ")
#             print()
        