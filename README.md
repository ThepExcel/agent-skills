# Claude Skills Collection

A collection of reusable skills for Claude Code and Claude.ai.

**Learn more:** [Claude Skills คืออะไร? วิธีสร้างและใช้งาน](https://www.thepexcel.com/claude-skills/)

---

## Installation

### For Claude Code (CLI)

```bash
# Clone this repo
git clone https://github.com/ThepExcel/claude-skills.git
cd claude-skills

# Create symlinks to make skills globally available
mkdir -p ~/.claude/skills
for skill in */; do
    [[ -d "$skill" && ! "$skill" == .* ]] && ln -s "$(pwd)/$skill" ~/.claude/skills/$(basename "$skill")
done
```

After installation, Claude Code will automatically use these skills when relevant.

### For Claude.ai (Web)

1. Download the skill folder you want (e.g., `deep-research/`)
2. **ZIP the entire folder** (not just the files inside!)
   ```bash
   # Correct way - ZIP the folder
   zip -r deep-research.zip deep-research/
   ```
3. Go to **Settings > Capabilities** in Claude.ai
4. Scroll down to **Skills** section and click **Upload skill**

> **Important:** ZIP must contain the folder structure. If you ZIP only the files, Claude won't find SKILL.md!
>
> **Requirements:** Pro, Max, Team, or Enterprise plan.

---

## Available Skills

### Original Skills (by ThepExcel + Claude)

Skills developed by [ThepExcel](https://www.thepexcel.com) in collaboration with Claude.

| Skill | Description |
|-------|-------------|
| [**create-visualization**](create-visualization/) | Data visualization, diagrams, and Manim animations |
| [**deep-research**](deep-research/) | Comprehensive 8-phase research with Graph-of-Thoughts, source triangulation, and claim verification |
| [**design-business-model**](design-business-model/) | Business Model Canvas, Lean Canvas, Value Proposition Canvas |
| [**explain-concepts**](explain-concepts/) | Master teaching methodology for explaining concepts with visualizations |
| [**extract-expertise**](extract-expertise/) | Extract domain expertise from experts and transform into Claude skills |
| [**generate-creative-ideas**](generate-creative-ideas/) | Creative thinking techniques and ideation frameworks |
| [**manage-business-strategy**](manage-business-strategy/) | Business management frameworks hub (SWOT, OKR, Porter's, BCG, etc.) |
| [**power-query-coaching**](power-query-coaching/) | Coach users to transform messy data using Power Query UI |
| [**problem-solving**](problem-solving/) | Structured problem-solving methodologies (5 Whys, Fishbone, Root Cause Analysis) |
| [**prompt-ai-image-video**](prompt-ai-image-video/) | Professional AI image/video prompt engineering with visual artist's eye |
| [**skill-creator**](skill-creator/) | Guide for creating new Claude Code skills |
| [**triz**](triz/) | TRIZ (Theory of Inventive Problem Solving) with 40 principles and contradiction matrix |

### Anthropic Official Skills (Pre-optimized)

Skills from Anthropic's official repository. These follow Anthropic's best practices and are already optimized for token efficiency.

| Skill | Description | Source |
|-------|-------------|--------|
| [**docx**](docx/) | Word document creation, editing, and analysis | [Anthropic Official](https://github.com/anthropics/skills) |
| [**pdf**](pdf/) | PDF text extraction and form filling | [Anthropic Official](https://github.com/anthropics/skills) |
| [**pptx**](pptx/) | PowerPoint presentation creation and editing | [Anthropic Official](https://github.com/anthropics/skills) |
| [**xlsx**](xlsx/) | Excel spreadsheet creation with formulas and formatting | [Anthropic Official](https://github.com/anthropics/skills) + ThepExcel |

> **Note:** xlsx enhanced by ThepExcel with Power Query routing to `/power-query-coaching`.

---

## Usage Examples

Once installed, invoke skills directly with `/skill-name` for guaranteed activation:

| Command | What It Does |
|---------|--------------|
| `/create-visualization` | Data visualization, diagrams, Manim animations |
| `/deep-research` | Comprehensive 8-phase research with source verification |
| `/design-business-model` | Business Model Canvas, Lean Canvas |
| `/docx` `/pdf` `/pptx` `/xlsx` | Office document operations |
| `/explain-concepts` | Master teaching methodology with visualizations |
| `/extract-expertise` | Transform domain expertise into Claude skills |
| `/generate-creative-ideas` | Creative thinking and ideation techniques |
| `/manage-business-strategy` | SWOT, OKR, Porter's Five Forces, BCG Matrix |
| `/power-query-coaching` | Step-by-step Power Query UI guidance |
| `/problem-solving` | 5 Whys, Fishbone, Root Cause Analysis |
| `/prompt-ai-image-video` | Professional AI image/video prompts |
| `/skill-creator` | Guide for creating new skills |
| `/triz` | 40 TRIZ principles and contradiction matrix |

---

## Skill Structure

Each skill is just a folder with at least one file: `SKILL.md`

```
my-skill/
├── SKILL.md          # Main file (required)
├── scripts/          # Executable code (optional)
├── references/       # Reference docs (optional)
└── assets/           # Templates, images (optional)
```

### 3-Level Progressive Loading

Skills use smart loading - Claude only loads what's needed:

| Level | When Loaded | Token Cost | Content |
|-------|-------------|------------|---------|
| **1. Metadata** | Session start | ~100 tokens | `name` + `description` from YAML |
| **2. Instructions** | Skill triggered | <5,000 tokens | SKILL.md body |
| **3. Resources** | When needed | Unlimited | Files in `references/`, `scripts/` |

This means you can have dozens of skills installed without performance impact!

---

## License

- **Original skills (ThepExcel):** MIT License - Feel free to use and modify.
- **Anthropic skills (docx, xlsx, pptx, pdf):** See LICENSE.txt in each skill folder.

---

## Author

Created by [Sira Ekabut](https://www.thepexcel.com) (ThepExcel)

*Skills marked as "ThepExcel + Claude" were developed through human-AI collaboration using Claude Code.*
