import subprocess
import os
import shutil
import sys

# Spec file
SPEC_FILE = os.path.join(".", "source", "Gui.spec")

# Destination is current dir
DEST_DIRECTORY = '.'

# Check for UPX
if os.path.isdir("upx"):
    upx_string = "--upx-dir=upx"
else:
    upx_string = ""

if os.path.isdir("build") and not sys.platform.find("mac") and not sys.platform.find("osx"):
    shutil.rmtree("build")

# Run pyinstaller for Gui
subprocess.run(" ".join([f"pyinstaller {SPEC_FILE} ",
                                      upx_string,
                                      "-y ",
                                      f"--distpath {DEST_DIRECTORY} ",
                                      ]),
                shell=True)
