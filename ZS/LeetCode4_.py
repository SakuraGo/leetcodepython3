'''

// 匈牙利算法
class Solution {
    private boolean[] visit;// visit[v2]=true表示点v2访问过
    private int[] link;// link[v2]=v1表示当前与v2相连的点是v1
    // 其中v1属于点集V1，v2属于点集V2，数组下标从0开始

    private boolean[][] board;// 棋盘，false表示坏的
    private int[][] dir = { { 1, 0 }, { -1, 0 }, { 0, -1 }, { 0, 1 } };

    public int domino(int n, int m, int[][] broken) {
        if (broken.length == 0) {// 无坏掉的
            return n * m >> 1;
        }

        // 初始化棋盘，false表示坏掉
        board = new boolean[n][m];
        for (int i = 0; i < n; ++i) {
            Arrays.fill(board[i], true);// 初始全部完好
        }
        for (int[] b : broken) {
            board[b[0]][b[1]] = false;// 设置坏掉的
        }

        return hungary();// 匈牙利算法计算最大骨牌数
    }

    private int hungary() {// 匈牙利算法，返回最大匹配数
        int n = board.length, m = board[0].length;
        visit = new boolean[n * m];
        link = new int[n * m];
        Arrays.fill(link, -1);
        int ret = 0;
        // 遍历点集V1中的点
        for (int r = 0; r < n; ++r) {
            for (int c = ((r & 1) == 0 ? 0 : 1); c < m; c += 2) {
                if (board[r][c]) {
                    Arrays.fill(visit, false);
                    if (find(r, c)) {
                        ++ret;
                    }
                }
            }
        }
        return ret;// 返回最大匹配数
    }

    private boolean find(int row, int col) {
        int n = board.length, m = board[0].length;
        for (int[] d : dir) {// 四个相邻点
            int r = row + d[0];
            int c = col + d[1];
            if (r < 0 || r >= n || c < 0 || c >= m) {
                continue;// 越界
            }
            int v2 = r * m + c;
            if (board[r][c] && !visit[v2]) {// 完好并且未访问过
                visit[v2] = true;
                if (link[v2] == -1 || find(link[v2] / m, link[v2] % m)) {
                    link[v2] = row * m + col;
                    return true;// 找到增广路径
                }
            }
        }
        return false;// 找不到增广路径
    }
}


'''