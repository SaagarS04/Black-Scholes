#!/usr/bin/env python
# coding: utf-8


import math
from scipy.stats import norm

def black_scholes_model_prob(s0, k, t, r, sigma): #Returns the probability of a stock reaching a price, k in a time period, t
    """
    Inputs:
    s0: The initial stock price.
    k: The predicted price of the stock.
    t: The time to expiration of the option in years.
    r: The risk-free interest rate.
    sigma: The volatility of the stock.
    Returns:
    The price of the option.
    """

    d1 = (math.log(s0 / k) + (r + sigma**2 / 2) * t) / (sigma * math.sqrt(t))
    return(norm.cdf(-d1))

def black_scholes_model(s0, k, t, r, sigma): #Returns the option price
    """
    Inputs:
    s0: The initial stock price.
    k: The strike price of the option.
    t: The time to expiration of the option in years.
    r: The risk-free interest rate.
    sigma: The volatility of the stock.
    Returns:
    The price of the option.
    """

    d1 = (math.log(s0 / k) + (r + sigma**2 / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)

    call_price = s0 * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
    return call_price


p1 = black_scholes_model_prob(10, 12, .5, .02, .7) + black_scholes_model_prob(10, 14, 1, .02, .7) #Finds the probability of either of the two cases happening
p2 = black_scholes_model_prob(10, 12, .5, .02, .7) * black_scholes_model_prob(10, 14, 1, .02, .7) #Finds the probability of both of the cases happening
pk1 = p1 - p2 #Finds the probability of one of the cases happening
pk2 = 1-pk1
k1 = 11
k2 = 10


fairOptionPrice = round((pk1 * black_scholes_model(10, k1, 1, .02, .7)) + (pk2 * black_scholes_model(10, k2, 1, .02, .7)), 2) #Finds the expected value of the stock option using the probabilities of each situation, rounded to two decimal places


print("The fair price for this warrant is: $" + str(fairOptionPrice)) #Prints the fair warrant price

