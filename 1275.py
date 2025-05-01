class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols = [0] * 3, [0] * 3
        diag = 0
        antidiag = 0
        player = 1
        for r, c in moves:

            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r+c == 2:
                antidiag += player
                
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(antidiag) == 3:
                return 'A' if player == 1 else 'B'

            player *= -1
        #print(f"rows: {rows}, cols: {cols}, diag: {diag}, anti_diag: {antidiag}")

        return 'Draw' if len(moves) == 9 else 'Pending' 