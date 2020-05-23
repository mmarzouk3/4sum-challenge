#Author Mariam Marzouk
#Solution for LeetCode challenge at https://leetcode.com/problems/4sum/
#Solution is O(n^4) time complexity because we have 4 nested loops iterating over nums.
#Space complexity is order O(n), since at most the solution set is C(n, 4) ("n choose 4").

#Beginner-friendly intution for algorithm:
#Our goal is to see if, given a list of numbers and a target, whether there
#exists a sum of 4 numbers whose sum equals the target. The basic approach
#we use is to set up 4 pointers, allowing us to iterate over the list
#to check all possible sums of 4. We are basically checking "n choose 4" sums,
#if you're familair with combinations from combinatorics.

def four_sum(nums, target):
    size = len(nums)
    result = []
    for i in range(0,size):
        for j in range(1,size):
            for k in range(2,size):
                for l in range(3,size):
                  if indices_are_different(i,j,k,l):
                      sum = nums[i] + nums[j] + nums[k] + nums[l]
                      if target == sum:
                          sum_list = [nums[i], nums[j], nums[k], nums[l]]
                          sum_list = sorted(sum_list)
                          if len(result) == 0:
                            result.append(sum_list)
                          else:
                            found = False
                            for list_ in result:
                              if list_ == sum_list:
                                found = True
                            if not found:
                              result.append(sum_list)
                        
    return result

def indices_are_different(i, j, k, l):
  list1 = [i, j, k, l]
  size = len(list1)
  for index in range(0, size):
      num_to_compare = list1[index]
      temp_list = list(list1)
      temp_list.pop(index)
      for num in temp_list:
          if num == num_to_compare:
              return False
  return True


if __name__ == "__main__":
  #change nums and target to test the code
  nums = [1, 0, -1, 0, -2, 2]
  target = 0
  result = four_sum(nums, target)
  print(str(result))