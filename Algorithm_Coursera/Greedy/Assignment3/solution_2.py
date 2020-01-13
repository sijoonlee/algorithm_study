# maximum-weight independent set

filename = "mwis.txt"
file = open(filename, "r") 
data = file.readlines()
num_vertex = int(data[0])
data = data[1:]
weights = [0 for i in range(num_vertex+1)] # start from index 1
for i, line in enumerate(data):
    weights[i+1] = int(line)

def wis():
    A = [0 for i in range(num_vertex+1)]
    A[0] = 0
    A[1] = weights[1]

    for i in range(2, num_vertex+1):
        A[i] = max(A[i-1], A[i-2] + weights[i])
    
    return A

def reconstruct(A):
    i = num_vertex
    S = []
    while i >= 2:
        if A[i-1] >= A[i-2] + weights[i]:
            i = i - 1
        else:
            S.append(i)
            i = i - 2
    if i == 1:
        S.append(i)
    
    return S


S = reconstruct(wis())

test = [ 1, 2, 3, 4, 17, 117, 517, 997 ]
result = []
for v in test:
    result.append(int(v in S))
print(result) #[1, 0, 1, 0, 0, 1, 1, 0]