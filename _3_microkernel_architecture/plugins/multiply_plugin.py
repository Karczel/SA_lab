class MultiplyPlugin:
    def __str__(self):
        return "multiply"

    def execute(self, b, a):
        print(f'Multiplying {a} and {b}: {a * b}')
