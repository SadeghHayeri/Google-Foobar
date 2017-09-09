def answer(n):
    n = int(n)

    table = {1: 0, 2: 1}

    def answer_helper(n):
        if n in table:
            return table[n]

        if n % 2 != 0:
            table[n] = min(answer_helper((n + 1) / 2) + 2,
                           answer_helper((n - 1) / 2) + 2)
        else:
            table[n] = answer_helper(n / 2) + 1

        return table[n]

    return answer_helper(n)
