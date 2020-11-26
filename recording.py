class Recording:
    data = list()

    def __init__(self, *args):
        self.data = list(args)

    def __str__(self):
        return ", ".join(self.data)