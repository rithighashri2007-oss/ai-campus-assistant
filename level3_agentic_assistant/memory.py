class Memory:
    def __init__(self):
        self.buffer = []

    def add(self, text):
        self.buffer.append(text)

        # keep memory small (human-like memory)
        if len(self.buffer) > 5:
            self.buffer.pop(0)

    def get(self):
        return "\n".join(self.buffer)
