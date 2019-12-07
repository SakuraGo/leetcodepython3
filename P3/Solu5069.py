

class Solution:
    def lastSubstring(self, s: str) -> str:
        temp,index = 'a',0
        comp = False
        length = 0
        tempStr = ''
        for ind,c in enumerate(s):
            # if comp is True:
            #     if s[ind-length:ind+1] > s[index:index+length+1]:
            #         index = ind
            #         comp = False
            #         length = 0

            if ord(c) > ord(temp):
                temp = c
                index = ind
                tempStr = c
            elif c == temp:
                if s[ind:] > s[index:]:
                    index = ind
                    temp = c



        return s[index:]

print(ord('b'))

for index,c in enumerate("qwer"):
    print(index)

if "qwer" > "gg":
    print("1")