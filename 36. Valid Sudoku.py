class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        k=-1
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    board[i][j]=k
                    k=k-1
        for i in board:
            if len(set(i))!=len(i):
                return False
        j=0
        while(j<9):
            l=[board[0][j],board[1][j],board[2][j],board[3][j],board[4][j],board[5][j],board[6][j],board[7][j],board[8][j]]
            if(len(set(l))!=len(l)):
                return False
            j=j+1
        i=0
        while(i<9):
            j=0
            while(j<9):
                l=[board[i][j],board[i][j+1],board[i][j+2],board[i+1][j],board[i+1][j+1],board[i+1][j+2],board[i+2][j],board[i+2][j+1],board[i+2][j+2]]
                j=j+3
                if(len(set(l))!=len(l)):
                    return False
            i=i+3
        return True
            
s=Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))