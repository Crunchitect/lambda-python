not_my_data = set(globals())

TRUE = lambda t: lambda f: t
FALSE = lambda t: lambda f: f

IDENTITY = lambda x: x

all_vars_str = set(globals()) - not_my_data - {'not_my_data'}
all_vars = set(globals()) - not_my_data - {'not_my_data', 'all_vars_str'}
all_vars = [eval(i) for i in all_vars]

if __name__ == '__main__':
    print(all_vars, all_vars_str)
