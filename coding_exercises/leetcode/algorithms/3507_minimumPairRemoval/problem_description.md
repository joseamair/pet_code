# 3507. Minimum Pair Removal to Sort Array I

**Ref:** [LeetCode Problem 3507](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i)

## Problem Summary

The goal of this exercise is to determine the minimum number of operations required to transform a list of integers into a **non-decreasing** (sorted) sequence.

### The Rules

You are given an integer array `nums`. You must repeatedly apply a specific operation until the array is sorted:

1. **Identify the Target Pair:** Look at all adjacent pairs in the current array.
2. **Selection Criteria:**
    * Find the pair with the **minimum sum**.
    * **Tie-Breaker:** If multiple pairs share the same minimum sum, choose the **leftmost** one (the one with the smallest index).
3. **The Operation:** Replace the selected pair with a single element equal to their sum.
4. **Repeat:** Continue this process until every element in the array is greater than or equal to the one before it.

**Output:** Return the total count of operations performed.
