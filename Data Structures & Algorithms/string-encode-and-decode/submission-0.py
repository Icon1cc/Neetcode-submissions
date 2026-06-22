class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j])

            word = s[j + 1: j+1 + word_length]

            decoded_string.append(word)

            i = j + 1 + word_length
        
        return decoded_string