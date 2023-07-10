#!/user/bin/python3
"""
    a class MyList that inherits from list
"""


class MyList(list):

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
