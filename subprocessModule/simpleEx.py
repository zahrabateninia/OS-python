#!/usr/bin/env python3
import subprocess
subprocess.run(["date"])
subprocess.run(["sleep","2"]) 
# The run function receives a list that starts with the name of the command
#  that we wanna call followed by any parameters that we wanna pass to that command