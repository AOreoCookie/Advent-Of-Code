#! /usr/bin/env python3

from re import search, match

def main():
  nP = r'[0-9]+'
  up = sum(-int(search(nP, line).group()) for line in open("input.txt") if bool(match("up", line))) 
  down = sum(int(search(nP, line).group()) for line in open("input.txt") if bool(match("down", line)))
  p1 = sum(int(search(nP, line).group()) for line in open("input.txt") if bool(match("forward", line))) * (up + down)

  (x, y, aim) = (0, 0, 0)
  for line in open("input.txt"):
    (cmd, val) = (line.split()[0], int(line.rstrip().split()[1]))
    (x, y) = (x+val, y+aim*val) if cmd == "forward" else (x , y)
    aim = aim - val if cmd == "up" else aim + val if cmd == "down" else aim
    p2 = (x * y)
    
  print(f"--------Advent of Code 2021 [Day 2]--------")
  print(f"[X] Part 1 Answer: {p1}\n[X] Part 2 Answer: {p2}")
  
if __name__ == "__main__": main()