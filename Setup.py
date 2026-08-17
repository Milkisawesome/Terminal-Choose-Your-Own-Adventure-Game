"""
build.py - Packages Main.py (which imports story.py) into a single
standalone executable using PyInstaller.

USAGE:
    1. Place this file in the same folder as Main.py and story.py.
    2. Run:  python build.py
    3. Find the finished executable in the "dist" folder that gets
       created next to this script.

REQUIREMENTS:
    - numpy must be installed (Main.py imports it directly):
          pip install numpy
    - pygame is optional (Main.py already handles it not being
      installed), but install it if you want sound in the built app:
          pip install pygame
    - PyInstaller will be installed automatically by this script if
      it isn't already present.
"""

import os
import subprocess
import sys

APP_NAME = "LastTrainToNowhere"
ENTRY_POINT = "Main.py"
REQUIRED_MODULE = "story.py"


def ensure_pyinstaller():
    """Install PyInstaller if it isn't already available."""
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("PyInstaller not found - installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def build():
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, ENTRY_POINT)
    story_path = os.path.join(here, REQUIRED_MODULE)

    if not os.path.isfile(entry_path):
        sys.exit(
            f"Could not find {ENTRY_POINT} in {here}.\n"
            f"Run this script from the same folder as {ENTRY_POINT} and {REQUIRED_MODULE}."
        )
    if not os.path.isfile(story_path):
        sys.exit(
            f"Could not find {REQUIRED_MODULE} in {here}.\n"
            f"{REQUIRED_MODULE} must sit right next to {ENTRY_POINT} "
            f"so PyInstaller can detect it via the 'import story' statement."
        )

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",        # bundle everything into a single executable
        "--console",        # this is a terminal/console game
        "--name", APP_NAME,
        "--clean",
        entry_path,
    ]

    print("Building executable, this may take a minute...")
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=here)

    dist_dir = os.path.join(here, "dist")
    exe_name = f"{APP_NAME}.exe" if sys.platform.startswith("win") else APP_NAME
    exe_path = os.path.join(dist_dir, exe_name)

    print("\nBuild complete!")
    print(f"Executable created at: {exe_path}")
    print("also generated - only the file in 'dist' is needed to run the game.")


if __name__ == "__main__":
    ensure_pyinstaller()
    build()