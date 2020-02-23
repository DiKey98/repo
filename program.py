
def do_action(client_id, wheels):
    move(client_id, wheels, sleep_time, speed)
    move(client_id, wheels, sleep_time, -speed)
    rotate(client_id, wheels, sleep_time, 2*speed)
    move(client_id, wheels, sleep_time, speed)


def get_coords(obj):
    return obj.coords
