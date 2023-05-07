# -*- coding: utf-8 -*-
"""
Created on Sun May 08 15:31:59 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""

from texteditor import TextEditor

# create a new text editor instance
editor = TextEditor()

# add some text to the editor
editor.insert('Hello, World!')
editor.display()

# move the cursor left and right
editor.move_left()
editor.display()

editor.move_right()
editor.display()

# add more text to the editor
editor.insert(' This is a test.')
editor.display()

# delete a character
editor.delete()
editor.display()