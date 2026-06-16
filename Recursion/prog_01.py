#Write a recursive function to print numbers from N to 1.
def countdown(n):
    if n == 0:  # Base case
        return

    countdown(n - 1)
    print(n)

countdown(5)