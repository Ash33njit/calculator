def population_variance(data):
    u = population_mean(data)
    leng = len(data)
    return round(division(leng, sum([(element - u) ** 2 for element in data])), 3)