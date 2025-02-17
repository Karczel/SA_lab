from plugins import *


class Microkernel:
    def __init__(self):
        self.plugin = {}

    def load_method(self, method):
        self.plugin[method.__str__()] = method

    def unload_method(self, method):
        self.plugin.pop(method.__str__(), None)

    def get_method(self, method_name):
        method = self.plugin.get(method_name)
        if method:
            return method.execute
        else:
            print(f"Running '{method_name}' plugin after unloading: Plugin '{method_name}' not found")
            return DoNothingPlugin().execute


if __name__ == '__main__':
    microkernel = Microkernel()
    microkernel.load_method(AddPlugin())
    microkernel.load_method(MultiplyPlugin())
    microkernel.load_method(SubtractPlugin())

    microkernel.get_method("add")(10, 5)
    microkernel.get_method("multiply")(10, 5)
    microkernel.get_method("subtract")(10, 5)

    microkernel.unload_method(AddPlugin())
    microkernel.get_method("add")(10, 5)
