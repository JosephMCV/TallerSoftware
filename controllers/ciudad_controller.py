from controllers.base_controller import CSVController
from models.ciudad import Ciudad


ciudad_controller = CSVController("database/ciudad.csv", Ciudad)

def get_ciudad_controller():
    return ciudad_controller