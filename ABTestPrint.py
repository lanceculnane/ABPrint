# A/B test from O'reilly's 'data science from scratch'
from __future__ import division
import math

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x-mu)/ math.sqrt(2) / sigma)) / 2
# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# it's between if it's less than hi, but not less than lo
def  normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# it's outside if it's not Between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# calculating probability of z being in tails- two-sided p value
def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

def estimated_parameters(N,n):
    """for an ad with total N reached and n clicks"""
    p = n/N    #gives probability of clicking ad
    sigma = math.sqrt((p * (1-p))/N)  #this estimates std dev
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A)/ math.sqrt(sigma_A ** 2 + sigma_B ** 2)

print ">>>>>><<<<<<"*20
N_A = int(raw_input("N_A: "))
n_A = int(raw_input("n_A: "))
N_B = int(raw_input("N_B: "))
n_B = int(raw_input("n_B: "))
z = a_b_test_statistic(N_A, n_A, N_B, n_B)
p = two_sided_p_value(z)
print "z-score: ", z
print "two-sided p value: ", p
