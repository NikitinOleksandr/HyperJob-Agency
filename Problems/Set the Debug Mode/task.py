initial_input = input()
IS_RELEASE_SERVER = bool
DEBUG = bool
if initial_input == "true":
    IS_RELEASE_SERVER = True
    DEBUG = False
elif initial_input == "false":
    IS_RELEASE_SERVER = False
    DEBUG = True
