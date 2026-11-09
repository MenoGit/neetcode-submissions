class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const hashmap = new Map<String,string[]>();
        for (let i=0; i<strs.length; i++) {
            const word = strs[i];
            const letters = word.split("");
            const sorted = letters.sort();
            const key = sorted.join("");
            if (hashmap.has(key)) {
                const temp = hashmap.get(key);
                temp.push(word);
                hashmap.set(key,temp);
            }
            else {
                const array_words: string[] = [word];
                hashmap.set(key,array_words)
            }        
        
        }
        return Array.from(hashmap.values())

    }
}
