import time
import sim

def do_action(client_id, wheels):
    move(client_id, wheels, sleep_time, speed)
    move(client_id, wheels, sleep_time, -speed)
    rotate(client_id, wheels, sleep_time, 0.5*speed)
    move(client_id, wheels, sleep_time, speed)
    move(client_id, wheels, sleep_time, -speed)
    rotate(client_id, wheels, 2*sleep_time, -0.5*speed)
    move(client_id, wheels, sleep_time, speed)
    move(client_id, wheels, sleep_time, -speed)
    rotate(client_id, wheels, sleep_time, -0.5 * speed)
    move(client_id, wheels, sleep_time, speed)
    move(client_id, wheels, sleep_time, -speed)
    rotate(client_id, wheels, 2 * sleep_time, 0.5 * speed)