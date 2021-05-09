
class Simulation:
    def __init__(self, config):
        self.config = config

    def set_shape_data(self, x_nodes, y_nodes, x, y, shape):
        self.x_nodes = int(x_nodes)
        self.y_nodes = int(y_nodes)
        self.x = int(x)
        self.y = int(y)
        self.shape = shape

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_stepped_simulation(self, stepped):
        self.stepped = stepped

    def set_load_from_outside(self, from_outside):
        self.from_outside = from_outside
