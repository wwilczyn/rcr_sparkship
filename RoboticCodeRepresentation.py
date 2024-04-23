from typing import List


COMMAND_NAME = 0
FREQUENCY = 1


class Node:
    def __init__(self, command_name, frequency=0, left_node=None, right_node=None):
        self.command_name = command_name[0]
        self.frequency = frequency
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        # return self.command_name + " (" + str(self.frequency) + ")" + "\n" + "\t" + "/\\"
        # return str(self.command_name).split('\'')[1]
        return self.command_name

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __getitem__(self):
        return self.command_name


root: Node


class RoboticCodeRepresentationGenerator:
    command_tuples = []

    def __init__(self, issued_commands: List[str]):
        unique_commands = []
        for command in issued_commands:
            if command not in unique_commands:
                unique_commands.append(command)

        for command in unique_commands:
            command_count = issued_commands.count(command)
            self.command_tuples.append((command, command_count))

        # bubble sort based on second key (number of command occurrences)
        last = len(self.command_tuples)
        print(self.command_tuples)
        for k in range(0, last):
            for i in range(0, last - k - 1):
                if self.command_tuples[i][1] < self.command_tuples[i + 1][1]:
                    new_item = self.command_tuples[i]
                    self.command_tuples[i] = self.command_tuples[i + 1]
                    self.command_tuples[i + 1] = new_item

        # make tree from command_tuples list
        last_command = self.command_tuples[-1][COMMAND_NAME]
        index = 0
        # command = self.command_tuples[index][0]
        new_node = Node(self.command_tuples[index], int(self.command_tuples[index][FREQUENCY]), None, None)
        global root
        root = new_node
        while new_node.command_name != last_command:
            if self.command_tuples[index][COMMAND_NAME] == last_command:
                break
            index += 1
            next_command = self.command_tuples[index]  # tuple: (command_name, frequency)
            new_node.right_node = Node(next_command, next_command[FREQUENCY], None, None)
            new_node = new_node.right_node

    def get_rcr(self, rcr_command: str) -> str:
        start = root
        rcr_string = "0"
        rcr_command = rcr_command.upper()

        # print("start: {}".format(start))
        # print(rcr_command)
        # print("rcr_command: ", rcr_command)

        while start.command_name != rcr_command:
            if start.right_node is not None:
                start = start.right_node
                rcr_string += "0"
            elif start.left_node is not None:
                start = start.left_node
                rcr_string += "1"
            else:
                print("right node: {}".format(start.right_node))
                print("left node: {}".format(start.left_node))
                break

        return rcr_string


# put commands in a list with number of occurrences of each (tuple)
file = open("RCR_commands.txt", mode="r")
commands = file.read().splitlines()
rcr = RoboticCodeRepresentationGenerator(commands)
print(RoboticCodeRepresentationGenerator.command_tuples)

saved_root = root
i = 0
while root is not None:
    print("\t"*i, root)
    root = root.right_node
    i += 1
root = saved_root
# print("root: ", root)
# print("root.right_node: ", root.right_node)

command_to_see = input("Enter the command name for which you want to see the RCR: ")
command_to_see = command_to_see.upper()
print("The RCR for {} is {}".format(command_to_see, rcr.get_rcr(rcr_command=command_to_see)))
