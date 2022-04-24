def a(input):
    pattern = input.split('/')
    for item in pattern:
        if item.startswith('pg.'):
            return item.split('.')[1]
    return 0

    # pattern = re.search(r"[0-9]+", input)
    # return pattern.group()
