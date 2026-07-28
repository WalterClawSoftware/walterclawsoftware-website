# Agent Operating Rules

- This is a public trust surface and a static Netlify deployment from the repository root.
- Keep claims honest and verifiable; do not invent testimonials, customer logos, usage counts, or proof.
- Preview and smoke-check customer-visible changes before production. Because the repository root is published, continuity documentation must remain safe for public exposure.
- Preserve the responsive-image invariant in `/site-quality.css`. Run
  `python3 scripts/check_site_geometry.py --self-test`, `--static`, and
  `--render` for every visual or deployment change.
- Intentional crops require `data-visual-crop="approved"`, a specific reason,
  and a matching reviewed `site-quality.json` entry.
- Keep Netlify production Git-only; never bypass the repository build gate with
  a direct production deploy.

## Cross-Agent Continuity

GitHub and named live production systems are the source of truth. This repository is shared by Codex and Hermes; neither agent should assume it has the other agent's conversation context.

Before editing:

1. Read `README.md`, this file, and `docs/PROJECT_STATUS.md`.
2. Inspect `git status` and preserve unrelated local work.
3. Fetch origin and review recent commits, open pull requests, relevant issues, and current CI when available.
4. Verify external store, deployment, signing, or release claims against the live system before treating them as current.

Before stopping after meaningful work:

1. Run the project-native tests, builds, and artifact checks required by the change.
2. Update `docs/PROJECT_STATUS.md` with current product state, completed work, verification actually performed, external systems changed, unresolved risks, and the next recommended action.
3. Commit and push completed verified work unless the active instruction explicitly says no commit, no push, draft only, or local only.
4. Verify the remote branch contains the commit before claiming success.
5. If blocked, preserve the work and report the exact branch, commit or dirty files, commands run, blocker, and next action.

Keep continuity files concise. Never include secrets, tokens, private keys, customer data, hidden prompts, or large transient logs. Live Git, GitHub, CI, builds, installed artifacts, stores, and deployments override stale handoff text.
