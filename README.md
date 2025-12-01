> Archived project. Kept for historical purposes.
> This work has been superseded by [gen-web](https://github.com/dlknowles/gen-web).

# web-boilerplate-generator

A small CLI tool that scaffolds a modern **Vite + TypeScript** web project in one command.

It’s opinionated on purpose. You get a clean starting point that builds and runs immediately.

---

## Requirements

- **Python** 3.10+
- **Node.js** (LTS) and **npm**

---

## Installation (local dev)

From the `web-boilerplate-generator` repo root:

```bash
pip install -e .
````

This installs a CLI called `gen-web` pointing to the local source in editable mode.

---

## Usage

From anywhere (after install):

```bash
gen-web my-app
```

This will create a new folder:

```
my-app/
  index.html
  package.json
  tsconfig.json
  vite.config.ts
  src/
    main.ts
    styles.css
  .gitignore
```

### Run the generated app

```bash
cd my-app
npm install
npm run dev
```

Then open the URL Vite prints (usually `http://localhost:5173/`).

---

## Project Layout (generated app)

**Root**

* `index.html` – HTML entry point
* `package.json` – npm scripts and devDependencies (Vite + TypeScript)
* `tsconfig.json` – basic TS config for a browser app
* `vite.config.ts` – minimal Vite config
* `.gitignore` – ignores `node_modules`, `dist`, and common junk

**`src/`**

* `main.ts` – TypeScript entry, mounts into `#app` and renders a basic page
* `styles.css` – simple baseline styles (centered card, neutral theme)

---

## What It Does (and Doesn’t)

**Does:**

* Create a runnable Vite + TypeScript project
* Wire up a simple main view and styles
* Replace the project name/title automatically in:

  * `package.json`
  * `index.html`
  * `src/main.ts`

**Does NOT:**

* Ask interactive questions
* Choose frameworks (React/Vue/Svelte/etc.)
* Add linting, testing, or formatting
* Handle deployment

Those can be layered on top of the generated project if you need them.

---

## CLI Details

The CLI entry point is defined in `pyproject.toml`:

```toml
[project]
name = "web-boilerplate-generator"
version = "0.1.0"

[project.scripts]
gen-web = "create_web_project:main"
```

So:

```bash
gen-web <project-name>
```

simply calls `create_web_project.main()` with `<project-name>`.

---

## Future Extensions

Potential additions later:

* Optional flags for frameworks (e.g. `--react`, `--svelte`)
* Optional Tailwind or other CSS setups
* Preconfigured ESLint/Prettier
* Template variants (landing page, dashboard, docs site, etc.)
