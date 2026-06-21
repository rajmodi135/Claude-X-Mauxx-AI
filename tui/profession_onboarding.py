"""
Claude x Mauxx AI — Profession Onboarding
First-run screen that asks the user's profession and configures the system accordingly.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Profession:
    name: str
    icon: str
    description: str
    presets: List[str]
    skills: List[str]
    model_tier: str
    color: str


# Profession profiles
PROFESSIONS = {
    "developer": Profession(
        name="Software Developer",
        icon="💻",
        description="Code, test, deploy — full software development lifecycle",
        presets=["webapp-fullstack", "api-microservice"],
        skills=["code-review", "verify", "run", "simplify", "deep-research"],
        model_tier="sonnet",
        color="cyan",
    ),
    "designer": Profession(
        name="Designer / UI-UX",
        icon="🎨",
        description="Design systems, UI components, prototypes, accessibility",
        presets=["webapp-fullstack"],
        skills=["frontend-design", "code-review", "verify", "deep-research"],
        model_tier="sonnet",
        color="magenta",
    ),
    "data-scientist": Profession(
        name="Data Scientist / ML Engineer",
        icon="📊",
        description="Data pipelines, ML models, notebooks, visualization",
        presets=["data-pipeline"],
        skills=["deep-research", "verify", "simplify"],
        model_tier="sonnet",
        color="green",
    ),
    "writer": Profession(
        name="Writer / Content Creator",
        icon="✍️",
        description="Documentation, blogs, copy, SEO-optimized content",
        presets=["docs-site"],
        skills=["deep-research", "frontend-design"],
        model_tier="haiku",
        color="yellow",
    ),
    "student": Profession(
        name="Student / Learner",
        icon="🎓",
        description="Learn new tech, build projects, get help with code",
        presets=["webapp-fullstack"],
        skills=["code-review", "deep-research", "simplify"],
        model_tier="haiku",
        color="blue",
    ),
    "devops": Profession(
        name="DevOps / SysAdmin",
        icon="⚙️",
        description="Infrastructure, CI/CD, Docker, K8s, monitoring",
        presets=["api-microservice"],
        skills=["code-review", "verify", "security-review", "deep-research"],
        model_tier="sonnet",
        color="red",
    ),
    "security": Profession(
        name="Security Engineer",
        icon="🔒",
        description="Penetration testing, compliance, vulnerability assessment",
        presets=["security-audit"],
        skills=["security-review", "code-review", "deep-research"],
        model_tier="opus",
        color="bright_red",
    ),
    "manager": Profession(
        name="Product Manager / Tech Lead",
        icon="📋",
        description="Project planning, code review, architecture decisions",
        presets=["webapp-fullstack", "api-microservice"],
        skills=["code-review", "deep-research", "simplify"],
        model_tier="sonnet",
        color="bright_cyan",
    ),
}


@dataclass
class OnboardingResult:
    profession: str
    preset: str
    model_tier: str
    skills: List[str]
    project_dir: str
    auto_mode: bool = True

    def to_dict(self) -> Dict:
        return {
            "profession": self.profession,
            "preset": self.preset,
            "model_tier": self.model_tier,
            "skills": self.skills,
            "project_dir": self.project_dir,
            "auto_mode": self.auto_mode,
        }


# Profession-based suggestions for first commands
SUGGESTIONS = {
    "developer": [
        "claude --config .claude/settings.json --preset webapp-fullstack",
        "Start a new React project",
        "Review my last commit",
        "Help me refactor this module",
    ],
    "designer": [
        "claude --config .claude/settings.json --preset frontend-design",
        "Build a landing page",
        "Design a design system",
        "Review my Figma exports",
    ],
    "data-scientist": [
        "claude --config .claude/settings.json --preset data-pipeline",
        "Analyze this dataset",
        "Build a ML pipeline",
        "Clean and visualize data",
    ],
    "writer": [
        "claude --config .claude/settings.json --preset docs-site",
        "Write technical documentation",
        "Create a blog post",
        "Review my article for clarity",
    ],
    "student": [
        "claude --config .claude/settings.json",
        "Learn Python basics",
        "Help me with this assignment",
        "Explain this concept",
    ],
    "devops": [
        "claude --config .claude/settings.json --preset api-microservice",
        "Set up CI/CD pipeline",
        "Dockerize this application",
        "Review my infrastructure",
    ],
    "security": [
        "claude --config .claude/settings.json --preset security-audit",
        "Audit this codebase",
        "Check for OWASP vulnerabilities",
        "Review my auth system",
    ],
    "manager": [
        "claude --config .claude/settings.json --preset webapp-fullstack",
        "Review project architecture",
        "Create a project roadmap",
        "Audit team productivity",
    ],
}


def get_profession_suggestions(profession: str) -> List[str]:
    """Get first-run suggestions based on profession."""
    return SUGGESTIONS.get(profession, SUGGESTIONS["developer"])


def get_profession(profession_name: str) -> Optional[Profession]:
    """Get profession details by name."""
    return PROFESSIONS.get(profession_name)


def get_default_preset_for_profession(profession_name: str) -> str:
    """Get the default preset for a profession."""
    prof = get_profession(profession_name)
    if prof and prof.presets:
        return prof.presets[0]
    return "webapp-fullstack"
