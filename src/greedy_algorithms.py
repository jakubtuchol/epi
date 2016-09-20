import attr
from attr.validators import instance_of


def three_sum(target, ls):
    """
    Question 18.5: Check if three numbers within input
    array sum to target
    """
    ls = sorted(ls)

    for idx, elt in enumerate(ls):
        if two_sum(target - elt, ls[:idx] + ls[idx + 1:]):
            return True
    return False


def two_sum(target, ls):
    """
    Check if two numbers within input array sum to target
    """
    complements = set()
    for num in ls:
        if num in complements:
            return True
        complements.add(target - num)

    return False


def find_majority_element(array):
    """
    Question 18.6
    """
    majority_elt = None
    count = 0
    for elt in array:
        if elt != majority_elt:
            if count == 0:
                majority_elt = elt
                count = 1
            else:
                count -= 1
        else:
            count += 1
    return majority_elt


@attr.s
class GasCity(object):
    id = attr.ib(validator=instance_of(str))
    gas = attr.ib(validator=instance_of(int))
    to_next = attr.ib(validator=instance_of(int))


@attr.s
class CityAndGas(object):
    id = attr.ib(validator=instance_of(str))
    remaining = attr.ib(validator=instance_of(int))


def find_ample_city(cities, mpg=20):
    """
    Question 18.7: Given a vector of cities with
    gas and mileages to each city, calculate the first
    city that you can start from and reach all other
    cities from
    """
    num_cities = len(cities)
    remaining_gallons = 0
    start_city = CityAndGas(id='', remaining=0)
    for idx in xrange(1, num_cities):
        last_city = cities[idx - 1]
        remaining_gallons += last_city.gas - last_city.to_next / mpg
        if remaining_gallons < start_city.remaining:
            start_city = CityAndGas(
                id=cities[idx].id,
                remaining=remaining_gallons
            )
    return start_city.id


def trapped_water(heights):
    """
    Question 18.8: Compute the maximum water
     trapped by a pair of vertical lines
    """
    max_water = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        max_water = max(
            max_water,
            (right - left) * min(heights[left], heights[right])
        )
        if heights[left] > heights[right]:
            right -= 1
        elif heights[left] < heights[right]:
            left += 1
        else:
            left += 1
            right -= 1
    return max_water
