from action import main
from action_module_support import SubscriberClass


subscriber = SubscriberClass()


@subscriber.loop
def run(**kwargs):
    return main(**kwargs)


run()
