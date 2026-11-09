class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        let fixed_point = 0;
        let l = fixed_point + 1;
        let r = nums.length - 1;
        const result: number[][] = []
        const sorted_nums: number[] = nums.sort((a, b) => a - b);
        
        while (fixed_point < nums.length -1) {

            let left = l;
            let right = r;
            while (left < right) {
                let sum = sorted_nums[fixed_point] + sorted_nums[left] + sorted_nums[right];
                
                if (sum == 0) {

                    result.push([sorted_nums[fixed_point], sorted_nums[left], sorted_nums[right]]);
                    while (sorted_nums[left] == sorted_nums[left+1]) left++;
                    left++;
                }
                if (sum < 0) left++;
                if (sum > 0) right--;
            }
            fixed_point++;
            while (fixed_point > 0 && sorted_nums[fixed_point] == sorted_nums[fixed_point-1]) fixed_point++;
            l = fixed_point + 1;
        }
        return result;
    }
}
