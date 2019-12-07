# 76. 最小覆盖子串
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tlen = len(t)
        slen = len(s)
        if tlen>slen:
            return ''
        targetDic = {}
        for c  in t:
            if c in targetDic.keys():
                targetDic[c] += 1
            else:
                targetDic[c] = 1
        compDic = {}
        for key in targetDic.keys():
            compDic[key] = 0
        for i in range(tlen):
            if s[i] in compDic.keys():
                compDic[s[i]] += 1

        if targetDic == compDic:
            return s[:tlen]

        minLen = 99129
        minPos = 0
        bflag = False
        i = 0
        j = tlen-1
        def isValidComp(tarDic,cDic):
            for k in tarDic.keys():
                if tarDic[k]>cDic[k]:
                    return False

            return True

        while j < slen and i<slen:

            if isValidComp(targetDic,compDic):
                bflag = True
                print('i===' + str(i))
                if (j-i)<minLen:
                    minLen = j-i
                    minPos = i
                i += 1
                print('delete:'+str(i-1))
                if s[i-1] in compDic.keys():
                    compDic[s[i-1]] -=1
            else:
                print('j:'+str(j))
                j+= 1
                if j>=slen:
                    print("asdf")
                    break
                if s[j] in compDic.keys():
                    compDic[s[j]] += 1


        if bflag is False:
            return ''
        return s[minPos:minPos+minLen+1]

res = Solution().minWindow("aaaaaaaaaaaabbbbbcdd","abcdd")
print(res)



# aaa = [1,2,3,5]
# bbb = [1,1,5,5]
# print(aaa>bbb)
#
# qwer = {'q':3,'p':5}
# print(qwer.values())






# def minWindow(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """
#
#     if not t or not s:
#         return ""
#
#     # Dictionary which keeps a count of all the unique characters in t.
#     dict_t = Counter(t)
#
#     # Number of unique characters in t, which need to be present in the desired window.
#     required = len(dict_t)
#
#     # left and right pointer
#     l, r = 0, 0
#
#     # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
#     # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
#     formed = 0
#
#     # Dictionary which keeps a count of all the unique characters in the current window.
#     window_counts = {}
#
#     # ans tuple of the form (window length, left, right)
#     ans = float("inf"), None, None
#
#     while r < len(s):
#
#         # Add one character from the right to the window
#         character = s[r]
#         window_counts[character] = window_counts.get(character, 0) + 1
#
#         # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
#         if character in dict_t and window_counts[character] == dict_t[character]:
#             formed += 1
#
#         # Try and co***act the window till the point where it ceases to be 'desirable'.
#         while l <= r and formed == required:
#             character = s[l]
#
#             # Save the smallest window until now.
#             if r - l + 1 < ans[0]:
#                 ans = (r - l + 1, l, r)
#
#             # The character at the position pointed by the `left` pointer is no longer a part of the window.
#             window_counts[character] -= 1
#             if character in dict_t and window_counts[character] < dict_t[character]:
#                 formed -= 1
#
#             # Move the left pointer ahead, this would help to look for a new window.
#             l += 1
#
#         # Keep expanding the window once we are done co***acting.
#         r += 1
#     return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
#


'''
def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

'''



