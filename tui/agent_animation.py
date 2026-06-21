"""
Mauxx AI Agent — Animated AI agent for the TUI.
Shows a small animated ASCII character with status messages.
"""

import random
from enum import Enum
from typing import Tuple


class AgentMood(Enum):
    NEUTRAL = "neutral"
    WORKING = "working"
    THINKING = "thinking"
    HAPPY = "happy"
    ERROR = "error"


class MauxxAgent:
    """
    Animated AI agent character.
    Renders as a small ASCII art face in the TUI.
    """

    # ASCII art frames for different moods
    FACES = {
        AgentMood.NEUTRAL: [
            "( •_•)",
            "( •_•)>⌐■-■",
            "(⌐■_■)",
        ],
        AgentMood.WORKING: [
            "(▀̿Ĺ̯▀̿ ̿)",
            "(≧∇≦)ﾉ",
            "(ノಠ益ಠ)ノ",
            "ᕦ(ò_óˇ)ᕤ",
        ],
        AgentMood.THINKING: [
            "(¬_¬)",
            "(¬‿¬)",
            "(⊙_◎)",
            "(◕‿◕✿)",
        ],
        AgentMood.HAPPY: [
            "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
            "ヽ(•‿•)ノ",
            "~(˘▾˘~)",
            "✧⁠◝⁠(⁠⁰⁠▿⁠⁰⁠)⁠◜⁠✧",
        ],
        AgentMood.ERROR: [
            "(╯°□°)╯︵ ┻━┻",
            "ಠ_ಠ",
            "(；一_一)",
        ],
    }

    # Status messages shown below the agent
    STATUS_MESSAGES = {
        "thinking": [
            "Analyzing your project...",
            "Connecting neural pathways...",
            "Loading context from memory...",
            "Processing request...",
            "Gathering intelligence...",
        ],
        "working": [
            "Writing code at light speed...",
            "Optimizing algorithms...",
            "Building the future...",
            "Crushing bugs...",
            "Making it elegant...",
        ],
        "waiting": [
            "Waiting for your command...",
            "Listening...",
            "Ready to assist...",
            "All systems nominal...",
            "Standing by...",
        ],
        "success": [
            "Mission accomplished!",
            "Another win for Mauxx AI!",
            "Flawless execution!",
            "Done and dusted!",
            "Your wish is my command!",
        ],
        "error": [
            "Encountered an issue...",
            "Let me fix that...",
            "Retrying with a different approach...",
            "Don't worry, I've got this...",
        ],
    }

    def __init__(self):
        self.mood = AgentMood.NEUTRAL
        self._frame = 0
        self._status = "waiting"
        self._msg_idx = 0

    @property
    def current_face(self) -> str:
        faces = self.FACES.get(self.mood, self.FACES[AgentMood.NEUTRAL])
        return faces[self._frame % len(faces)]

    @property
    def status_message(self) -> str:
        msgs = self.STATUS_MESSAGES.get(self._status, self.STATUS_MESSAGES["waiting"])
        return msgs[self._msg_idx % len(msgs)]

    def animate(self) -> Tuple[str, str, str]:
        """Advance animation by one frame. Returns (face, status, color_hint)."""
        self._frame += 1

        # Occasionally shuffle status message
        if self._frame % 10 == 0:
            self._msg_idx = random.randint(0, 4)

        face = self.current_face
        status = self.status_message

        # Color hints for the rendering
        color_map = {
            AgentMood.NEUTRAL: "cyan",
            AgentMood.WORKING: "bright_cyan",
            AgentMood.THINKING: "yellow",
            AgentMood.HAPPY: "green",
            AgentMood.ERROR: "red",
        }

        return face, status, color_map.get(self.mood, "cyan")

    def set_mood_from_text(self, text: str):
        """Auto-set mood based on Claude output text."""
        t = text.lower()
        if "error" in t or "fail" in t or "sorry" in t:
            self.mood = AgentMood.ERROR
            self._status = "error"
        elif "success" in t or "done" in t or "complete" in t:
            self.mood = AgentMood.HAPPY
            self._status = "success"
        elif "think" in t or "plan" in t or "analyz" in t:
            self.mood = AgentMood.THINKING
            self._status = "thinking"
        elif "write" in t or "edit" in t or "build" in t or "create" in t:
            self.mood = AgentMood.WORKING
            self._status = "working"
        else:
            self.mood = AgentMood.NEUTRAL
            self._status = "waiting"

    def random_face(self) -> str:
        """Get a random face from any mood."""
        all_faces = []
        for faces in self.FACES.values():
            all_faces.extend(faces)
        return random.choice(all_faces)

    # Glitch effect (for cyberpunk feel)
    def glitch(self) -> str:
        """Return a glitched face for occasional cyberpunk effect."""
        base = self.random_face()
        # Simple glitch: swap some characters
        glitched = list(base)
        for i in range(min(3, len(glitched))):
            idx = random.randint(0, len(glitched) - 1)
            glitched[idx] = random.choice(['▓', '▒', '░', '█', '▄', '▀'])
        return ''.join(glitched)
