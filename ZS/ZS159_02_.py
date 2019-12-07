from typing import  List
class Solution:

    def __init__(self):
        self._data = set()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder,key= lambda x:len(x))

        for path in folder:
            # folders = path.split("/")
            foundflag = False
            for headpath in self._data:
                if path.startswith(headpath):
                    if len(path.split("/"))> len(headpath.split("/")):
                        foundflag = True
                        break
            if foundflag is False:
                self._data.add(path)
            else:
                continue

        # for path in self._data:
        res = []
        res = list(self._data)
        return res



