def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Only alphanumeric
    if not s.isalnum():
        return False

    # Rule 3: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 4 + 5: Numbers, if present, must be at the end and cannot start with 0
    for i, char in enumerate(s):
        if char.isdigit():
            # First number cannot be '0'
            if char == "0":
                return False
            # After first digit, everything must be digits
            if not s[i:].isdigit():
                return False
            break  # no need to check further

    return True


if __name__ == "__main__":
    main()
