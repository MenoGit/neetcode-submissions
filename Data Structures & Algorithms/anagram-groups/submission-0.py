class Solution:
    def groupAnagrams(self, strs):
        hash = {}
        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string in hash:
                hash[sorted_string].append(word)
            else:
                hash[sorted_string] = [word]
        return list(hash.values())
