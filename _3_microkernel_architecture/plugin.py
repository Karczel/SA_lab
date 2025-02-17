class Plugin:
    def execute(self, *args):
        raise NotImplementedError("Plugins must implement the execute method.")
