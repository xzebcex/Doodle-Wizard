# Doodle Wizard

import shutil
import sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR = chr(9532)  # Character 9532 is '┼'

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
# Leave room at the bottom few rows for the command info lines.
CANVAS_HEIGHT -= 5

# The keys for canvas will be (x, y) integer tuples for the coordinate,
# and the value is a set of letters W, A, S, D that tell what kind of line
# should be drawn.
canvas = {}
cursor_X = 0
cursor_Y = 0


def get_canvas_string(canvas_data, cx, cy):
    # Returns a multiline string of the line drawn in canvas data.
    canvas_str = ''

    # canvas data is a dictionary with (x, y) tuple keys and values that
    # are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    # directions the lines are drawn at each xy point.
    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == cx and row_num == cy:
                canvas_str += '#'
                continue

            # Add the line character for this point to canvas str.
            cell = canvas_data.get((column_num, row_num))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += CROSS_CHAR
            elif cell == None:
                canvas_str += ' '
        canvas_str += '\n'  # Add a newline at the end of each row.
    return canvas_str


moves = []
while True:  # Main program loop.
    # Draw the lines based on the data in canvas:
    print(get_canvas_string(canvas, cursor_X, cursor_Y))

    response = input('WASD keys to move, H for help, C to clear, '
                     + 'F to save, or QUIT.\n> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()  # Quit the program.
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.\n')
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}  # Erase the canvas data.
        moves.append('C')  # Record this move.
    elif response == 'F':
        # Save the canvas string to a text file:
        try:
            filename = input('Enter filename to save to:')

            # Make sure the filename ends with .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(get_canvas_string(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # Ignore this letter and continue to the next one.
        moves.append(command)  # Record this move

        # The first line we add needs to form a full line:
        if canvas == {}:
            if command in ('W', 'S'):
                # Make the first line a horizontal one:
                canvas[(cursor_X, cursor_Y)] = set(['W', 'S'])
        elif command in ('A', 'D'):
            # Make the first line a vertical one:
            canvas[(cursor_X, cursor_Y)] = set(['A', 'D'])

        # Update x and y:
        if command == 'W' and cursor_Y > 0:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_Y = cursor_Y - 1
        elif command == 'S' and cursor_Y < CANVAS_HEIGHT - 1:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_Y = cursor_Y + 1
        elif command == 'A' and cursor_X > 0:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_X = cursor_X - 1
        elif command == 'D' and cursor_X < CANVAS_WIDTH - 1:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_X = cursor_X + 1
        else:
            # If the cursor doesn't move because it would have moved off
            # the edge of the canvas, then don't change the set at
            # canvas[(cursorX, cursorY)].
            continue

        # If there's no set for (cursorX, cursorY), add an empty set:
        if (cursor_X, cursor_Y) not in canvas:
            canvas[(cursor_X, cursor_Y)] = set()

        # Add the direction string to this xy point's set:
        if command == 'W':
            canvas[(cursor_X, cursor_Y)].add('S')
        elif command == 'S':
            canvas[(cursor_X, cursor_Y)].add('W')
        elif command == 'A':
            canvas[(cursor_X, cursor_Y)].add('D')
        elif command == 'D':
            canvas[(cursor_X, cursor_Y)].add('A')
