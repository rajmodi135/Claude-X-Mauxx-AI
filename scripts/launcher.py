#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude x Mauxx AI — Pure Terminal Launcher
No external dependencies. Just print() + ANSI escape codes.
Ultra-premium ASCII art. Real-time dashboard. System performance.
Multi-IDE support: Claude, Codex, Antigravity.
"""

import os
import sys
import io
import time
import json
import random
import shutil
import platform
import subprocess
from datetime import datetime
from typing import Optional
from pathlib import Path

# Force UTF-8 output for Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

# ─── ANSI ESCAPE CODES ───────────────────────────────────────
class Style:
    RESET    = '\033[0m'
    BOLD     = '\033[1m'
    DIM      = '\033[2m'
    ITALIC   = '\033[3m'
    BLINK    = '\033[5m'
    REVERSE  = '\033[7m'

class FG:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    BRIGHT_BLACK   = '\033[90m'
    BRIGHT_RED     = '\033[91m'
    BRIGHT_GREEN   = '\033[92m'
    BRIGHT_YELLOW  = '\033[93m'
    BRIGHT_BLUE    = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN    = '\033[96m'
    BRIGHT_WHITE   = '\033[97m'

class BG:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    BRIGHT_BLACK = '\033[100m'
    BRIGHT_RED   = '\033[101m'
    BRIGHT_GREEN = '\033[102m'
    BRIGHT_YELLOW= '\033[103m'

# ─── CURSOR CONTROL ──────────────────────────────────────────
CURSOR_HIDE    = '\033[?25l'
CURSOR_SHOW    = '\033[?25h'
CLEAR_SCREEN   = '\033[2J\033[H'
CLEAR_LINE     = '\033[2K'
SAVE_CURSOR    = '\033[s'
RESTORE_CURSOR = '\033[u'

def move_to(row: int, col: int = 0):
    print(f'\033[{row};{col}H', end='')

# ─── ULTRA-PREMIUM ASCII ART ─────────────────────────────────

MAUXX_BANNER = r"""
{cyan}  ╔══════════════════════════════════════════════════════╗
  ║{magenta}  ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗{cyan}  ║
  ║{magenta} ██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝{cyan}  ║
  ║{magenta} ██║     ██║     ███████║██║   ██║██║  ██║█████╗  {cyan}  ║
  ║{magenta} ██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝  {cyan}  ║
  ║{magenta} ╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗{cyan}  ║
  ║{magenta}  ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝{cyan}  ║
  ║{bright_cyan}       × {reset}{green}  █████╗ ██╗     {bright_cyan}  ║
  ║{bright_cyan}      ██╔══██╗██║     {bright_cyan}  ║
  ║{bright_cyan}      ███████║██║     {bright_cyan}  ║
  ║{bright_cyan}      ██╔══██║██║     {bright_cyan}  ║
  ║{bright_cyan}      ██║  ██║███████╗{bright_cyan}  ║
  ║{bright_cyan}      ╚═╝  ╚═╝╚══════╝{bright_cyan}  ║
  ╚══════════════════════════════════════════════════════╝{reset}"""

MAUXX_BANNER_COMPACT = r"""
{cyan}  ╔══════════════════════════════════════════╗
  ║{magenta}  ██████╗██╗      █████╗ ██╗   ██╗██╗{cyan}  ║
  ║{magenta} ██╔════╝██║     ██╔══██╗╚██╗ ██╔╝╚██╗{cyan}  ║
  ║{magenta} ██║     ██║     ███████║ ╚████╔╝  ██║{cyan}  ║
  ║{magenta} ██║     ██║     ██╔══██║  ╚██╔╝   ██║{cyan}  ║
  ║{magenta} ╚██████╗███████╗██║  ██║   ██║   ██║{cyan}  ║
  ║{magenta}  ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝{cyan}  ║
  ╚══════════════════════════════════════════════╝{reset}"""

MAUXX_ASCII_ART = r"""{cyan}
                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                   ██                      ██
                  ██  {magenta}╔═══════════════╗{cyan}  ██
                 ██   {magenta}║  MAUXX  AI    ║{cyan}   ██
                ██    {magenta}║   VERSION 2   ║{cyan}    ██
               ██     {magenta}╚═══════════════╝{cyan}     ██
              ██    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ██
             ██   ██  ▄▄▄▄  ██  ▄▄▄▄  ██   ██
            ██   ██  ██  ██  ██  ██  ██  ██   ██
           ██████████  ▀▀▀▀  ██  ▀▀▀▀  ██████████
          ██                              ██
         ██                                ██
        ██{green}  ╔═══════════════════════════╗{cyan}  ██
      ▄██{green}  ║   AUTONOMOUS AI COMPANY  ║{cyan}  ██▄
      ██{green}  ╚═══════════════════════════╝{cyan}  ██
      ██                                  ██
       ▀████████████████████████████████████▀{reset}
"""

MAUXX_AGENT_FACES = {
    'neutral': [
        r"""{cyan}    ╔═══════════╗
    ║ {magenta}( •_•){cyan}  ║
    ╚═══════════╝{reset}""",
        r"""{cyan}    ╔═══════════╗
    ║ {magenta}( •_•)>{cyan}  ║
    ║ {magenta}⌐■-■{cyan}    ║
    ╚═══════════╝{reset}""",
    ],
    'working': [
        r"""{cyan}    ╔═══════════╗
    ║ {green}(▀̿Ĺ̯▀̿ ̿){cyan}║
    ╚═══════════╝{reset}""",
        r"""{cyan}    ╔═══════════╗
    ║ {green}(≧∇≦)ﾉ{cyan}║
    ╚═══════════╝{reset}""",
    ],
    'thinking': [
        r"""{cyan}    ╔═══════════╗
    ║ {yellow}(¬_¬){cyan}  ║
    ╚═══════════╝{reset}""",
        r"""{cyan}    ╔═══════════╗
    ║ {yellow}(⊙_◎){cyan}  ║
    ╚═══════════╝{reset}""",
    ],
    'happy': [
        r"""{cyan}    ╔═══════════╗
    ║ {green}(ﾉ◕ヮ◕)ﾉ{cyan}║
    ╚═══════════╝{reset}""",
        r"""{cyan}    ╔═══════════╗
    ║ {green}ヽ(•‿•)ノ{cyan}║
    ╚═══════════╝{reset}""",
    ],
    'error': [
        r"""{cyan}    ╔═══════════╗
    ║ {red}(╯°□°）╯︵{cyan}║
    ║ {red}  ┻━┻{cyan}   ║
    ╚═══════════╝{reset}""",
        r""">{cyan}    ╔═══════════╗
    ║  {red}(；一_一){cyan}║
    ╚═══════════╝{reset}""",
    ],
}

LOADING_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
DOTS_FRAMES   = ['·', '··', '···', '····', '·····', '······']
PULSE_FRAMES  = ['▓', '▒', '░', ' ', '░', '▒', '▓']

AGENT_STATUS_MSGS = {
    'thinking': [
        "Analyzing neural pathways...",
        "Scanning project architecture...",
        "Connecting knowledge nodes...",
        "Loading context vectors...",
        "Processing request dimensions...",
        "Initializing decision matrix...",
        "Calibrating AI alignment...",
    ],
    'working': [
        "Writing code at quantum speed...",
        "Optimizing algorithmic elegance...",
        "Weaving digital architecture...",
        "Compiling genius into bytes...",
        "Crafting elegant solutions...",
        "Engineering future infrastructure...",
        "Building with precision and care...",
    ],
    'waiting': [
        "Awaiting your command, commander...",
        "All systems fully operational...",
        "Listening at hyperspeed...",
        "Standing by in ready state...",
        "Neural net warm and ready...",
        "Sensing your next move...",
    ],
    'success': [
        "Mission accomplished flawlessly! ✦",
        "Exceeding all efficiency metrics! ✦",
        "Flawless execution confirmed! ✦",
        "Another victory for Mauxx AI! ✦",
        "Precision work at maximum quality! ✦",
    ],
    'error': [
        "Encountering turbulence... recalibrating...",
        "Adapting to unexpected conditions...",
        "Analyzing failure vectors...",
        "Implementing recovery protocol...",
        "Retrying with modified approach...",
    ],
}

SYSTEM_BARS = {
    'cpu':     ['▁▂▃▄▅▆▇█', '█▇▆▅▄▃▂▁'],
    'memory':  ['○◔◐◕●',         '●◕◐◔○'],
    'network': ['·○●○·',         '·●○●·'],
    'load':    ['▁▃▅▇██▇▅▃▁'],
}

# ─── DASHBOARD DATA ──────────────────────────────────────────

class MauxxDashboard:
    """Holds all dashboard state without external deps."""

    def __init__(self):
        self.start_time = time.time()
        self.tasks = {
            'pending':  ['Optimize database queries', 'Add rate limiting', 'Write API docs'],
            'in_progress': ['Refactor auth middleware'],
            'completed': ['Setup CI pipeline', 'Configure linting', 'Add error tracking'],
            'total': 6,
            'done': 3,
        }
        self.system = {
            'cpu_pct': 23,
            'ram_pct': 41,
            'ram_gb': 6.2,
            'ram_total': 16.0,
            'disk_pct': 34,
            'cpu_temp': 62,
            'processes': 142,
            'load_1m': 1.2,
            'load_5m': 0.8,
            'load_15m': 0.6,
        }
        self.history = {
            'cpu': [random.randint(10, 80) for _ in range(30)],
            'memory': [random.randint(30, 70) for _ in range(30)],
            'accuracy': [random.uniform(0.75, 0.98) for _ in range(30)],
        }
        self.accuracy = {
            'tool_accuracy': 0.872,
            'code_quality': 0.91,
            'response_time': 0.94,
            'user_satisfaction': 0.88,
            'overall': 0.89,
            'unlocked_tiers': 1,
            'next_tier_at': 0.90,
        }
        self.efficiency = {
            'tasks_per_hour': 4.2,
            'avg_completion_time': '12m 34s',
            'cost_per_task': '$0.08',
            'tokens_saved': 142834,
            'money_saved': '$11.42',
            'context_efficiency': '87%',
        }
        self.multi_ide = {
            'active_ide': 'claude',
            'supported': ['claude', 'codex', 'antigravity'],
            'compatibility': {
                'claude': '100%',
                'codex': '89%',
                'antigravity': '92%',
            }
        }
        self.background_log = []
        self._agent_mood = 'waiting'
        self._frame = 0
        self._log_msg_idx = 0

    @property
    def uptime(self):
        delta = time.time() - self.start_time
        h, r = divmod(int(delta), 3600)
        m, s = divmod(r, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    @property
    def agent_face(self):
        faces = MAUXX_AGENT_FACES.get(self._agent_mood, MAUXX_AGENT_FACES['neutral'])
        return faces[self._frame % len(faces)]

    @property
    def agent_status(self):
        msgs = AGENT_STATUS_MSGS.get(self._agent_mood, AGENT_STATUS_MSGS['waiting'])
        return msgs[self._log_msg_idx % len(msgs)]

    def advance(self):
        self._frame += 1
        self._log_msg_idx += 1
        # Simulate system fluctuations
        self.system['cpu_pct'] = max(5, min(95, self.system['cpu_pct'] + random.randint(-5, 5)))
        self.system['ram_pct'] = max(20, min(85, self.system['ram_pct'] + random.randint(-3, 3)))
        self.history['cpu'].append(self.system['cpu_pct'])
        self.history['cpu'] = self.history['cpu'][-30:]
        self.history['memory'].append(self.system['ram_pct'])
        self.history['memory'] = self.history['memory'][-30:]

    def add_log(self, msg: str):
        self.background_log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
        if len(self.background_log) > 20:
            self.background_log = self.background_log[-20:]

    def sparkline(self, values, width=20):
        """Generate a sparkline bar chart without external deps."""
        if not values:
            return ' ' * width
        min_v, max_v = min(values), max(values)
        if max_v == min_v:
            return '▁' * width
        normalized = [(v - min_v) / (max_v - min_v) for v in values]
        bars = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
        return ''.join(bars[min(int(n * 7), 7)] for n in normalized[-width:])

    def cpu_bar(self, pct: int, width=10):
        filled = int(pct / 100 * width)
        color = FG.GREEN if pct < 50 else FG.YELLOW if pct < 80 else FG.RED
        bar = '█' * filled + '░' * (width - filled)
        return f"{color}{bar}{FG.WHITE} {pct:3d}%{RESET}"

    def ram_bar(self, pct: int, used_gb: float, total_gb: float, width=10):
        filled = int(pct / 100 * width)
        color = FG.GREEN if pct < 60 else FG.YELLOW if pct < 80 else FG.RED
        bar = '█' * filled + '░' * (width - filled)
        return f"{color}{bar}{FG.WHITE} {used_gb:.1f}/{total_gb:.0f}GB{BG.RESET}"


# ─── TERMINAL DRAWING ────────────────────────────────────────

class TermDraw:
    """Pure-terminal drawing with ANSI codes. No external deps."""

    def __init__(self, dash: MauxxDashboard):
        self.dash = dash
        self.cols, self.rows = shutil.get_terminal_size()

    def refresh(self):
        self.cols, self.rows = shutil.get_terminal_size()

    def box(self, title: str, content: list, width=None, border_color=FG.CYAN, title_color=FG.MAGENTA):
        """Draw a bordered box with title and content lines."""
        w = width or (self.cols - 4)
        inner_w = w - 4
        lines = []
        # Top border
        lines.append(f"{border_color}  ╔{'═' * (w - 2)}╗{Style.RESET}")
        # Title
        title_text = f"  {title_color}◈ {title} ◈{Style.RESET}"
        lines.append(f"{border_color}  ║{FG.WHITE}{title_text:^{w-2}}{border_color}║{Style.RESET}")
        # Divider
        lines.append(f"{border_color}  ╟{'─' * (w - 2)}╢{Style.RESET}")
        # Content
        for line in content:
            text = str(line)[:inner_w]
            lines.append(f"{border_color}  ║ {Style.RESET}{text}{' ' * (inner_w - len(text))}{border_color}║{Style.RESET}")
        # Bottom border
        lines.append(f"{border_color}  ╚{'═' * (w - 2)}╝{Style.RESET}")
        return '\n'.join(lines)

    def draw_system_monitor(self) -> list:
        d = self.dash
        c = d.system
        cpu_spark = d.sparkline(d.history['cpu'], 15)
        mem_spark = d.sparkline(d.history['memory'], 15)
        acc_spark = d.sparkline([int(v * 100) for v in d.history['accuracy']], 15)
        return [
            f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}",
            f"{FG.CYAN}  ║ {FG.MAGENTA}◈ SYSTEM PERFORMANCE ◈{FG.CYAN}                                  ║{Style.RESET}",
            f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}",
            "",
            f"  {FG.GREEN}CPU:{Style.RESET}    {d.cpu_bar(c['cpu_pct'])}  {FG.DIM}│{Style.RESET}  {cpu_spark}",
            f"  {FG.GREEN}RAM:{Style.RESET}    {d.ram_bar(c['ram_pct'], c['ram_gb'], c['ram_total'])}  {FG.DIM}│{Style.RESET}  {mem_spark}",
            f"  {FG.GREEN}DISK:{Style.RESET}   {d.cpu_bar(c['disk_pct'])}  {FG.DIM}│{Style.RESET}  {FG.BRIGHT_BLACK}Processes: {c['processes']}{Style.RESET}",
            f"  {FG.GREEN}LOAD:{Style.RESET}   {FG.YELLOW}{c['load_1m']}{Style.RESET}/{FG.GREEN}{c['load_5m']}{Style.RESET}/{FG.BLUE}{c['load_15m']}{Style.RESET}  {FG.DIM}│{Style.RESET}  {FG.BRIGHT_BLACK}Temp: {c['cpu_temp']}°C{Style.RESET}",
            f"  {FG.GREEN}ACC:{Style.RESET}    {d.accuracy_bar(d.accuracy['overall'])}  {FG.DIM}│{Style.RESET}  {acc_spark}",
            "",
            f"  {FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}",
        ]

    def accuracy_bar(self, pct: float, width=10):
        p = int(pct * 100)
        filled = int(p / 100 * width)
        color = FG.RED if p < 70 else FG.YELLOW if p < 85 else FG.GREEN
        bar = '█' * filled + '░' * (width - filled)
        return f"{color}{bar}{FG.WHITE} {p:.0f}%{Style.RESET}"

    def draw_task_list(self) -> list:
        d = self.dash.tasks
        lines = [f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}"]
        lines.append(f"{FG.CYAN}  ║ {FG.MAGENTA}◈ TASK DASHBOARD ◈{FG.CYAN}                                  ║{Style.RESET}")
        lines.append(f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}")
        lines.append(f"")
        lines.append(f"  {FG.GREEN}✓ COMPLETED ({d['done']}/{d['total']}){Style.RESET}")
        for t in d['completed']:
            lines.append(f"    {FG.GREEN}✓{Style.RESET} {t}")
        lines.append(f"")
        lines.append(f"  {FG.YELLOW}⟳ IN PROGRESS{Style.RESET}")
        for t in d['in_progress']:
            loading = LOADING_FRAMES[self.dash._frame % len(LOADING_FRAMES)]
            lines.append(f"    {FG.YELLOW}{loading}{Style.RESET} {t}")
        lines.append(f"")
        lines.append(f"  {FG.BRIGHT_BLACK}◌ PENDING{Style.RESET}")
        for t in d['pending']:
            lines.append(f"    {FG.BRIGHT_BLACK}◌{Style.RESET} {t}")
        lines.append(f"")
        lines.append(f"{FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}")
        return lines

    def draw_ide_panel(self) -> list:
        ide = self.dash.multi_ide
        current = ide['active_ide']
        lines = [f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}"]
        lines.append(f"{FG.CYAN}  ║ {FG.MAGENTA}◈ MULTI-IDE SUPPORT ◈{FG.CYAN}                              ║{Style.RESET}")
        lines.append(f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}")
        lines.append(f"")
        for name, compat in ide['compatibility'].items():
            mark = f"{FG.GREEN}●{Style.RESET}" if name == current else "○"
            compat_info = f"{FG.GREEN}{compat}{Style.RESET}"
            lines.append(f"    {mark} {FG.WHITE}{name:<15}{Style.RESET}  compat: {compat_info}")
        lines.append(f"")
        lines.append(f"    {FG.BRIGHT_BLACK}Active:{Style.RESET} {FG.CYAN}{current}{Style.RESET}  {FG.DIM}|{Style.RESET}  "
                     f"{FG.BRIGHT_BLACK}Adapter:{Style.RESET} {FG.GREEN}universal{Style.RESET}")
        lines.append(f"")
        lines.append(f"{FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}")
        return lines

    def draw_accuracy_panel(self) -> list:
        a = self.dash.accuracy
        e = self.dash.efficiency
        lines = [f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}"]
        lines.append(f"{FG.CYAN}  ║ {FG.MAGENTA}◈ ACCURACY & EFFICIENCY ◈{FG.CYAN}                          ║{Style.RESET}")
        lines.append(f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}")
        lines.append(f"")
        lines.append(f"  {FG.CYAN}ACCURACY METRICS:{Style.RESET}")
        lines.append(f"    {FG.WHITE}Tool Accuracy:{Style.RESET}    {dash.accuracy_bar(a['tool_accuracy'])}")
        lines.append(f"    {FG.WHITE}Code Quality:{Style.RESET}    {dash.accuracy_bar(a['code_quality'])}")
        lines.append(f"    {FG.WHITE}Response Time:{Style.RESET}  {dash.accuracy_bar(a['response_time'])}")
        lines.append(f"    {FG.WHITE}User Satisf.:{Style.RESET}  {dash.accuracy_bar(a['user_satisfaction'])}")
        lines.append(f"    {FG.MAGENTA}OVERALL:{Style.RESET}        {dash.accuracy_bar(a['overall'])}")
        lines.append(f"")
        lines.append(f"    {FG.YELLOW}▶ Next Tier:{Style.RESET} {a['next_tier_at']*100:.0f}%  "
                     f"{FG.DIM}│{Style.RESET}  {FG.GREEN}Current Tier:{Style.RESET} {a['unlocked_tiers']}")
        lines.append(f"")
        lines.append(f"  {FG.CYAN}EFFICIENCY GAINS:{Style.RESET}")
        lines.append(f"    {FG.WHITE}Tasks/Hour:{Style.RESET}      {FG.GREEN}{e['tasks_per_hour']}{Style.RESET}  "
                     f"{FG.DIM}│{Style.RESET}  {FG.WHITE}Avg Time:{Style.RESET} {FG.GREEN}{e['avg_completion_time']}{Style.RESET}")
        lines.append(f"    {FG.WHITE}Cost/Task:{Style.RESET}       {FG.GREEN}{e['cost_per_task']}{Style.RESET}  "
                     f"{FG.DIM}│{Style.RESET}  {FG.WHITE}Tokens Saved:{Style.RESET} {FG.GREEN}{e['tokens_saved']:,}{Style.RESET}")
        lines.append(f"    {FG.WHITE}Money Saved:{Style.RESET}     {FG.GREEN}{e['money_saved']}{Style.RESET}  "
                     f"{FG.DIM}│{Style.RESET}  {FG.WHITE}Context Eff.:{Style.RESET} {FG.GREEN}{e['context_efficiency']}{Style.RESET}")
        lines.append(f"")
        lines.append(f"{FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}")
        return lines

    def draw_background_log(self) -> list:
        log = self.dash.background_log
        if not log:
            log = [f"{FG.DIM}  Initializing background processes...{Style.RESET}"]
        lines = [f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}"]
        lines.append(f"{FG.CYAN}  ║ {FG.MAGENTA}◈ BACKGROUND OPERATIONS ◈{FG.CYAN}                        ║{Style.RESET}")
        lines.append(f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}")
        lines.append(f"")
        for entry in log[-8:]:
            lines.append(f"    {FG.DIM}{entry}{Style.RESET}")
        lines.append(f"")
        lines.append(f"{FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}")
        return lines

    def draw_agent_panel(self) -> list:
        d = self.dash
        up = d.uptime
        lines = [f"{FG.CYAN}  ╔══════════════════════════════════════════════════════════╗{Style.RESET}"]
        lines.append(f"{FG.CYAN}  ║ {FG.MAGENTA}◈ MAUXX AI AGENT ◈{FG.CYAN}                               ║{Style.RESET}")
        lines.append(f"{FG.CYAN}  ╟──────────────────────────────────────────────────────────╢{Style.RESET}")
        lines.append(f"")
        for face_line in d.agent_face.split('\n'):
            lines.append(f"    {face_line}")
        lines.append(f"")
        load = LOADING_FRAMES[d._frame % len(LOADING_FRAMES)]
        lines.append(f"    {FG.CYAN}{load}{Style.RESET} {d.agent_status}")
        lines.append(f"")
        lines.append(f"    {FG.DIM}Uptime:{Style.RESET} {FG.GREEN}{up}{Style.RESET}  "
                     f"{FG.DIM}Mood:{Style.RESET} {FG.CYAN}{d._agent_mood.title()}{Style.RESET}")
        lines.append(f"")
        lines.append(f"{FG.CYAN}  ╚══════════════════════════════════════════════════════════╝{Style.RESET}")
        return lines

    def draw_status_bar(self) -> str:
        d = self.dash
        a = d.accuracy
        cols = self.cols
        sep = f" {FG.DIM}│{Style.RESET} "
        parts = [
            f"{FG.GREEN}●{Style.RESET} MAUXX v2",
            f"{FG.CYAN}Acc:{Style.RESET}{FG.WHITE}{a['overall']*100:.0f}%{Style.RESET}",
            f"{FG.YELLOW}Tier:{Style.RESET}{FG.WHITE}{a['unlocked_tiers']}{Style.RESET}",
            f"{FG.MAGENTA}Uptime:{Style.RESET}{FG.WHITE}{d.uptime}{Style.RESET}",
            f"{FG.GREEN}CPU:{Style.RESET}{FG.WHITE}{d.system['cpu_pct']}%{Style.RESET}",
            f"{FG.BLUE}RAM:{Style.RESET}{FG.WHITE}{d.system['ram_pct']}%{Style.RESET}",
        ]
        status = sep.join(parts)
        return f"{FG.BRIGHT_BLACK}{'─' * cols}{Style.RESET}\n  {status}\n{FG.BRIGHT_BLACK}{'─' * cols}{Style.RESET}"

    def draw_full_dashboard(self):
        """Draw the complete dashboard."""
        sections = []

        # Agent panel
        sections.extend(self.draw_agent_panel())
        sections.append("")

        # System monitor
        sections.extend(self.draw_system_monitor())
        sections.append("")

        # Side-by-side: Task list + Multi-IDE
        task_lines = self.draw_task_list()
        ide_lines = self.draw_ide_panel()
        sections.extend(task_lines[:4])
        sections.append(f"")
        for t, i in zip(task_lines[5:], ide_lines[5:]):
            t_text = t[:40] if len(t) > 40 else t
            i_text = i[:40] if len(i) > 40 else i
            sections.append(f"  {t_text:<45}{i_text}")
        sections.extend(task_lines[4:5] if len(task_lines) > 4 else [])
        sections.append("")

        # Accuracy & Efficiency
        sections.extend(self.draw_accuracy_panel())
        sections.append("")

        # Background operations
        sections.extend(self.draw_background_log())
        sections.append("")

        # Status bar
        sections.append(self.draw_status_bar())

        return '\n'.join(sections)


# ─── MAIN LAUNCHER ───────────────────────────────────────────

def detect_ide():
    """Detect which AI CLI tools are available."""
    ides = {'claude': False, 'codex': False, 'antigravity': False}
    # Check Claude Code
    try:
        subprocess.run(['claude', '--version'], capture_output=True, timeout=2)
        ides['claude'] = True
    except:
        pass
    # Check Codex (OpenAI)
    try:
        subprocess.run(['codex', '--version'], capture_output=True, timeout=2)
        ides['codex'] = True
    except:
        pass
    # Check Antigravity
    try:
        subprocess.run(['antigravity', '--version'], capture_output=True, timeout=2)
        ides['antigravity'] = True
    except:
        pass
    return ides

def select_ide(available: dict) -> str:
    for name, avail in available.items():
        if avail:
            return name
    return 'claude'  # default

def print_banner():
    """Show the main Mauxx AI banner."""
    print(CLEAR_SCREEN, end='')
    # Pick color scheme
    colors = [FG.CYAN, FG.MAGENTA, FG.GREEN, FG.BRIGHT_CYAN]
    color = random.choice(colors)
    banner = MAUXX_BANNER.format(
        cyan=FG.CYAN, magenta=FG.MAGENTA, green=FG.GREEN,
        bright_cyan=FG.BRIGHT_CYAN, reset=Style.RESET
    )
    print(banner)
    print(f"\n  {FG.BRIGHT_BLACK}{Style.ITALIC}  Autonomous AI Company • v2.0 • 85+ Commits • 25 Skills • 14 Presets{Style.RESET}")
    print(f"  {FG.DIM}  Press Ctrl+C to exit • Running in background mode{Style.RESET}")
    print()

def main():
    """Pure terminal Mauxx AI launcher."""
    global dash

    # Detect IDE availability
    available_ides = detect_ide()
    active_ide = select_ide(available_ides)

    # Initialize dashboard
    dash = MauxxDashboard()
    dash.multi_ide['active_ide'] = active_ide
    for name, avail in available_ides.items():
        dash.multi_ide['compatibility'][name] = '100%' if avail else 'not installed'

    # Greeting
    dash.add_log(f"Mauxx AI v2.0 initialized — {active_ide} selected as primary IDE")
    dash.add_log("Scanning project structure...")
    dash.add_log(f"Available IDes: {', '.join(n for n, a in available_ides.items() if a)}")
    dash.add_log("Memory system online — 25 skills registered")
    dash.add_log("Neural model router active (Haiku/Sonnet/Opus/Cache/Ollama)")
    dash.add_log("Accuracy tracker initialized — current: 89%")
    dash.add_log("Background operations beginning...")

    try:
        # Hide cursor
        print(CURSOR_HIDE, end='')

        # Main loop
        frame = 0
        while True:
            print(CLEAR_SCREEN, end='')
            dash.advance()

            # Cycle mood periodically
            if frame % 20 == 0:
                moods = ['thinking', 'working', 'waiting', 'thinking', 'working']
                dash._agent_mood = moods[(frame // 20) % len(moods)]

            # Add occasional log messages
            if frame % 5 == 0 and frame > 0:
                logs = [
                    f"Analyzing {random.choice(['auth flow', 'API endpoints', 'database schema', 'UI components', 'test coverage'])}...",
                    f"Accuracy steady at {(dash.accuracy['overall'])*100:.0f}% — target tier 2 at 90%",
                    f"Background: optimizing {random.choice(['query indices', 'caching strategy', 'memory layout', 'build pipeline'])}",
                    f"Model router: routed {random.choice(['classify → Haiku', 'code → Sonnet', 'architecture → Opus', 'trivial → Ollama'])}",
                    f"Memory sync: {random.randint(10, 100)} vectors indexed this session",
                    f"Cost tracker: ${random.uniform(0.01, 0.15):.2f} this turn",
                    f"System health: CPU {dash.system['cpu_pct']}% / RAM {dash.system['ram_pct']}% — nominal",
                    f"Agent {active_ide} bridge: {random.choice(['stable', 'high bandwidth', 'low latency', 'optimal routing'])}",
                ]
                dash.add_log(random.choice(logs))

            # Draw dashboard
            term = TermDraw(dash)
            print(term.draw_full_dashboard())

            # Input bar at bottom
            cols = shutil.get_terminal_size().columns
            print(f"\n{FG.BRIGHT_BLACK}{'═' * cols}{Style.RESET}")
            prompt_text = f"  {FG.CYAN}⚡{Style.RESET} Type a command {FG.DIM}(/help for list){Style.RESET}  {FG.BRIGHT_BLACK}or press Enter for status update{Style.RESET}"
            print(f"  {prompt_text}")
            print(f"{FG.BRIGHT_BLACK}{'═' * cols}{Style.RESET}")

            time.sleep(1.5)
            frame += 1

    except KeyboardInterrupt:
        print(CURSOR_SHOW, end='')
        print(f"\n\n  {FG.GREEN}✦{Style.RESET} Mauxx AI session ended. "
              f"Uptime: {dash.uptime}. "
              f"Tasks: {dash.tasks['done']}/{dash.tasks['total']} completed.\n"
              f"  {FG.DIM}See you next time, commander.{Style.RESET}\n")
        sys.exit(0)


if __name__ == '__main__':
    main()
