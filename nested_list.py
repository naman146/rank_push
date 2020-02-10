"""Create a list of name and marks of the student such that there is list and store 
them in a nested list and print the name(s) of any student(s) having the second lowest grade."""

main_list = []
N=int(input())
if 2<=N<=5:
       for _ in range(N):
              name = input()
              score=float(input())
              inner_list=[name,score]
              main_list.append(inner_list)

       main_list.sort(key= lambda x:x[1],reverse=True)
       index=[]
       for i in range(len(main_list)-1):
              if main_list[i][1] > main_list[i+1][1]:
                     index.append(i)
       print_list=[]
       if len(index)>1:
              for i in range(index[len(index)-2],index[len(index)-1]):
                     print_list.append(main_list[i+1][0])
       else:
              for i in range(index[0]+1):
                     print_list.append(main_list[i][0])

       print_list.sort()
       for i in print_list:
              print(i)
if N<2 or N>5:
       exit()
