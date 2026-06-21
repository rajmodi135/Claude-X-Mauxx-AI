"""
Claude x Mauxx AI — Claude Code Wrapper
Runs Claude Code as a subprocess and parses its output for stats.
"""

import subprocess
import asyncio
import re
import json
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ClaudeStats:
    """Stats parsed from Claude Code output."""
    tokens_used: int = 0
    tokens_total: int = 200000
    tasks_pending: int = 0
    tasks_total: int = 0
    tasks_completed: int = 0
    current_step: str = "Waiting..."
    current_plan: str = ""
    estimated_eta: str = "--:--:--"
    cost_session: float = 0.0
    cost_today: float = 0.0
    uptime: str = "0:00:00"
    agent_message: str = "I'm listening..."


class ClaudeWrapper:
    """Wraps Claude Code as an async subprocess with output parsing."""

    def __init__(self, project_dir: str = None, config_path: str = None):
        self.project_dir = project_dir or "."
        self.config_path = config_path
        self.process: Optional[asyncio.subprocess.Process] = None
        self.stats = ClaudeStats()
        self.start_time = datetime.now()
        self._buffer = ""

        # Patterns to extract from Claude output
        self._patterns = {
            'tokens': re.compile(r'(\d[\d,]*)\s*/\s*(\d[\d,]*)k?\s*tokens', re.I),
            'steps': re.compile(r'Step\s*(\d+)\s*of\s*(\d+)', re.I),
            'plan': re.compile(r'Plan:\s*(.+)', re.I),
            'cost': re.compile(r'[\$€£]\s*(\d+\.?\d*)', re.I),
            'percentage': re.compile(r'(\d+)%'),
        }

    @property
    def elapsed(self) -> str:
        delta = datetime.now() - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes:02d}:{seconds:02d}"

    def parse_output(self, text: str):
        """Parse Claude Code output for stats."""
        # Token usage
        m = self._patterns['tokens'].search(text)
        if m:
            self.stats.tokens_used = int(m.group(1).replace(',', ''))
            total = m.group(2).replace('k', '').replace(',', '')
            try:
                self.stats.tokens_total = int(total) * 1000 if 'k' not in m.group(2) else int(total) * 1000
            except ValueError:
                pass

        # Steps
        m = self._patterns['steps'].search(text)
        if m:
            self.stats.tasks_completed = int(m.group(1)) - 1
            self.stats.tasks_total = int(m.group(2))
            self.stats.tasks_pending = self.stats.tasks_total - self.stats.tasks_completed

        # Plan
        m = self._patterns['plan'].search(text)
        if m:
            self.stats.current_plan = m.group(1).strip()

        # Cost
        m = self._patterns['cost'].search(text)
        if m:
            try:
                self.stats.cost_session = float(m.group(1))
            except ValueError:
                pass

        # Progress
        m = self._patterns['percentage'].search(text)
        if m:
            pct = int(m.group(1))
            # Estimate ETA based on elapsed time and progress
            if pct > 0:
                elapsed_seconds = (datetime.now() - self.start_time).total_seconds()
                total_estimated = elapsed_seconds / (pct / 100)
                remaining = total_estimated - elapsed_seconds
                r_hours, r_rem = divmod(int(remaining), 3600)
                r_min, r_sec = divmod(r_rem, 60)
                self.stats.estimated_eta = f"{r_hours}:{r_min:02d}:{r_sec:02d}"

        self.stats.uptime = self.elapsed

    def update_agent_message(self, text: str):
        """Set a brief agent message based on context."""
        text_lower = text.lower()
        if "error" in text_lower or "fail" in text_lower:
            self.stats.agent_message = "⚠ Analyzing error..."
        elif "test" in text_lower or "pytest" in text_lower or "npm test" in text_lower:
            self.stats.agent_message = "🧪 Running tests..."
        elif "git" in text_lower:
            self.stats.agent_message = "📦 Version control..."
        elif "deploy" in text_lower or "release" in text_lower:
            self.stats.agent_message = "🚀 Deploying..."
        elif "write" in text_lower or "edit" in text_lower or "create" in text_lower:
            self.stats.agent_message = "✏️ Writing code..."
        elif "read" in text_lower or "search" in text_lower:
            self.stats.agent_message = "🔍 Reading files..."
        elif "plan" in text_lower or "design" in text_lower:
            self.stats.agent_message = "🧠 Planning..."
        else:
            self.stats.agent_message = "⚡ Working..."

    async def start(self):
        """Start Claude Code as a subprocess."""
        cmd = ["claude"]
        if self.config_path:
            cmd.extend(["--config", self.config_path])
        cmd.extend(["--dangerously-skip-permissions"])

        self.process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
            cwd=self.project_dir,
        )
        return self.process

    async def read_output(self) -> str:
        """Read one line of output from Claude Code."""
        if not self.process or not self.process.stdout:
            return ""
        try:
            line = await asyncio.wait_for(self.process.stdout.readline(), timeout=1.0)
            text = line.decode('utf-8', errors='replace')
            self.parse_output(text)
            self.update_agent_message(text)
            return text
        except asyncio.TimeoutError:
            return ""

    async def write_input(self, text: str):
        """Write input to Claude Code."""
        if self.process and self.process.stdin:
            self.process.stdin.write((text + "\n").encode('utf-8'))
            await self.process.stdin.drain()

    async def stop(self):
        """Stop Claude Code."""
        if self.process:
            self.process.terminate()
            try:
                await asyncio.wait_for(self.process.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                self.process.kill()
                await self.process.wait()

    def get_stats_dict(self) -> dict:
        return {
            'tokens_used': self.stats.tokens_used,
            'tokens_total': self.stats.tokens_total,
            'tokens_pct': round((self.stats.tokens_used / max(self.stats.tokens_total, 1)) * 100, 1),
            'tasks_pending': self.stats.tasks_pending,
            'tasks_total': self.stats.tasks_total,
            'tasks_completed': self.stats.tasks_completed,
            'current_step': self.stats.current_step,
            'current_plan': self.stats.current_plan,
            'estimated_eta': self.stats.estimated_eta,
            'cost_session': self.stats.cost_session,
            'uptime': self.stats.uptime,
            'agent_message': self.stats.agent_message,
        }
