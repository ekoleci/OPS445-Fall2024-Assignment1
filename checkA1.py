#!/usr/bin/env python3

import unittest
from datetime import datetime, date, timedelta
from random import randint, shuffle
import sys, os
import subprocess as sp
from importlib import import_module
import ast, inspect

'''
ASSIGNMENT 1 CHECK SCRIPT
Author: Eric Brauer eric.brauer@senecapolytechnic.ca

Description:
TestAfter .. TestDBDA all are testing functions inside students' code. 
TestFinal will run the code as a subprocess and evaluate the std.output.

The precise requirements of each student-created function are specified elsewhere.

The script assumes that the student's filename is named 'assignment1.py' and exists in the same directory as this check script.

NOTE: Feel free to _fork_ and modify this script to suit needs. I will try to fix any issues that arise but this script is provided as-is, with no obligation of warranty or support.
'''

class TestAfter(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dtypes(self):
        "after() is returning string"
        i = '01/10/2023'
        error_msg = 'Your after() function should accept one string as arg, and return a string.'
        self.assertIsInstance(self.a1.after(i), str, error_msg)

        
    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{d:02}/{m:02}/{y}'

    def test_after_date(self):
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            
            eobj = dobj1 + timedelta(1)
            e = eobj.strftime('%d/%m/%Y')
            error_msg = (f'after function not returning correct answer.\n'
                         f'inputs: {date1}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.after(date1), e, error_msg)
   
    def test_leap(self):
        "after() works with leap year"
        i = '28/02/2020'
        e = '29/02/2020'
        error_msg = "Your after() function is returning the wrong answer for a leap year"
        self.assertEqual(self.a1.after(i), e, error_msg)


class TestBefore(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dtypes(self):
        "before() is returning string"
        i = '01/10/2023'
        error_msg = 'Your before() function should accept one string as arg, and return a string.'
        self.assertIsInstance(self.a1.after(i), str, error_msg)

        
    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{d:02}/{m:02}/{y}'

    def test_before_date(self):
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            
            eobj = dobj1 + timedelta(-1)
            e = eobj.strftime('%d/%m/%Y')
            error_msg = (f'before function not returning correct answer.\n'
                         f'inputs: {date1}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.before(date1), e, error_msg)
   
    def test_leap(self):
        "before() works with leap year"
        i = '01/03/2020'
        e = '29/02/2020'
        error_msg = "Your before() function is returning the wrong answer for a leap year"
        self.assertEqual(self.a1.before(i), e, error_msg)


class TestDayOfWeek(unittest.TestCase): 

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dow(self):
        "test day of week function"
        testdates = [
            '23/01/2023', '22/01/2023',
            '01/11/2022', '31/10/2022',
            '15/06/2024', '14/06/2024',
            '01/03/2022', '28/02/2022',
            '01/01/2022', '31/12/2021'
        ]
        error_msg = 'day_of_week() not returning the expected day of week'
        for datestr in testdates:
            dobj = datetime.strptime(datestr, '%d/%m/%Y')
            e = dobj.strftime('%a')
            self.assertEqual(self.a1.day_of_week(datestr), e, error_msg)

class TestMonMax(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_mon_max(self):
        "test the mon_max function"
        y = 2023
        mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i, e in mon_dict.items():
            error_msg = f'bad output from mon_max function. Input month: {i}. Expected: {e}'
            self.assertEqual(self.a1.mon_max(i, y), e, error_msg)

    def test_leap_max(self):
        "test mon_max with feb of leap/non-leap years"
        years = {2022: 28, 2020: 29, 2024: 29, 2023: 28, 1960: 29, 1969: 28, 2000: 29, 1900: 28}
        for i, e in years.items():
            error_msg = f'bad output from mon_max function. Input year: {i}. Input month: 2. Expected: {e}'
            self.assertEqual(self.a1.mon_max(2, i), e, error_msg)


class TestLeap(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_leap_func(self):
        "leap_year function exists and returns True/False"
        test_dat = {
            2022: False,
            2020: True,
            2024: True,
            2023: False,
            1960: True,
            1969: False,
            2000: True,
            1900: False
        }
        error_msg = 'leap_year() not returning correct True/False for a specific year'
        for i,e in test_dat.items():
            self.assertEqual(self.a1.leap_year(i), e, error_msg)


class TestValidDate(unittest.TestCase): 

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_valid_dates(self):
        "making sure valid dates return True"
        test_dat = [
            '25/01/2022',
            '13/03/2011',
            '01/01/2001',
            '30/11/1539',
            '29/02/2020',
            '19/01/2038'
        ]
        error_msg = 'valid_date() not returning true for a valid date'
        for date in test_dat:
            self.assertEqual(self.a1.valid_date(date), True, error_msg)
    
    def test_invalid_dates(self):
        "making sure invalid dates return False"
        test_dat = [
            '01/25/2022',
            '01/20/2001',
            '00/11/1539',
            '29/02/2021',
            '31/04/2023'
        ]
        error_msg = 'valid_date() not returning false for an invalid date'
        for date in test_dat:
            self.assertEqual(self.a1.valid_date(date), False, error_msg)


class TestDayIter(unittest.TestCase): 

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{d:02}/{m:02}/{y}'
    

    def test_after_iter(self):
        "does day_iter work with positive numbers"
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            num = randint(0, 500)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%d/%m/%Y')
            error_msg = (f'day_iter function not returning correct answer.\n'
                         f'inputs: {date1} {num}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.day_iter(date1, num), e, error_msg)
    
    def test_before_iter(self):
        "does day_iter work with negative numbers"
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            num = randint(-500, -1)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%d/%m/%Y')
            error_msg = (f'day_iter function not returning correct answer.\n'
                         f'inputs: {date1} {num}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.day_iter(date1, num), e, error_msg)


class TestModuleRestriction(unittest.TestCase):
    "no modules apart from allowed are being imported"
    
    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        try:
            self.assertTrue(os.path.exists(file), msg=error_output)
        except AssertionError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
    
    def test_unallowed_module(self):
        "you have imported a prohibited module"
        allowed = ["sys"]  # list of permitted modules
        try:
            src = inspect.getsource(import_module(self.filename.split('.')[0]))
            tree = ast.parse(src)
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
        stimp = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    stimp.append(alias.name)
        for modname in stimp:
            if modname not in allowed:
                raise AssertionError(f'You have imported a prohibited module.\n'
                    f'module {modname} is not allowed. Review the Wiki' 
                    ' instructions again.')


class TestFinal(unittest.TestCase): 

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)

    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{d:02}/{m:02}/{y}'
    

    def test_pos_arg(self):
        "script returns expected output with positive number"
        for _ in range(1, 3):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            num = randint(0, 500)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%a, %d/%m/%Y')
            error_msg = (f'Running your script with arguments\n'
                         f'"{date1} {num}" should return the output:'
                         f'"The end date is {e}."\n'
                         f'Fix your output and try again.\n')
            input = [date1, str(num)]
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=10)
            self.assertIn(e, output.decode('utf-8'), error_msg)

    def test_neg_arg(self):
        "script returns expected output with negative number"
        for _ in range(1, 3):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%d/%m/%Y')
            num = randint(-500, -1)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%a, %d/%m/%Y')
            error_msg = (f'Running your script with arguments\n'
                         f'"{date1} {num}" should return the output:'
                         f'"The end date is {e}."\n'
                         f'Fix your output and try again.\n')
            input = [date1, str(num)]
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=10)
            self.assertIn(e, output.decode('utf-8'), error_msg)
    
    def test_invalid_date(self):
        "output contains usage when bad date"
        test_dat = [
            '01/25/2022',
            '01/20/2001',
            '00/11/1539',
            '29/02/2021',
            '31/04/2023'
        ]
        error_msg = "Error: Entering an invalid date should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        for datestr in test_dat:
            input = [datestr, '100']
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate(timeout=10)
            self.assertRegex(output.decode('utf-8'), e, error_msg)

    def test_invalid_num(self):
        "output contains usage when bad number" 
        error_msg = "Error: Entering an invalid second argument should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        input = ['20/04/1969', 'e']
        cmd = [self.pypath, self.filename] + input
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = p.communicate(timeout=10)
        self.assertRegex(output.decode('utf-8'), e, error_msg)
    
    def test_arg_length(self):
        "when args != 2, output contains usage"
        error_msg = "Error: Entering wrong number of args should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        input = ['25/01/2023']
        cmd = [self.pypath, self.filename] + input
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = p.communicate()
        self.assertRegex(output.decode('utf-8'), e, error_msg)

if __name__ == "__main__":
    unittest.main(buffer=True)  # buffer line suppresses a1 printlines from check script output.

