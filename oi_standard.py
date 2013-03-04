# oi testing

import os
import sys
import time
import subprocess

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


print "oi"
time.sleep(.5)
print "is"
time.sleep(.5)
print "back"
time.sleep(1)
print "!"
time.sleep(.5)
print bcolors.WARNING +"Enter message text. Type Ctrl-d on new line to send or Ctrl-c to cancel:\n" + bcolors.ENDC

userMessage = raw_input()

new_env = os.environ.copy()

new_env["DISPLAY"] = "bayridge.nycb.mpc.local:0.0"
subprocess.Popen( ["python2.6.4", "oi_gui.py", userMessage], env=new_env)

