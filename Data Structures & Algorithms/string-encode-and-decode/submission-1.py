class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + word + "\t"
        return encoded


            

    def decode(self, s: str) -> List[str]:
        results = []
        current_segment = ""
        count = 0
        for char in s:
            if char  == "\t":
                count = count + 1
                results.append(current_segment)
                current_segment = ""
            else:
                current_segment = current_segment + char
        
     
        
        return results


