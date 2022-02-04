"""An example function definition."""

"""Example 1."""
# def my_max(a: int, b: int) -> int:
#    """Returns the largest argument."""
#    if a >= b:
#        return a
#    else: 
#        return b


# x: int = 6
# y: int = 5 + 2
# z: int = my_max(x, y)

# print(z)

"""Example 2."""
# def hello_n(n: int) -> int:
#    """example."""
#    return "hello " + str(n)


# print(hello_n(3))

"""Example 3."""


def my_max(a: int, b: int) -> int:
    """Returns largest argument."""
    if a >= b:
        return a

    return b


print(my_max(10, 0))
