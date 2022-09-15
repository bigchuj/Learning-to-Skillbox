# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result

# TODO оптимизировать функцию

from math import factorial as fact


def calculating_math_func(data, calculations=dict()):

    if data not in calculations:

        calculations[data] = (fact(data), pow(data, 3))

    return pow(calculations[data][0] / calculations[data][1], 10)
