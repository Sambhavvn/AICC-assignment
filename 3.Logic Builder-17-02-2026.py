def fizz_buzz_logic(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def run_fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = fizz_buzz_logic(i)
        print(result)

        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1

    print("\n--- Counts ---")
    print("Fizz:", fizz_count)
    print("Buzz:", buzz_count)
    print("FizzBuzz:", fizzbuzz_count)

run_fizz_buzz()