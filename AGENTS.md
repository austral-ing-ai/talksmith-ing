# Repository Guidelines

## Project Structure & Module Organization

This repository is currently a blank scaffold. Keep the root limited to project
configuration and documentation. As implementation begins, use a predictable
layout:

- `src/` for production source code, organized by feature or domain.
- `tests/` for automated tests that mirror `src/` paths.
- `assets/` for checked-in static assets such as images or fixtures.
- `docs/` for design notes and contributor-facing documentation.

Avoid placing generated output, local caches, or secrets under version control.

## Build, Test, and Development Commands

No build system is configured yet. When one is introduced, document the
canonical commands in `README.md` and keep them runnable from the repository
root. Prefer a small, consistent set such as:

- `npm run dev` — start the local development server.
- `npm test` — run the complete automated test suite.
- `npm run lint` — check formatting and static-analysis rules.
- `npm run build` — create a production build.

Do not add ad-hoc one-off commands when an existing script can be extended.

## Coding Style & Naming Conventions

Follow the formatter and linter selected for the project; do not hand-format
around their output. Use 2-space indentation for JSON, YAML, Markdown lists,
and JavaScript/TypeScript unless the chosen language tooling specifies
otherwise. Name files and directories in `kebab-case` (for example,
`user-profile.ts`), variables and functions in `camelCase`, and types/classes
in `PascalCase`. Keep modules focused and favor clear names over abbreviations.

## Testing Guidelines

Add tests with every behavior change. Store them under `tests/` or beside the
module when the selected framework expects co-location, using names such as
`user-profile.test.ts`. Cover normal behavior, validation failures, and
regressions. Run the full test and lint commands before opening a pull request.

## Commit & Pull Request Guidelines

There is no existing Git history to establish a convention. Use concise,
imperative commits, optionally scoped: `feat(auth): add session validation` or
`fix: handle empty response`. Keep commits single-purpose. Pull requests should
explain the change and its validation, link related issues, and include
screenshots or recordings for visible UI changes. Flag configuration, migration,
or security implications explicitly.
