#! /usr/bin/env python3

def main():
  upDowns = [(line.split()[0], -int(line.rstrip().split()[1])) if line.split()[0] == "up" else (line.split()[0], int(line.rstrip().split()[1])) for line in open("input.txt")]
  p1 = sum(int(line.rstrip().split()[1]) for line in open("input.txt") if line.split()[0] == "forward") * sum(tup[1] for tup in upDowns)

  (x, y, aim) = (0, 0, 0)
  for line in open("input.txt"):
    (cmd, val) = (line.split()[0], int(line.rstrip().split()[1]))
    (x, y) = (x+val, y+aim*val) if cmd == "forward" else (x , y)
    aim = aim - val if cmd == "up" else aim + val if cmd == "down" else aim
    p2 = (x * y)
    
  print(f"--------Advent of Code 2021 [Day 2]--------")
  print(f"[X] Part 1 Answer: {p1}\n[X] Part 2 Answer: {p2}")

if __name__ == "__main__": main()


"""
--- Part One ---
with open('input.txt') as f:
  for line in f:
    line = line.rstrip().split(" ")
    (dir, amount) = (line[0], int(line[1]))
    if dir == "forward": x = x + amount
    elif dir == "up": y = y - amount
    else: y = y + amount


"""