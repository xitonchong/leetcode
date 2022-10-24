
from collections import defaultdict

class LongestIncreasingSubsequence:
    def __init__(self, list_):
        # you can think subsequnece as directed graph network
        self.list_ = list_
        self.longest_list = []


    def DepthFirstTraversal(self, i, node, longest):
        # util for recursively finding longest subsequence 
        #visited[node]= True

        # iterate to the next node
        if (i != len(self.list_)-1):
            next_node = self.list_[i+1]
            if (node < next_node):
                longest.append(next_node)
                node = next_node
            self.DepthFirstTraversal(i+1, node, longest)
        return longest

    def find(self):
        # init visited table
        longest = []
        for i, node in enumerate(self.list_):
            #visited = [False] * len(self.list_)
            sequence = [node]
            sequence = self.DepthFirstTraversal(i, node, sequence)
            if len(sequence) > len(longest):
                longest = sequence 

        print(longest, len(longest))
        return longest


    def find_bisect(self):
        from bisect import bisect_left

        ans = []
        for i, num in enumerate(self.list_):
            ind  = bisect_left(ans, num)
            if ind == len(ans):
                ans.append(num)
            else: 
                ans[ind] = num
        print(ans)
        return ans



if __name__ == '__main__':
    arr = [50, 3, 10, 7, 40, 80]
    lis = LongestIncreasingSubsequence(arr)
    lis.find()

    arr = [3, 10, 2, 1, 20]
    lis = LongestIncreasingSubsequence(arr)
    lis.find()

    arr = [0,1,0,3,2,3]
    lis = LongestIncreasingSubsequence(arr)
    assert lis.find_bisect() == [0,1,2,3]
    