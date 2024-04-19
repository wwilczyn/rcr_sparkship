from typing import List


class Node:
    def __init__(self, command_name, frequency=0, left_node=None, right_node=None):
        self.command_name = command_name
        self.frequency = frequency
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        # return self.command_name + " (" + str(self.frequency) + ")" + "\n" + "\t" + "/\\"
        # return str(self.command_name).split('\'')[1]
        return self.command_name[0]

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __getitem__(self):
        return self.command_name


class RoboticCodeRepresentationGenerator:
    command_tuples = []
    root: Node

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
            for i in range(0, last-k-1):
                if self.command_tuples[i][1] < self.command_tuples[i + 1][1]:
                    new_item = self.command_tuples[i]
                    self.command_tuples[i] = self.command_tuples[i + 1]
                    self.command_tuples[i + 1] = new_item

        index = 0
        last = self.command_tuples[-1]
        self.root = Node(self.command_tuples[index], int(self.command_tuples[index][1]), None, None)
        while self.command_tuples[index+1] != last:
            command = Node(self.command_tuples[index], int(self.command_tuples[index][1]), None, None)
            print('\t' * index, command)
            if command.frequency >= int(self.command_tuples[index+1][1]):
                command.right_node = Node(self.command_tuples[index+1], int(self.command_tuples[index+1][1]), None, None)
            else:
                command.left_node = Node(self.command_tuples[index+1], int(self.command_tuples[index+1][1]), None, None)
            index += 1

    def get_rcr(self, rcr_command: str) -> str:
        start = self.root
        rcr_string = "0"
        rcr_command = rcr_command.upper()

        print(start)
        print(rcr_command)

        while start.command_name[0] != rcr_command:
            if start.right_node is not None:
                start = start.right_node
                rcr_string.join("0")
            elif start.left_node is not None:
                start = start.left_node
                rcr_string.join("1")
            else:
                print(start.right_node)
                print(start.left_node)
                break

        return rcr_string


# put commands in a list with number of occurrences of each (tuple)
file = open("RCR_commands.txt", mode="r")
commands = file.read().splitlines()
rcr = RoboticCodeRepresentationGenerator(commands)
print(RoboticCodeRepresentationGenerator.command_tuples)

command_to_see = input("Enter the command name for which you want to see the RCR: ")
command_to_see = command_to_see.upper()
print("The RCR for {} is {}".format(command_to_see, rcr.get_rcr(rcr_command=command_to_see)))
