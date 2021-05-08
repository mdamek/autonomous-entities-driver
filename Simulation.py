
class Simulation:
    def __init__(self, config):
        self.config = config

    def set_shape(self, shape):
        self.shape = shape

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_stepped_simulation(self, stepped):
        self.stepped = stepped

    def set_load_from_outside(self, from_outside):
        self.from_outside = from_outside
