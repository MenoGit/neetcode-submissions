class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let left = 0;
        let right: number = numbers.length-1

        while (left < right) {
            let value = numbers[left] + numbers[right]
            if (value == target) {
                return [left+1,right+1];
            }
            if (value < target) {
                left++;
            }
            else {
                right--;
            }
        }
    }
}
