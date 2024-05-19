### Question

Calculate a raised to the power b.

a raised to the power of a number is multiplying a that many times.
a^b = a _ a _ a _ a _ ... _ b.
2^4 = 2 _ 2 _ 2 _ 2

we can write 2^4 = 2 _ 2^3,
Hence, a^b = a _ a^b-1

when b==1, a^b = a^1 = a
Hence, 2^1 = 2. So b==1 can be considered as a bases case where we return 'a' itself,

#### Solution Optimized

in prev example, we were reducing the function just by the factor of one, each time base^exponent-1, base^exponent-2, base^exponent-3
but base^exponent = base^exponent/2 \* base^exponent/2. in this case, the function is getting divided by 2 each time.
N/2 -> N/4 -> N/8 -> N/16 -> N/32 ... 1; and so one. if we calculate the time complexity for this series it will O(logN)

N/2^k = 1 => N = 2^k => k = log(N .base2) is the number of steps we take until we reach to 1 which is the base case.

we need to consider the negative for exponent as well as it really adds up to our recursive calls, better to define one for it.

pow(2, 3) = 2^3 = 8
pow(3, 2) = 3^2 = 9

pow(2, -3) = 2^-3 = (1/2^3) = (1/2)^3
pow(3, -2) = 3^-2 = (1/3^2) = (1/3)^2

we can see the pattern that x is getting divided by 1 and exponent is becoming positive, Hence we can add this condition as well.

you can see another if condition which is checking for odd and even exponents, because if exponent is even, for instance pow(3, 4) = 3^2 _ 3^2 and pow(3, 5) != 3^2 _ 3^2.
thus, for odd exponents, we need to multiply the base at the end( temp _ temp _ x).
