def nthTermOfGeometricSeries(A, B, N):
    # Calculate the common ratio
    r = B / A
    
    # Calculate the nth term using the formula
    nthTerm = A * (r ** (N - 1))
    
    return nthTerm

A = 2
B = 6
N = 5

nth_term = nthTermOfGeometricSeries(A, B, N)
print("The {}th term of the geometric series is: {}".format(N, nth_term))
