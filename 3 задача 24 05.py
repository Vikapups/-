def three_args(a, b = None, c = None):
    if a is not None and ( b is None or b is not None) and (c is None or c is not None):
        print(f'переданы аргументы:{a, b, c}')
        
three_args(2, 5, 6)