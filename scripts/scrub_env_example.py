from pathlib import Path

path = Path(".env.example")
if path.exists():
    path.write_text(
        """# ── Required ──────────────────────────────────────────────────
GROQ_API_KEY=YOUR_GROQ_API_KEY
GROQ_MODEL=llama-3.3-70b-versatile

# ── Optional: GitHub integration ──────────────────────────────
GITHUB_TOKEN=YOUR_GITHUB_TOKEN

# ── Optional: Slack integration ───────────────────────────────
SLACK_WEBHOOK=YOUR_SLACK_WEBHOOK
SLACK_CHANNEL=#standup
SLACK_USERNAME=git-standup-ai

# ── Optional: Tuning ──────────────────────────────────────────
GROQ_TEMPERATURE=0.3
GROQ_MAX_TOKENS=2048
MAX_AGENT_TURNS=12
REQUEST_TIMEOUT=20
CACHE_DIR=.gsa_cache
LOG_LEVEL=INFO

# ── Optional: Multi-repo ──────────────────────────────────────
# DEFAULT_REPOS=["../backend","../frontend","../infra"]
""",
        encoding="utf-8",
    )
else:
    raise FileNotFoundError('.env.example not found')
