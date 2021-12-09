class GlobalState:
    def __init__(self):
        self._id_counter = 0

    def get_next_id(self):
        x = self._id_counter
        self._id_counter += 1
        return x
