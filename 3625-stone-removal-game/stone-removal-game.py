class Solution:
    def canAliceWin(self, n: int) -> bool:
        total = moves = 0

        for remove in range(10, 0, -1):
            total += remove
            if total > n:
                break
            moves += 1

        return moves % 2 == 1
        