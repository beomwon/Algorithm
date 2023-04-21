class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str, digits))
        return list(map(int,str(int(num)+1)))