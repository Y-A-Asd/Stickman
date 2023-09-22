class PickleHandler:
    def __init__(self, name):
        self.filename = name
    def write(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)
    def read(self):
        with open(self.filename, 'rb') as f:
            data = pickle.load(f)
        return data