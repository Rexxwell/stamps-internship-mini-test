# from sympy import isprime

def printReverseOrderNumbers(numbers: list[int]) -> None:
    for i in range(len(numbers) - 1, -1, -1):
        number = numbers[i]
        
        # Do not print prime numbers
        # Manually checks that a number is not a prime number.
        if (isPrime(number)):
            continue

        # Uses an external library called sympy,
        # which needs to be installed first before the program can run.
        # elif (isprime(number)):
        #     continue

        # Replace numbers divisible by both 3 and 5 with the text "FooBar."
        elif (number % 3 == 0 and number % 5 == 0):
            print("FooBar", end=", ")

        # Replace numbers divisible by 3 with the text "Foo."
        elif (number % 3 == 0):
            print("Foo", end=", ")
        
        # Replace numbers divisible by 5 with the text "Bar."
        elif (number % 5 == 0):
            print("Bar", end=", ")
        else:
            print(f"{number}", end=", ")

def isPrime(number: int) -> bool:
    if (number <= 1):
        return False
    elif (number == 2):
        return True
    elif (number % 2 == 0):
        return False

    # Loop through numbers from 3 up to the square root of the target number
    # and verify if any division has a remainder of zero.
    # We go by steps of 2 because we can ignore checking the even numbers,
    # which we checked before.
    for i in range(3, int(number**0.5) + 1, 2):
        if (number % i == 0):
            return False
    return True

numbers = []
for i in range(1, 101):
    numbers.append(i)
printReverseOrderNumbers(numbers)