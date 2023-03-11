# Doodle Wizard

## Description
Doodle Wizard is a simple command-line application for producing ASCII art by moving the cursor and painting lines behind it as it advances. It draws several sorts of lines on a canvas that fills the terminal window using a set of ASCII letters.

## Installing and Running
Python 3 is required to run Doodle Wizard. Clone this repository and browse to the project folder in your terminal to install.
Run the Python3 doodle wizard.py command to launch Doodle Wizard.

## How to Use
Doodle Wizard is operated using a set of keyboard instructions. To move the mouse and draw lines in different directions, use the WASD keys. There are the following commands available:
W: Draw a vertical line above the cursor by moving it up.
A: Drag the pointer to the left and create a horizontal line to the left.
S: Move the cursor down and draw a vertical line below it.
D: Draw a vertical line below the cursor by moving it down.
H: Display the help screen, which provides a command list.
C: Erase all lines and clear the canvas.
F: Save the current drawing to a text file.
When you start Doodle Wizard, a canvas will cover the terminal window. Move the pointer around the canvas with the WASD keys and create lines behind it as it goes. Lines will link to make boxes and other objects if you draw in any direction..

## Add a License
The MIT License applies to this project.

## How to Contribute
Contributions are appreciated! Please raise an issue or send a pull request if you detect a bug or have a suggestion for an exciting new feature.

## Additional Points
The size of the canvas is governed by the size of your terminal window. Try adjusting your terminal window if your canvas is too tiny or too huge.
Doodle Wizard represents several sorts of lines with a collection of ASCII characters. You may change the appearance of these characters by changing the constants at the start of the doodle wizard.py file.
The current drawing is stored to a move list. When you save the artwork to a file, these motions are saved alongside the ASCII image. This list of steps can be used to replicate the drawing later or to write a script that draws the same pattern automatically.

## Conclusion
Doodle Wizard is a fun and easy command-line tool for creating ASCII art. It's simple to use and configure, and it lets you build complicated patterns with a few keystrokes. Experiment with it and see what you can come up with!
