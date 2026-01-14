# Claude Toolkit

A comprehensive collection of skills, commands, and documentation for Claude Code.

**Repository:** `ThepExcel/claude-toolkit`
**Marketplace name:** `claude-toolkit`
**Author:** [ThepExcel](https://www.thepexcel.com)

---

## Quick Install

```bash
/plugin marketplace add ThepExcel/claude-toolkit
/plugin install research-skills@claude-toolkit
```

---

## For AI Agents: Claude Code Complete Reference

This section is designed for AI agents (Claude, GPT, etc.) to understand Claude Code's architecture and use it effectively.

### Table of Contents

1. [Configuration Scope System](#1-configuration-scope-system)
2. [CLAUDE.md System](#2-claudemd-system)
3. [Memory System](#3-memory-system)
4. [Skills vs Slash Commands](#4-skills-vs-slash-commands)
5. [Creating Skills](#5-creating-skills)
6. [Creating Slash Commands](#6-creating-slash-commands)
7. [MCP (Model Context Protocol)](#7-mcp-model-context-protocol)
8. [Hooks System](#8-hooks-system)
9. [Plugin Marketplace](#9-plugin-marketplace)
10. [File Organization Best Practices](#10-file-organization-best-practices)

---

### 1. Configuration Scope System

Claude Code uses a hierarchical configuration system with three scopes:

| Scope | Location | Applies To | Version Control |
|-------|----------|------------|-----------------|
| **User** | `~/.claude/` | All projects globally | No (personal) |
| **Project** | `.claude/` in repo root | Current project only | Yes (shared) |
| **Local** | `.claude.local/` or `settings.local.json` | Current project, personal | No (gitignored) |

#### Precedence Order (highest to lowest)
1. Local settings override project settings
2. Project settings override user settings
3. User settings are the default

#### Key Files by Scope

```
~/.claude/                          # USER SCOPE
├── settings.json                   # User preferences, permissions
├── CLAUDE.md                       # Global instructions for all projects
├── skills/                         # User-installed skills
├── commands/                       # User slash commands
└── agents/                         # User subagents

.claude/                            # PROJECT SCOPE (version controlled)
├── settings.json                   # Project settings
├── CLAUDE.md                       # Project-specific instructions
├── skills/                         # Project skills
├── commands/                       # Project slash commands
├── agents/                         # Project subagents
└── hooks.json                      # Automation hooks

.claude/settings.local.json         # LOCAL SCOPE (gitignored)
# Personal overrides for this project
```

#### settings.json Structure

```json
{
  "permissions": {
    "allow": ["Bash(git:*)", "Read", "Write"],
    "deny": ["Bash(rm -rf:*)"],
    "defaultMode": "default"
  },
  "enabledPlugins": {
    "plugin-name@marketplace": true
  },
  "model": "claude-sonnet-4",
  "contextWindow": 200000
}
```

---

### 2. CLAUDE.md System

CLAUDE.md files provide persistent instructions that Claude reads automatically at the start of every conversation.

#### File Locations (all are read, in order)

| Location | Purpose | When Read |
|----------|---------|-----------|
| `~/.claude/CLAUDE.md` | Global instructions | Always |
| `./CLAUDE.md` | Project root instructions | When in project |
| `./subdirectory/CLAUDE.md` | Directory-specific | When working in that directory |

#### Best Practices for CLAUDE.md

1. **Keep it concise** - ~150-200 instructions max for reliable following
2. **Use structured format** - Headers, tables, code blocks
3. **Include three elements:**
   - **WHAT**: Project structure, tech stack, file locations
   - **WHY**: Purpose, goals, context
   - **HOW**: Commands to run, coding conventions, verification steps

#### CLAUDE.md Template

```markdown
# Project Name

## Context
Brief description of what this project does.

## Tech Stack
- Language: TypeScript
- Framework: Next.js
- Database: PostgreSQL

## Project Structure
\`\`\`
src/
├── components/    # React components
├── pages/         # Next.js pages
└── lib/           # Utility functions
\`\`\`

## Commands
- `npm run dev` - Start development server
- `npm test` - Run tests
- `npm run build` - Build for production

## Coding Conventions
- Use TypeScript strict mode
- Prefer functional components
- Write tests for new features

## Important Files
- `src/lib/api.ts` - API client
- `src/config.ts` - Configuration
```

---

### 3. Memory System

Claude Code can persist context across conversations using a memory file.

#### memory.md Pattern

Create `memory.md` in project root:

```markdown
# Project Memory

## User Preferences
- Prefers concise responses
- Uses VS Code as editor
- Timezone: UTC+7

## Project Decisions
- Chose PostgreSQL over MongoDB for relational queries
- Using Tailwind CSS for styling

## Lessons Learned
- Always run `npm install` after pulling
- Tests require DATABASE_URL env variable

## Recurring Patterns
- Deploy workflow: test → build → deploy
- PR review requires 2 approvals
```

#### When to Update Memory
- After learning user preferences
- After making architectural decisions
- After encountering and solving problems
- After discovering project-specific gotchas

---

### 4. Skills vs Slash Commands

| Aspect | Skills | Slash Commands |
|--------|--------|----------------|
| **Invocation** | Claude decides automatically | User types `/command` |
| **Trigger** | Description matching in context | Explicit user request |
| **Location** | `skills/name/SKILL.md` | `commands/name.md` |
| **Complexity** | Can include scripts, references | Single markdown file |
| **Use case** | Complex, context-dependent tasks | Quick, repeatable actions |

#### When to Use Skills
- Task requires Claude to decide when to apply it
- Complex workflow with multiple steps
- Needs supporting files (scripts, references)
- Should be available across platforms (Claude.ai, API)

#### When to Use Slash Commands
- User explicitly triggers the action
- Quick, simple task
- Terminal-style command experience
- One-file simplicity

---

### 5. Creating Skills

#### Skill Directory Structure

```
skills/
└── my-skill/
    ├── SKILL.md              # Required: main instructions
    ├── SOURCES.md            # Recommended: attribution
    ├── scripts/              # Optional: executable code
    │   └── helper.py
    ├── references/           # Optional: supporting docs
    │   ├── guide.md
    │   └── examples.md
    └── assets/               # Optional: templates, images
        └── template.txt
```

#### SKILL.md Format

```markdown
---
name: skill-name
description: Describe when Claude should use this skill. Be specific about triggers like "when user asks to create X" or "when analyzing Y".
version: 1.0.0
---

# Skill Name

## When to Use
- User asks to "create something"
- User needs help with "specific task"
- Context involves "certain keywords"

## Instructions

Step-by-step instructions for Claude to follow.

### Step 1: Understand the Request
Gather necessary information...

### Step 2: Execute the Task
Perform the main action...

### Step 3: Verify Results
Confirm the output is correct...

## Examples

### Example 1: Basic Usage
User: "Help me with X"
Action: Do Y, then Z

### Example 2: Advanced Usage
User: "Complex request about X"
Action: First A, then B, finally C

## Guidelines
- Always verify before executing
- Ask for clarification if ambiguous
- Follow project conventions
```

#### SKILL.md Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase, hyphens, max 64 chars |
| `description` | Yes | Trigger description, max 1024 chars |
| `version` | No | Semantic version (e.g., "1.0.0") |
| `allowed-tools` | No | Restrict which tools skill can use |

---

### 6. Creating Slash Commands

#### Command File Location

```
.claude/commands/my-command.md      # Project scope
~/.claude/commands/my-command.md    # User scope
```

#### Command File Format

```markdown
---
description: Brief description shown in /help
argument-hint: <required-arg> [optional-arg]
allowed-tools: Bash, Read, Write
---

## Context

Current information Claude should know:
- Git status: !`git status --short`
- Current branch: !`git branch --show-current`

## Your Task

Based on the context above, perform these steps:

1. First step
2. Second step
3. Final step

Do not do anything else.
```

#### Dynamic Context with !`command`

Use `!`backticks`` to inject command output:

```markdown
## Context
- Current directory: !`pwd`
- Files changed: !`git diff --name-only`
- Package version: !`node -p "require('./package.json').version"`
```

#### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | Shown in command help |
| `argument-hint` | No | Usage hint: `<required> [optional]` |
| `allowed-tools` | No | Restrict tools: `Bash(git:*), Read` |

---

### 7. MCP (Model Context Protocol)

MCP allows Claude Code to connect to external tools and services.

#### Configuration File Locations

| File | Scope | Purpose |
|------|-------|---------|
| `~/.claude/.mcp.json` | User | Personal MCP servers |
| `.mcp.json` | Project | Shared MCP servers |
| `.claude/settings.local.json` | Local | Personal project overrides |

#### .mcp.json Format

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_KEY": "${API_KEY}",
        "HOST": "${HOST:-localhost}"
      }
    },
    "http-server": {
      "type": "http",
      "url": "https://api.example.com/mcp"
    }
  }
}
```

#### MCP Server Types

| Type | Use Case | Configuration |
|------|----------|---------------|
| `stdio` | Local process | `command`, `args`, `env` |
| `http` | Remote API | `url` |

#### Environment Variable Expansion
- `${VAR}` - Use environment variable
- `${VAR:-default}` - Use default if not set

#### Adding MCP Servers via CLI

```bash
# Add stdio server
claude mcp add github --command "npx" --args "-y @anthropic/mcp-github"

# Add with environment
claude mcp add-json db '{"command":"npx","args":["-y","@anthropic/mcp-postgres"],"env":{"DATABASE_URL":"${DATABASE_URL}"}}'

# List servers
claude mcp list

# Remove server
claude mcp remove github
```

---

### 8. Hooks System

Hooks execute code in response to Claude Code events.

#### Hook Configuration

`.claude/hooks.json`:

```json
{
  "hooks": {
    "sessionStart": {
      "command": "echo 'Session started at $(date)' >> ~/.claude/session.log"
    },
    "preToolUse": {
      "command": "python3 .claude/hooks/validate.py",
      "timeout": 5000
    },
    "postToolUse": {
      "command": ".claude/hooks/log-tool.sh"
    },
    "userPromptSubmit": {
      "command": "python3 .claude/hooks/preprocess.py"
    },
    "stop": {
      "command": "echo 'Session ended' >> ~/.claude/session.log"
    }
  }
}
```

#### Hook Types

| Hook | Trigger | Use Case |
|------|---------|----------|
| `sessionStart` | Session begins | Setup, logging |
| `preToolUse` | Before tool execution | Validation, blocking |
| `postToolUse` | After tool execution | Logging, cleanup |
| `userPromptSubmit` | User sends message | Preprocessing |
| `stop` | Session ends | Cleanup, summary |

#### Hook Response (for preToolUse)

Hook script can output JSON to control behavior:

```json
{"allowed": false, "reason": "Operation blocked by policy"}
```

---

### 9. Plugin Marketplace

#### Installing from Marketplace

```bash
# Add marketplace
/plugin marketplace add owner/repo-name

# List available plugins
/plugin list marketplace-name

# Install plugin
/plugin install plugin-name@marketplace-name

# Install with scope
/plugin install plugin-name@marketplace-name -s project
/plugin install plugin-name@marketplace-name -s user

# Update marketplace
/plugin marketplace update marketplace-name

# Remove plugin
/plugin uninstall plugin-name@marketplace-name
```

#### Creating a Marketplace

Repository structure:

```
my-marketplace/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── skill-one/
│   │   └── SKILL.md
│   └── skill-two/
│       └── SKILL.md
├── plugins/                    # Mixed-component plugins
│   └── my-plugin/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/
│       ├── skills/
│       └── hooks/
└── README.md
```

#### marketplace.json Format

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "marketplace-name",
  "version": "1.0.0",
  "description": "Description of this marketplace",
  "owner": {
    "name": "Owner Name",
    "email": "email@example.com"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "description": "What this plugin does",
      "source": "./plugins/plugin-name",
      "category": "productivity",
      "tags": ["tag1", "tag2"],
      "skills": [
        "./skills/skill-one",
        "./skills/skill-two"
      ]
    }
  ]
}
```

#### plugin.json Format (for individual plugins)

```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Author Name"
  }
}
```

---

### 10. File Organization Best Practices

#### Recommended Project Structure

```
project/
├── .claude/                    # Claude Code config (version controlled)
│   ├── settings.json
│   ├── commands/
│   │   └── deploy.md
│   ├── skills/
│   │   └── project-skill/
│   │       └── SKILL.md
│   ├── agents/
│   │   └── reviewer.md
│   └── hooks.json
├── .claude/settings.local.json # Personal settings (gitignored)
├── .mcp.json                   # MCP servers (version controlled)
├── CLAUDE.md                   # Project instructions
├── memory.md                   # Persistent context
└── src/                        # Project source code
```

#### .gitignore Recommendations

```gitignore
# Claude Code local settings
.claude/settings.local.json
.claude.local/

# Personal skills (if using symlinks)
.claude/skills/*
!.claude/skills/project-specific/
```

#### Naming Conventions

| Component | Convention | Example |
|-----------|------------|---------|
| Skills | lowercase-with-hyphens | `deep-research` |
| Commands | lowercase-with-hyphens | `deploy-prod` |
| Agents | lowercase-with-hyphens | `code-reviewer` |
| Config files | lowercase.json | `settings.json` |

---

## Available Skills in This Repository

| Skill | Description |
|-------|-------------|
| `deep-research` | 8-phase research with citations and source verification |
| `explain-concepts` | Educational explanations with examples |
| `problem-solving` | Systematic problem analysis with Polya method |
| `triz` | TRIZ innovation methodology |
| `generate-creative-ideas` | Creative ideation with SCAMPER and more |
| `design-business-model` | Business Model Canvas and Lean Canvas |
| `manage-business-strategy` | Strategic analysis frameworks |
| `xlsx` | Excel spreadsheet creation |
| `docx` | Word document creation |
| `pptx` | PowerPoint presentation creation |
| `pdf` | PDF document handling |
| `power-query-coaching` | Power Query M code coaching |
| `optimize-prompt` | AI prompt optimization |
| `prompt-ai-image-video` | Image/video generation prompts |
| `skill-creator` | Create new Claude skills |
| `extract-expertise` | Extract domain knowledge from experts |
| `create-visualization` | Diagrams and Manim animations |

---

## Installation

### Claude Code (Recommended)

```bash
# Add marketplace
/plugin marketplace add ThepExcel/claude-toolkit

# Install skill bundles
/plugin install research-skills@claude-toolkit
/plugin install innovation-skills@claude-toolkit
/plugin install document-skills@claude-toolkit
```

### Manual Installation

```bash
git clone https://github.com/ThepExcel/claude-toolkit.git
cd claude-toolkit

# Symlink skills to user scope
mkdir -p ~/.claude/skills
for skill in skills/*/; do
    ln -sf "$(pwd)/$skill" ~/.claude/skills/$(basename "$skill")
done
```

### Claude.ai

1. Download skill folder from `skills/`
2. ZIP the folder
3. Settings > Capabilities > Skills > Upload

---

## License

- **ThepExcel skills:** MIT License
- **Document skills (docx, xlsx, pptx, pdf):** See LICENSE.txt in each folder ([Anthropic Official](https://github.com/anthropics/skills))

---

## Author

Created by [Sira Ekabut](https://www.thepexcel.com) (ThepExcel)

*Developed through human-AI collaboration using Claude Code.*
