# https://stackoverflow.com/questions/3215168/how-to-get-character-in
degree_sign = u'/N{DEGREE SIGN}'

tests_cases = [2, 4, 23.2]

for item in tests_cases:
    print("{}{}C".format(item, degree_sign))