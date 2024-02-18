def pont(n):
    sequence = [0,1]
    if n <= 0:
        return "write chiclo > 0"
    elif n ==1:
        return [0]
    elif n == 2:
        return sequence
    else:
        for i in range(2, n):
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
            return sequence
print(pont(100))