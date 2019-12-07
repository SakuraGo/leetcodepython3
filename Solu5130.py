# 5130. 最小的必要团队  显示英文描述
# 题目难度 Hard
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
#
# 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。
#
# 我们可以用每个人的编号来表示团队中的成员：例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
#
# 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按任意顺序返回答案，本题保证答案存在。

# 输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# 输出：[0,2]

from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dataDic = {}
        resDic = {0:[]}
        kcDic = {}
        for kecheng in req_skills:
            kcDic[kecheng] = len(kcDic)

        for i in  range(len(people)):
            s = 0  ##个人技能表示
            for skill in people[i]:
                s +=  1<<kcDic[skill]

            for combin , plis in list(resDic.items()):
                newPlis = plis + [i]
                newComb = combin | s
                if newComb not in resDic.keys() or len(newPlis) < len(resDic[newComb]):
                    resDic[newComb] = newPlis
                    print(newComb,newPlis)

        print(resDic)

        return  resDic[(1<<len(req_skills))-1]

'''

class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):

        d = {}
        for ss in req_skills:
            d[ss] = len(d)
        f = {0: []}
        for i in range(len(people)):
            p = people[i]
            s = 0
            for x in p:
                s += (1 << d[x])
            for t, l in list(f.items()):
                r = s | t
                q = l + [i]
                if r not in f or len(f[r]) > len(q):
                    f[r] = q
        return f[(1 << len(d)) - 1]


'''
print(((1<<3)-1))
rr = ["java","nodejs","reactjs"]
pp = [["java"],["nodejs"],["nodejs","reactjs"]]
res = Solution().smallestSufficientTeam(rr,pp)

print(res)