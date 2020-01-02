# Scheduling Algo

filename = 'jobs.txt'
file = open(filename, "r") 
data = file.readlines()
num_jobs = int(data[0])

weights = [0 for i in range(0, num_jobs)]
lengths = [0 for i in range(0, num_jobs)]
scores = [0 for i in range(0, num_jobs)]
for i in range(0, num_jobs):
    weights[i] = int(data[i+1].split(' ')[0])
    lengths[i] = int(data[i+1].split(' ')[1])
    scores[i] = weights[i] - lengths[i]

if __name__=="__main__":
    
    print(data[:10])
    print(weights[:10])
    print(lengths[:10])

    sorted_idx = sorted(range(num_jobs), key = lambda k: (scores[k], weights[k]), reverse=True)

    completion_time = 0
    weighted_summation = 0
    for i in sorted_idx:
        completion_time += lengths[i]
        weighted_summation += completion_time * weights[i]

    print(weighted_summation) # 69119377652