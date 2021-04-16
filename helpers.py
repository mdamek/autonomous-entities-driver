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
    def start_mock_and_show_next_page(controller, simulation_name, shape):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_mock(shape)
    @staticmethod
    def start_rabbits_and_show_next_page(controller, simulation_name, shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_rabbits(shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency)
    @staticmethod
    def start_torch_and_show_next_page(controller, simulation_name, shape, spawnChance, personSpawnChance, fireSpawnChance, exitSpawnChance, personMaxSpeed, fireSpreadingFrequency):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_torch(shape, spawnChance, personSpawnChance, fireSpawnChance, exitSpawnChance, personMaxSpeed, fireSpreadingFrequency)
    @staticmethod
    def start_fortwist_and_show_next_page(controller, simulation_name, shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, 
    foraminiferaLifeActivityCost, algaeStartEnergy, algaeRegenerationRate, algaeEnergeticCapacity):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_fortwist(shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, foraminiferaLifeActivityCost, algaeStartEnergy, 
        algaeRegenerationRate, algaeEnergeticCapacity)
    @staticmethod
    def start_game_and_show_next_page(controller, simulation_name, shape, lifeSpawnChance, loadFromOutside):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_game(shape, lifeSpawnChance, loadFromOutside)
    @staticmethod
    def start_game_and_show_draw_page(controller, simulation_name, shape):
        sr.start_motion_sensor(shape)
        controller.set_simulation_name_shape_and_show_frame("DrawPage", simulation_name, shape)
    @staticmethod
    def kill_simulation_and_back_to_start(controller):
        controller.show_frame("StartPage")
        sr.kill_simulation()