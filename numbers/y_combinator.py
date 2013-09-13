'''
The Y combinator is a fixed-point combinator, a higher-order function that
takes a function as input and returns the fixed point of that function. More
specifically, if f is a function with fixed point x,

    x = (Y f) = (f (Y f)) = (f x)
'''

def Y(f):
    def g(x):
        return f(x, x)
    def h(x):
        return f(x, x)
    return g(h)
