class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        #count the occureances of each value 

        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        #Initialize the frequency list
        frequency = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            frequency[c].append(n)

        result = []

        for i in range(len(frequency)-1, 0, -1):
            for n  in frequency[i]:
                result.append(n)
                if len(result)==k:
                    return result


    '''
    function topKFrequent(nums, k):
    hashmap = {}  // to store frequency of each number
    for each num in nums:
        increase the frequency of num in hashmap

    frequencyArray = array of empty lists with size of (nums.length + 1)
    for each num and count in hashmap:
        append num to frequencyArray[count]

    result = []
    for i from the end of frequencyArray to start:
        for each num in frequencyArray[i]:
            if length of result is less than k:
                add num to result

    return result
'''