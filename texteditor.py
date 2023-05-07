# -*- coding: utf-8 -*-
"""
Created on Sun May 08 15:31:59 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""



from positionallist import PositionalList

class TextEditor:
    """A text editor that stores and displays a string of characters
    using a positional list list and a cursor object.
    """

    def __init__(self):
        self._container = PositionalList()
        self._cursor = None

    def _set_cursor(self, position):
        """Set the cursor to the given position."""
        if self._cursor is not None:
            # Remove the cursor symbol from the previous position
            self._cursor._node._element = self._cursor._node._element[:-1]
        self._cursor = self._container.make_position(position)
        # Add the cursor symbol to the new position
        self._container.replace(self._cursor, self._cursor.element() + '|')

    def _get_string(self):
        """Return the string representation of the list."""
        return ''.join(str(p.element()) for p in self._container)

    def move_left(self):
        """Move the cursor left one character if possible."""
        if self._cursor is not None and self._cursor != self._container.first():
            self._set_cursor(self._container.before(self._cursor))

    def move_right(self):
        """Move the cursor right one character if possible."""
        if self._cursor is not None and self._cursor != self._container.last():
            self._set_cursor(self._container.after(self._cursor))

    def insert(self, c):
        """Insert the character 'c' just after the cursor."""
        if self._cursor is not None:
            self._container.add_after(self._cursor, c)
            self._set_cursor(self._container.after(self._cursor))

    def delete(self):
        """Delete the character just after the cursor if possible."""
        if self._cursor is not None and self._cursor != self._container.last():
            old_position = self._container.after(self._cursor)
            self._container.delete(old_position)
            self._set_cursor(self._cursor)

    def display(self):
        """Display the string and the cursor position."""
        string = self._get_string()
        cursor_pos = 0 if self._cursor is None else self._container.find_position(self._cursor)
        print(string)
        print('-' * cursor_pos + '^')