import os
import shutil
import tempfile
import ctypes
from ctypes import wintypes
from pathlib import Path

def resource_path(filename: str) -> str:
    """
    Returns the absolute path to a file in app/resources
    """
    # Directory of this utils.py file
    current_dir = Path(__file__).resolve()

    # Go up one level to 'app' and into 'resources'
    resources_dir = current_dir.parent / "resources"

    return str(resources_dir / filename)

def windows_config(window):
        # --- PyInstaller-safe ctypes icon setup ---
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = wintypes.HWND(int(window.winId()))

    # Extract icon to a temporary file so LoadImageW can access it
    ico_src = resource_path("favicon.ico")
    temp_dir = tempfile.gettempdir()
    ico_temp = os.path.join(temp_dir, "favicon.ico")
    shutil.copyfile(ico_src, ico_temp)

    # Small icon (16x16)
    hicon_small = ctypes.windll.user32.LoadImageW(
        None,
        ico_temp,
        1,  # IMAGE_ICON
        16,
        16,
        0x00000010  # LR_LOADFROMFILE
    )

    # Big icon (32x32)
    hicon_big = ctypes.windll.user32.LoadImageW(
        None,
        ico_temp,
        1,  # IMAGE_ICON
        32,
        32,
        0x00000010  # LR_LOADFROMFILE
    )

    user32.SendMessageW(hwnd, 0x0080, 0, hicon_small)  # WM_SETICON small
    user32.SendMessageW(hwnd, 0x0080, 1, hicon_big)    # WM_SETICON big

    # Set console title (optional)
    ctypes.windll.kernel32.SetConsoleTitleW("ANorm.exe")