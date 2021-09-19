import os
import subprocess
import tempfile

import appscript

appscript.app('Terminal').do_script('appium --session-override')
#print(abc)
import subprocess
output = subprocess.getoutput("ps -A | grep appium")
print(output.find("node"))
# -1 chưa mở apppium

