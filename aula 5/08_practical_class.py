def val_int(question, min, max):
    x = int(input(question))
    while(x < min or x > max):
        x = int(input(question))
    return x
def factorial (num):
    """_summary_
    function that calculates the factorial of an integer    
    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    fact = 1
    if num == 0:
        return fact
    #this part only executes if num > 0
    for i in range(1, num + 1, 1):
        fact *= i
    return fact

x = val_int('Enter a number to calculate the factorial: ', 0, 99999)
print(f"{x}! = {factorial(x)}")