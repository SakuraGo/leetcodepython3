# 5176. 猜字谜
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
#
# 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
#
# 单词 word 中包含谜面 puzzle 的第一个字母。
# 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
# 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
# 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

from  typing import  List
'''
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:



        res = []
        for puz in puzzles:
            sett = set()
            for c in puz:
                sett.add(c)
            # memoDic[puz] = sett
            # print(sett)
            resCnt = 0
            for word in words:
                firstWord = False
                for c in word:
                    if c == puz[0]:
                        firstWord = True
                    if c not in sett:
                        firstWord = False
                        continue
                if firstWord == False:
                    continue
                else:
                    resCnt += 1

            res.append(resCnt)
        return res

# ["aaaa","asas","able","ability","actt","actor","access"]
# ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

# ["apple","pleas","please"]
# ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]



'''
## 依然是超时。。
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mp = {}    ## 这个mp 的key存储了某种字母组合，value 存储了该组合所拥有的的word个数。
        for word in words:
            st = set(word)
            s = 0
            for ch in st:
                s |= 1 << (ord(ch) - ord('a'))
            mp[s] = mp.get(s, 0) + 1
        ans = [0] * len(puzzles)
        for idx, p in enumerate(puzzles):
            for i in range(1 << 6):   ## i 的意义就是确保每一种可能的谜底都被计算过一遍，如果取了和 i 一样的位置，那么相应的谜底的个数（如果有的话），就要被加入 到ans[idx]
                ss = 1 << (ord(p[0]) - ord('a'))
                for j in range(6):     ##  因为puzzle只有最多7位，这里从遍历 0-6 ，+1位因为第一位已经处理过，也就是 计算了 1-7的每个位置上的字母
                    if (i & (1 << j)) > 0:
                        ss |= (1 << (ord(p[j + 1]) - ord('a')))
                ans[idx] += mp.get(ss, 0)
        return ans


'''
class Solution {
public:
    map<int,int> a;
    vector<int> ans;
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        a.clear();
        int n=words.size(),m=puzzles.size(),i,j,k;
        ans.resize(m,0);
        for(i=0;i<n;i++)
        {
            for(j=k=0;j<words[i].size();j++)k|=1<<words[i][j]-'a';
            a[k]++;
        }
        for(i=0;i<m;i++)
        {
            for(j=k=0;j<puzzles[i].size();j++)k|=1<<puzzles[i][j]-'a';
            for(j=k;j;j=j-1&k)if(j>>puzzles[i][0]-'a'&1)ans[i]+=a[j];
        }
        return ans;
    }
};
'''

'''
class Solution {
public:
    unordered_map<int,int>mp;
    bool vis[27];
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        for(int i=0;i<words.size();i++){
            int sta=0;
            for(int j=0;j<words[i].size();j++){
                if(!vis[words[i][j]-'a']){
                    vis[words[i][j]-'a']=1;
                    sta|=(1<<(words[i][j]-'a'));
                }
            }
            memset(vis,0,sizeof(vis));
            mp[sta]++;
        }
        vector<int> A;
        for(int i=0;i<puzzles.size();i++){
            int n=puzzles[i].size(),ans=0;
            int tp=1<<n;
            for(int j=1;j<tp;j++)if(j&1){     ##这里 j&1 包含了 对于第一位的判断。。
                int sta=0;
                for(int k=0;k<n;k++){
                    if(j&(1<<k)){
                        sta|=(1<<puzzles[i][k]-'a');
                    }
                }
                ans+=mp[sta];
            }
            A.push_back(ans);
        }
        return A;
    }
};
'''


res = Solution().findNumOfValidWords(["apple","pleas","please"],["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"])

print(res)

