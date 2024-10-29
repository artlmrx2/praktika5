async def prime_factors(number: int) -> list:
    factors = []
    divisor = 2
    
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
        if divisor * divisor > number:
            if number > 1:
                factors.append(number)
            break
            
    return factors