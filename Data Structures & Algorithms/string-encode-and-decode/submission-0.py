class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s

        return encoded

    def decode(self, encoded: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(encoded):
            j = encoded.find("#", i)
            length = int(encoded[i:j])

            word = encoded[j + 1 : j + 1 + length]
            decoded.append(word)

            i = j + 1 + length

        return decoded