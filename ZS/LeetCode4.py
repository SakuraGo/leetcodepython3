# 4.覆盖
#
# 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2
# 的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。
#
#
#
# 输入：n, m代表棋盘的大小；broken是一个b * 2
# 的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。
#
# 输出：一个整数，代表最多能在棋盘上放的骨牌数。

from  typing import List

class Solution:

    def __init__(self):
        self._res = 0
        self._rows = 0
        self._cols = 0
        self._curRet = 0
        self._visited = []

    def isValid(self,row,col):
        return row>=0 and row< self._rows and col>=0 and col< self._cols

    def dfs(self,row,col):
        # print(row,col)
        # if self.isValid(row,col) is False:
        #     return
        if row >= self._rows:
            return
        if col >= self._cols:
            self.dfs(row+1,0)
            return  ##如果大于列数了 ，只能走上面dfs这条路，下面的逻辑不能运行了。。要return掉
        ##如果碰到障碍或者已经被占了..
        if  self._visited[row][col]>0:
            self.dfs(row,col+1)

        ##横着加。。
        if self._visited[row][col] == 0 and  self.isValid(row,col+1) and self._visited[row][col+1] == 0:
            self._curRet += 1
            self._res = max(self._res,self._curRet)
            self._visited[row][col] = 1
            self._visited[row][col+1] = 1

            self.dfs(row,col+2)
            self._curRet -= 1
            self._visited[row][col] = 0
            self._visited[row][col+1] = 0

        ##竖着加
        if self._visited[row][col] == 0 and  self.isValid(row+1,col) and self._visited[row+1][col] == 0:
            self._curRet += 1
            self._res = max(self._res,self._curRet)
            self._visited[row][col] = 1
            self._visited[row+1][col] = 1
            self.dfs(row,col+1)
            self._curRet -= 1
            self._visited[row][col] = 0
            self._visited[row+1][col] = 0


    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        self._rows = n
        self._cols = m
        ##使用题解中的dfs思路暴力回溯

        self._visited = [[0 for col in range(m)] for row in range(n)]
        for point in broken:
            r,c = point ##这样是可以的！
            self._visited[r][c] = 2

        self.dfs(0,0)

        return self._res

res = Solution().domino(7,7,[])
print("qwer",res)

'''
    int ret = 0; //摆放计数
    int max = 0; //最大值计数

    /**
     * 解题思路：
     * 1、构建棋盘，将棋盘上正常的为0，坏了的位置为2，摆放了骨牌的为1
     * 2、对于一个位置和骨牌有三种组合：横着放、竖着放、不放，如需计算正确的值需要所有的情况都计算到，所以回溯实现
     * <p>
     * 执行耗时不是很好，但是自己写出来的好理解
     * 执行用时 :1297 ms, 在所有 java 提交中击败了12.90%的用户
     * 内存消耗 :35.6 MB, 在所有 java 提交中击败了100.00%的用户
     *
     * @param n
     * @param m
     * @param broken
     * @return
     */
    public int domino(int n, int m, int[][] broken) {
        ret = 0;
        max = 0;
        //构造棋盘
        int[][] map = new int[n][m];
        for (int i = 0; i < broken.length; i++) {
            int[] item = broken[i];
            map[item[0]][item[1]] = 2;
        }
        dfs(map, 0, 0);

        return max;
    }

    /**
     * 循环的过程是横向一行行逐格摆放，如到一行的末尾无法摆放则换行，如超过行数则计算摆放的最大个数
     *
     * @param map
     * @param row
     * @param col
     */
    private void dfs(int[][] map, int row, int col) {
        if (row >= map.length) { //如超过行数则计算摆放的最大个数
            max = Math.max(max, ret);
            return;
        }
        if (col >= map[row].length) {//如到一行的末尾无法摆放则换行
            dfs(map, row + 1, 0);
            return;
        }
        if (map[row][col] > 0) {//遇坏格子则跳过
            dfs(map, row, col + 1);
            return;
        }
        //试着横着放
        boolean h = false;
        if (col < map[row].length - 1 && map[row][col + 1] == 0) {
            h = true;
            map[row][col]++;
            map[row][col + 1]++;
            ret++;
            dfs(map, row, col + 2);
            //横向状态重置
            ret--;
            map[row][col]--;
            map[row][col + 1]--;
        }
        //试着竖着放
        boolean v = false;
        if (row < map.length - 1 && map[row + 1][col] == 0) {
            v = true;
            map[row][col]++;
            map[row + 1][col]++;
            ret++;
            dfs(map, row, col + 1);
            //竖向状态重置
            ret--;
            map[row][col]--;
            map[row + 1][col]--;
        }
        //如横着和竖着都不行，试着不放，跳2格
        if (!h && !v) {
            dfs(map, row, col + 2);
        }
    }

'''

a,b = [1,2]
print(a,b)