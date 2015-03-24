from sys import argv, exit

NUMPAD = ["1","2","3","4","5","6","7","8","9",'*',"0",'#']

class Dial():
    current_position = 0
    total_moves = 0
    position = {}

    def __init__(self):
        for i in xrange(12):
            if (i % 3 != 2):
                self.position[i] = self.get_table_for_position(i)

    def get_table_for_position(self, i):
        table = {}
        for j in xrange(12):
            table[j] = {}

            if j == 0:
                table[j]['position'] = 0
                table[j]['movements'] = i / 3 + (i % 3)
            if j == 1:
                table[j]['movements'] = i / 3
                table[j]['position'] = i % 3
            if j == 2:
                table[j]['position'] = 1
                table[j]['movements'] = 1 - (i % 3) + i / 3
            
            if j == 9:
                table[j]['position'] = 9
                table[j]['movements'] = 3 - i / 3 + (i % 3)
            if j == 10:
                table[j]['movements'] = 3 - i / 3
                table[j]['position'] = 9 + i % 3
            if j == 11:
                table[j]['position'] = 10
                table[j]['movements'] = 1 - (i % 3) + 3 - i / 3

            ###

            if j == 3:
                table[j]['position'] = 3
                if i / 3 == 1:
                    table[j]['movements'] = i % 3
                else:
                    table[j]['movements'] = abs(1 - i / 3) + (i % 3)
            if j == 4:
                table[j]['movements'] = abs(1 - i / 3)
                if i / 3 == 1:
                    table[j]['position'] = i
                else:
                    table[j]['position'] = 3 + (i % 3)
            if j == 5:
                table[j]['position'] = 4
                if i / 3 == 1:
                    table[j]['movements'] = 1 - (i % 3)
                else:
                    table[j]['movements'] = abs(1 - i / 3) + 1 - (i % 3)

            if j == 6:
                table[j]['position'] = 6
                if i / 3 == 2:
                    table[j]['movements'] = i % 3
                else:
                    table[j]['movements'] = abs(2 - i / 3) + (i % 3) 
            if j == 7:
                table[j]['movements'] = abs(2 - i / 3)
                if i / 3 == 2:
                    table[j]['position'] = i
                else:
                    table[j]['position'] = 6 + (i % 3)
            if j == 8:
                table[j]['position'] = 7
                if i / 3 == 2:
                    table[j]['movements'] = 1 - (i % 3)
                else:
                    table[j]['movements'] = abs(2 - i / 3) + 1 - (i % 3)

        return table

    def move(self, i):
        index = get_index_of_number(i)
        self.total_moves += self.position[self.current_position][index]['movements']
        self.current_position = self.position[self.current_position][index]['position']

def get_index_of_number(i):
    return NUMPAD.index(i)

def number_of_movements(number):
    dial = Dial()
    for i in number:
        dial.move(i)

    return dial.total_moves



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

