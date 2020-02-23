import time
import sim

def connect(host, port):
    _, err = sim.connect_toremote_api(host, port)
    return err