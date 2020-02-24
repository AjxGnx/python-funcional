def calculate_p_escalar(t1, t2):
    result = 0

    for i in range(len(t1)):
        result += (t1[i] * t2[i])

    return result


print(calculate_p_escalar((3, 5), (2, 3)))
