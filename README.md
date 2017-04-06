Practice tasks from www.leetcode.com

This project is trying to store all the Python scripts wrote for the tasks from www.leetcode.com.

## Code Notes

* **Two pointers**

This method is trying to define two pointers for a list, one starts from the leftmost, and the other starts, and a while loop is used to push these points to traverse to the middle of the list, in this case try to find out the element which fulfills the condition.
```
while left < right:
   if nums[left] + nums[right] == target:
      result.append([nums[i],nums[left],nums[right]])
      right -= 1
      left += 1
      while left < right and nums[left] == nums[left-1]:
         left += 1
      while left < right and nums[right] == nums[right+1]:
         right -= 1
   elif nums[left] + nums[right] < target:
      left += 1
   else:
      right -=1

```

* **Depth-First Search**

This algorithm is to traverse all the elements in the giving list *nums* and return the path it has traversed, if the sum of the visited vertices equal to *target*, the path will be added and sent to the result, if the sum of the path it has traversed is equal or below 0, it considers the vertex has a dead end, so thealgorithm backs up to the parent and tries to continue visiting unvisited vertices from there.

```
def dfsfunc(self, nums, target, index, path, result):
        if target < 0:
            return
        elif target == 0:
            result.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfsfunc(nums, target - nums[i], i, path + [nums[i]], result)
```
