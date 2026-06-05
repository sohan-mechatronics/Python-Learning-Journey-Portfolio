def check_prime(num):

    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            count += 1

    if count == 2:
        return "Prime Number"

    else:
        return "Not Prime Number"


number = int(input("Enter Number: "))

print(check_prime(number))