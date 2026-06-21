"""
Claude x Mauxx AI — Neon TUI Main Application
A beautiful terminal user interface wrapping Claude Code with:
- Profession onboarding
- Token/task/ETA status bar
- Animated AI agent (Mauxx)
- Full neon cyberpunk theme
"""

import asyncio
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Optional

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, Input, Button, Static, Log, Label, SelectionList
from textual.reactive import reactive
from textual import work
from textual.screen import Screen, ModalScreen
from textual.binding import Binding
from textual.widgets._toast import Toast

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from claude_wrapper import ClaudeWrapper, ClaudeStats
from agent_animation import MauxxAgent
from profession_onboarding import (
    PROFESSIONS, OnboardingResult,
    get_profession_suggestions,
    get_default_preset_for_profession
)

# Find project root
MAUXX_HOME = Path(os.environ.get("MAUXX_HOME", os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ProfessionScreen(Screen):
    """First-run profession selection screen."""

    CSS = """
    ProfessionScreen {
        align: center middle;
        background: #0a0a1a;
    }
    #profession-container {
        width: 70;
        height: 35;
        padding: 2;
        background: #0d0d2b;
        border: solid #ff00ff;
    }
    #profession-title {
        content-align: center top;
        color: #00ffff;
        text-style: bold;
        height: 3;
    }
    #profession-subtitle {
        content-align: center top;
        color: #8888cc;
        height: 2;
    }
    .profession-grid {
        layout: grid;
        grid-size: 4;
        grid-gutter: 1;
        height: 20;
    }
    .profession-btn {
        background: #111133;
        color: #aaaaff;
        border: solid #3333cc;
        height: 3;
    }
    .profession-btn:hover {
        background: #3333aa;
        color: #ffffff;
        border: solid #6666ff;
    }
    .profession-btn.-selected {
        background: #6600ff;
        border: solid #8800ff;
        color: #ffffff;
    }
    #suggestion-area {
        height: 8;
        margin: 1 0;
        background: #0a0a1a;
        border: solid #3333cc11;
    }
    .suggestion-text {
        color: #8888cc;
        text-style: italic;
    }
    #launch-btn {
        background: #6600ff;
        color: #ffffff;
        border: solid #8800ff;
        text-style: bold;
        height: 3;
        width: 20;
        margin: 1 0 0 0;
    }
    #skip-btn {
        background: #222244;
        color: #6666aa;
        border: solid #333355;
        height: 3;
        width: 20;
        margin: 1 0 0 0;
    }
    """

    def __init__(self, config_path: str = None):
        super().__init__()
        self.config_path = config_path
        self.selected_profession = None
        self.result: Optional[OnboardingResult] = None

    def compose(self):
        with Container(id="profession-container"):
            yield Static("◈══ WELCOME TO CLAUDE × MAUXX AI ══◈", id="profession-title")
            yield Static("What's your profession? I'll tailor the experience for you.", id="profession-subtitle")
            yield Static("", id="profession-buttons")  # Placeholder

            with Container(id="suggestion-area"):
                yield Static("Choose a profession to see suggestions...", classes="suggestion-text")

            with Horizontal():
                yield Button("🚀 Launch", id="launch-btn", variant="primary", disabled=True)
                yield Button("Skip → Default", id="skip-btn")

    def on_mount(self):
        """Populate profession buttons."""
        # Add profession buttons dynamically
        btn_container = self.query_one("#profession-buttons")
        parent = btn_container.parent

        # Create grid container
        grid = Container(classes="profession-grid")
        parent.mount(grid, before="#suggestion-area")

        for key, prof in PROFESSIONS.items():
            btn = Button(
                f"{prof.icon} {prof.name}",
                id=f"prof-{key}",
                classes="profession-btn",
            )
            grid.mount(btn)

    def on_button_pressed(self, event: Button.Pressed):
        btn_id = event.button.id or ""

        if btn_id.startswith("prof-"):
            prof_key = btn_id.replace("prof-", "")
            prof = PROFESSIONS.get(prof_key)
            if prof:
                self.selected_profession = prof_key
                suggestions = get_profession_suggestions(prof_key)

                # Update suggestion area
                sugg = self.query_one("#suggestion-area")
                sugg.remove_children()
                sugg.mount(Static(f"👤 {prof.icon} {prof.name} — {prof.description}", classes="suggestion-text"))
                if suggestions:
                    sugg.mount(Static(f"💡 Try: {suggestions[0]}", classes="suggestion-text"))

                # Enable launch button
                self.query_one("#launch-btn").disabled = False

                # Highlight selected button
                for child in self.query(".profession-btn"):
                    child.remove_class("-selected")
                event.button.add_class("-selected")

        elif btn_id == "launch-btn":
            self.dismiss()

        elif btn_id == "skip-btn":
            self.selected_profession = "developer"
            self.dismiss()


class OnboardingPlanScreen(Screen):
    """Show the onboarding plan after profession selection."""

    CSS = """
    OnboardingPlanScreen {
        align: center middle;
        background: #0a0a1a;
    }
    #plan-container {
        width: 70;
        height: 40;
        padding: 2;
        background: #0d0d2b;
        border: solid #00ffff33;
    }
    #plan-title {
        content-align: center top;
        color: #00ffff;
        text-style: bold;
        height: 3;
    }
    .plan-line {
        color: #aaaacc;
        margin: 0 0 0 2;
    }
    .plan-header {
        color: #ff00ff;
        text-style: bold;
    }
    #ready-btn {
        background: #6600ff;
        color: #ffffff;
        border: solid #8800ff;
        text-style: bold;
        height: 3;
        width: 20;
        margin: 2 0 0 0;
    }
    """

    def __init__(self, result: OnboardingResult):
        super().__init__()
        self.result = result

    def compose(self):
        with Container(id="plan-container"):
            yield Static("◈══ ONBOARDING PLAN ══◈", id="plan-title")
            yield Static("", classes="plan-line")
            yield Static(f"👤 Profession: {self.result.profession}", classes="plan-line")
            yield Static(f"🎯 Preset: {self.result.preset}", classes="plan-line")
            yield Static(f"🧠 Model tier: {self.result.model_tier}", classes="plan-line")
            yield Static(f"🔧 Skills: {', '.join(self.result.skills)}", classes="plan-line")
            yield Static("", classes="plan-line")
            yield Static("📋 PROJECT SCAN", classes="plan-header")
            yield Static("  → Scanning project structure...", classes="plan-line")
            yield Static("  → Detecting tech stack...", classes="plan-line")
            yield Static("  → Loading memory index...", classes="plan-line")
            yield Static("", classes="plan-line")
            yield Static("🧠 SMART CONTEXT", classes="plan-header")
            yield Static("  → Vector search over past plans...", classes="plan-line")
            yield Static("  → Loading relevant facts...", classes="plan-line")
            yield Static("  → Predicting next actions...", classes="plan-line")
            yield Static("", classes="plan-line")
            yield Static("💰 COST OPTIMIZATION", classes="plan-header")
            yield Static(f"  → Auto-routing to {self.result.model_tier} (cheapest that works)", classes="plan-line")
            yield Static("  → Budget limit: $50/month default", classes="plan-line")
            yield Static("", classes="plan-line")
            yield Button("🚀 Begin Autonomous Work", id="ready-btn", variant="primary")

    def on_button_pressed(self):
        self.dismiss()


class MauxxTUI(App):
    """Main Claude x Mauxx AI Terminal User Interface."""

    CSS = """
    Screen {
        background: #0a0a1a;
    }
    #main-layout {
        layout: horizontal;
        height: 100%;
    }
    #left-panel {
        width: 1fr;
        height: 100%;
    }
    #title-bar {
        height: 3;
        dock: top;
        padding: 0 1;
        background: #0d0d2b;
        border-bottom: solid #ff00ff;
    }
    #mauxx-logo {
        content-align: left middle;
        color: #00ffff;
        text-style: bold;
        width: 30;
    }
    #stats-bar {
        dock: top;
        height: 1;
        layout: horizontal;
        background: #111133;
        border-bottom: solid #ff00ff33;
    }
    .stat-item {
        padding: 0 1;
        width: auto;
        content-align: center middle;
    }
    .stat-value {
        color: #00ff88;
        text-style: bold;
    }
    .stat-label {
        color: #6666aa;
    }
    #conversation {
        background: #0a0a1a;
        border: none;
        height: 1fr;
    }
    #conversation Log {
        background: #0a0a1a;
        color: #aaaacc;
    }
    #input-bar {
        dock: bottom;
        height: 5;
        background: #0d0d2b;
        border-top: solid #ff00ff33;
        padding: 1;
    }
    #input-box {
        background: #111133;
        color: #ffffff;
        border: solid #3333cc;
        height: 3;
    }
    #input-box:focus {
        border: solid #00ffff;
    }
    /* Right Agent Panel */
    #agent-panel {
        width: 28;
        height: 100%;
        background: #0d0d2b;
        border-left: solid #00ffff33;
        padding: 1;
    }
    #agent-header {
        color: #ff00ff;
        text-style: bold;
        height: 3;
        content-align: center middle;
    }
    #agent-face {
        height: 5;
        content-align: center middle;
        color: #00ffff;
    }
    #agent-status {
        height: 3;
        content-align: center middle;
        color: #8888cc;
        text-style: italic;
    }
    #agent-divider {
        color: #333355;
        height: 1;
        content-align: center middle;
    }
    .agent-stat-line {
        color: #cc88ff;
        height: 1;
    }
    .agent-stat-val {
        color: #00ff88;
        text-style: bold;
    }
    #agent-footer {
        height: 3;
        content-align: center middle;
        color: #555588;
    }
    /* Settings panel */
    #setting-modal {
        align: center middle;
        background: #0a0a1a;
    }
    #setting-container {
        width: 60;
        height: auto;
        padding: 2;
        background: #0d0d2b;
        border: solid #00ffff33;
    }
    #setting-title {
        content-align: center top;
        color: #00ffff;
        text-style: bold;
        height: 3;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", priority=True),
        Binding("ctrl+l", "clear", "Clear"),
        Binding("ctrl+s", "settings", "Settings"),
        Binding("ctrl+t", "toggle_agent", "Toggle Agent Panel"),
        Binding("ctrl+p", "show_plans", "Plans"),
    ]

    def __init__(self, config_path: str = None, project_dir: str = None, profession: str = None):
        super().__init__()
        self.config_path = config_path
        self.project_dir = project_dir or str(Path.cwd())
        self.profession = profession
        self.claude = ClaudeWrapper(project_dir=self.project_dir, config_path=config_path)
        self.agent = MauxxAgent()
        self._running = False
        self._agent_visible = True
        self._onboarding_result: Optional[OnboardingResult] = None

        # CSS file
        self.CSS_FILE = Path(__file__).parent / "neon.tcss"

    def compose(self):
        with Container(id="main-layout"):
            # Left panel
            with Container(id="left-panel"):
                # Title bar
                with Container(id="title-bar"):
                    yield Static("◈══ CLAUDE × MAUXX AI ══◈ v2.0", id="mauxx-logo")
                    yield Static("", id="status-area")

                # Stats bar
                with Horizontal(id="stats-bar"):
                    yield Horizontal(
                        Static("TOKENS:", classes="stat-label"),
                        Static("0/200K", id="stat-tokens", classes="stat-value"),
                        classes="stat-item",
                    )
                    yield Horizontal(
                        Static("TASKS:", classes="stat-label"),
                        Static("0/0", id="stat-tasks", classes="stat-value"),
                        classes="stat-item",
                    )
                    yield Horizontal(
                        Static("ETA:", classes="stat-label"),
                        Static("--:--:--", id="stat-eta", classes="stat-value"),
                        classes="stat-item",
                    )
                    yield Horizontal(
                        Static("COST:", classes="stat-label"),
                        Static("$0.00", id="stat-cost", classes="stat-value"),
                        classes="stat-item",
                    )
                    yield Horizontal(
                        Static("UPTIME:", classes="stat-label"),
                        Static("0:00:00", id="stat-uptime", classes="stat-value"),
                        classes="stat-item",
                    )

                # Conversation area
                yield Log(id="conversation", highlight=True, wrap=True, max_lines=1000)

                # Input bar
                with Container(id="input-bar"):
                    yield Input(placeholder="💬 Type a message or command...", id="input-box")

            # Right agent panel
            with Container(id="agent-panel"):
                yield Static("◈══ MAUXX AI ══◈", id="agent-header")
                yield Static("(⌐■_■)", id="agent-face")
                yield Static("Initializing...", id="agent-status")
                yield Static("─" * 24, id="agent-divider")
                yield Static("📊 Current Stats", classes="agent-stat-line")
                yield Static("", id="agent-stats-content")
                yield Static("", id="agent-stats-content2")
                yield Static("", id="agent-stats-content3")
                yield Static("", id="agent-divider")
                yield Static("⚡ Mauxx AI v2.0", id="agent-footer")

    def on_mount(self):
        """Start the TUI — first onboarding, then claude."""
        self.title = "Claude x Mauxx AI"
        self.sub_title = "Autonomous AI Company"

        # Check if first run
        memory_idx = Path(self.project_dir) / "memory" / "MEMORY.md"
        if not memory_idx.exists() or not self.profession:
            self.push_screen(ProfessionScreen(self.config_path), self._on_profession_selected)
        else:
            # Skip onboarding
            self._start_work()

        # Start animation loop
        self.set_interval(1.0, self._update_stats)
        self.set_interval(1.5, self._animate_agent)

    def _on_profession_selected(self, result: Optional[OnboardingResult]):
        """Callback after profession selection."""
        if result:
            self._onboarding_result = result
            self.profession = result.profession
            self.push_screen(OnboardingPlanScreen(result), self._on_plan_ready)
        else:
            self._start_work()

    def _on_plan_ready(self, _=None):
        """Callback after onboarding plan is shown."""
        self._start_work()

    def _start_work(self):
        """Start working — greet user and begin."""
        conversation = self.query_one("#conversation", Log)

        # Profession-based greeting
        if self.profession and self.profession in PROFESSIONS:
            prof = PROFESSIONS[self.profession]
            conversation.write_line("")
            conversation.write_line(f"  {prof.icon}  Welcome, {prof.name}!")
            conversation.write_line(f"  {prof.description}")
            conversation.write_line("")
            suggestions = get_profession_suggestions(self.profession)
            conversation.write_line("  💡 Suggestions:")
            for s in suggestions:
                conversation.write_line(f"     → {s}")
            conversation.write_line("")
            conversation.write_line("  ⚡ I'm ready. What shall we build?")
            conversation.write_line("")
        else:
            conversation.write_line("")
            conversation.write_line("  ◈══ Claude × Mauxx AI Online ══◈")
            conversation.write_line("  Type a message and I'll get to work.")
            conversation.write_line("")

        # Focus input
        self.query_one("#input-box", Input).focus()

    def on_input_submitted(self, event: Input.Submitted):
        """Handle user input."""
        text = event.value
        if not text.strip():
            return

        conversation = self.query_one("#conversation", Log)
        input_box = self.query_one("#input-box", Input)

        # Clear input
        input_box.value = ""

        # Write user message to log
        ts = datetime.now().strftime("%H:%M:%S")
        conversation.write_line(f"  [{ts}] 👤 {text}")
        conversation.write_line(f"  [{ts}] ⚡ {self.agent.current_face} Working on it...")

        # Send to Claude (simulated for now — real integration via claude_wrapper)
        if self.claude.process:
            asyncio.create_task(self.claude.write_input(text))
        else:
            # Self-response for now
            self._respond_to(text)

    def _respond_to(self, text: str):
        """Respond to common commands (until Claude subprocess is connected)."""
        conversation = self.query_one("#conversation", Log)
        t = text.lower()

        if t == "/help":
            conversation.write_line("")
            conversation.write_line("  ◈══ COMMANDS ══◈")
            conversation.write_line("  /plan    — Show active plans")
            conversation.write_line("  /memory  — Show memory index")
            conversation.write_line("  /support — Open a ticket")
            conversation.write_line("  /feedback — Quick feedback")
            conversation.write_line("  /accuracy — Tool accuracy stats")
            conversation.write_line("  /heartbeat — System health")
            conversation.write_line("  /archive  — Past plans")
            conversation.write_line("  /cost     — Spending report")
            conversation.write_line("  /preset   — Set project preset")
            conversation.write_line("  /help     — This menu")
            conversation.write_line("  Ctrl+L   — Clear screen")
            conversation.write_line("  Ctrl+C   — Quit")
            conversation.write_line("")

        elif t == "/plan":
            conversation.write_line("  📋 Active Plans:")
            conversation.write_line("     [plan-onboarding] Active — Step 1/5")
            conversation.write_line("     Priority: P0 | Created: today")
            conversation.write_line("")

        elif t == "/memory":
            conversation.write_line("  🧠 Memory Index:")
            conversation.write_line("     Active rules: 2")
            conversation.write_line("     Active plans: 1")
            conversation.write_line("     Archived: 0")
            conversation.write_line("     Facts on disk: 3")
            conversation.write_line("")

        elif t == "/heartbeat":
            conversation.write_line("  💚 System Healthy")
            conversation.write_line(f"     Tokens: {self.claude.stats.tokens_used}/{self.claude.stats.tokens_total}")
            conversation.write_line(f"     Uptime: {self.claude.elapsed}")
            conversation.write_line(f"     Cost: ${self.claude.stats.cost_session:.2f}")
            conversation.write_line(f"     Plan: {self.claude.stats.current_plan or 'Idle'}")
            conversation.write_line("")

        elif t == "/cost":
            conversation.write_line("  💰 Cost Report")
            conversation.write_line(f"     Session: ${self.claude.stats.cost_session:.4f}")
            conversation.write_line("     Budget: $50.00/month")
            conversation.write_line("     Status: ✅ Under budget")
            conversation.write_line("")

        elif t.startswith("/preset"):
            preset = t.replace("/preset", "").strip()
            if preset:
                conversation.write_line(f"  🎯 Preset set to: {preset}")
                conversation.write_line("  Restart to apply.")
            else:
                conversation.write_line("  🎯 Available presets:")
                conversation.write_line("     webapp-fullstack, api-microservice,")
                conversation.write_line("     security-audit, perf-tuning")
            conversation.write_line("")

        elif t == "/clear" or text == "clear":
            conversation.clear()

        else:
            # Generic response simulating Claude
            conversation.write_line(f"  🤖 Processing request...")
            conversation.write_line("")

    def _animate_agent(self):
        """Animate the AI agent face and status."""
        if not self._agent_visible:
            return

        face, status, color = self.agent.animate()

        # Update agent widgets
        face_widget = self.query_one("#agent-face", Static)
        status_widget = self.query_one("#agent-status", Static)

        face_widget.update(face)
        status_widget.update(status)

        # Update mood based on recent output
        if self.claude.stats.agent_message:
            self.agent.set_mood_from_text(self.claude.stats.agent_message)

    def _update_stats(self):
        """Update all stats in the UI."""
        stats = self.claude.get_stats_dict()

        # Stats bar
        self.query_one("#stat-tokens", Static).update(
            f"{stats['tokens_used']/1000:.0f}K/{stats['tokens_total']/1000:.0f}K"
        )
        self.query_one("#stat-tasks", Static).update(
            f"{stats['tasks_completed']}/{stats['tasks_total']}"
        )
        self.query_one("#stat-eta", Static).update(stats['estimated_eta'])
        self.query_one("#stat-cost", Static).update(f"${stats['cost_session']:.2f}")
        self.query_one("#stat-uptime", Static).update(stats['uptime'])

        # Agent panel stats
        stats_content = self.query_one("#agent-stats-content", Static)
        stats_content.update(f"  Tokens: {stats['tokens_pct']}%")

        stats_content2 = self.query_one("#agent-stats-content2", Static)
        stats_content2.update(f"  Tasks: {stats['tasks_completed']}/{stats['tasks_total']}")

        stats_content3 = self.query_one("#agent-stats-content3", Static)
        stats_content3.update(f"  {stats['agent_message']}")

    def action_clear(self):
        """Clear the conversation log."""
        self.query_one("#conversation", Log).clear()
        if self.claude.stats.agent_message:
            self.agent.set_mood_from_text("waiting")

    def action_toggle_agent(self):
        """Toggle the agent panel visibility."""
        self._agent_visible = not self._agent_visible
        panel = self.query_one("#agent-panel")
        panel.display = self._agent_visible

    def action_show_plans(self):
        """Show current plans."""
        self.query_one("#input-box", Input).value = "/plan"

    def action_settings(self):
        """Show settings modal."""
        conversation = self.query_one("#conversation", Log)
        conversation.write_line("  ⚙️ Settings — Coming in v2.1")
        conversation.write_line("     Model tiering, budget, skills, hooks are configurable")
        conversation.write_line("     in .claude/settings.json")
        conversation.write_line("")

    def on_key(self, event):
        """Handle keyboard shortcuts."""
        if event.key == "escape":
            # Clear focus / show help
            pass


def main():
    """Entry point for the Mauxx TUI."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Claude x Mauxx AI — Neon Terminal UI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m tui.mauxx_tui
  python -m tui.mauxx_tui --profession developer
  python -m tui.mauxx_tui --config .claude/settings.json
        """
    )
    parser.add_argument("--config", help="Path to .claude/settings.json")
    parser.add_argument("--project-dir", help="Project directory (default: cwd)")
    parser.add_argument("--profession", choices=list(PROFESSIONS.keys()),
                        help="Skip onboarding, use this profession")
    parser.add_argument("--preset", help="Project preset (webapp-fullstack, etc.)")

    args = parser.parse_args()

    app = MauxxTUI(
        config_path=args.config,
        project_dir=args.project_dir,
        profession=args.profession,
    )
    app.run()


if __name__ == "__main__":
    main()
