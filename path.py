import os


def set_log_name():

    # print([name[0].(1) for name in os.walk("./logs/")])
    for dirs in os.walk("./logs/"):
        print(dirs)
        for name in dirs:
            print(name)