def collatz(n):
    """
    collatz(n)

    Collatz application from the Collatz conjecture (more famously known as the Syrracuze conjecture):
        returns n/2 if n is even
        returns 3*n+1 if n is odd

    Parameters
    ----------
    n: int
    """
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1


def collatz_detailed(n, a, b):
    """
    collatz_detailed(n, a, b)

    Detailed version of the Collatz application from Collatz conjecture: returns the application of Collatz
    conjecture (see above function collatz), while also keeping track of the parity of the taken branchs: a gets
    increased if n is even and b gets increased if n was odd.

    This function is mainly defined for its use in an iterative call of Collatz application, as in the time-of-flight
    computation (see flight function below).

    Parameters
    ----------
    n: int
    a: int, former number of times passing by the even branch
    b: int, former number of times passing by the odd branch
    """
    if n % 2 == 0:
        return int(n/2), a+1, b
    else:
        return 3*n+1, a, b+1


def flight(n):
    """
    flight(n)

    Function returning the number (time-of-flight, t) of iterations needed to get to 1 when iteratively calling Collatz
    application.

    Parameters
    ----------
    n: int
    """
    iteration = 0
    while n != 1:
        n = collatz(n)
        iteration += 1
    return iteration


def flight_detailed(n):
    """
    flight_detailed(n)

    Detailed version of the flight function (see above). Returns the number (time-of-flight, t) of iterations needed to
    get to 1 when iteratively calling Collatz, while also keeping track of the parity of the taken branchs.
    Return a tuple: (t, #of_even_branches_taken, #of_odd_branches_taken)

    Parameters
    ----------
    n: int
    """
    a, b = 0, 0
    while n != 1:
        n, a, b = collatz_detailed(n, a, b)
    return a+b, a, b


def vect_flight(vect):
    res = []
    for n in vect:
        res.append(flight(n))
    return res


def rise(n):
    """
    rise(n)

    Function returning the number (time-of-rise, r) of iterations needed for n to get below its initial value when
    iteratively calling Collatz application.

    Parameters
    ----------
    n: int
    """
    memory = n
    iteration = 0
    if n != 1:
        while n >= memory:
            n = collatz(n)
            iteration += 1
    return iteration


def rise_detailed(n):
    """
    rise_detailed(n)

    Detailed version of the rise function (see above). Returns the number (time-of-rise, r) of iterations needed for n
    to get below its initial value when iteratively calling Collatz application, while also keeping track of the parity
    of the taken branches. Return a tuple: (r, #of_even_branches_taken, #of_odd_branches_taken)

    Parameters
    ----------
    n: int
    """
    memory = n
    a, b = 0, 0
    if n != 1:
        while n >= memory:
            n, a, b = collatz_detailed(n, a, b)
    return a+b, a, b


def vect_rise(vect):
    res = []
    for n in vect:
        res.append(rise(n))
    return res
