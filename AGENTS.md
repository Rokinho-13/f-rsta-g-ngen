# AGENTS.md

This file provides context and guidelines for AI coding agents working on the Restaurangjouren project.

## Project Overview

**Restaurangjouren** is a Swedish food wholesale supplier website serving restaurants, cafés, and commercial kitchens since 1989. The project is a static HTML/CSS website showcasing their services, products, and delivery options.

**Target Audience:** Restaurant owners and professional kitchens in Stockholm, Uppsala, and Gotland
**Primary Language:** Swedish
**Tech Stack:** Pure HTML5, CSS3 (no frameworks, no build process)

## Project Structure

```
f-rsta-g-ngen/
├── index.html                           # Main landing page
├── forbattringar-restaurangjouren.md   # Website improvement suggestions document
├── README.md                           # Project readme
└── AGENTS.md                           # This file
```

## Development Environment

### Prerequisites
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- A simple HTTP server for local testing (optional but recommended)

### Local Development

**Option 1: Direct file opening**
```bash
# Simply open the HTML file in your browser
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows
```

**Option 2: Local HTTP server (recommended)**
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (if you have npx)
npx serve

# Then open: http://localhost:8000
```

### File Editing
No build process required. Simply:
1. Edit the HTML/CSS files directly
2. Refresh your browser to see changes
3. All styles are embedded in `<style>` tags within index.html

## Code Style & Conventions

### HTML
- Use semantic HTML5 elements (`<header>`, `<nav>`, `<section>`, `<footer>`)
- Maintain consistent indentation (4 spaces)
- Use Swedish language for all user-facing content
- Keep accessibility in mind (alt attributes, semantic markup)

### CSS
- All CSS is embedded in the `<style>` section of index.html
- Use BEM-like naming where appropriate (`.category-card`, `.header-top`)
- Mobile-first approach with `@media` queries for responsive design
- Color scheme:
  - Primary green: `#1a5c3a`
  - Secondary green: `#145230`
  - Accent orange: `#ff6b35`
  - Light green: `#8fbc8f`

### Content Guidelines
- All text must be in Swedish
- Maintain professional tone suitable for B2B customers
- Key messaging points:
  - 3000+ products
  - Next-day delivery
  - Operating since 1989
  - Service areas: Stockholm, Uppsala, Gotland

## Making Changes

### When modifying index.html:
1. **Read the file first** to understand current structure
2. **Preserve the existing layout structure** unless explicitly changing it
3. **Test responsive behavior** (check the `@media (max-width: 768px)` section)
4. **Maintain color consistency** with the existing green/orange theme
5. **Keep all content in Swedish**

### Common Tasks

**Adding a new section:**
```html
<!-- Add between existing <section> tags -->
<section class="your-section-name">
    <div class="container">
        <!-- Your content here -->
    </div>
</section>
```

**Adding a new CSS class:**
```css
/* Add in the <style> section, grouped with similar components */
.new-component {
    /* styles */
}
```

**Updating navigation:**
```html
<!-- Find the <nav> section and add/modify links -->
<nav>
    <ul>
        <li><a href="/new-page">New Page</a></li>
    </ul>
</nav>
```

## Testing & Validation

### Before committing changes:

**1. HTML Validation**
```bash
# Use W3C validator or online service
# https://validator.w3.org/
```

**2. Browser Testing**
- Test in Chrome/Firefox/Safari
- Check mobile responsive view (DevTools → Toggle device toolbar)
- Verify all breakpoints work correctly

**3. Accessibility Check**
- Ensure proper heading hierarchy (h1 → h2 → h3)
- Check that links have descriptive text
- Verify color contrast meets WCAG standards

**4. Visual Review**
- Header sticky behavior works
- All hover states function properly
- Spacing and alignment are consistent
- Icons display correctly
- Footer sections align properly

### Link Checking
Since this is a static prototype, many links are placeholders:
- Links starting with `/` are internal navigation placeholders
- Verify external links (if any) are valid

## Known Improvement Suggestions

The file `forbattringar-restaurangjouren.md` contains a prioritized list of UX improvements suggested for the real restaurangjouren.se website. When implementing features, refer to this document for:
- Critical fixes (🔴)
- Important improvements (🟠)
- Nice-to-have enhancements (🟡)

**Top priorities from the improvement doc:**
1. Login form moved to separate page (already implemented in this version)
2. Clear "Become a customer" CTA (implemented)
3. Strong USP messaging (implemented)
4. Clear navigation structure (improved in this version)
5. Enhanced footer (implemented with more sections)

## Git Workflow

### Branch naming
- Feature branches: `claude/feature-name-xxxxx`
- All branches must start with `claude/` and end with the session ID

### Commit messages
- Write in Swedish or English
- Be descriptive and concise
- Examples:
  - ✅ "Lägg till förbättrad footer med fler sektioner"
  - ✅ "Fix responsive layout för mobil"
  - ✅ "Add customer testimonials section"
  - ❌ "Update"
  - ❌ "Fix stuff"

### Pull Requests
- Provide a clear description of changes
- Reference any related improvement suggestions from `forbattringar-restaurangjouren.md`
- Include screenshots for visual changes
- List what was tested

**PR Title format:**
```
[Type] Brief description

Examples:
[Feature] Lägg till kundrecensioner
[Fix] Korrigera mobilnavigation
[Enhancement] Förbättra footer-struktur
```

**PR Description template:**
```markdown
## Summary
Brief description of what changed and why

## Changes
- Bullet point list of changes
- Include file names and sections modified

## Testing
- [ ] Tested in Chrome
- [ ] Tested in Firefox
- [ ] Tested mobile responsive view
- [ ] Checked accessibility
- [ ] HTML validates

## Screenshots
[If visual changes, include before/after screenshots]

## Related
References issue #X or improvement from forbattringar-restaurangjouren.md
```

## Important Notes

1. **No JavaScript framework:** This is intentionally a simple HTML/CSS project. Do not add React, Vue, or other frameworks unless explicitly requested.

2. **No build tools:** No webpack, npm, or build process. Keep it simple.

3. **Embedded styles:** All CSS stays in the `<style>` tag in index.html for now. Do not create separate CSS files unless the file grows beyond 1000 lines.

4. **Swedish content:** All user-facing text must be in Swedish. Code comments can be in English or Swedish.

5. **B2B focus:** Remember this is B2B (business-to-business), not B2C. The tone should be professional and service-oriented.

6. **Placeholder links:** Most links are placeholders. That's intentional for this prototype.

## Quick Reference

**Company Info:**
- Name: Restaurangjouren i Sverige AB
- Founded: 1989
- Phone: 010-682 01 00
- Email: info@restaurangjouren.se
- Address: Rörvägen 60, 136 50 Jordbro
- Org.nr: 556460-7736
- Service areas: Stockholm, Uppsala, Gotland
- Order deadline: 17:00 for next-day delivery

**Key Features:**
- 3000+ products
- Next-day delivery
- Wholesale prices
- 35+ years experience

## Questions?

If you're unsure about:
- **Design decisions:** Check `forbattringar-restaurangjouren.md` for guidance
- **Color schemes:** Stick to the existing green (#1a5c3a) and orange (#ff6b35) theme
- **Content tone:** Professional, helpful, B2B-focused
- **Structure:** Keep the single-page layout unless changing the overall architecture

---

*Last updated: 2026-01-18*
