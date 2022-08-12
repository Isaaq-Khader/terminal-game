import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)

from project.player_name.name_player import *
import test.tud_test_base as ttb

class TestClassLogicHelpers:
    def test_stillNotY_y(self):
        result = stillNotY('y')
        assert result == False

    def test_stillNotY_Y(self):
        result = stillNotY('Y')
        assert result == False

    def test_stillNotY_N(self):
        result = stillNotY('N')
        assert result == True

    def test_stillNotY_n(self):
        result = stillNotY('n')
        assert result == True

    def test_stillNotY_unknown(self):
        result = stillNotY('asdf')
        assert result == True

    def test_stillNotY_unknown(self):
        result = stillNotY('')
        assert result == True

    def test_validateInput_y(self):
        result = validateInput('y')
        assert result == False

    def test_validateInput_Y(self):
        result = validateInput('Y')
        assert result == False

    def test_validateInput_n(self):
        result = validateInput('n')
        assert result == False
    
    def test_validateInput_N(self):
        result = validateInput('N')
        assert result == False

    def test_validateInput_unknown(self):
        result = validateInput('asdf')
        assert result == True

    def test_validateInput_unknown(self):
        result = validateInput('')
        assert result == True
    
class TestClassInputHelpers:    
    def test_getName(self):
        ttb.set_keyboard_input(['Isack'])
        result = getName()
        assert result == 'Isack'

    def test_getYoN_y(self):
        ttb.set_keyboard_input(['y'])
        result = getYoN('Isack')
        assert result == 'y'
    
    def test_getYoN_Y(self):
        ttb.set_keyboard_input(['Y'])
        result = getYoN('Isack')
        assert result == 'Y'

    def test_getYoN_n(self):
        ttb.set_keyboard_input(['n'])
        result = getYoN('Isack')
        assert result == 'n'

    def test_getYoN_N(self):
        ttb.set_keyboard_input(['N'])
        result = getYoN('Isack')
        assert result == 'N'

    def test_getYoN_unknown(self):
        ttb.set_keyboard_input(['asdf'])
        result = getYoN('Isack')
        assert result == 'asdf'

    def test_checkValidity_y(self):
        ttb.set_keyboard_input(['y'])
        inputResult, validResult = checkValidity()
        assert inputResult == 'y' and validResult == False
    
    def test_checkValidity_Y(self):
        ttb.set_keyboard_input(['Y'])
        inputResult, validResult = checkValidity()
        assert inputResult == 'Y' and validResult == False

    def test_checkValidity_n(self):
        ttb.set_keyboard_input(['n'])
        inputResult, validResult = checkValidity()
        assert inputResult == 'n' and validResult == False

    def test_checkValidity_N(self):
        ttb.set_keyboard_input(['N'])
        inputResult, validResult = checkValidity()
        assert inputResult == 'N' and validResult == False

    def test_checkValidity_y(self):
        ttb.set_keyboard_input(['fdsa'])
        inputResult, validResult = checkValidity()
        assert inputResult == 'fdsa' and validResult == True

class TestClassNameThePlayer:
    def test_cleanInputs_y(self):
        ttb.set_keyboard_input(['Isack', 'y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isack'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ']
    
    def test_cleanInputs_Y(self):
        ttb.set_keyboard_input(['Isack', 'Y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isack'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ']

    def test_cleanInputs_n(self):
        ttb.set_keyboard_input(['Isack', 'n', 'Isaaq', 'y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isaaq'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ',
                          "\nOkay! Let's change it.\n",
                          'What is your name: ',
                          'Your name is Isaaq, is that correct?',
                          '(Y/N): ']

    def test_cleanInputs_N(self):
        ttb.set_keyboard_input(['Isack', 'N', 'Isaaq', 'Y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isaaq'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ',
                          "\nOkay! Let's change it.\n",
                          'What is your name: ',
                          'Your name is Isaaq, is that correct?',
                          '(Y/N): ']
    
    def test_badInputs_oneUnknown_Y(self):
        ttb.set_keyboard_input(['Isack', 'asdf', 'Y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isack'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ',
                          '(Y/N)?: ']
    
    def test_badInputs_oneUnknown_N(self):
        ttb.set_keyboard_input(['Isack', 'asdf', 'N', 'Isaaq', 'Y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isaaq'
        assert output == ['What is your name: ',
                        'Your name is Isack, is that correct?',
                        '(Y/N): ',
                        '(Y/N)?: ',
                        "\nOkay! Let's change it.\n",
                        'What is your name: ',
                        'Your name is Isaaq, is that correct?',
                        '(Y/N): ']

    def test_badInputs_multipleUnknown_N(self):
        ttb.set_keyboard_input(['Isack', 'asdf', '', 'YNYN', 'N', 'Isaaq', 'Y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Isaaq'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ',
                          '(Y/N)?: ',
                          '(Y/N)?: ',
                          '(Y/N)?: ',
                          "\nOkay! Let's change it.\n",
                          'What is your name: ',
                          'Your name is Isaaq, is that correct?',
                          '(Y/N): ']

    def test_badInputs_multipleUnknown_N(self):
        ttb.set_keyboard_input(
            ['Isack', 'NYNYN', '', 'N', 'Isaaq', 'YYY', 'n', 'Qaasi', 'y'])
        name = namePlayer()
        output = ttb.get_display_output()
        assert name == 'Qaasi'
        assert output == ['What is your name: ',
                          'Your name is Isack, is that correct?',
                          '(Y/N): ',
                          '(Y/N)?: ',
                          '(Y/N)?: ',
                          "\nOkay! Let's change it.\n",
                          'What is your name: ',
                          'Your name is Isaaq, is that correct?',
                          '(Y/N): ',
                          '(Y/N)?: ',
                          "\nOkay! Let's change it.\n",
                          'What is your name: ',
                          'Your name is Qaasi, is that correct?',
                          '(Y/N): ']
