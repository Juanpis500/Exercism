import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Obtain all the proper divisors
    divisors = set()
    
    for index in range(1, int(math.isqrt(number)) + 1):
        if number % index == 0:
            divisors.add(index)
            divisors.add(number // index)
            
    divisors = sorted(list(divisors))
    divisors = divisors[:-1]
    
    if sum(divisors) == number:
        return 'perfect'
    if sum(divisors) > number:
        return 'abundant'
    if sum(divisors) < number:
        return 'deficient'
    return None