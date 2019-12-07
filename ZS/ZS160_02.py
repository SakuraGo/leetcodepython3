# 5239. 循环码排列  显示英文描述
# 用户通过次数 85
# 用户尝试次数 101
# 通过次数 85
# 提交次数 121
# 题目难度 Medium
# 给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：
#
# p[0] = start
# p[i] 和 p[i+1] 的二进制表示形式只有一位不同
# p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
from typing import List

# 1 <= n <= 16
# 0 <= start < 2^n

class Solution:

    ##生成0~2^n-1 的格雷码
    def genGrayCode(self,n):
        if n == 1: ##递归终结..
            return [0,1]
        ## ..未终结..
        lis0 = self.genGrayCode(n-1)
        lis1 = lis0[::-1]
        lis1 = [num+(1<<(n-1)) for num in lis1]
        lis = lis0+lis1
        return lis


    def circularPermutation(self, n: int, start: int) -> List[int]:
        lisss = self.genGrayCode(n)
        # print(lisss)
        # for num in lisss:
        #     print(bin(num))
        iddd = 0
        for idx,numm in enumerate(lisss):
            if numm == start:
                iddd = idx
                break

        return lisss[iddd:]+lisss[0:iddd]

        return []

# print(bin(3))

Solution().circularPermutation(3,3)

'''
三步解决问题

生成格雷码，与第89题相同
找到start的位置
旋转数组，与第189题相同
如何生成格雷码？
基于格雷码是反射码的事实，利用如下规则：

1位格雷码有两个码字
(n+1)位格雷码中的前2^n个码字等于n位格雷码的码字，按顺序书写，加前缀0
(n+1)位格雷码中的后2^n个码字等于n位格雷码的码字，按逆序书写，加前缀1
n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
例如： 生成一个3位格雷码的过程

初始: 0,1
复制前一行，添加前缀0: 00, 01
逆序复制前一行，添加前缀1: 11, 10
于是得到 00, 01, 11, 10
复制前一行，添加前缀0: 000, 001, 011, 010
逆序复制前一行，添加前缀1: 110, 111, 101, 100
于是得到 000, 001, 011, 010, 110, 111, 101, 100

vector<int> circularPermutation(int n, int start) {
    vector<int> res = {0,1};
    for(int i = 2;i <= n;i++){
        for(int j = res.size()-1;j >= 0;j--){
            res.push_back(res[j] + (1 << (i-1)));
        }
    }
		
    int l = 0,r = res.size()-1;
    while(l <= r){
        if(res[l] == start || res[r] == start) break;
        l++,r--;
    }
		
    if(res[l] == start){
        reverse(res.begin(),res.end());
        reverse(res.begin(),res.end()-l);
        reverse(res.end()-l,res.end());
    }else{
        reverse(res.begin(),res.end());
        reverse(res.begin(),res.begin()+l+1);
        reverse(res.begin()+l+1,res.end());
    }
    return res;
}

'''