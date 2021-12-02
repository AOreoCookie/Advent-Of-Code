#! /usr/bin/env python3

def main():
  nums = [int(num.rstrip()) for num in open("input.txt")]
  p1 = sum(1 for i, j in zip(nums, nums[1:]) if i < j)
  p2 = sum(1 for i, j, k, l in zip(nums, nums[1:], nums[2:], nums[3:]) if i+j+k < j+k+l)
  print(f"--------Advent of Code 2021 [Day 1]--------")
  print(f"[X] Part 1 Answer: {p1}\n[X] Part 2 Answer: {p2}\n")
  
if __name__ == "__main__": main()