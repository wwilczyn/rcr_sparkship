class Node:
    def __init__(self, cmd_name, left_node=None, right_node=None):
        self.command_name = cmd_name
        self.left_node = left_node
        self.right_node = right_node

    def get_value(self):
        return self.command_name


file = open("RCR_commands.txt", mode="r")
commands = file.read().splitlines()

for command in commands:
    print(command)
