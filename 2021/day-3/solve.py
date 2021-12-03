#! /usr/bin/env python3
import timeit
#### Helper Functions ####
def parseLst(idx: int, lst: list[str], findWhat: str) -> tuple:
  if idx == 12 or len(lst) == 1: 
    return ('DONE', 12)
  o, z = sum(1 for num in lst if num[idx] == "1"), sum(1 for num in lst if num[idx] == "0")
  match findWhat:
    case "Common":
      if o > z or o == z:
        return ('1', idx)
      else:
        return ('0', idx)
    
    case _:
      if o > z or o == z:
        return ('0', idx)
      else:
        return ('1', idx)

def findValue(lst: list[str], tup: tuple, findWhat: str) -> int:
  (n, idx) = tup
  if len(lst) == 1 or idx == 12:
    return lst[0]
  else:
    newLst = [num for num in lst if num[idx] == n]
  return findValue(newLst, parseLst(idx+1, newLst, findWhat), findWhat)

#### Parts ####
def part1(lst: list[str]) -> int:
  ep, g = '', ''
  for i in range(0, 12):
    o, z = sum(1 for num in lst if num[i] == "1"), sum(1 for num in lst if num[i] == "0")
    if z < o: 
      ep += '0' 
    else: 
      ep += '1'
  g = g.join('1' if x == '0' else '0' for x in ep)
  return int(ep, 2) * int(g, 2)

def part2(lst: list[str]) -> int:
  v1 = findValue(lst, parseLst(0, lst, "Common"), "Common")
  v2 = findValue(lst, parseLst(0, lst, "Least"), "Least")
  return int(v1,2) * int(v2, 2)


def main():
  start = timeit.default_timer()

  nums = [line.rstrip() for line in open("input.txt")]
  print(f"--------Advent of Code 2021 [Day 3]--------")
  print(f"[X] Part 1 Answer: {part1(nums)}\n[X] Part 2 Answer: {part2(nums)}\n")
  stop = timeit.default_timer()
  print('Time: ', stop - start)  

if __name__ == "__main__": main()