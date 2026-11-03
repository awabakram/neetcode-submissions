class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        
        print(encoded)
        
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordlen = int(s[i:j])
            word = s[j+1:j+wordlen+1]
            decoded.append(word)
            i = j + wordlen + 1

        return decoded

