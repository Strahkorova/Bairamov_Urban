
def all_variants(text):
    r = len(text)
    while r > 0:
        for i in range(len(text)):
            if i != r:
                yield text[i: r]
            else:
                break
        r -= 1


a = all_variants("abc")
for i in a:
    print(i)
