using System;

namespace LeetCode._1.TwoSum
{
    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {
            Array.Sort(nums);
            int[] result = new int[2];
            if (nums == null)
            {
                throw new NullReferenceException();
            }
            if (nums != null && nums.Length > 0)
            {
                result[0] = 0;
                result[1] = 1;
            }
            while (nums[result[0]] + nums[result[1]] != target)
            {
                if (nums[result[0]] + nums[result[1]] < target && result[1] < nums.Length - 1)
                {
                    result[1]++;
                }
                else if (nums[result[0]] + nums[result[1]] < target && result[1] == nums.Length - 1)
                {
                    if (result[0] + 1 < result[1])
                    {
                        result[0]++;
                    }
                    else
                    {
                        return null;
                    }
                }
                else if (nums[result[0]] + nums[result[1]] > target && result[1] > result[0] + 1)
                {
                    result[1]--;
                }
                else
                {
                    return null;
                }
            }
            return result;
        }

        public void Test1()
        {
            var result = TwoSum(new int[] { 1, 2, 7, 11, 15 }, 9);
            if (result != null)
            {
                Console.WriteLine($"[{result[0]}, {result[1]}]");
            }
        }
    }
}