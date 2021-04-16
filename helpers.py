import scripts_runner as sr 

class Helpers:
    @staticmethod
    def validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
                if value_if_allowed:
                    try:
                        float(value_if_allowed)
                        return True
                    except ValueError:
                        return False
                else:
                    return False


class SimulationDriver:
    @staticmethod
    def start_simulation_and_show_next_page(controller, simulation_name, shape):
        print(simulation_name, shape)
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_simulation(simulation_name, shape)
    @staticmethod
    def kill_simulation_and_back_to_start(controller):
        controller.show_frame("StartPage")
        sr.kill_simulation()