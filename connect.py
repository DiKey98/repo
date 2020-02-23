import time
import sim

#Необходимо описать эту функцию
def connect(host, port):
    _, err = sim.connect_toremote_api(host, port)
    return err