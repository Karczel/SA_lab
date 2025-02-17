class AddPlugin:
    def __str__(self):
        return "add"

    def execute(self, b, a):
        print(f'Adding {a} and {b}: {a + b}')
