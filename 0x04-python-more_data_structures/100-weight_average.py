#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    else:

        product_score = 0
        sum_weight = 0

        for score, weight in my_list:

            product_score += score * weight
            sum_weight += weight

        weighted_average = product_score / sum_weight

    return weighted_average
