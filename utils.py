# utils.py o en tu servicio de tareas
state_flow = {
    "stories": "to_do",
    "to_do": "in_progress",
    "in_progress": "testing",
    "testing": "done",
    "done": None  # Ya no hay siguiente
}
