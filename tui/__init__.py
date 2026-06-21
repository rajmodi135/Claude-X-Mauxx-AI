#!/usr/bin/env python3
"""
Claude x Mauxx AI — Neon TUI Launcher
Entry point to launch the Mauxx AI terminal user interface.
"""

import sys
import os

# Ensure the tui directory is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mauxx_tui import main

if __name__ == "__main__":
    main()
