def is_prime(number):
    result = "True"
    for i in range(2, number):
        if number % i == 0:
            result = "False"
    print(result)

is_prime(7)

"""The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97"""