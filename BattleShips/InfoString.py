# InfoString.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

# MainProgram
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""Class that defines block text information to be called

created as a simple class as is only a shell that will not be called on
directly except via initialised child classes.
"""


class InfoString:
    _text = str

    def show_text(self):
        print(self._text)

"""Test assertion:
If _text = "this is a string"
Then method should print string
"""
"""
# test code:
my_text_test = InfoString()
my_text_test._text = "this is a test"
my_text_test.show_text()
#Test outcome: successful
"""