
'''check out https://leetcode.com/problems/zigzag-conversion/description/'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        self.numRows = numRows
        allRows = [''] * numRows
        down = True
        rowCount = 0
        for charac in s:
            allRows[rowCount] += charac

            # terminal conditions
            if (rowCount == numRows - 1 and down):  # hit the bot row
                down = not down
                rowCount = self.legitRowCount(rowCount - 1)

            elif (rowCount == 0 and not down):  # hit the top row
                down = not down
                rowCount = self.legitRowCount(rowCount + 1)

            else:
                rowCount = self.legitRowCount(rowCount + 1) if down else self.legitRowCount(rowCount - 1)
        finalStr = ''
        for row in allRows:
            finalStr += row

        return finalStr

    def legitRowCount(self, rowCount):
        if rowCount < 0: return 0
        if rowCount > self.numRows - 1: return self.numRows - 1
        return rowCount