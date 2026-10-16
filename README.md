# Claude Code Action Demo

Playground repo for testing [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) PR reviews.

## Workflows

- `.github/workflows/claude-code-review.yml`: automatic review on every PR (opened / synchronize / ready_for_review / reopened).
- `.github/workflows/claude.yml`: interactive. Mention `@claude` in a PR/issue comment, review comment, or issue.

Both authenticate with the `CLAUDE_CODE_OAUTH_TOKEN` repository secret.

## Project

A tiny Python "shop" package used as review fodder.

```sh
python -m pytest
```
