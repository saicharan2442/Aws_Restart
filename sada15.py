#Exercise 1: Using os.system

import os
os.system("ls")

#Exercise 2: Using subprocess.run
import subprocess

# Exercise 2: Run "ls"
print("\nExercise 2: Listing files in the current directory")
subprocess.run(["ls"])

# Exercise 3: Run "ls -l" (long listing format)
print("\nExercise 3: Listing files with long format")
subprocess.run(["ls", "-l"])

# Exercise 4: Run "ls -l README.md" (specific file)
print("\nExercise 4: Listing details for README.md")
subprocess.run(["ls", "-l", "README.md"])

# Exercise 5: Retrieve system information using "uname -a"
command = "uname"
commandArgument = "-a"
print(f"\nExercise 5: Gathering system information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])

# Exercise 6: Retrieve information about active processes using "ps -x"
command = "ps"
commandArgument = "-x"
print(f"\nExercise 6: Gathering active process information with command: {command} {commandArgument}")
subprocess.run([command, commandArgument])

'''
subprocess.run(["ls"]) → lists files in the current directory.

subprocess.run(["ls", "-l"]) → shows detailed listing (permissions, size, date).

subprocess.run(["ls", "-l", "README.md"]) → shows detailed info for a specific file.

subprocess.run(["uname", "-a"]) → prints system information (kernel, machine type, OS).

subprocess.run(["ps", "-x"]) → prints active processes.
'''