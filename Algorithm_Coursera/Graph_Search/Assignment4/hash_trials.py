from linkedlist import LinkedList
import hashlib

class Hash_chaining(object):
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.bucket = [LinkedList() for i in range(bucket_size)]
    # too slow
    # def hash(self, key):
    #     k = 0
    #     for s in list(hashlib.md5(str(key).encode('utf-8')).hexdigest()[:6]):
    #         k += ord(s)
    #     return k % self.bucket_size

    # def hash(self, key):
    #     k = int.from_bytes(hashlib.md5(str(key).encode('utf-8')).digest(), byteorder='little')
    #     return k % self.bucket_size

    def hash(self, key):
        return (key >> 11) % self.bucket_size

    def add(self, key):
        pos = self.hash(key)
        self.bucket[pos].add(key)

    def desc(self):
        total = 0
        count = 0
        count_ones = 0
        count_twos = 0
        for ll in self.bucket:
            if ll.length != 0:
                count += 1
            if ll.length == 1:
                count_ones += 1
            elif ll.length == 2:
                count_twos += 1
            total += ll.length
        return total, count, count_ones, count_twos

    def find(self, key):
        pos = self.hash(key)
        return self.bucket[pos].lookup(key)




if __name__ == "__main__":

    bucket_size = int(500000)
    test = Hash_chaining(bucket_size)

    filename = "algo1-programming_prob-2sum.txt"
    #filename = "test.txt"
    file = open(filename, "r") 
    data = file.readlines()
    arr = []
    for line in data:
        arr.append(int(line))
    
    for item in arr:
        test.add(item)

    print(test.desc()) #(999752, 432279, 135042, 135499)
    
    print(test.find(53645918962))    
    # exist = []
    # for t in range(-10000, 10000+1):
    #     for x in arr:
    #         if t-x is not x:
    #             if test.find(t-x):
    #                 exist.append(t)
    #                 break
    # print(len(exist))
