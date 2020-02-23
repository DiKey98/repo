
def do_action(client_id, wheels):
    move(client_id, wheels, sleep_time, 5*speed)
    move(client_id, wheels, sleep_time, -speed)


def main():
    return 0