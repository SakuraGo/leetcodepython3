class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = len(nums) - 1
            if nums[i] + nums[k] + nums[k - 1] < target:
                res.append(nums[i] + nums[k] + nums[k - 1])
            elif nums[i] + nums[j] + nums[j + 1] > target:
                res.append(nums[i] + nums[j] + nums[j + 1])
            else:
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    res.append(s)
                    if s == target:
                        return target
                    elif s < target:
                        j += 1
                    else:
                        k -= 1
        res.sort(key=lambda x: abs(x - target))
        return res[0]

'''
    Arrays.sort(nums);

    int sum=nums[0]+nums[1]+nums[nums.length-1];

    for (int i = 0; i <nums.length-2 ; i++) {
        int j=i+1;
        int k=nums.length-1;
        while (j<k){
            int cur=nums[i]+nums[j]+nums[k];
            if(cur<target&&Math.abs(target-sum)<=Math.abs(cur-target)){
                
                j++;
            }else if(cur==target){
                return cur;
            }else if(cur>target&&Math.abs(target-sum)>=Math.abs(cur-target)){
                sum=cur;
                k--;
            }else if(cur>target&& Math.abs(target-sum)<Math.abs(cur-target)){
                     k--;
            }else if(cur<target&&Math.abs(target-sum)>Math.abs(cur-target)){
                sum=cur;
                j++;
            }


        }
    }
    return sum;
'''