#!/usr/bin/env python3
import time

def task_one(n):
    """Simulate a CPU-bound task: sum of squares."""
    total = 0
    for i in range(n):
        total += i * i
    return total

def task_two(n):
    """Simulate another task: string concatenation."""
    result = ""
    for i in range(n):
        result += str(i)
    return result

def task_three(n):
    """Simulate I/O-bound task with sleep."""
    for _ in range(n):
        time.sleep(0.01)

def main():
    print("Starting tasks...")
    task_one(10000)
    task_two(5000)
    task_three(5)
    print("Tasks complete.")

if __name__ == "__main__":
    main()
