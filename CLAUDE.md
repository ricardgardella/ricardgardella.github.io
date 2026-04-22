# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio website for Ricard Gardella (AI Data & Software Engineer), hosted on GitHub Pages at ricardgardella.com. A static site with no build system — pure HTML, CSS, and JavaScript.

## No Build System

There is no package.json, bundler, or build pipeline. Changes are deployed by pushing to the `main` branch on GitHub, which triggers GitHub Pages to serve the updated files automatically.

**SCSS note:** `assets/scss/styles.scss` is the source stylesheet, but it must be manually compiled to `assets/css/styles.css`. If you edit styles, edit `styles.scss` and recompile — or edit `styles.css` directly for quick fixes. There is no automated SCSS compilation configured in this repo.

## Architecture

Everything lives in a single `index.html` (~1,050 lines). There is no routing or component system.

- `assets/js/main.js` — All JavaScript: navigation, accordion, tabs, modals, Swiper initialization, scroll events, dark/light theme toggle (persisted in `localStorage`)
- `assets/scss/styles.scss` — Source styles with CSS custom properties for theming (HSL-based color system, breakpoints at 568px / 768px / 968px)
- `assets/css/styles.css` — Compiled CSS (what the browser loads)
- `assets/pdf/CV_Ricard.pdf` — Downloadable CV

## External Libraries (CDN)

- **Swiper.js** (bundled locally in `assets/`) — Three carousel instances: Portfolio, Testimonials, and Trusted By
- **Unicons v3.0.6** — Icons via CDN
- **Font Awesome 6.5.1** — Icons via CDN
- **Google Fonts (Poppins)** — Typography via CDN
- **Calendly** — Meeting scheduling widget embedded inline in the Home section

## Theme System

Dark/light theme is controlled by toggling the `dark-theme` class on `<body>` and `nav-color` on `<header>`. The active theme is saved to `localStorage` under the key `selected-theme`. The signature image (`assets/img/`) swaps between black and white variants on theme change — see the toggle logic in `main.js`.
