class hashMap(object):
    def __init__(self,n):
        self.len=n
        self.maps = [0]*n  # 总表

    def find_map(self, k):  # 通过hash函数计算索引值
        index = hash(k) % self.len
        return index

    def add(self, k, v):
        index = self.find_map(k)
        self.maps[index]=v

    def get(self, k):
        index = self.find_map(k)
        return self.maps[index]