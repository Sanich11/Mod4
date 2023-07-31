a = 'ABCDAA'


def strcounter_1(s):  # Решение сложности N ** 2
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)


# strcounter_1(a)


def strcounter_2(s):    # Решение сложности N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)

strcounter_2(a)
