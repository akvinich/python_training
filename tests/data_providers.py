import time
from model.customer import Customer


def current_time_millis():

    return int(round(time.time() * 1000))


valid_customers = [Customer(project="mobile", kindproject="hire", name="Vital",
                            country="US", email="vital%s@smith.me" % current_time_millis(),
                            number="246000"),
                   # ...
                   ]