def is_prime(n):
    """
    Checks if a number n is prime using the loop-else construct.

    A prime number is a natural number greater than 1
    that has no positive divisors other than 1 and itself.
    """
    # 1. Handle the base condition:
    # A prime number must be a natural number greater than 1
    if n < 2:
        return False

    # Calculate the limit for checking divisors.
    # We only need to check up to the square root of n.
    limit = int(n**0.5) + 1

    # 2. Iterate through all possible divisors from 2 up to the limit
    for i in range(2, limit):
        # Check for divisibility
        if n % i == 0:
            # If a divisor is found, the number is NOT prime.
            # We return False and exit the function immediately.
            return False

    # 3. The 'else' block for the loop
    # (only runs if the loop completes normally,
    #  i.e., without hitting 'return False').
    # If no divisors were found, the number IS prime.
    else:
        return True

def generate_primes(upper_bound):
    for num in range(2, upper_bound + 1):
        if is_prime(num): print(num)

def user_input():
    i = 0
    while i < 3:
        i += 1
        try:
            n = input("Enter a number to test [or 'q' to quit]: ")
            if n == 'q': break # quit handler
            elif ',' in n:
                print("idih, g kelaz bgt pakai tanda koma desimal\n")
                continue
            elif 0 < float(n) < 1:
                print("Testing limits, aren't you?\n")
                continue
            elif '.' in n:
                print("Please input an integer value.\n")
                continue
            elif float(n) < 0:
                print("Please input a positive number.\n")
                continue
            n = int(n)
        except ValueError:
            print("Please input a numerical value.\n")
        else:
            break
    else:
        print("Too many invalid attempts.\n")
        n = 't.m.i.a.'

    return n

def main():
    print("\nPRIME CHECKER")
    while True:
        n = user_input()
        if n in ['q', 't.m.i.a.']:
            print()
            break
        elif n == 1:
            print("  You have submitted")
            print("  the multipilicative identity,")
            print("  a natural number which is")
            print("  neither a prime nor a composite number.\n")
        elif is_prime(n):
            print(f"{n} is a prime number.\n")
        else:
            print(f"{n} is a composite number.\n")

# --- executive part of the code ---
'''
if __name__ == '__main__':
    main()
'''

generate_primes(1000)
# ----------------------------------
