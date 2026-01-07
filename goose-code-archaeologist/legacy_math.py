import math

def f1(n):
    """
    Calculate the nth Fibonacci number.

    The function implements a simple recursive algorithm:
    - Base cases: if n <= 1, return n.
    - Recursive case: f1(n-1) + f1(n-2).

    Parameters
    ----------
    n : int
        The position in the Fibonacci sequence. Must be a non‑negative integer.

    Returns
    -------
    int
        The Fibonacci number at position n.

    Notes
    -----
    This implementation is for demonstration purposes and is not efficient for large n
    due to exponential time complexity. In production code, consider an iterative
    approach or memoization.
    """
    if n <= 1: return n
    return f1(n-1) + f1(n-2)

def f2(lat1, lon1, lat2, lon2):
    """
    Compute the great‑circle distance between two latitude/longitude points on Earth.

    Uses the haversine formula to calculate the shortest distance over the
    Earth's surface.

    Parameters
    ----------
    lat1, lon1 : float
        Latitude and longitude of the first point in decimal degrees.
    lat2, lon2 : float
        Latitude and longitude of the second point in decimal degrees.

    Returns
    -------
    float
        Distance in kilometers.

    Notes
    -----
    The Earth's radius is taken as 6371 km. For higher precision use an oblate spheroid model.
    """
    R = 6371  # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def p(data):
    """
    Compute the population standard deviation of a sequence of numbers.

    Parameters
    ----------
    data : Iterable[float]
        A collection of numeric values.

    Returns
    -------
    float
        The population standard deviation.

    Notes
    -----
    The function calculates the mean, then the variance as the average squared
    deviation from the mean, and finally returns the square root of the variance.
    """
    m = sum(data) / len(data)
    v = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(v)
