from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashTable = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))

            hashTable[sorted_word].append(word)

        return list(hashTable.values())

            