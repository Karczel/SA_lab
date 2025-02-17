class SubtractPlugin:
    def __str__(self):
        return "subtract"

    def execute(self, b, a):
        print(f'Subtracting {a} from {b}: {a - b}')
