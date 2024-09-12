"""
    Define a function isPrime which purpose is to determine if
    the number it receives as argument is a prime number or not.
    
    Step1:
        test the argument received to ensure it is an int > 1
    Step2:
        with the help of a loop try to divide the argument received 
        (lets call it "number") by 2,3,4,5, up to number-1
        For instance, if number is 17 you can test: 2,3,4,5,...,15,16
        Ex: if number % 2 == 0 then 2 is a divisor of number
        As soon as you find a divisor of "number" you can return False
    Step3:
        At the end of the loop, you will have tested all possible
        divisor of number, you can return True: "number" is a 
        prime number
"""

class ArgumentError(Exception):
    """
    An exception related to a problem with a function argument
    """
    pass

def isPrime(number):
    """
    isPrime() test if a number received as argument is a prime number or not
    Parameters
    ----------
    number : an int
        The number to be tests

    Raises
    ------
    ArgumentError if the arguement received is not an int.

    Returns
    -------
    bool: True if the argument is a prime number False if not.

    """
    if isinstance(number, int):     
        if number > 1:
            divisor=2
            # The purpose of this loop is to divide "number" by
            # 2,3,4, ... up to number-1 to check if there is a divisor of 
            # "number"
            # If we don't find any divisor, "number" is a prime number
            
            while divisor < number:
                if number % divisor == 0:
                    return False
                divisor = divisor + 1  
                
            return True
        else:
            return False
    else:
        raise ArgumentError("Wrong kind of argument: an int is expected !")



tests=[-1,2,"abc",4,5,6,7,3.4, 11,26,27,1233]

for e in tests:
    try:
        if isPrime(e):
            print(e, "is a prime number")
        else: 
            print(e,"is NOT a prime number")
    except ArgumentError as ex:
        print("With the argument", e)
        print("an exception is detected:", ex)