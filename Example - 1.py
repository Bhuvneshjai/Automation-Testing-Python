# Python program to take integer input  in Python

n = int(input("Enter number to print : "))
arr = list(map(int, input(f"Enter {n} values : ").strip().split()))[:n]
print(f"Values of {n} are {arr}")