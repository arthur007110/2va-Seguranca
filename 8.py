# a)
N = 13962799
e = 3
value_to_sign = 821
signature = 8674413

verification = pow(signature, e, N)
verification == value_to_sign
# Resultado retornado: True

# b)
N = 34300129
e = 61
value_to_sign = 2478
signature = 27535246

verification = pow(signature, e, N)
verification == value_to_sign
# Resultado retornado: False

# c)
N = 5898461
e = 23
value_to_sign = 419
signature = 2607727

verification = pow(signature, e, N)
verification == value_to_sign
# Resultado retornado: False
