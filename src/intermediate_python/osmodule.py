import os
def show_info() -> None:
    #get current working directory
    print("Current working directory:", os.getcwd())

    # check the environment variable
    print("Environment variables:", os.environ)