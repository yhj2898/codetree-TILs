A = input()

# Please write your code here.
cnt=1
result=''

for i in range(len(A)-1):
    if A[i] == A[i+1]:
        cnt+=1
    else:
        result += A[i] + str(cnt)
        cnt=1

result += A[-1] + str(cnt)

print(len(result), result, sep='\n')


