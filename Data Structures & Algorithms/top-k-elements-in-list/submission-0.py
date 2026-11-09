class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] = hash[num] + 1
            else:
                hash[num] = 1
        arr = []
        for key, value in hash.items():
            if len(arr) == 0:
                arr.append(key)
            else:
                i = 0
                while i<len(arr) and value > hash[arr[i]]:
                    i += 1
                arr.insert(i,key)
        return arr[-k:]

        