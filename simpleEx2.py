#!/usr/bin/env python3
import subprocess
result = subprocess.run(["ls", "this_file_doe_not_exist"])
print(result.returncode)