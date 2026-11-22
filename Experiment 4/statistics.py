import statistics

# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)

# Arithmetic operations
print("\nArithmetic Operations")
print("Addition:", sum(numbers))
print("Subtraction:", numbers[0] - numbers[1])
print("Multiplication:", numbers[0] * numbers[1])
print("Division:", numbers[0] / numbers[1])

# Statistical calculations
print("\nStatistical Calculations")
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Range:", max(numbers) - min(numbers))
print("Standard Deviation:", statistics.stdev(numbers))
