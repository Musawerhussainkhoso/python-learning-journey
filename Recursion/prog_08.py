def is_palindrome(text: str, left: int, right: int) -> bool:
    """
    Check whether a string is a palindrome using recursion.
    """

    # Base case: all characters have been checked
    if left >= right:
        return True

    # Characters do not match
    if text[left] != text[right]:
        return False

    # Check the next inner pair
    return is_palindrome(text, left + 1, right - 1)


user_text = input("Enter a word or sentence: ")

# Remove spaces and convert to lowercase
cleaned_text = user_text.replace(" ", "").lower()

if not cleaned_text:
    print("Please enter some text.")
else:
    result = is_palindrome(
        cleaned_text,
        0,
        len(cleaned_text) - 1
    )

    if result:
        print(f'"{user_text}" is a palindrome.')
    else:
        print(f'"{user_text}" is not a palindrome.')