#!/usr/bin/env python3
"""
═══ CLAUDE × MAUXX AI — NEON TUI LAUNCHER ═══

Runs the Mauxx AI terminal interface.
Install dependencies: pip install textual rich

Usage:
    python run.py                          # Start TUI with onboarding
    python run.py --profession developer   # Skip onboarding
    python run.py --profession designer    # Skip onboarding
    python run.py --help                   # Full options
"""

import sys
import os
from pathlib import Path

# Add this directory to path
sys.path.insert(0, str(Path(__file__).parent))

from mauxx_tui import main

if __name__ == "__main__":
    main()
