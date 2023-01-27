class Lambda:
    def __init__(self, code):
        self.code = code

    def to_function(self):
        code = self.code
        python_code = ''
        skip_index = -1
        for r, i in enumerate(code):
            if r == skip_index:
                continue
            if i == 'L':
                try:
                    code[r + 1]
                except IndexError:
                    assert False, "No variable after lambda"
                python_code += f'lambda {code[r + 1]}'
                skip_index = r + 1
            elif i == '.':
                python_code += ':'
            else:
                python_code += i
        return eval(python_code)


if __name__ == "__main__":
    with open("examples/identity.lambda", "r") as f:
        lambda_code = f.read()
        print(lambda_code)
        output_function = Lambda(lambda_code).to_function()
        print(output_function(2))
