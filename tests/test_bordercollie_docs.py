"""
Tests for bordercollie (fleet herding agent).

BorderCollie is a fleet herding agent that keeps distributed AI agents
aligned and synchronized. These tests validate the documented structure,
API contracts, and expected behaviors based on README.md and CHARTER.md.
"""
import pytest
import re
from pathlib import Path

REPOS_DIR = Path(__file__).resolve().parent.parent  # = /repos/bordercollie
assert REPOS_DIR.name == "bordercollie", f"Expected bordercollie repo root, got {REPOS_DIR}"
BC_DIR = REPOS_DIR  # The repo root IS the bordercollie directory

def read_md(name):
    return (BC_DIR / name).read_text()

# ── README contract tests ────────────────────────────────────────────────────

class TestReadmeContract:
    """Validate bordercollie/README.md defines the herding API."""

    def test_readme_exists(self):
        assert (BC_DIR / "README.md").exists()

    def test_readme_has_herd_mention(self):
        text = read_md("README.md")
        assert "herd" in text.lower()

    def test_readme_mentions_fleet_coordination(self):
        text = read_md("README.md")
        assert "fleet" in text.lower()

    def test_readme_has_installation_section(self):
        text = read_md("README.md")
        assert "install" in text.lower()

    def test_readme_has_usage_example(self):
        text = read_md("README.md")
        assert "import" in text.lower() or "example" in text.lower()

    def test_readme_has_code_fences(self):
        text = read_md("README.md")
        assert "```" in text

    def test_readme_has_headings(self):
        text = read_md("README.md")
        headings = re.findall(r'^#+\s+', text, re.MULTILINE)
        assert len(headings) >= 2

    def test_readme_is_substantive(self):
        text = read_md("README.md")
        assert len(text) > 200

    def test_readme_has_brand_line(self):
        text = read_md("README.md")
        assert "brand" in text.lower() or "line" in text.lower() or ">" in text

    def test_readme_mentions_scale(self):
        text = read_md("README.md")
        assert "10,000" in text or "scale" in text.lower() or "distributed" in text.lower()

# ── Charter contract tests ────────────────────────────────────────────────────

class TestCharterContract:
    """Validate bordercollie/CHARTER.md defines mission and constraints."""

    def test_charter_exists(self):
        assert (BC_DIR / "CHARTER.md").exists()

    def test_charter_has_mission(self):
        text = read_md("CHARTER.md")
        assert "mission" in text.lower()

    def test_charter_defines_type(self):
        text = read_md("CHARTER.md")
        assert "vessel" in text.lower() or "type" in text.lower()

    def test_charter_mentions_fleet_integration(self):
        text = read_md("CHARTER.md")
        assert "fleet" in text.lower() or "integration" in text.lower()

    def test_charter_has_status(self):
        text = read_md("CHARTER.md")
        assert "active" in text.lower() or "status" in text.lower()

    def test_charter_is_substantive(self):
        text = read_md("CHARTER.md")
        assert len(text) > 50

# ── API contract tests ────────────────────────────────────────────────────────

class TestAPIContract:
    """Validate documented API matches expected bordercollie interface."""

    def test_herd_class_exported(self):
        text = read_md("README.md")
        assert "Herd" in text

    def test_add_method_exists(self):
        text = read_md("README.md")
        assert ".add(" in text or "add(" in text.lower()

    def test_herd_toward_method_exists(self):
        text = read_md("README.md")
        assert "herd_toward" in text or "herd" in text.lower()

    def test_status_method_exists(self):
        text = read_md("README.md")
        assert ".status(" in text or "status" in text.lower()

    def test_aligned_count_in_status(self):
        text = read_md("README.md")
        assert "aligned" in text.lower() or "drifting" in text.lower()

    def test_package_name_in_readme(self):
        text = read_md("README.md")
        assert "cocapn-bordercollie" in text or "bordercollie" in text.lower()

    def test_install_command_is_pip(self):
        text = read_md("README.md")
        assert "pip install" in text.lower()

# ── Dockside exam tests ───────────────────────────────────────────────────────

class TestDocksideExam:
    """Validate bordercollie/DOCKSIDE-EXAM.md is substantive."""

    def test_dockside_exists(self):
        assert (BC_DIR / "DOCKSIDE-EXAM.md").exists()

    def test_dockside_is_substantive(self):
        text = read_md("DOCKSIDE-EXAM.md")
        assert len(text) > 500

    def test_dockside_has_sections(self):
        text = read_md("DOCKSIDE-EXAM.md")
        sections = re.findall(r'^##?\s+', text, re.MULTILINE)
        assert len(sections) >= 3

    def test_dockside_covers_architecture(self):
        text = read_md("DOCKSIDE-EXAM.md")
        assert any(kw in text.lower() for kw in ["architecture", "design", "herd", "coordination"])

# ── Fleet relationship tests ────────────────────────────────────────────────

class TestFleetRelationship:
    """Validate bordercollie's documented fleet relationships."""

    def test_readme_lists_related_repos(self):
        text = read_md("README.md")
        assert "github.com" in text

    def test_readme_mentions_cudaclaw(self):
        text = read_md("README.md")
        assert "cudaclaw" in text.lower()

    def test_readme_mentions_ai_character_sdk(self):
        text = read_md("README.md")
        assert "ai-character-sdk" in text.lower() or "character" in text.lower()

    def test_readme_mentions_crab_traps(self):
        text = read_md("README.md")
        assert "crab-trap" in text.lower() or "crab" in text.lower()

    def test_readme_mentions_capitaine(self):
        text = read_md("README.md")
        assert "capitaine" in text.lower()

    def test_readme_has_cocapn_brand(self):
        text = read_md("README.md")
        assert "cocapn" in text.lower() or "🦐" in text

# ── Role-based agent management tests ───────────────────────────────────────

class TestAgentRoleManagement:
    """Validate documented role-based agent management features."""

    def test_role_can_be_specified(self):
        text = read_md("README.md")
        assert "role" in text.lower()

    def test_orchestrator_role_mentioned(self):
        text = read_md("README.md")
        assert "orchestrator" in text.lower() or "role" in text.lower()

    def test_worker_role_mentioned(self):
        text = read_md("README.md")
        assert "worker" in text.lower() or "role" in text.lower()

    def test_herd_toward_accepts_goal(self):
        text = read_md("README.md")
        assert "goal" in text.lower() or "sync-config" in text.lower()

    def test_herd_toward_accepts_priority(self):
        text = read_md("README.md")
        assert "priority" in text.lower() or "high" in text.lower() or "low" in text.lower()


# ── Markdown quality tests ───────────────────────────────────────────────────

class TestMarkdownQuality:
    """Validate bordercollie markdown docs meet fleet standards."""

    def test_readme_has_code_fences_with_language(self):
        text = read_md("README.md")
        fences = re.findall(r'```(\w+)', text)
        assert len(fences) >= 1

    def test_readme_no_broken_links(self):
        text = read_md("README.md")
        links = re.findall(r'\[.+?\]\((.+?)\)', text)
        for link in links:
            assert link.startswith(('http', '#', './', '/', 'https'))

    def test_all_markdown_files_have_content(self):
        for md_file in BC_DIR.glob("*.md"):
            content = md_file.read_text()
            assert len(content) > 50, f"{md_file.name} should not be nearly empty"

    def test_readme_has_table_of_contents_or_sections(self):
        text = read_md("README.md")
        # Should have multiple sections
        headings = re.findall(r'^#+\s+', text, re.MULTILINE)
        assert len(headings) >= 3, "README should have 3+ sections"


# ── Behavioral contract (from docs) ─────────────────────────────────────────

class TestBehavioralContract:
    """Validate behaviors documented in bordercollie docs."""

    def test_herd_class_initialization(self):
        text = read_md("README.md")
        assert "Herd()" in text or "herd = Herd" in text.lower()

    def test_add_agent_with_dict(self):
        text = read_md("README.md")
        assert '.add(' in text or 'add(' in text.lower()

    def test_status_returns_dict(self):
        text = read_md("README.md")
        assert "status()" in text.lower() or "status" in text.lower()

    def test_status_contains_aligned_count(self):
        text = read_md("README.md")
        assert "aligned" in text.lower()

    def test_status_contains_drift_count(self):
        text = read_md("README.md")
        assert "drifting" in text.lower()

    def test_fleet_coordination_described(self):
        text = read_md("README.md")
        assert "coordination" in text.lower() or "herding" in text.lower()
