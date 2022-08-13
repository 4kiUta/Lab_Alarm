def f(x: int) -> float:
    float_number = x/2
    return float_number

## The ':' tells people who read the program (and some third-party libraries/programs, e. g. pylint) 
## that x should be a int. Not necessarly need to be a Int for the code to run, but it will give problems.

## The '->' tells people who read the program that the return of this function should be a float number
## -> is used to indicate the type that the function returns.


print(f.__annotations__)

## The ':' tells people who read the program (and some third-party libraries/programs, e. g. pylint) 
## that x should be a int. Not necessarly need to be a Int for the code to run, but it will give problems.

# It is accessed as f.__annotations__['x'], and doesn't have any meaning by itself. See the documentation for more information


## decorators @
