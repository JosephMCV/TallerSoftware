from controllers.base_controller import CSVController
from models.persona import Persona


persona_controller = CSVController("database/persona.csv", Persona)

def get_persona_controller():
    return persona_controller