# cs-biotech-website

Website for the University of Toronto CS-Biotech educational modules project.  
Live at: **https://cs-biotech.github.io**

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync
```

This installs Pelican, the Alchemy theme (from GitHub), and all other dependencies into a local `.venv`.

## Making changes

All content lives in `content/pages/index.md`. Edit it, then rebuild:

```bash
make build
```

To preview locally in your browser at `http://localhost:8000`:

```bash
make serve
```

## Deployment

Pushing to `main` automatically builds and deploys the site to GitHub Pages via the workflow in `.github/workflows/deploy.yml`. No manual steps needed.

## Template customisation

The theme is [pelican-alchemy](https://github.com/nairobilug/pelican-alchemy). Project-level overrides in `templates/` take precedence over the theme's own templates:

- `templates/base.html` — adds the GoatCounter analytics snippet to every page
- `templates/include/footer.html` — removes the default Authors/Archives/Categories footer links

To override any other theme template, copy it from `.venv/Lib/site-packages/alchemy/templates/` into `templates/` and edit it there.
