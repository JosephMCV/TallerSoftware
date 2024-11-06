
from controllers import persona_controller
from controllers.ciudad_controller import get_ciudad_controller
from controllers.persona_controller import get_persona_controller


ciudad_controller = get_ciudad_controller()
persona_controller = get_persona_controller()

limit = 50

ciudades = ciudad_controller.get_all()
for i, ciudad in enumerate(ciudades):
    print(f"{i}: {ciudad}")
    
    if i >= limit:
        print(f"Showing only {limit} ciudades of {len(ciudades)}\n")
        break
    
personas = persona_controller.get_all()
for i, persona in enumerate(personas):
    print(persona)
    
    if i >= limit:
        print(f"Showing only {limit} personas of {len(personas)}")
        break