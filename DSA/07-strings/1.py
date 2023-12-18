import numpy as np

def r_squared(y, es):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        es: a list of values es by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, es = np.array(y), np.array(es)
    SEE = ((es - y)**2).sum()
    mMean = y.sum()/float(len(y))
    movement = ((mMean - y)**2).sum()
    return 1 - SEE/movement