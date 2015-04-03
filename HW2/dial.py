from sys import argv, exit, maxsize

NUMPAD = ["1","2","3","4","5","6","7","8","9","*","0","#"];
STEP_LEFT, STEP_RIGHT, STEP_UP, STEP_DOWN = -1, 1, -3, 3

class Dial():
    current_position = 0
    total_movements = 0
    matrix = {}

    def get_number_of_steps(self, start, end):
        """Returns number of movements from start to end.
        Gets the number from a table, calculates shortest path greedily otherwise and stores the value.

        start - start position
        end - end position

        return - number of movements from start to end
        """
        if start < 0 or start >= len(NUMPAD) or end < 0 or end >= len(NUMPAD):
            return maxsize

        if start not in self.matrix:
            self.matrix[start] = {}
        if end in self.matrix[start]:
            return self.matrix[start][end]

        if start == end:
            self.matrix[start][end] = 0
        else:
            self.matrix[start][end] = maxsize

            if end > start: 
                if start % 3 == 0: # check right
                    self.matrix[start][end] = min(self.matrix[start][end], 1 + self.get_number_of_steps(start + STEP_RIGHT, end))
                self.matrix[start][end] = min(self.matrix[start][end], 1 + self.get_number_of_steps(start + STEP_DOWN, end)) # check down
            if end < start: 
                if start % 3 == 1: # check left
                    self.matrix[start][end] = min(self.matrix[start][end], 1 + self.get_number_of_steps(start + STEP_LEFT, end))
                self.matrix[start][end] = min(self.matrix[start][end], 1 + self.get_number_of_steps(start + STEP_UP, end)) # check up

        return self.matrix[start][end]

    def move(self, number):
        """Moves to the specified position.
        Adds number of made movements to the total and updates current position.

        number - number where we should move
        """
        index_finger_positions = self.get_index_finger_positions(number)
        movements = maxsize
        position = 0

        for index_finger_position in index_finger_positions:
            temp_movements = self.get_number_of_steps(self.current_position, index_finger_position)
            if temp_movements < movements:
                movements = temp_movements
                position = index_finger_position

        self.total_movements += movements
        self.current_position = position

    def get_index_finger_positions(self, number):
        """Returns position(s) of index finger by the given number.

        number - index in NUMPAD that should be pressed

        return - index in NUMPAD where the index finger should be located
        """
        number_index = NUMPAD.index(number)
        if number_index % 3 == 0:
            return [number_index]
        if number_index % 3 == 1:
            return [number_index-1, number_index]
        if number_index % 3 == 2:
            return [number_index-1]

def number_of_movements(number):
    """Returns number of movements required for dialing the specified number."""
    dial = Dial()
    for i in number:
        dial.move(i)

    return dial.total_movements

def main(filename):
    with open(filename, 'r') as f:
        number_of_numbers = int(f.readline().strip())
        for i in xrange(number_of_numbers):
            print number_of_movements(f.readline().strip())

def usage():
    print argv[0], "<input file>"
    exit(1)

if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    else:
        main(argv[1])

