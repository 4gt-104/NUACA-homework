# Bulb Inversion Assignment

## Problem Statement

You are given a row of **N** bulbs, numbered from **1** to **N**, all of which are initially off (unlit). The task involves performing **K** consecutive linear inversions on this row of bulbs.

### What is a Linear Inversion?
A linear inversion inverts the state of every **P**-th bulb in the row. This means:
- If the bulb is off, it will be turned on.
- If the bulb is on, it will be turned off.

For example, if **P = 3**, then bulbs at positions 3, 6, 9, etc., will be inverted.

### Goal
After performing all **K** inversions, you need to determine how many bulbs remain lit.

## Example

Given:
- **N = 10** (number of bulbs)
- **P = 3** (every 3rd bulb is inverted)
- **K = 2** (2 consecutive inversions)

The sequence of operations would look like this:
1. After the first inversion (P = 3): Bulbs at positions 3, 6, 9 are lit.
2. After the second inversion (P = 3): Bulbs at positions 3, 6, 9 are toggled back to off, leaving all bulbs unlit.

Thus, after all the inversions, **0 bulbs** remain lit.

## Task
Write a program that:
1. Takes **N** (the number of bulbs), **P** (the interval of bulbs to invert), and **K** inversions as input.
2. Simulates the inversion process.
3. Outputs the number of bulbs that remain lit after all inversions.

## Input
- **N**: Integer (1 ≤ N ≤ 10^5) – the number of bulbs.
- **P**: Integer (1 ≤ P ≤ N) – the interval at which bulbs are inverted.
- **K**: Integer (1 ≤ K ≤ 1000) – the number of consecutive inversions.

## Output
- The number of bulbs that remain lit after all **K** inversions.

## Assumptions
- All bulbs are initially off.
- Bulb numbering starts from 1.


## Requirements

The program doesn't rely on any external packages or modules beyond those available in the Python3 standard library, so it should run smoothly with ``Python`` versions ``~= 3.8``.

## How to Run the Program
1. Input the values of **N**, **P**, and **K** in `INPUT.TXT`.
2. Run the following block of code.

```bash
python3 main.py
```

## Answer Explanation

The Python program provided calculates how many bulbs remain lit after performing a series of consecutive linear inversions on a row of bulbs. Below is a detailed breakdown of the solution:

### Input
The program reads input from `INPUT.TXT`, which contains two lines:
1. The first line contains two integers: the total number of bulbs (**N**) and the number of inversions (**K**).
2. The second line contains a list of integers representing the positions of the bulbs to be inverted during each of the **K** inversions.

### Key Components

- **GCD and LCM**:
  - The **gcd(a, b)** function calculates the greatest common divisor of two numbers **a** and **b**, which is used to compute the least common multiple (LCM) efficiently.
  - The **lcm(a, b, number_of_bulbs)** function computes the least common multiple of two numbers **a** and **b** but only returns the LCM if it is less than or equal to the total number of bulbs, ensuring it is relevant for this problem.

- **Inversion Tracking**:
  - The program keeps track of inversions using a list called **effective_inversions**, which contains 50 boolean values (one for each inversion type). If an inversion type is encountered, its boolean value toggles from `False` to `True` (or vice versa), indicating the inversion is active.

- **Merging Inversions**:
  - The **merge(divisioner, coef)** function updates the **map_data** dictionary. This dictionary keeps track of how many bulbs are affected by each inversion (or combination of inversions) and stores the result in a coefficient (**coef**). If the coefficient becomes zero after combining inversions, the entry is removed.

- **Main Loop**:
  - For each inversion in **effective_inversions**, the program first checks whether that inversion is active. If so, it iterates over the current inversions stored in **map_data** and computes their LCM with the new inversion using the **lcm()** function. This helps in determining which bulbs are affected by multiple inversions.
  - The **merge()** function is then used to update the affected bulbs.

### Final Calculation
- After processing all inversions, the program calculates how many bulbs remain lit by iterating over the **map_data** dictionary. The key represents the position of the bulbs being inverted, and the value represents the coefficient that determines how many of those bulbs are still lit.
- The final result is written to `OUTPUT.TXT`.

### Example:
For an input of:

```
10 2
3 3
```

- There are 10 bulbs, and two inversions are performed on the 3rd bulb. After both inversions, all bulbs are turned off, so the result will be `0`, indicating that no bulbs remain lit. This value is written to `OUTPUT.TXT`.