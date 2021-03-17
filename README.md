# Triangle-problem

This script reads from the given triangle.txt file and outputs the sum of the maximum adjacent values going down the triangle one element at a time. For this triangle, the sum my function produced is 732,506. My main method was to use dynamic programming with a bottom up approach. I broke down the problem into many subproblems, modeling it with an n x n matrix to store the local maximum sums at each step in iteration. This way, I would not have to check every possible path or use recursion to make the run time less efficient.

Initially, I had interpreted the problem incorrectly and thought I needed to add the maximum of each line in the triangle to the total sum, so I was instructed to recreate my solution. In recreating it, before using the dynamic programming method I tried to model the triangle using a binary search tree, quickly realizing that would not work since the elements in the triangle were added to the tree linearly, so two or more elements in the same line would be counted. I still have included this implementation as it was a part of my attempt.
