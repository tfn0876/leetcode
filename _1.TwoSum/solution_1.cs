using System;

namespace LeetCode._1.TwoSum
{
    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {
            int[] sortedNums = new int[nums.Length];
            int[] sortedPositiveNums = new int[nums.Length];
            Array.Copy(nums, sortedNums, nums.Length);
            Array.Sort(sortedNums);
            Array.Copy(sortedNums, sortedPositiveNums, nums.Length);
            // For sliding number to start from 0
            for (int i = 0; i < sortedPositiveNums.Length; i++)
            {
                sortedPositiveNums[i] -= sortedNums[0];
            }
            int[] result = new int[2];
            if (sortedNums == null)
            {
                throw new NullReferenceException();
            }
            for (int i = 0; i < sortedPositiveNums.Length; i++)
            {
                int newTarget = target - 2 * sortedNums[0] - sortedPositiveNums[i];
                if (newTarget < 0)
                {
                    return null;
                }
                int findIndex = findNumber(newTarget, sortedPositiveNums, i + 1, sortedPositiveNums.Length - 1);
                if (findIndex > 0)
                {
                    return convertIndex(nums, sortedNums, new int[] { i, findIndex });
                }
            }
            return result;
        }
        public int[] convertIndex(int[] nums, int[] sortedNums, int[] toConvert)
        {
            int?[] result = new int?[2];
            for (int i = 0; i < nums.Length; i++)
            {
                if (result[0] == null && nums[i] == sortedNums[toConvert[0]])
                {
                    result[0] = i;
                }
                else if (result[1] == null && nums[i] == sortedNums[toConvert[1]])
                {
                    result[1] = i;
                }
            }
            Array.Sort(result);
            return new int[] { result[0].Value, result[1].Value };
        }
        public int findNumber(int target, int[] num, int start, int end)
        {
            if (start > end) { return -1; }
            int middle = (start + end) / 2;
            if (num[middle] == target) return middle;
            else if (num[middle] > target) return findNumber(target, num, start, middle - 1);
            else return findNumber(target, num, middle + 1, end);
        }

        public void Test()
        {
            Test1();
            Test2();
            Test3();
        }

        public void Test1()
        {
            Console.WriteLine("Test 1");
            Console.WriteLine($"[3, 3], 6");
            var result = TwoSum(new int[] { 3, 3 }, 6);
            if (result != null)
            {
                Console.WriteLine($"[{result[0]}, {result[1]}]");
            }
        }

        public void Test2()
        {
            Console.WriteLine("Test 2");
            Console.WriteLine($"[-1, -2, -3, -4, -5], -8");
            var result = TwoSum(new int[] { -1, -2, -3, -4, -5 }, -8);
            if (result != null)
            {
                Console.WriteLine($"[{result[0]}, {result[1]}]");
            }
        }
        public void Test3()
        {
            Console.WriteLine("Test 3");
            Console.WriteLine($"[2, 7, 11, 15], 9");
            var result = TwoSum(new int[] { 2, 7, 11, 15 }, 9);
            if (result != null)
            {
                Console.WriteLine($"[{result[0]}, {result[1]}]");
            }
        }
    }
}