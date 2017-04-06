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

