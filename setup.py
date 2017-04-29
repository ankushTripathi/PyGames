__author__ = 'ankush'
from cx_Freeze import setup, Executable

executables = [Executable("events.py")]

setup(name='snakes',
      options = {"build.exe":{"packages":["pygame"]}},
      version='0.1',
      description='Simple snakes game',
      executables=executables
      )


