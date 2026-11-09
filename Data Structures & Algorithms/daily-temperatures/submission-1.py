class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        result = [0] * length
        stack.append([temperatures[0],0])
        for index,value in enumerate(temperatures[1:],start =1):
            #print(f"stack={stack}")
            #print(f"result={result}")
            
         #   print(value)
          #  print(stack[-1])
            if value <  stack[-1][0]:
                stack.append([value,index])
            else:
                while stack != []: 
                    if value>stack[-1][0]:
                        smaller = stack.pop()
                        result[smaller[1]] = index-smaller[1]
                    else:
                        break

                stack.append([value,index])

        return result
