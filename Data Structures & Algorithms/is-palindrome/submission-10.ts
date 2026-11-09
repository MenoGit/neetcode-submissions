class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isCharAlphanumeric(char: string): boolean {
        if (char.length !== 1) return false;

        const code = char.charCodeAt(0);

        const isDigit = code >= 48 && code <= 57;   // 0-9
        const isUpper = code >= 65 && code <= 90;   // A-Z
        const isLower = code >= 97 && code <= 122;  // a-z

        return isDigit || isUpper || isLower;
        }

    isPalindrome(s: string): boolean {
        let left = 0;
        let right = s.length - 1;
        while (left < right) {
            while (left<s.length && this.isCharAlphanumeric(s[left]) == false) left++;

            while (right >= 0 && this.isCharAlphanumeric(s[right]) == false) right--;
            if(left>right) break;

            if (s[left].toLowerCase() != s[right].toLowerCase()) {
                return false;
            }
            left++;
            right--;
        }
        return true
    }
}
