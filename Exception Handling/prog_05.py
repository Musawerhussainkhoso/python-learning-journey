#One Advanced Practice Program
try:
    numbers = [10, 20, 30]

    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index out of range!")

except ValueError:
    print("Please enter a valid integer!")

finally:
    print("Execution finished.")