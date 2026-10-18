# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project follows [Semantic Versioning](https://semver.org/).

## [1.2.0] - 2026-10-19

### Changed
- Rebranded from "Gümüşhaneliler Egzoz" to "ER AL Egzoz" across the site, logo, share image, structured data and documentation
- Repository renamed to `eral-egzoz`; the site now lives at https://alikaganalbayrak.github.io/eral-egzoz/

## [1.1.1] - 2026-10-18

### Changed
- Documentation (README, CHANGELOG), code comments and build output are now in English. Site content stays in Turkish.

## [1.1.0] - 2026-10-18

### Added
- Dedicated service pages: DPF cleaning, catalytic converter, exhaust replacement, exhaust repair, exhaust welding, fault diagnosis
- Services dropdown in the main navigation
- "About" section on the home page
- `sitemap.xml`, per-page titles and descriptions, canonical URLs
- schema.org `Service`, `FAQPage` and `BreadcrumbList` structured data
- Open Graph share image (`og-image.png`) and Apple touch icon
- 404 page
- Template-based build (`tools/build.py`) and image generator (`tools/make_images.py`)

### Changed
- The business is presented as "Gümüşhaneliler Egzoz"
- Home page heading now targets Esenyurt local search
- Fault finder result links to the matching service page
- `main.js` runs safely on every page

## [1.0.0] - 2026-10-18

### Added
- Fault finder: 14 symptoms, car details, single most likely fault with urgency level
- Pre-filled WhatsApp message and copy button
- Corporate design based on the shop's red, yellow and white business card
- Navigation, quick-contact card, services, why-us, process, FAQ and contact sections
- Live open / closed indicator based on Istanbul time
- Mobile menu and sticky WhatsApp / call dock
- SEO meta tags and schema.org `AutoRepair` structured data
