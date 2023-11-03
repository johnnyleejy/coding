import os
import re


# After refactoring the code, it is now easily readable, and we also have a reusable function
# Creating a duplicate file to write the new contents and then renaming it is redundant,
# We can just edit the file directly instead.
def updateFileBuildNumber(filepath: str, variable: str):
    # Read and write permissions will suffice.
    # We should not unnecessarily grant additional permissions
    os.chmod(filepath, 0o660)

    # Read file data
    # Use with open as it is better practice
    # It automatically closes the file for us and also ensures the file is properly closed
    with open(filepath, "r") as file:
        lines = file.readlines()

    # Loop each line and edit target variable with the BuildNum environment variable
    with open(filepath, "w") as file:
        for line in lines:
            line = re.sub(f"{variable}=\d+", f"{variable}={os.environ['BuildNum']}", line)
            file.write(line)


def main():
    filedetails1 = (os.path.join(os.environ["SourcePath"], "develop", "global", "src", 'SConstruct'), 'point')
    filedetails2 = (os.path.join(os.environ["SourcePath"], "develop", "global", "src", 'VERSION'),
                    'ADLMSDK_VERSION_POINT')
    # Use a single utility function instead of duplicating code using updateSconstruct() and updateVersion() methods
    updateFileBuildNumber(filedetails1[0], filedetails1[1])
    updateFileBuildNumber(filedetails2[0], filedetails2[1])


main()
