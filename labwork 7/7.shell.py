import os

if __name__ == '__main__':
    # home_dir = os.system("cd ~")
    # os.chdir('/home')
    # print(home_dir)
    exit = True
    os.system('echo Type exit to get out of the terminal')
    while exit:
        command = input(">>> ")
        if command == "exit":
            exit = False
        else:
            os.system(command)