A = input()
B = input()

# Please write your code here.
i=0
while i <= len(A)-len(B):
    if A[i:i+len(B)] == B:
        A = A[:i] + A[i+len(B):]
        i=0
    else:
        i+=1
print(A)