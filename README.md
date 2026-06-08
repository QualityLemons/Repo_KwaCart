# KwaCart

**Milestone Project 3 — Level 5 Diploma in Web Software Engineering**

KwaCart is a Django-based facilitation platform built around **Liberating Structures** — 23 participatory methods that help groups do their best thinking together. It gives facilitators a bank of ready-made tools — warm-ups, reflection exercises, peer consultation formats, and more — that participants can complete individually or together in a live collaborative session. Responses are archived and exportable as Markdown and RTF documents.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Tech Stack](#tech-stack)
3. [User Stories](#user-stories)
4. [Agile Methodology](#agile-methodology)
5. [UX Design](#ux-design)
6. [Project Structure](#project-structure)
7. [Public Pages (no account required)](#public-pages-no-account-required)
8. [Key Features](#key-features)
9. [Epic: Radical Inclusion — AAC-Accessible Live Sessions](#epic-radical-inclusion--aac-accessible-live-sessions)
   - [Access for blind users](#access-for-blind-users)
10. [Epic: LS Pathway Finder](#epic-ls-pathway-finder)
11. [Facilitation Tools](#facilitation-tools)
10. [Collaborative Sessions](#collaborative-sessions)
11. [Archive & Exports](#archive--exports)
12. [Data Models](#data-models)
13. [User Accounts](#user-accounts)
14. [Running Locally](#running-locally)
15. [Deployment](#deployment)
16. [Security](#security)
17. [Admin](#admin)
18. [Adding a New Tool](#adding-a-new-tool)
19. [Validation](#validation)
20. [Lighthouse Audit](#lighthouse-audit)
21. [Testing](#testing)
22. [Credits](#credits)

---

## Purpose

Organisations often struggle to create the conditions for honest, constructive dialogue. KwaCart provides a lightweight facilitation toolkit — grounded in Liberating Structures methodology — that any team can use to surface challenges, share hopes, and warm up to productive conversation. The platform removes the friction of paper-based activities by letting every participant log in, work through a structured prompt, and instantly see a combined result when the facilitator closes the session.

### Mission

KwaCart is designed to grow and progress the real possibility of improving access to — and use of — Liberating Structures by, with, and for:

- **Leadership and management teams** seeking structured approaches to collective decision-making
- **Amateur and emerging facilitators** who want low-barrier access to professional facilitation methods
- **Vulnerable, at-risk, and in-need communities** who could benefit from new approaches to solution-focused co-operation but have historically been excluded from these conversations

### Accessibility commitment

KwaCart improves access to Liberating Structures through active co-design informed by user feedback from a wide range of participants, including:

- Young people and adults with **blindness or visual impairment**
- Individuals with **different physical and developmental abilities**
- People who actively use **augmented and alternative communication (AAC) equipment and tools**

These voices directly shape the platform's inclusive pacing features, AAC composing support, companion pairing flow, and screen-reader-compatible interface.

### Value

Accessible Liberating Structures creates new possibilities in contexts where these tools have never been used before. KwaCart enables:

- **Evidence collection** — gathering structured input from a wider, more representative group of participants
- **Shared question-forming** — co-creating the questions that matter most to a community
- **Advice and suggestion processes** — running structured rounds that surface distributed knowledge equitably
- **Plan development** — building next steps that reflect the full range of perspectives in the room

The value of these outcomes is proportional to the trust placed in them — and trust is proportional to inclusion. KwaCart is built on the belief that expanding who can participate as a facilitator, and who can meaningfully contribute as a participant, improves the quality of inputs, outputs, and outcomes for everyone. It is hoped that this format encourages and motivates more organisations, teams, and community groups to widen the pool of potential facilitators among them, take advantage of new opportunities for engagement, and move at the speed of trust in their use of these tools.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 6.0.4 |
| Database (dev) | SQLite (`db.sqlite3`) |
| Database (production) | PostgreSQL (Heroku Postgres add-on) |
| Static files | WhiteNoise 6.6 |
| Media / export file storage | Cloudinary (production) / local filesystem (development) |
| Production server | Gunicorn 25.x |
| Hosting | Heroku (production), Replit (development) |

---

## User Stories

| # | As a… | I want to… | So that… |
|---|---|---|---|
| 1 | Visitor | browse the landing page without logging in | I can understand what the platform offers before committing to an account |
| 2 | Visitor | use a free tool (Min Specs or 15% Solutions) without an account | I can experience the platform's value before signing up |
| 3 | Visitor | join the waiting list with my email | I am notified when the platform opens more widely |
| 4 | Visitor | submit a feature request | I can influence the product roadmap |
| 5 | New user | register for an account with my email and a password | I can save my work and participate in sessions |
| 6 | Returning user | log in to my account | I can access my archive and join live sessions |
| 7 | Logged-in user | browse the full tool catalog | I can choose the right facilitation tool for my situation |
| 8 | Logged-in user | draft a tool response at my own pace, with autosave | I can refine my thinking without losing progress |
| 9 | Logged-in user | submit a solo draft and receive a downloadable Markdown and RTF export | I have a portable record of my thinking |
| 10 | Facilitator (host) | start a collaborative session for any tool | I can run a real-time group activity |
| 11 | Facilitator | share a session link with signed-in participants | Colleagues who already have accounts can join immediately |
| 12 | Facilitator | display a guest QR code that participants scan to join without an account | I can include participants who haven't registered, such as external guests or workshop attendees |
| 13 | Guest participant | scan a QR code, enter only my name, and fill in a session form | I can contribute to a live session without creating an account |
| 14 | Facilitator | see participant names (including guests) update in real time as people join | I can gauge readiness before starting |
| 15 | Facilitator | start, pause, and reset a countdown timer that all participants see in sync | I can time-box each phase of the activity |
| 16 | Facilitator | close the session when everyone has responded | All contributions are locked and a combined export is generated automatically |
| 17 | Participant (signed-in or guest) | be redirected automatically when the host closes the session | I see the combined results without needing to refresh |
| 18 | Logged-in user | view my archive of solo submissions and sessions | I can revisit and reflect on past work |
| 19 | Logged-in user | download Markdown and RTF exports for any archived record | I can share outputs or store them outside the platform |
| 20 | Staff user | view the waiting-list table in the archive dashboard | I can manage the rollout and follow up with prospective users |
| 21 | CEO | run structured dialogue sessions across teams and levels of my organisation using a shared facilitation tool | I can break down communication barriers, surface what people actually think, and replace top-down messaging with genuine two-way conversation |
| 22 | Middle manager | deploy a live session tool so that everyone involved in a stalled project can contribute their perspective in real time and see each other's responses immediately when the session closes | the process feels transparent and trustworthy, and the team can move forward together based on evidence rather than assumption |
| 23 | Youth worker | guide a group of young people through a series of facilitation tools, saving every session's responses to a growing archive | the group builds a real record of their collective thinking while also developing practical skills in scribing, facilitation, and working with structured data |
| 24 | Participant using an eye-gaze tracker or switch-scanning system | toggle a static, high-contrast interface with an abstract time indicator | I can compose my thoughts without ticking countdowns or layout changes pulling my focus and causing physical fatigue |
| 25 | Session host | see a visual indicator when an AAC user is actively drafting a response — even if their input field is currently empty | I do not prematurely close a session and cut off a voice while they are mid-composition |

---

## Agile Methodology

The project was planned and delivered using an Agile approach across five one-week sprints. A GitHub Project board tracked every user story through four columns — **Backlog → In Progress → In Review → Done** — providing a continuous, visible record of progress.

### GitHub Project board

The board is linked to the repository and uses GitHub Issues as cards. Each issue corresponds to a user story by number (e.g. Issue #8 maps to US-08 in the table above). Labels on each issue show its MoSCoW priority and the sprint it was scheduled in. Commit messages reference the closing issue number (`Closes #N`) so that merging a branch automatically moves the card to Done.

### MoSCoW prioritisation

All 23 user stories were prioritised at the start of the project. The categories below reflect the decisions made in Sprint 1 planning.

| Priority | User stories | Rationale |
|---|---|---|
| **Must Have** | US 1, 5, 6, 7, 8, 9, 10, 16, 18 | Without these the application has no usable core: public landing, authentication, solo tool drafting and submission, session creation and closure, and the archive. |
| **Should Have** | US 2, 11, 12, 13, 14, 15, 17, 19 | Guest QR access, the timer, real-time participant status, and auto-redirect on session close significantly improve the live facilitation experience but the platform can function without them. |
| **Could Have** | US 3, 4, 20, 21, 22, 23 | Waiting list, feature requests, and the staff dashboard are useful for managing the rollout but are not part of the core facilitation workflow. The CEO, manager, and youth-worker personas (US 21–23) describe future deployment contexts that informed design decisions without requiring dedicated features. |
| **Won't Have (this release)** | — | No features were formally deferred to a later release; all Must and Should stories were completed within the five sprints. |

### Sprint log

Each sprint had a defined goal, a set of user stories pulled from the backlog, and a review at the end before the next sprint was planned.

| Sprint | Goal | User stories delivered |
|---|---|---|
| **1 — Foundation** | Working Django project with email authentication, landing page, and public nav | US 1, 5, 6 |
| **2 — Solo tool flow** | Tool catalog, draft editor with autosave, submit endpoint, Markdown/RTF/HTML export, archive dashboard | US 7, 8, 9, 18, 19 |
| **3 — Collaborative sessions** | Session creation, signed-in participant joining, real-time status polling, timer, session close and combined export | US 10, 11, 14, 15, 16, 17 |
| **4 — Guest access and public engagement** | Guest join via QR / UUID token (no account required), free try-it pages, waiting list, feature request, staff waiting-list view | US 2, 3, 4, 12, 13, 20 |
| **5 — Hardening and deployment** | Custom error pages, full validation pass (W3C/JSHint/flake8), security audit, Heroku deployment configuration, README completion | US 21, 22, 23 (context-driven design review); all earlier stories re-tested |

---

## UX Design

### Design goals

The overriding goal was to minimise friction at every step. Facilitation tools are used in workshops and meetings where participants are time-pressed and sometimes unfamiliar with digital tools. The UI therefore prioritises clarity over visual richness: generous whitespace, a single-column form layout, labels above fields (never placeholder-only), and a limited palette applied consistently.

### Information architecture

The site is divided into two clear zones:

- **Public** — landing page, about, two free try-it tools, waiting list, feature request, login, register. Visitors can experience the platform's value before committing to an account.
- **Authenticated** — tool catalog, draft editor, collaborative sessions, archive dashboard, downloads. Everything that stores or retrieves personal data sits behind login.

This boundary was a deliberate design decision: making the free tools genuinely free (no sign-up wall) reduces the barrier to a first-use experience, which is the primary conversion moment for a platform like this.

Within the authenticated zone a further privilege layer exists: only the session host can close a session; only staff users see the waiting-list table. These role distinctions are surfaced visibly in the UI (the Close Session button only appears to the host; the waiting-list panel is hidden from regular users) so the access model is legible without reading documentation.

### Colour palette rationale

Six colours were chosen and assigned specific semantic roles so the palette carries meaning rather than just decoration:

| Colour | Hex | Semantic role | Reasoning |
|---|---|---|---|
| Purple | `#5D3A9B` | Primary brand, buttons, links | Associated with creativity and facilitation; distinctive without being aggressive |
| Teal | `#40B0A6` | Success states, result borders, open sessions | Calm, positive — signals that something has worked or is live |
| Gold | `#E1BE6A` | "Free" badges, count labels, CTA highlight | Draws attention without urgency; works alongside purple without clashing |
| Orange | `#E66100` | Step numbers, running-timer button | Conveys active/in-progress state without the alarm connotations of red |
| Yellow | `#FEFE62` | "Already on list" duplicate notice | High contrast on light backgrounds; distinct from the success teal |
| Pink | `#D35FB7` | Accent use | Completes the palette; used sparingly to avoid diluting meaning |

All colour choices were checked for WCAG AA contrast (≥ 4.5:1) against their backgrounds during development.

### Navigation and form design decisions

- **Single-column forms** — all tool forms use a single-column layout so the reading order is linear and keyboard navigation is predictable. This also avoids the ambiguity of multi-column grid forms on narrow screens.
- **Server-side validation with inline errors** — form errors are rendered next to the offending field and linked via `aria-describedby` (wired by `aria_wiring.js`) so screen readers announce the error when the field is focused. Client-side validation (e.g. `required` attributes) is used only as a first-pass convenience, never as the sole guard.
- **Autosave on keystroke** — the draft editor saves two seconds after the user stops typing rather than requiring an explicit save action. This removes the cognitive load of remembering to save, which matters in workshop settings where a facilitator may close a laptop lid without warning.
- **QR code for guest access** — the QR code was chosen specifically to eliminate the friction of typing a URL on a mobile device during a live session. Scanning a code is a single gesture; copying a URL and opening a browser takes five to eight steps on most phones.
- **Timer server-sync** — rather than each participant's browser running its own clock (which drifts), the timer state is stored server-side and polled every four seconds. All participants and the host see the same remaining time regardless of when they joined the session.
- **Post/Redirect/Get on all forms** — every form POST that mutates state (submitting a response, signing up to the waiting list, submitting a feature request, running a free try-it tool) redirects to a GET after success. This means pressing the browser back button and then forward never triggers a "Confirm Form Resubmission" dialog and never creates a duplicate record.

### Wireframes

Hand-drawn wireframes showing the intended layout and key interactive regions for the application.

#### Landing page and site overview

The landing page presents the KwaCart brand, tagline, and three entry points: register, log in, and join the waiting list. Below the fold, three content sections correspond to the three main informational pages: What is KwaCart?, How to use KwaCart, and AAC tools for KwaCart.

![Landing page wireframe](docs/wireframes/wf-landing.png)

---

#### User flow — How to use KwaCart

The onboarding journey: Register → Log in → choose a Pathway by time / group size / goals → toggle AAC features and connect equipment → start a session → share session links with participants.

![User flow wireframe](docs/wireframes/wf-user-flow.png)

---

#### Tool blueprint — draft editor and session form

Every tool shares a common blueprint: a basic explainer of how the tool is used, minimum time required, AAC access format, and accessibility links for group mode. Below the explainer sits the timer (Start / Pause / Stop), one or more labelled text-input fields, and a Save / Submit action.

![Tool blueprint wireframe](docs/wireframes/wf-tool-blueprint.png)

---

#### AAC features — display modes and LS Tools list

The AAC features page has a display-options bar at the top with three states: **E-Z read**, **Accessibility Mode**, and **Standard display**. A fourth option surfaces **Blind user elements** (screen-reader-only content). Below the bar, the LS Tools list shows each tool card with its name, an E-Z read description, an image, and a minimum-time chip.

![AAC features wireframe](docs/wireframes/wf-aac-features.png)

---

#### AAC Calm Timer

Replaces the standard digit countdown with a quiet colour block: green = plenty of time, amber/gold = some time, red = not a lot of time. Design goal: make KwaCart ADA and AAC compliant from the beginning — useful for children and adults with different developmental and physical abilities, and understandable for carers and support workers.

![AAC Calm Timer wireframe](docs/wireframes/wf-aac-calm-timer.png)

---

#### AAC letter board — context for pacing

An AAC letter board showing the full alphabet, digits, punctuation, and emoji rows. The note at the bottom — *average time to 1 word: 17 seconds* — grounds the Inclusive Pacing and Calm Timer design decisions in real-world AAC usage data.

![AAC letter board wireframe](docs/wireframes/wf-aac-letter-board.png)

---

#### KwaCart Databank (Archive dashboard)

The Archive dashboard groups saved content by tool, showing each entry with session metadata, last-use date, and status. Selecting an entry expands a two-column detail view: the **main user's** responses on the left and **contributing users / follows** on the right. Three download buttons appear at the bottom of each expanded entry: **MD** (Markdown), **RTF**, and **DEL** (delete).

![Databank wireframe](docs/wireframes/wf-databank.png)

---

#### Knowledge Bank

Goal: download to Markdown (`.md`) or Rich Text Format (`.rtf`) to ensure full knowledge capture from events. A future export path converts the same content to Open Office, MS Word, or HTML so outputs are usable in any organisation's existing toolchain.

![Knowledge Bank wireframe](docs/wireframes/wf-knowledge-bank.png)

---

### Page designs (implemented UI)

The screenshots below show the implemented design for each key page.

#### Landing Page
The public homepage — introduces the platform, links to free tools, registration, and the waiting list.

![Landing page](docs/screenshots/landing.jpg)

#### About Page
Explains Liberating Structures, the 23 tools, and the project background.

![About page](docs/screenshots/about.jpg)

#### Register
New account creation — email address and password. Redirects to login on success.

![Register page](docs/screenshots/register.jpg)

#### Log In
Email-based login. Redirects authenticated users directly to the tool catalog.

![Login page](docs/screenshots/login.jpg)

#### Free Tool — Min Specs
Try Min Specs without an account. Includes a 5-minute countdown timer, structured form, and instant output.

![Min Specs free try](docs/screenshots/tool-min-specs.jpg)

#### Free Tool — 15% Solutions
Try 15% Solutions without an account. Same timer and structured output experience.

![15% Solutions free try](docs/screenshots/tool-15-percent.jpg)

#### Waiting List Signup
Visitors can register their interest before accounts open publicly.

![Waiting list](docs/screenshots/waiting-list.jpg)

#### Feature Request
Visitors and users can submit ideas for new tools or platform improvements.

![Feature request](docs/screenshots/feature-request.jpg)

#### Guest Join
Participants who scan the QR code land here. They enter only their name — no account needed — and go straight to the session form.

![Guest join](docs/screenshots/guest-join.jpg)

#### Accessibility
Explains AAC support, Calm timer, and large-target mode, and screen-reader / blind-user access. A display-options bar at the top of the page lets any visitor toggle **Easy-read version** or **Accessibility Mode** before logging in. The page has three sections: AAC features, Blind & screen-reader access, and an all-tools reference.

> Screenshot pending — see the [Accessibility wireframe](#aac-features--display-modes-and-ls-tools-list) in the Wireframes section above.

### User Flow

```mermaid
flowchart LR
    V([Visitor])      --> LP[Landing Page]
    LP                --> |Try free|    FT[Free Tool - Min Specs / 15% Solutions]
    LP                --> |Join|        WL[Waiting List]
    LP                --> |Idea|        FR[Feature Request]
    LP                --> |Sign in|     LOG[Login / Register]
    LOG               --> CAT[Tool Catalog]
    CAT               --> |Work Solo|   DRAFT[Draft Editor - autosave]
    CAT               --> |Facilitate|  HOST[Session Host View - QR / Timer / Controls]
    DRAFT             --> |Submit|      ARC[Archive Dashboard]
    HOST              --> |QR scan|     GNAME[Guest: Enter Name]
    GNAME             --> GFORM[Guest Session Form - focused participant UI]
    GFORM             --> |polls|       HOST
    HOST              --> |Close|       ARC
    ARC               --> |Download|    EXP[Markdown / RTF Export]
```

---

### Page Access Map

| Colour | Meaning |
|---|---|
| Public (no login) | Landing, About, Free Tools, Waiting List, Feature Request, Login, Register |
| Login required | Tool Catalog, Draft Editor, Session pages, Archive Dashboard, Archive Detail, Downloads |
| Staff / Admin only | Waiting list table in dashboard, Django Admin (`/admin/`) |

---

## Project Structure

```
KwaCart/
├── config/
│   ├── settings/
│   │   ├── base.py          Shared settings
│   │   ├── local.py         Dev overrides (DEBUG=True, ALLOWED_HOSTS from REPLIT_DOMAINS)
│   │   └── production.py    Production settings (Gunicorn, WhiteNoise, SECURE_PROXY_SSL_HEADER)
│   ├── urls.py              Root URL config — home, about, waiting-list, feature-request, accounts, tools, archive
│   └── wsgi.py
│
├── accounts/                Email-based auth
│   ├── models.py            Custom User + UserManager (validate_password enforced)
│   ├── forms.py             Registration / login forms
│   └── utils.py             log_action() helper (writes to AuditLog)
│
├── tools/                   Facilitation tool engine
│   ├── registry.py          TOOL_CATALOG — single source of truth for all 23 tools
│   ├── implementations.py   BaseTool subclasses (validate + process)
│   ├── forms.py             Django Form classes for each tool
│   ├── views.py             Solo draft + collaborative session + free try-it flows
│   ├── urls.py              URL patterns
│   └── utils.py             get_tool_metadata() + SHA-256 canvas file handling
│
├── archive/                 Sessions, submissions, waiting list, feature requests
│   ├── models.py            ToolSession, ToolInstance, AuditLog, WaitingListEntry, FeatureRequest
│   ├── admin.py             Admin registrations for all archive models
│   ├── views.py             Archive dashboard + detail + waiting list signup + feature request
│   ├── views_downloads.py   Secure file download (solo + session exports)
│   ├── urls.py
│   ├── urls_waiting_list.py  Public waiting-list routes
│   └── urls_feature_request.py  Public feature-request routes
│
├── exporters/
│   ├── pipeline.py          run_export_pipeline() / run_session_export_pipeline()
│   ├── md_gen.py            Markdown generation (solo + combined)
│   └── rtf_gen.py           RTF generation (solo + combined)
│
├── templates/
│   ├── base.html            Site chrome (nav, messages, .sr-only utility)
│   ├── landing.html         Public homepage — no login required
│   ├── about.html           About page
│   ├── accounts/            Login, registration templates
│   ├── archive/
│   │   ├── dashboard.html              Personal archive + waiting-list section (staff only)
│   │   ├── detail.html
│   │   ├── waiting_list_signup.html    Public signup
│   │   └── feature_request.html        Public feature request form
│   └── tools/
│       ├── catalog.html          Tool bank
│       ├── tool_try.html         Free try-it page (no login, countdown timer)
│       ├── draft_editor.html     Solo drafting interface
│       ├── session_open.html     Live collaborative session (QR code share)
│       ├── session_closed.html   Combined results + download links
│       ├── info_box.html         What / How / Why / agreements panel
│       ├── _timer.html           Countdown timer (server-sync, aria-live, offline detection)
│       └── _drawing_canvas.html  Drawing canvas with accessibility announcements
│
├── media/drawings/          Canvas PNG files (SHA-256 content-based filenames)
├── static/
├── manage.py
└── requirements.txt
```

---

## Public Pages (no account required)

| URL | Description |
|---|---|
| `/` | Landing page — introduces the platform, links to free tools and waiting list |
| `/about/` | About page — explains Liberating Structures, the 23 tools, and the project |
| `/tools/min-specs/try/` | Free try-it page for Min Specs |
| `/tools/15-percent-solutions/try/` | Free try-it page for 15% Solutions |
| `/waiting-list/` | Waiting-list signup (email + optional name) |
| `/request-a-feature/` | Feature request form (name, email, title, description) |
| `/accounts/login/` | Log in |

### Free try-it pages
Both free tools include the full form and result output, a **5-minute countdown timer** with Start / Pause / Reset controls, a progress bar, and screen-reader-friendly milestone announcements. A "Join the waiting list" nudge is shown instead of a "Create account" call-to-action.

### Waiting list
Visitors can sign up at `/waiting-list/`. Duplicate email addresses are handled gracefully. Staff users see the full waiting-list table in the archive dashboard.

### Feature requests
Visitors and users can submit a feature idea at `/request-a-feature/`. Submissions are stored in the `FeatureRequest` model and are visible to staff only via the Django admin. The form collects name, email, a short title, and a description.

---

## Key Features

### Solo tool use
Any logged-in user can pick a tool from the catalog, draft at their own pace (autosave on every keystroke), and submit when ready. Submission processes the response and stores downloadable Markdown and RTF files.

### Collaborative sessions
A facilitator creates a **session** for any tool. Participants join via a shared URL or **QR code** displayed on the session page. Every four seconds, the page polls for participant list updates, timer state, and session-closed redirects. When the facilitator closes the session, all responses are processed and a combined export is generated.

#### Guest QR code access (no account needed)
The session page shows two share options:

- **Signed-in link** — for participants who already have an account.
- **Guest QR code** — a separate link (and scannable QR code) that lets anyone join without creating an account. Scanning the code takes the participant to a name-entry page; after entering their name they go straight to the form. The host sees all participants — including guests — listed by name in real time.

Guest responses are saved alongside signed-in responses and appear in the combined results when the session closes. Guests see a prompt to create an account at the end if they'd like to keep a personal archive in future.

### Drawing canvas
Tools with `show_canvas: True` in the registry include a freehand drawing canvas. Drawings are saved as PNG files in `media/drawings/` using SHA-256 content-based filenames. The file path (not the data URL) is stored in `payload_input`. The canvas includes keyboard and screen-reader accessibility support with ARIA live announcements for every toolbar action.

### Archive dashboard
`/archive/dashboard/` shows solo submissions, sessions the user hosts or has joined (with role and status), and a waiting-list table (staff users only).

### Timer widget
Tools can opt in to a countdown timer. The timer:

- MM:SS display; turns amber at ≤ 10 s, red at zero. Start / Pause / Reset controls with a phase progress bar.
- **Server sync** — all participants see the same remaining time via the poll endpoint; late-joiners sync immediately.
- **Milestone announcements** at 5 min, 2 min, 1 min, 30 s, and 10 s via ARIA live regions.
- **Pause badge** — visible "Paused" indicator; host-only amber reminder if paused for over 5 minutes (configurable via `pause_reminder_threshold_sec`).
- **Offline detection** — stale badge on `window.offline`; reconnection toast when the connection recovers.
- **AAC Calm mode** — replaces ticking digits with a static colour block (green → amber → red) to reduce eye-fatigue for eye-gaze users.

### What / How / Why info panel
Every tool page includes a structured instruction panel with **What**, **How**, **Why**, and optional **Agreements**. A **Load example data** button pre-fills the form.

### Tool catalog
Each tool card shows its title, a short tagline, and **Start solo** / **Start session** buttons.

---

## Epic: Radical Inclusion — AAC-Accessible Live Sessions

> **As an inclusive facilitator,** I want KwaCart to natively support Alternative and Augmentative Communication (AAC) workflows, devices, and pacing, so that non-verbal, switch-scanning, and eye-gaze users can actively participate in live sessions without physical or temporal exclusion.

AAC users include people who communicate via eye-gaze trackers, switch-scanning systems, or dedicated communication software such as Grid 3. These users often compose responses in an external application before pasting them into the browser — meaning their input field can be empty for minutes at a time while they are actively working. Standard ticking countdown timers also create involuntary re-fixation on every digit change, causing physical fatigue for eye-gaze users over a sustained session.

KwaCart addresses both problems through two complementary sub-features described below.

---

### User Story 24 — Visual Pacing & Reduced Eye-Fatigue

> **As a participant using an eye-gaze tracker or switch-scanning system,**
> I want to toggle a static, high-contrast interface with an abstract time indicator,
> **so that** I can compose my thoughts without layout changes or ticking countdowns pulling my focus and causing physical fatigue.

#### Acceptance Criteria

| # | Given | When | Then |
|---|---|---|---|
| AC1 | A live session page with a running digit countdown | I toggle **Calm timer** | The numeric display is replaced by a static colour block: 🟢 Green (plenty of time) → 🟡 Amber (under half) → 🔴 Red (expiring). The colour drifts gradually; it never ticks. |
| AC2 | Calm timer is active | Any poll response arrives | The page layout does not reflow. No floating banners, no pop-up "Saved" notices, and no dynamic resizing occur while Calm timer is on. |
| AC3 | **Accessibility Mode** is toggled on | Any interactive element is rendered | Every input box and submit button meets a minimum touch / gaze target of **80 × 80 px** with at least **24 px** clear padding between adjacent interactive elements. All CSS transitions are set to `0 ms` (zero-motion guarantee). |

#### Workflow screenshots

The standard digit timer — visible on any free-try page before toggling Calm mode:

![Standard digit timer](docs/screenshots/aac-timer-standard.jpg)

The wireframe below shows the Calm Timer colour states and explains the design goal behind the feature:

![Calm timer wireframe](docs/wireframes/wf-aac-calm-timer.png)

#### Implementation notes

| File | Role |
|---|---|
| `static/js/timer.js` | `calmMode` flag; `renderCalmBlock()` replaces `.timer-display` with `.calm-block`; colour computed from `elapsedFraction` |
| `static/css/timer.css` | `.calm-block` with `transition: background-color 4s ease`; `.a11y-theme .calm-block` with `transition: none` |
| `static/css/accessibility_theme.css` | High-contrast colours, `min-height / min-width: 80px`, `gap: 24px`, `transition: none !important` |
| `templates/tools/_timer.html` | **Calm timer** toggle button rendered for `{% raw %}{% if not is_host %}{% endraw %}` only; hosts always need the exact digit display |
| `static/js/accessibility_theme.js` | Reads `localStorage.kwacart_a11y_theme`; applies `.a11y-theme` to `<html>` before first paint to prevent FOUC |

---

### User Story 25 — Composition Presence Flag

> **As a session host,**
> I want to see a visual indicator on my dashboard when an AAC user is actively drafting a response — even if their browser input field is currently empty,
> **so that** I do not prematurely close a session and cut off a voice while they are mid-composition.

#### Acceptance Criteria

| # | Given | When | Then |
|---|---|---|---|
| AC1 | A participant using external communication software (e.g. Grid 3) | They interact with their device keyboard while the KwaCart tab is focused | The app emits an `active` metadata heartbeat to the server (`POST /session/{id}/composing/`) and refreshes it every 15 seconds while keyboard activity continues |
| AC2 | An active heartbeat has been received within the past 30 seconds | The host's participant roster is rendered | A **✏ Composing…** status label appears next to that participant's name in the live roster |
| AC3 | The host clicks **Close Session** | At least one participant has an active heartbeat | A warning modal appears: *"One participant is still composing — closing now may cut off their response."* The host may choose **Close anyway** or **Wait for [name]** |

#### Workflow screenshots & wireframe

The user-flow wireframe below shows the full onboarding journey including the AAC features toggle step where participants connect their equipment before a session begins:

![User flow wireframe](docs/wireframes/wf-user-flow.png)

#### Implementation notes

| File | Role |
|---|---|
| `static/js/session_composing.js` | Authenticated-participant heartbeat: listens for `keydown` on `document`, POSTs to `session_composing` URL, debounced to one POST per 15 s, clears on `visibilitychange` |
| `static/js/guest_composing.js` | Identical logic for unauthenticated guest participants |
| `archive/models.py` | `ToolInstance.composing_heartbeat_at` — `DateTimeField(null=True)` updated on every heartbeat POST |
| `tools/views.py` | `session_composing` view — `@login_required` / guest-token gated; stamps `composing_heartbeat_at = now()` |
| `tools/views.py` | `session_status` response includes `composing_users` list (instances with heartbeat < 30 s old) |
| `static/js/session_poll.js` | On each poll, reads `composing_users` and updates the roster chip label to **✏ Composing…** |
| `templates/tools/session_open.html` | **I'm composing…** `<button aria-pressed>` rendered for `{% raw %}{% if not is_host %}{% endraw %}` participants; JS toggles its pressed state and starts/stops the heartbeat |
| `static/js/session_close.js` | Intercepts the Close Session click; if the current poll data contains any `composing_users`, renders the warning modal before allowing the POST to proceed |

---

### Access for blind users

> **As a blind or low-vision participant or facilitator,**
> I want every page, form, and interactive control to be operable and understandable with a screen reader and keyboard alone,
> **so that** I can take a full and equal part in KwaCart sessions without needing a mouse or sighted assistance.

This work is described on the live [Accessibility page](/accessibility/#blind-access) alongside the AAC features above. The implementation spans every public and authenticated page and is summarised below.

#### Acceptance Criteria

| # | Given | When | Then |
|---|---|---|---|
| AC1 | Any page in the application | A keyboard user presses **Tab** once after page load | A visible "Skip to main content" link appears; activating it moves focus to the `<main>` landmark, bypassing the navigation bar |
| AC2 | A screen reader is active | The user navigates by landmarks | A `<main id="main-content">` region and a labelled `<nav aria-label="Main navigation">` are present on every page |
| AC3 | The log-in or sign-up form has a validation error | The page re-renders with the error | The error container carries `role="alert" aria-live="assertive"` so the error is announced immediately; the offending field is marked `aria-invalid="true"` and linked to the error via `aria-describedby` |
| AC4 | The sign-up form's password field receives focus | The help text (password requirements) is present | The help text element is linked to the field via `aria-describedby` so a screen reader reads the requirements automatically |
| AC5 | The archive dashboard is rendered with saved submissions | A screen reader user navigates the tables | Each table has a `<caption>` naming it; every `<th>` carries `scope="col"`; every View / Preview / Delete / Open button or link has a unique contextual `aria-label` including the tool name and date |
| AC6 | The tool catalog is in "Work Solo" or "Facilitate" mode | A screen reader user navigates to the page | A screen-reader-only `<h1>` announces the current mode so the page is never without a page title |
| AC7 | The drawing canvas toolbar is rendered | A screen reader user navigates the toolbar buttons | Pen-size buttons are labelled "Pen size: small / medium / large"; the eraser button is labelled "Eraser tool" |
| AC8 | A timer or autosave event occurs during a session | The value or state changes without a page reload | An `aria-live` region announces the change (timer milestones, "Draft saved") so the user is informed without looking at the screen |

#### Implementation notes

| File | What changed |
|---|---|
| `templates/registration/login.html` | Skip link; `<main id="main-content">`; `aria-label` on `<nav>` and `<form>`; `role="alert" aria-live="assertive"` on non-field-errors |
| `templates/registration/signup.html` | As above; `id="id_password1-help"` on the password requirements paragraph |
| `templates/landing.html` | Skip link; `<main id="main-content">`; `aria-label="Main navigation"` on `<nav>` |
| `templates/about.html` | As landing.html |
| `static/css/landing.css` `about.css` `login.css` `signup.css` | `.skip-link` and `.sr-only` utility rules (already present in `base.css` for pages that extend `base.html`) |
| `static/js/aria_wiring.js` | Extended to wire `[id$="-help"]` elements to their input via `aria-describedby` (appends to any existing value); existing error-wiring logic unchanged |
| `templates/archive/dashboard.html` | `<caption class="sr-only">` on both tables; `scope="col"` on all `<th>`; contextual `aria-label` on every View / Preview / Delete / Open link and button |
| `templates/tools/catalog.html` | Screen-reader-only `<h1>` announcing "Work Solo" or "Facilitate" in the respective catalog modes |
| `templates/tools/_drawing_canvas.html` | `aria-label` on S / M / L pen-size buttons and the eraser button |

---

## Epic: LS Pathway Finder

> **As a facilitator planning a workshop,** I want to answer a few quick questions about my time, group size, and goals, so that the platform recommends the most appropriate Liberating Structures for my session — without me having to read through all 23 tools manually.

Facilitators arriving at KwaCart often know what outcome they want (e.g. "surface hidden challenges" or "build psychological safety") but are unsure which LS method will fit their constraints. The Pathway Finder removes that friction by guiding them through a structured five-step wizard and returning a prioritised, scored list of tools they can launch immediately.

---

### User Story 26 — Contextual Pathway Recommendations

> **As a facilitator,**
> I want to answer three quick questions (time available, group size, and working modality) and then tap the goals that matter most to my group,
> **so that** I receive a ranked list of Liberating Structures best suited to my session — with one-click launch into Solo or Facilitate mode.

#### Acceptance Criteria

| # | Given | When | Then |
|---|---|---|---|
| AC1 | An authenticated user navigates to `/tools/pathway/` | The page loads | A five-step wizard is displayed with a progress indicator showing steps 1–5 |
| AC2 | Steps 1–3 are completed (time, people, modality) | The user clicks **Next** | Each answer is stored client-side; the wizard advances without a page reload |
| AC3 | Step 4 is reached | The page renders | 33 goal circles are displayed in randomised order using a Wong colorblind-safe palette; tapping any circle toggles its selected state and reads the goal aloud via the Web Speech API |
| AC4 | At least one goal circle is selected | The user advances to step 5 | Tools are scored against the selected goals and sorted by match percentage; each result card shows title, tagline, match bar, and **Work Solo** / **Facilitate** buttons |
| AC5 | The user clicks **Work Solo** or **Facilitate** on a result card | — | A POST form submits the correct CSRF token and redirects to the appropriate tool session page |

#### Workflow screenshots

**Step 1 — How much time do you have?**
Seven time-range buttons; the progress indicator highlights step 1.

![Pathway Finder — step 1: time available](docs/screenshots/pathway-step1-time.jpg)

**Step 2 — How many people are attending?**
Five group-size options; steps 1–2 are now filled in the progress indicator.

![Pathway Finder — step 2: group size](docs/screenshots/pathway-step2-size.jpg)

**Step 3 — In-person or virtual?**
Three modality buttons; a Back button and a **Next: pick your goals →** button appear at the bottom once a choice is made.

![Pathway Finder — step 3: modality](docs/screenshots/pathway-step3-modality.jpg)

**Step 4 — Goal circles (unselected)**
33 goal circles rendered in a randomised order using the Wong colorblind-safe palette. Tapping any circle toggles its selected state and reads the goal aloud via the Web Speech API.

![Pathway Finder — step 4: goal circles](docs/screenshots/pathway-step4-goals.jpg)

**Step 4 — Goal circles (with selections)**
Three goals selected (outlined in white with a tick): "Name the big tension", "Meet new people fast", and "Plan step by step". "Clear what blocks you" is also ticked.

![Pathway Finder — step 4: goals selected](docs/screenshots/pathway-step4-goals-selected.jpg)

**Step 5 — Your recommended pathway**
All five steps filled; ranked result cards show the tool title, tagline, and **Work Solo** / **Start a Session** launch buttons for each match.

![Pathway Finder — step 5: results](docs/screenshots/pathway-step5-results.jpg)

#### Implementation notes

| File | Role |
|---|---|
| `tools/views.py` | `pathway_finder` — `@login_required`; passes `tools_data` dict (title + tagline per slug) as JSON via `json_script` filter |
| `templates/tools/pathway_finder.html` | Five-step wizard markup; tool data injected with `{% raw %}{{ tools_data\|json_script:"pathway-tools-data" }}{% endraw %}`; result cards include POST forms for session launch |
| `static/js/pathway_finder.js` | All recommendation logic runs client-side; `buildCircles()` renders 33 goal circles; `scoreTools()` computes match percentage; `showStep()` is exposed on `window` for Back button inline handlers |
| `static/css/pathway_finder.css` | Wizard layout, circle grid, match-percentage bars, result card styles |

---

## Facilitation Tools

23 tools are currently registered across two categories.

### Low-Risk Warm-ups

| Tool | Tagline |
|---|---|
| I am and I like | A quick energiser — go around the circle, share your name and something you love. |

### Facilitation

| Tool | Tagline |
|---|---|
| 1-2-4-All | Turn any question into group insight — alone, then pairs, then fours, then everyone. |
| 15% Solutions | What can you start doing right now, with the freedom and resources you already have? |
| 25/10 Crowd Sourcing | Surface your group's boldest ideas in 30 minutes with cards and a countdown from 25. |
| Appreciative Interviews | Uncover what's already working by sharing stories of peak success. |
| Conversation Café | Calm group dialogue on a hard question — a talking object and four structured rounds. |
| Discovery & Action Dialogue | Seven questions that surface hidden solutions already working in your group. |
| Drawing Together | A silent, simultaneous visual exercise using five universal shapes. |
| Five Structural Elements | Get into pairs, share challenges and expectations, build new connections fast. |
| Helping Heuristics | Practise four ways of helping in 15 minutes and discover your default pattern. |
| Idea Generation | A minute of individual reflection, then share with the group. |
| Improv Prototyping | Act out the problem, spot what works, and rebuild a better version on the spot. |
| Impromptu Networking | Meet three people, share your challenge, walk away with fresh ideas. |
| Min Specs | Strip your rules down to the bone. What absolutely must stay? |
| Nine Whys | Ask "why?" nine times and find out what actually drives you. |
| Shift & Share | Ditch the long presentations. Rotate through rapid-fire innovation stations instead. |
| TRIZ | List everything that would guarantee failure — then stop doing those things. |
| Troika Consulting | Three people, three turns, back turned. Straight-talking peer advice in 30 minutes. |
| User Experience Fishbowl | Insiders share the unfiltered story. The room listens, then asks. |
| What, So What, Now What? | Debrief any shared experience in three stages — facts first, then meaning, then action. |
| Wicked Questions | Name the contradictions your group is navigating — and make them visible. |
| Wise Crowds | 15 minutes of focused peer advice on a real challenge, with the client's back turned. |
| Wise Crowds (Large Group) | Scale peer consultation to a full room — one client, primary team, satellite groups. |

### Wicked Questions — live session walkthrough

The screenshots below show a complete Wicked Questions session from first response through to the combined Markdown export.

**Round 1 — Individual questions (timer: 21:10)**
Participants write their own "How is it that…?" pairs of opposites into the first textarea while the session timer runs.

![Wicked Questions — individual response form](docs/screenshots/wicked-q-session-form1.jpg)

**Round 2 — Small group question added (timer: 11:55)**
A second field appears for the small group's most impactful Wicked Question. Both fields are live and editable until the host closes the session.

![Wicked Questions — small group field](docs/screenshots/wicked-q-session-form2.jpg)

**Round 3 — Whole-group refinement added (timer: 01:59)**
The third field captures the whole group's refined Wicked Question. All three fields are visible simultaneously; the session closes when the timer reaches zero or the host clicks Close.

![Wicked Questions — whole group refinement field](docs/screenshots/wicked-q-session-form3.jpg)

**Session closed — combined results page**
After the host closes the session, all participants see the combined results. The download bar offers Markdown and RTF exports. Each participant's response card shows `group_question`, `individual_questions`, and `whole_group_refinement` as labelled fields.

![Wicked Questions — session closed and combined results](docs/screenshots/wicked-q-session-closed.jpg)

**Markdown export preview**
The generated Markdown file follows the standard KwaCart export format: tool slug as the heading, session metadata, then each participant's responses as bold-labelled paragraphs.

![Wicked Questions — Markdown export](docs/screenshots/wicked-q-export-md.jpg)

---

## Collaborative Sessions

| Step | Who | What happens |
|---|---|---|
| Create | Host | Clicks **Start session** on a tool card → session created, shareable URL and QR code generated |
| Share | Host | Copies the URL or displays the QR code for participants to scan |
| Join | Participant | Opens URL, logs in if not already, sees the form |
| Respond | Everyone | Fills in the form, clicks **Save my response** (editable until session closes) |
| Monitor | Host | Sees participant list update live; a green tick appears next to anyone who has saved |
| Close | Host only | Clicks **Close session and reveal results** → all responses locked, exports generated |
| View | Everyone | Combined results page shows all contributions; host and participants can download MD/RTF |

**Access control:**

- Only logged-in users can join.
- Only the host can close a session.
- Downloads are restricted to the host and participants; anyone else gets a 404.
- The status polling endpoint returns 403 to non-participants.

---

## Archive & Exports

### Solo submissions
On submit, the pipeline generates two files per record:

- `archives/md/<date>_<slug>_<id>.md`
- `archives/rtf/<date>_<slug>_<id>.rtf`

Files are downloadable from the archive detail page.

### Combined session exports
When a session is closed, the pipeline generates two combined files:

- `archives/md/<date>_<slug>_session_<uuid>.md`
- `archives/rtf/<date>_<slug>_session_<uuid>.rtf`

Each file lists every participant's processed output in sequence. Download links appear at the top of the closed-session page.

### File storage — Cloudinary

In production, export files are stored on **Cloudinary** rather than the local server filesystem. This is necessary because Heroku uses an ephemeral filesystem — any file written locally is lost when the dyno restarts or sleeps. Cloudinary stores the files permanently and serves them via CDN.

The storage backend is configured in `config/settings/production.py` using Django's `STORAGES` dict:

```python
STORAGES = {
    'default': {'BACKEND': 'cloudinary_storage.storage.RawMediaCloudinaryStorage'},
    'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
}
```

The exporters write files using Django's `default_storage.save()` API, so they are storage-backend-agnostic. In local development, `default_storage` falls back to the local filesystem and no Cloudinary connection is required.

Files are uploaded as **raw assets** (stored exactly as-is, no transformation) and sit under:

```
archives/md/     ← Markdown exports
archives/rtf/    ← RTF exports
```

When a download is requested, Django streams the file directly from Cloudinary to the user's browser via `FileResponse`. Nothing is written to the Heroku dyno.

### Cloudinary MediaFlows automation

A **MediaFlows** workflow (`KwaCart-ArchiveTag`) runs automatically every time an export file is uploaded. It is triggered by the `asset uploaded` event scoped to `resource_type = raw` and `asset_folder starts_with archives`.

The workflow applies the following to each uploaded asset:

1. **Get Asset Information** — fetches the asset record from the Cloudinary Admin API, making `format`, `created_at`, and `public_id` available to downstream steps.
2. **Update Tags** — applies `session-export` and the file format (`md` or `rtf`) as searchable tags.
3. **Update Contextual Metadata** — writes three key/value pairs: `source_app = kwacart`, `export_format = md|rtf`, `export_date = <upload timestamp>`.

This means every export in the Cloudinary Media Library is filterable by tool, format, and date without querying the Django database.

---

## Data Models

The complete database contains **19 tables**: 6 application tables (owned by the KwaCart app code), 9 Django framework tables (managed by Django's core and contrib apps), and 4 third-party tables (managed by django-axes for brute-force protection). All three groups are documented below.

### SQL Table Name Reference

Django names every table `{app_label}_{model_name}` (lowercase). The mapping between model names used in this document and the physical SQL table names is:

| SQL table name | Model / source | Area |
|---|---|---|
| `accounts_user` | `User` | Application |
| `accounts_user_groups` | `User` ↔ `Group` M2M join | Application / Django auth |
| `accounts_user_user_permissions` | `User` ↔ `Permission` M2M join | Application / Django auth |
| `archive_toolsession` | `ToolSession` | Application |
| `archive_toolinstance` | `ToolInstance` | Application |
| `archive_auditlog` | `AuditLog` | Application |
| `archive_waitinglistentry` | `WaitingListEntry` | Application |
| `archive_featurerequest` | `FeatureRequest` | Application |
| `auth_group` | Django `Group` | Django auth |
| `auth_group_permissions` | `Group` ↔ `Permission` M2M join | Django auth |
| `auth_permission` | Django `Permission` | Django auth |
| `django_content_type` | Django `ContentType` | Django contrib |
| `django_admin_log` | Django admin action log | Django contrib |
| `django_migrations` | Migration history tracker | Django core |
| `django_session` | Server-side session store | Django contrib |
| `axes_accessattempt` | Axes login attempt aggregator | django-axes |
| `axes_accessattemptexpiration` | Axes attempt expiry record | django-axes |
| `axes_accessfailurelog` | Axes individual failure record | django-axes |
| `axes_accesslog` | Axes successful login/logout record | django-axes |

The ERD diagrams below cover the six application tables. Framework and third-party tables are described in the [Framework and Third-party Tables](#framework-and-third-party-tables) subsection.

---

**Cardinality key**

| Symbol | Meaning |
|---|---|
| `\|\|` | Exactly one — the FK on this end is mandatory (NOT NULL) |
| `\|o` | Zero or one — the FK on this end is optional (nullable) |
| `o{` | Zero or many |
| `\|{` | One or many |

**Attribute key:** `PK` = primary key · `FK` = foreign key · `UK` = unique constraint · All fields are `NOT NULL` unless the description explicitly states "NULLABLE".

---

### Diagram 1 — Core Session Model

`USER`, `TOOL_SESSION`, and `TOOL_INSTANCE` are the three tables that drive all facilitation activity. `TOOL_INSTANCE` acts as a rich bridge between users and sessions — see [Assumptions](#assumptions) below.

```mermaid
erDiagram
    USER {
        int id PK "auto-increment surrogate key"
        string email UK "NOT NULL · unique login identifier · max 254"
        string username "NULLABLE · max 150 · not used for login"
        string password "NOT NULL · PBKDF2-SHA256 hash"
        boolean is_staff "NOT NULL · default FALSE · grants admin access"
        boolean is_superuser "NOT NULL · default FALSE · full permission bypass"
        boolean is_active "NOT NULL · default TRUE · soft-delete flag"
        datetime date_joined "NOT NULL · auto on INSERT"
        datetime last_login "NULLABLE"
    }

    TOOL_SESSION {
        uuid id PK "NOT NULL · random UUID4 · used in share URLs"
        int host_id FK "NOT NULL · USER · CASCADE DELETE"
        string tool_slug "NOT NULL · registry key · max 100"
        string tool_version "NOT NULL · snapshot at creation · max 20"
        string status "NOT NULL · ENUM open|closed · default open"
        datetime created_at "NOT NULL · auto on INSERT"
        datetime closed_at "NULLABLE · set when host closes session"
        datetime timer_started_at "NULLABLE · set when host starts timer"
        datetime timer_paused_at "NULLABLE · cleared on resume or reset"
        float timer_elapsed_before_pause "NOT NULL · cumulative pause seconds · default 0"
        int pause_reminder_threshold_sec "NULLABLE · default 300 · NULL disables"
        boolean inclusive_pacing "NOT NULL · extended-time feature flag · default FALSE"
        int inclusive_pacing_multiplier "NOT NULL · ENUM 3 or 5 · default 3"
        boolean verbal_breakout_active "NOT NULL · breakout signal · default FALSE"
        uuid guest_token "NOT NULL · embedded in guest QR-code URL"
        string pairing_code "NOT NULL · 3-digit companion code · blank OK · indexed"
        string md_file "NULLABLE · Cloudinary path to combined export · max 500"
        string rtf_file "NULLABLE · Cloudinary path to combined export · max 500"
    }

    TOOL_INSTANCE {
        int id PK "auto-increment surrogate key"
        int user_id FK "NULLABLE · USER · CASCADE DELETE · NULL for guests"
        string guest_name "NOT NULL · blank OK · populated on guest join"
        uuid session_id FK "NULLABLE · TOOL_SESSION · CASCADE DELETE · NULL for solo"
        string tool_slug "NOT NULL · snapshot of tool at creation · max 100"
        string tool_version "NOT NULL · snapshot of version at creation · max 20"
        string status "NOT NULL · ENUM draft|archived · default draft"
        json payload_input "NOT NULL · raw form submission dict · default empty"
        json payload_output "NULLABLE · tool-processed result dict"
        string html_file "NULLABLE · Cloudinary path · max 500"
        string md_file "NULLABLE · Cloudinary path · max 500"
        string rtf_file "NULLABLE · Cloudinary path · max 500"
        json attachments "NOT NULL · multimedia list · default empty"
        datetime composing_heartbeat_at "NULLABLE · AAC composing heartbeat"
        datetime created_at "NOT NULL · auto on INSERT"
        datetime updated_at "NOT NULL · auto on every SAVE"
        datetime submitted_at "NULLABLE · set when status becomes archived"
    }

    USER ||--o{ TOOL_SESSION : "hosts"
    USER |o--o{ TOOL_INSTANCE : "owns"
    TOOL_SESSION |o--o{ TOOL_INSTANCE : "contains"
```

**Relationship notes**

| Relationship | Left cardinality | Right cardinality | Detail |
|---|---|---|---|
| USER → TOOL_SESSION | One user | Zero or many sessions | `host_id` is NOT NULL; deleting a user cascades to all their sessions |
| USER → TOOL_INSTANCE | Zero or one user | Zero or many instances | `user_id` is nullable — NULL identifies a guest participant |
| TOOL_SESSION → TOOL_INSTANCE | Zero or one session | Zero or many instances | `session_id` is nullable — NULL identifies a solo submission |

---

### Diagram 2 — Public Engagement

`WAITING_LIST_ENTRY` and `FEATURE_REQUEST` are standalone tables with no foreign keys to other tables and no relationship to each other. Both accept submissions without authentication; both are visible only via Django admin.

```mermaid
erDiagram
    WAITING_LIST_ENTRY {
        int id PK "auto-increment"
        string email UK "NOT NULL · unique · max 254"
        string name "NOT NULL · blank OK · optional · max 200"
        datetime signed_up_at "NOT NULL · auto on INSERT"
    }

    FEATURE_REQUEST {
        int id PK "auto-increment"
        string name "NOT NULL · blank OK · optional · max 200"
        string email "NOT NULL · blank OK · optional · max 254"
        string title "NOT NULL · short summary · max 300"
        text description "NOT NULL · free text"
        datetime submitted_at "NOT NULL · auto on INSERT"
    }
```

---

### Diagram 3 — Audit Trail

`AUDIT_LOG` records security-relevant events. The foreign key to `USER` uses `SET NULL` on delete so that log entries survive account removal, preserving a complete security history.

```mermaid
erDiagram
    USER {
        int id PK
        string email UK "unique login identifier"
    }

    AUDIT_LOG {
        int id PK "auto-increment"
        int user_id FK "NULLABLE · USER · SET NULL on delete"
        string action "NOT NULL · ENUM login|submit|download|access_denied"
        string resource_id "NULLABLE · ID of the affected object · max 100"
        string ip_address "NULLABLE · IPv4 or IPv6 · max 45 chars"
        datetime timestamp "NOT NULL · auto on INSERT"
        json metadata "NOT NULL · additional context dict · default empty"
    }

    USER |o--o{ AUDIT_LOG : "generates"
```

**Relationship note:** `user_id` is nullable (`SET NULL`) rather than `CASCADE DELETE` so that audit records are never silently removed when a user account is deleted. A NULL `user_id` in an audit row means the originating account no longer exists.

---

### Attribute Glossary

The following text descriptions supplement the ERD diagrams. Each attribute is listed with its Django field type, SQL equivalent, and business meaning.

#### USER

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `AutoField` (inherited) | `INT NOT NULL PK` | Auto-increment surrogate primary key |
| `email` | `EmailField(unique=True)` | `VARCHAR(254) NOT NULL UNIQUE` | Unique login identifier; replaces Django's default username |
| `username` | `CharField(max_length=150, null=True, blank=True)` | `VARCHAR(150) NULL` | Retained from `AbstractUser` but unused for authentication; may be empty or NULL |
| `first_name` | `CharField(max_length=150)` (inherited) | `VARCHAR(150) NOT NULL DEFAULT ''` | Inherited from `AbstractUser`; not collected or displayed by KwaCart; always an empty string in practice |
| `last_name` | `CharField(max_length=150)` (inherited) | `VARCHAR(150) NOT NULL DEFAULT ''` | Inherited from `AbstractUser`; not collected or displayed by KwaCart; always an empty string in practice |
| `password` | `CharField` (inherited) | `VARCHAR(128) NOT NULL` | PBKDF2-SHA256 hashed credential; never stored as plaintext |
| `is_staff` | `BooleanField(default=False)` | `BOOLEAN NOT NULL DEFAULT FALSE` | Grants access to Django admin site and staff-only views |
| `is_superuser` | `BooleanField(default=False)` | `BOOLEAN NOT NULL DEFAULT FALSE` | Bypasses all permission checks |
| `is_active` | `BooleanField(default=True)` | `BOOLEAN NOT NULL DEFAULT TRUE` | Soft-delete flag; inactive users cannot log in |
| `date_joined` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically when the account is created |
| `last_login` | `DateTimeField(null=True)` | `DATETIME NULL` | Updated by Django's auth framework on each successful login |

#### TOOL_SESSION

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `UUIDField(primary_key=True, default=uuid4)` | `UUID NOT NULL PK` | Random UUID4; used directly in share URLs so IDs are unguessable |
| `host_id` | `ForeignKey(User, CASCADE)` | `INT NOT NULL FK → USER` | The authenticated user who created and controls the session |
| `tool_slug` | `CharField(max_length=100)` | `VARCHAR(100) NOT NULL` | Registry key identifying which facilitation tool the session runs |
| `tool_version` | `CharField(max_length=20)` | `VARCHAR(20) NOT NULL` | Snapshot of the tool's version string at session creation; allows future tool changes without corrupting existing sessions |
| `status` | `CharField(max_length=10, choices=…, default='open')` | `VARCHAR(10) NOT NULL` | Two-state lifecycle: `open` (accepting responses) or `closed` (locked) |
| `created_at` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically on INSERT |
| `closed_at` | `DateTimeField(null=True)` | `DATETIME NULL` | Set when the host calls session close; NULL while the session is open |
| `timer_started_at` | `DateTimeField(null=True)` | `DATETIME NULL` | Server timestamp when the countdown timer was last started; NULL until first start |
| `timer_paused_at` | `DateTimeField(null=True)` | `DATETIME NULL` | Set when host pauses timer; cleared on resume or reset; NULL while running |
| `timer_elapsed_before_pause` | `FloatField(default=0)` | `FLOAT NOT NULL DEFAULT 0` | Cumulative seconds elapsed across all pauses; allows accurate remaining-time calculation |
| `pause_reminder_threshold_sec` | `IntegerField(null=True, default=300)` | `INT NULL DEFAULT 300` | Seconds of pause before a visual reminder appears to the host; NULL disables the reminder |
| `inclusive_pacing` | `BooleanField(default=False)` | `BOOLEAN NOT NULL DEFAULT FALSE` | Enables the Inclusive Pacing feature so AAC participants receive a longer personal timer |
| `inclusive_pacing_multiplier` | `IntegerField(default=3, choices=[(3,…),(5,…)])` | `INT NOT NULL DEFAULT 3` | Time multiplier offered under Inclusive Pacing; constrained to 3 or 5 |
| `verbal_breakout_active` | `BooleanField(default=False)` | `BOOLEAN NOT NULL DEFAULT FALSE` | Signals that the group has moved to verbal discussion while AAC participants continue composing |
| `guest_token` | `UUIDField(default=uuid4)` | `UUID NOT NULL` | Random UUID embedded in the guest QR-code URL; possession of this token grants guest access |
| `pairing_code` | `CharField(max_length=3, blank=True, db_index=True)` | `VARCHAR(3) NOT NULL DEFAULT '' INDEXED` | Three-digit companion-pairing code displayed alongside the QR code; cleared to empty string on session close |
| `md_file` | `FileField(null=True)` | `VARCHAR(500) NULL` | Cloudinary storage path for the combined Markdown export; NULL until the session is closed and the export is generated |
| `rtf_file` | `FileField(null=True)` | `VARCHAR(500) NULL` | Cloudinary storage path for the combined RTF export; same lifecycle as `md_file` |

#### TOOL_INSTANCE

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `AutoField` | `INT NOT NULL PK` | Auto-increment surrogate primary key |
| `user_id` | `ForeignKey(User, CASCADE, null=True)` | `INT NULL FK → USER` | The authenticated user who owns this instance; NULL for guest participants |
| `guest_name` | `CharField(max_length=100, blank=True)` | `VARCHAR(100) NOT NULL DEFAULT ''` | Display name entered by a guest on the join page; empty string for authenticated users |
| `session_id` | `ForeignKey(ToolSession, CASCADE, null=True)` | `UUID NULL FK → TOOL_SESSION` | The session this instance belongs to; NULL for solo (non-collaborative) submissions |
| `tool_slug` | `CharField(max_length=100)` | `VARCHAR(100) NOT NULL` | Snapshot of the tool identifier at the time this instance was created |
| `tool_version` | `CharField(max_length=20)` | `VARCHAR(20) NOT NULL` | Snapshot of the tool version at creation |
| `status` | `CharField(max_length=10, choices=…, default='draft')` | `VARCHAR(10) NOT NULL DEFAULT 'draft'` | Lifecycle state: `draft` (in progress) or `archived` (submitted and locked) |
| `payload_input` | `JSONField(default=dict)` | `JSON NOT NULL DEFAULT '{}'` | Raw dictionary of the user's form field submissions; used as input to the tool's processing logic |
| `payload_output` | `JSONField(null=True)` | `JSON NULL` | Tool-processed result dictionary; NULL until the instance is archived |
| `html_file` | `FileField(null=True)` | `VARCHAR(500) NULL` | Cloudinary path for the individual HTML export |
| `md_file` | `FileField(null=True)` | `VARCHAR(500) NULL` | Cloudinary path for the individual Markdown export |
| `rtf_file` | `FileField(null=True)` | `VARCHAR(500) NULL` | Cloudinary path for the individual RTF export |
| `attachments` | `JSONField(default=list)` | `JSON NOT NULL DEFAULT '[]'` | List of multimedia attachment objects (audio clips, symbol-board images); each object carries `type`, `url`, `public_id`, and `name` |
| `composing_heartbeat_at` | `DateTimeField(null=True)` | `DATETIME NULL` | Timestamp updated every ~8 seconds by the AAC composing heartbeat; treated as active while within the last 15 seconds |
| `created_at` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically on INSERT |
| `updated_at` | `DateTimeField(auto_now=True)` | `DATETIME NOT NULL` | Updated automatically on every SAVE |
| `submitted_at` | `DateTimeField(null=True)` | `DATETIME NULL` | Set when the instance transitions from `draft` to `archived` |

#### WAITING_LIST_ENTRY

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `AutoField` | `INT NOT NULL PK` | Auto-increment surrogate primary key |
| `email` | `EmailField(unique=True)` | `VARCHAR(254) NOT NULL UNIQUE` | Visitor's email address; uniqueness prevents duplicate sign-ups |
| `name` | `CharField(max_length=200, blank=True)` | `VARCHAR(200) NOT NULL DEFAULT ''` | Optional display name; empty string if visitor did not provide one |
| `signed_up_at` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically on INSERT |

#### FEATURE_REQUEST

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `AutoField` | `INT NOT NULL PK` | Auto-increment surrogate primary key |
| `name` | `CharField(max_length=200, blank=True)` | `VARCHAR(200) NOT NULL DEFAULT ''` | Optional submitter name; empty string if not provided |
| `email` | `EmailField(blank=True)` | `VARCHAR(254) NOT NULL DEFAULT ''` | Optional contact email; empty string if not provided (no `null=True` — Django stores empty string, not NULL) |
| `title` | `CharField(max_length=300)` | `VARCHAR(300) NOT NULL` | Short one-line summary of the requested feature |
| `description` | `TextField()` | `TEXT NOT NULL` | Full description: problem statement and proposed solution |
| `submitted_at` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically on INSERT |

#### AUDIT_LOG

| Attribute | Django field | SQL type | Description |
|---|---|---|---|
| `id` | `AutoField` | `INT NOT NULL PK` | Auto-increment surrogate primary key |
| `user_id` | `ForeignKey(User, SET_NULL, null=True)` | `INT NULL FK → USER` | The user who performed the action; SET NULL on user deletion so the log entry is preserved |
| `action` | `CharField(max_length=20, choices=…)` | `VARCHAR(20) NOT NULL` | Event type: `login`, `submit`, `download`, or `access_denied` |
| `resource_id` | `CharField(max_length=100, null=True)` | `VARCHAR(100) NULL` | Primary key or identifier of the object the action touched; NULL when not applicable |
| `ip_address` | `GenericIPAddressField(null=True)` | `VARCHAR(45) NULL` | Client IP address (IPv4 or IPv6); NULL if not captured |
| `timestamp` | `DateTimeField(auto_now_add=True)` | `DATETIME NOT NULL` | Set automatically on INSERT; rows are never updated |
| `metadata` | `JSONField(default=dict)` | `JSON NOT NULL DEFAULT '{}'` | Additional free-form context (e.g. browser user-agent, session ID, error detail) |

---

### System Constraints

| Constraint | Table | Definition | Purpose |
|---|---|---|---|
| `UNIQUE (email)` | `USER` | `ALTER TABLE user ADD UNIQUE (email)` | Enforces email as the sole login identifier; prevents duplicate accounts |
| `UNIQUE (email)` | `WAITING_LIST_ENTRY` | `ALTER TABLE waiting_list_entry ADD UNIQUE (email)` | Prevents a visitor from signing up to the waiting list more than once |
| `UNIQUE (session_id, user_id) WHERE session_id IS NOT NULL` | `TOOL_INSTANCE` | Partial unique index | Prevents a registered user from having more than one response per collaborative session; does not apply to solo submissions (`session_id IS NULL`) or guest rows (`user_id IS NULL`) |
| `CASCADE DELETE` on `TOOL_SESSION.host_id` | `TOOL_SESSION` | `ON DELETE CASCADE` | Deleting a user removes all their hosted sessions, which in turn cascades to all instances within those sessions |
| `CASCADE DELETE` on `TOOL_INSTANCE.user_id` | `TOOL_INSTANCE` | `ON DELETE CASCADE` | Deleting a user removes their solo and session instance records |
| `CASCADE DELETE` on `TOOL_INSTANCE.session_id` | `TOOL_INSTANCE` | `ON DELETE CASCADE` | Closing and then deleting a session removes all participant instances |
| `SET NULL` on `AUDIT_LOG.user_id` | `AUDIT_LOG` | `ON DELETE SET NULL` | Preserves audit records after user deletion; `user_id` becomes NULL |
| `inclusive_pacing_multiplier IN (3, 5)` | `TOOL_SESSION` | Django-level choices | Constrains the time multiplier to the two values the UI exposes; enforced in Django form validation rather than a DB check constraint |
| `status IN ('open', 'closed')` | `TOOL_SESSION` | Django-level choices | Session lifecycle is binary; only these two values are valid |
| `status IN ('draft', 'archived')` | `TOOL_INSTANCE` | Django-level choices | Instance lifecycle is one-directional: `draft` → `archived`; never reversed |
| `action IN ('login','submit','download','access_denied')` | `AUDIT_LOG` | Django-level choices | Constrains the event vocabulary to four defined action types |

---

### Assumptions

#### `TOOL_INSTANCE` as a rich bridge table

`TOOL_INSTANCE` resolves what would otherwise be a many-to-many relationship between `USER` and `TOOL_SESSION`:

- A user can participate in many sessions; a session can have many user participants.
- Rather than a thin join table (just two foreign keys), `TOOL_INSTANCE` carries the full payload — `payload_input`, `payload_output`, export files, attachments, and lifecycle state — making it a **rich association** in Domain-Driven Design terms.

The table deviates from a classical bridge table in two important ways:

1. **Both foreign keys are nullable.** `user_id = NULL` denotes a guest participant (no account). `session_id = NULL` denotes a solo submission (no collaborative session). This means the table covers three distinct use cases in a single model:

   | `user_id` | `session_id` | Meaning |
   |---|---|---|
   | NOT NULL | NULL | Solo submission by a registered user |
   | NOT NULL | NOT NULL | Session contribution by a registered user |
   | NULL | NOT NULL | Session contribution by an unregistered guest |

2. **The uniqueness constraint is partial.** `UNIQUE (session_id, user_id) WHERE session_id IS NOT NULL` prevents duplicate session contributions from the same registered user but deliberately excludes solo rows and guest rows (where `user_id` is NULL) from the constraint.

#### Guest authentication via `guest_token` and `guest_instance_id`

Guest participants are not stored as `USER` rows. Instead:

- The `TOOL_SESSION.guest_token` UUID is embedded in the QR-code URL. Possession of the URL grants access to the guest join flow.
- After a guest enters their name, a `TOOL_INSTANCE` row is created with `user_id = NULL` and `guest_name` set. The new instance's `id` is stored in the guest's browser session under the key `guest_instance_{session_id}`.
- Subsequent requests (polls, buffer saves) authenticate the guest by reading this key from their browser session and verifying the referenced `TOOL_INSTANCE` exists and belongs to the correct session. This is a session-cookie-based token, not a database foreign key.

#### Companion pairing code

`TOOL_SESSION.pairing_code` is a three-digit string (e.g. `"042"`) generated at session creation and cleared to an empty string (`""`) when the session closes. It is a convenience alias — not a security credential — for locating the guest QR-code URL on a companion device without typing a full UUID URL. Security relies entirely on the `guest_token` UUID.

#### Export files (`md_file`, `rtf_file`, `html_file`)

All three export file fields store Cloudinary storage paths (or relative local paths in development), not the file content itself. The actual files live on Cloudinary (production) or the local `media/` directory (development). In production, Django's `DEFAULT_FILE_STORAGE` backend is `django-cloudinary-storage`, so the path stored in the database is a Cloudinary public ID.

---

### Framework and Third-party Tables

These tables are created and managed by Django's built-in apps and the django-axes package. KwaCart does not define models for them directly; they are described here so that the full database schema is accounted for.

---

#### Django authentication tables

##### `auth_permission`

Stores every permission code that Django's permission system can reference. Populated automatically via migrations whenever a new model is created.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `name` | `VARCHAR(255) NOT NULL` | Human-readable label (e.g. "Can add tool session") |
| `content_type_id` | `INT NOT NULL FK → django_content_type` | Links the permission to a specific model |
| `codename` | `VARCHAR(100) NOT NULL` | Machine name (e.g. `add_toolsession`) |

**Unique constraint:** `(content_type_id, codename)`

##### `auth_group`

Named collections of permissions that can be assigned to users en masse. Not used actively in KwaCart but present as part of Django's auth framework.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `name` | `VARCHAR(150) NOT NULL UNIQUE` | Group name (e.g. "Facilitators") |

##### `auth_group_permissions`

Many-to-many join table between `auth_group` and `auth_permission`.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `group_id` | `INT NOT NULL FK → auth_group` | |
| `permission_id` | `INT NOT NULL FK → auth_permission` | |

**Unique constraint:** `(group_id, permission_id)`

##### `accounts_user_groups`

Many-to-many join table between `accounts_user` and `auth_group`. Allows a user to belong to one or more permission groups.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `user_id` | `INT NOT NULL FK → accounts_user` | |
| `group_id` | `INT NOT NULL FK → auth_group` | |

**Unique constraint:** `(user_id, group_id)`

##### `accounts_user_user_permissions`

Many-to-many join table that grants individual permissions directly to a user, bypassing group membership.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `user_id` | `INT NOT NULL FK → accounts_user` | |
| `permission_id` | `INT NOT NULL FK → auth_permission` | |

**Unique constraint:** `(user_id, permission_id)`

---

#### Django contrib tables

##### `django_content_type`

Tracks every installed model as a `(app_label, model)` pair. Used by the permission system and the admin log to create generic foreign keys without hard-coded table names.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `app_label` | `VARCHAR(100) NOT NULL` | App name (e.g. `archive`) |
| `model` | `VARCHAR(100) NOT NULL` | Model name in lowercase (e.g. `toolsession`) |

**Unique constraint:** `(app_label, model)`

##### `django_admin_log`

Records every create, update, and delete action performed through the Django admin interface.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `action_time` | `DATETIME NOT NULL` | When the action occurred |
| `user_id` | `INT NOT NULL FK → accounts_user` | Staff user who performed the action |
| `content_type_id` | `INT NULL FK → django_content_type` | Which model was affected |
| `object_id` | `TEXT NULL` | Primary key of the affected object |
| `object_repr` | `VARCHAR(200) NOT NULL` | String representation of the object at action time |
| `action_flag` | `SMALLINT NOT NULL` | 1 = Addition · 2 = Change · 3 = Deletion |
| `change_message` | `TEXT NOT NULL` | JSON description of what changed |

##### `django_migrations`

Tracks which migrations have been applied to the database. Django reads this table before running `migrate` to determine what work remains.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `app` | `VARCHAR(255) NOT NULL` | App label (e.g. `archive`) |
| `name` | `VARCHAR(255) NOT NULL` | Migration filename without `.py` (e.g. `0015_toolsession_verbal_breakout`) |
| `applied` | `DATETIME NOT NULL` | When the migration was applied |

##### `django_session`

Server-side session storage. Each row is one browser session, keyed by the session cookie value. Django's session middleware reads and writes this table on every authenticated request.

| Column | SQL type | Description |
|---|---|---|
| `session_key` | `VARCHAR(40) NOT NULL PK` | The value stored in the browser's `sessionid` cookie |
| `session_data` | `TEXT NOT NULL` | Base64-encoded, signed, pickled session dictionary |
| `expire_date` | `DATETIME NOT NULL` | Session expiry; rows past this date are inactive and purged by `clearsessions` |

---

#### django-axes tables

[django-axes](https://django-axes.readthedocs.io/) provides brute-force login protection. It records every login attempt and locks out IP addresses or usernames that exceed the configured failure threshold. KwaCart uses axes to protect the `/accounts/login/` endpoint.

##### `axes_accessattempt`

Aggregated record of login failures per `(username, ip_address, user_agent)` combination. The `failures_since_start` counter is incremented on each failure; when it reaches the lockout threshold the account or IP is blocked.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `user_agent` | `VARCHAR(255) NOT NULL` | Browser user-agent string |
| `ip_address` | `VARCHAR(39) NULL` | Client IP (IPv4 or IPv6) |
| `username` | `VARCHAR(255) NULL` | Email address attempted |
| `http_accept` | `VARCHAR(1025) NOT NULL` | `Accept` header value |
| `path_info` | `VARCHAR(255) NOT NULL` | URL path of the login endpoint |
| `attempt_time` | `DATETIME NOT NULL` | Timestamp of the first failure in this attempt group |
| `get_data` | `TEXT NOT NULL` | Captured GET parameters |
| `post_data` | `TEXT NOT NULL` | Captured POST parameters (credentials are masked) |
| `failures_since_start` | `INT NOT NULL` | Running count of failures for this combination |

**Unique constraint:** `(username, ip_address, user_agent)`

##### `axes_accessattemptexpiration`

One-to-one extension of `axes_accessattempt` that records when a locked-out attempt should automatically expire.

| Column | SQL type | Description |
|---|---|---|
| `access_attempt_id` | `INT NOT NULL PK FK → axes_accessattempt` | One-to-one link |
| `expires_at` | `DATETIME NOT NULL` | When the lockout expires and the attempt counter resets |

##### `axes_accessfailurelog`

Append-only log of every individual login failure. Unlike `axes_accessattempt` (which aggregates), each row here is one failed request.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `user_agent` | `VARCHAR(255) NOT NULL` | Browser user-agent string |
| `ip_address` | `VARCHAR(39) NULL` | Client IP |
| `username` | `VARCHAR(255) NULL` | Email address attempted |
| `http_accept` | `VARCHAR(1025) NOT NULL` | `Accept` header value |
| `path_info` | `VARCHAR(255) NOT NULL` | URL path |
| `attempt_time` | `DATETIME NOT NULL` | Timestamp of this specific failure |
| `locked_out` | `BOOLEAN NOT NULL` | TRUE if this failure triggered a lockout |

##### `axes_accesslog`

Records every **successful** login and logout event. Used to compute the session duration and to detect anomalous login patterns.

| Column | SQL type | Description |
|---|---|---|
| `id` | `INT NOT NULL PK` | Auto-increment |
| `user_agent` | `VARCHAR(255) NOT NULL` | Browser user-agent string |
| `ip_address` | `VARCHAR(39) NULL` | Client IP |
| `username` | `VARCHAR(255) NULL` | Email address that logged in |
| `http_accept` | `VARCHAR(1025) NOT NULL` | `Accept` header value |
| `path_info` | `VARCHAR(255) NOT NULL` | URL path of the login endpoint |
| `attempt_time` | `DATETIME NOT NULL` | When the user logged in |
| `logout_time` | `DATETIME NULL` | When the user logged out; NULL if still active |
| `session_hash` | `VARCHAR(64) NOT NULL` | Hash of the Django session key for this login |

---

## User Accounts

Authentication is email-based (no username). The custom `User` model uses `email` as `USERNAME_FIELD`. Django's built-in password validators are enforced at the model layer via `validate_password()`.

| URL | Purpose |
|---|---|
| `/accounts/login/` | Log in |
| `/accounts/register/` | Create an account |
| `/accounts/logout/` | Log out (redirects to login) |
| `/archive/dashboard/` | Personal archive + session list |
| `/tools/` | Tool catalog |

---

## Running Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Apply migrations
python manage.py migrate

# 3. Create a superuser
python manage.py createsuperuser

# 4. Start the development server
python manage.py runserver 0.0.0.0:5000
```

The app will be available at `http://localhost:5000`.

**Environment:** The project reads settings from `config.settings.local` by default (`DJANGO_SETTINGS_MODULE` is set in `manage.py`). No `.env` file is required for local development — `ALLOWED_HOSTS` falls back to `localhost` / `127.0.0.1` when the `REPLIT_DOMAINS` environment variable is absent.

---

## Deployment

KwaCart is deployed as a production web application so that facilitators, participants, and community groups can use it reliably from any device — without needing to install software or manage infrastructure. The hosted version is the primary way vulnerable, at-risk, and in-need communities access the platform, making a stable, accessible deployment directly tied to the platform's core mission of widening participation in Liberating Structures.

The production stack is:

| Component | Technology | Role |
|---|---|---|
| Application server | Gunicorn 25.x | Runs the Django WSGI application |
| Web framework | Django 6.0.4 | Handles routing, authentication, sessions, and ORM |
| Database | PostgreSQL (Heroku Postgres) | Stores all user, session, and archive data |
| Static files | WhiteNoise | Serves CSS, JS, and fonts directly from Gunicorn — no separate CDN needed |
| Media and exports | Cloudinary | Stores user-generated export files (HTML, Markdown, RTF) outside the dyno filesystem |
| Hosting platform | Heroku | Manages the dyno lifecycle, config vars, add-ons, and TLS |

---

### Heroku

The project is fully configured for Heroku deployment. The files Heroku requires are already in the repository:

| File | Purpose |
|---|---|
| `Procfile` | Declares the `web` process (Gunicorn) and the `release` process (runs `migrate` on every deploy) |
| `runtime.txt` | Pins the Python version to `python-3.12.12` |
| `requirements.txt` | All dependencies with exact version pins |
| `config/settings/production.py` | Production settings — reads all secrets from environment variables |

**Step-by-step deployment**

1. Create a new Heroku app from the [Heroku dashboard](https://dashboard.heroku.com/) or with the CLI:
   ```
   heroku create your-app-name
   ```

2. Add the Heroku Postgres add-on (this automatically sets `DATABASE_URL`):
   ```
   heroku addons:create heroku-postgresql:essential-0
   ```

3. Set the required config vars (replace the placeholder values):
   ```
   heroku config:set DJANGO_SETTINGS_MODULE=config.settings.production
   heroku config:set SECRET_KEY='<a long random string — never reuse the dev key>'
   heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
   heroku config:set CSRF_TRUSTED_ORIGINS='https://your-app-name.herokuapp.com'
   heroku config:set CLOUDINARY_URL='cloudinary://<api_key>:<api_secret>@<cloud_name>'
   ```

4. Push the code to Heroku:
   ```
   git push heroku main
   ```
   Heroku will automatically:
   - Install dependencies from `requirements.txt`
   - Run `python manage.py collectstatic --noinput` (WhiteNoise serves the result)
   - Run `python manage.py migrate --noinput` (the `release` process in `Procfile`)
   - Start Gunicorn via the `web` process

5. Create a superuser so you can access `/admin/`:
   ```
   heroku run python manage.py createsuperuser
   ```

**Required config vars summary**

| Variable | Value |
|---|---|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` |
| `SECRET_KEY` | A strong random string (50+ characters) |
| `ALLOWED_HOSTS` | `your-app-name.herokuapp.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app-name.herokuapp.com` |
| `DATABASE_URL` | Set automatically by the Heroku Postgres add-on |
| `CLOUDINARY_URL` | From Cloudinary dashboard → API Environment variable (format: `cloudinary://key:secret@cloud`) |

---

### Replit

The project also runs on Replit with `config.settings.local` (set in `manage.py`). Static files are served by WhiteNoise and the dev server runs on port 5000:

```
gunicorn --bind=0.0.0.0:5000 --reuse-port config.wsgi:application
```

`python manage.py migrate` and `python manage.py collectstatic` run as build steps before the server starts. SSL termination is handled by the Replit proxy; `SECURE_PROXY_SSL_HEADER` is set correctly in `production.py` for when `config.settings.production` is active there.

---

## Security

### 1 — Secrets and environment variables

All sensitive values are read from environment variables at runtime and are **never hard-coded in the source tree**:

| Secret | Where it lives | How it is read |
|---|---|---|
| `SECRET_KEY` | Replit environment secret | `os.environ.get('SECRET_KEY', '')` in `config/settings/production.py`; a deliberately broken-looking dev-only fallback is used in `base.py` so it can never be mistaken for a real key |
| `ALLOWED_HOSTS` | `ALLOWED_HOSTS` env var (production) | Parsed from a comma-separated string in `config/settings/production.py` |
| `CSRF_TRUSTED_ORIGINS` | `CSRF_TRUSTED_ORIGINS` env var | Same pattern — exact domain list, never a wildcard |

The following files are listed in `.gitignore` and are **never committed to the repository**:

| Entry | What it covers |
|---|---|
| `.env` | Any local environment file |
| `db.sqlite3` | Development database (contains all user data) |
| `media/` | User-uploaded and generated export files |
| `staticfiles/` | Build output from `collectstatic` |
| `*.log` | Server and application logs |
| `local_settings.py` | Any developer-local settings override |

### 2 — Login protection

Every route that accesses or modifies user data is guarded before the view body runs:

| Mechanism | Applied to |
|---|---|
| `@login_required` decorator | `tool_catalog`, `draft_editor`, `autosave_endpoint`, `submit_tool`, `session_create`, `session_detail`, `session_close`, `session_status`, `timer_start`, `timer_pause`, `timer_reset`, `session_set_pause_reminder`, `archive_record_delete`, `secure_download`, `secure_session_download` |
| `LoginRequiredMixin` on CBVs | `ArchiveDashboardView`, `ArchiveDetailView` |
| `redirect_authenticated_user = True` | `UserLoginView` — already-logged-in users are redirected away from the login page |

Public routes (landing page, about, free try-it tools, waiting list, feature request, login, register) carry no login requirement by design. Guest session participants authenticate via a URL-embedded `guest_token` UUID rather than a Django account; the `session_status` poll endpoint validates the `guest_instance_id` stored in the browser session and returns `403` if it is absent or invalid.

### 3 — Ownership and object-level permissions

Authenticated users can only access and modify their own data. Every view that retrieves a user-owned object passes `user=request.user` (or `host=request.user`) directly to `get_object_or_404`, so a crafted URL that substitutes another user's primary key receives a `404` — not a `403`, which would confirm the record exists:

| View | Ownership guard |
|---|---|
| `draft_editor` | `get_object_or_404(ToolInstance, id=instance_id, user=request.user, status='draft', session__isnull=True)` |
| `submit_tool` | Same constraint — also enforces `session__isnull=True` so session contributions cannot be submitted via the solo endpoint |
| `ArchiveDetailView` | `get_queryset()` returns `ToolInstance.objects.filter(user=self.request.user)` |
| `archive_record_delete` | `get_object_or_404(ToolInstance, pk=pk, user=request.user)` |
| `secure_download` | `get_object_or_404(ToolInstance, id=instance_id, user=request.user)` |
| `secure_session_download` | `Q(host=request.user) \| Q(instances__user=request.user)` — host or participant only |
| `session_close`, `timer_start/pause/reset`, `session_set_pause_reminder` | `get_object_or_404(ToolSession, id=session_id, host=request.user)` — host only |
| `session_status` poll | Explicit `is_host or is_participant` check → `403` for non-participants |

**Staff-only content:** the waiting-list table in the archive dashboard is rendered only when `user.is_staff` is `True`; the Django admin (`/admin/`) requires `is_staff` via Django's built-in admin authentication.

**Download file-type whitelist:** `views_downloads.py` validates `file_type` against `VALID_FILE_TYPES = {'md', 'rtf', 'html'}` before calling `getattr(instance, f'{file_type}_file')`, preventing arbitrary attribute access via a crafted URL.

**Additional hardening measures**

| Measure | Detail |
|---|---|
| CSRF protection | Django's `CsrfViewMiddleware` is active; all state-changing POST forms include `{% raw %}{% csrf_token %}{% endraw %}` |
| Password validation | `validate_password()` called in `UserManager.create_user()` before `set_password()` |
| Secure cookies (production) | `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True` |
| HSTS (production) | `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`, `SECURE_HSTS_PRELOAD = True` |
| Gunicorn | Pinned to ≥ 23.0.0 (addresses HTTP request-smuggling CVEs in 21.x) |
| Canvas file hashing | SHA-256 content-addressable PNG filenames prevent path traversal in `media/drawings/` |
| Audit log | Login events, tool submissions, and file downloads are recorded with IP address and timestamp in `AuditLog` |

---

## Admin

The Django admin at `/admin/` provides full CRUD for:

- `ToolSession` — view and manage collaborative sessions.
- `ToolInstance` — view individual submissions.
- `AuditLog` — read-only activity trail.
- `WaitingListEntry` — view and export waiting-list signups.
- `FeatureRequest` — view submitted feature ideas (staff only).
- `User` — manage accounts and permissions.

Default superuser credentials (development only):
- Email: `admin@example.com`
- Password: `admin12345`

---

## Adding a New Tool

1. **Create a form** in `tools/forms.py` — one `forms.Form` subclass with the fields you need.

2. **Create an implementation** in `tools/implementations.py` — subclass `BaseTool`, implement `validate()` and `process()`. `process()` must return a dict.

3. **Register the tool** in `tools/registry.py` — add an entry to `TOOL_CATALOG`:

```python
'my-tool-slug': {
    'class': 'tools.implementations.MyTool',
    'form_class': 'tools.forms.MyToolForm',
    'title': 'My Tool',
    'tagline': 'One punchy sentence shown on the catalog card.',
    'category': 'Facilitation',
    'what': 'Physical setup description.',
    'how': 'Step-by-step instructions.',
    'why': 'Facilitation rationale.',
    'agreements': ['Ground rule one.'],   # optional
    'example_input': {'field': 'value'},  # optional — powers Load example data
    'display_fields': ['field', 'word_count'],
    'timer_seconds': 300,                 # optional — session countdown timer
    'try_timer_seconds': 60,              # optional — solo try-it page timer
    'try_timer_label': 'Reflect alone',   # optional — label shown on try-it timer
    'show_canvas': False,                 # optional — enable freehand drawing canvas
},
```

No URL changes, migrations, or template changes are needed — the catalog, draft editor, and session pages pick up new tools automatically. To expose a tool on a public free try-it page, add its slug to `FREE_TOOL_SLUGS` in `tools/views.py`.

---

## Validation

All HTML, CSS, JavaScript, and Python source code has been validated and is free of errors.

---

### HTML — W3C Nu Html Checker

Every public page was checked against the [W3C Nu Html Checker](https://validator.w3.org/nu/). All pages return **"Document checking completed. No errors or warnings to show."**

| Page | URL checked | Result |
|---|---|---|
| Landing | `/` | No errors |
| About | `/about/` | No errors |
| Log in | `/accounts/login/` | No errors |
| Register | `/accounts/signup/` | No errors |

**Landing page (no errors):**

![W3C HTML validation — landing page](docs/validation/html_landing.png)

**About page (no errors):**

![W3C HTML validation — about page](docs/validation/html_about.png)

**Register page (no errors):**

![W3C HTML validation — register page](docs/validation/html_signup.png)

---

### CSS — W3C Jigsaw CSS Validator

The shared stylesheet `static/css/base.css` was validated against the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) at **CSS level 3 + SVG**. Result: **"Congratulations! No Error Found."**

![W3C CSS validation — base.css](docs/validation/css_base.png)

---

### JavaScript — JSHint

All 11 JavaScript files in `static/js/` were checked using **JSHint 2.13.6** with the configuration below. The result is **0 errors** across all files.

```json
{
  "browser": true,
  "esversion": 11,
  "globals": { "getCookie": true, "QRCode": true }
}
```

Files checked (all pass with 0 errors):

| File | Notes |
|---|---|
| `autosave.js` | — |
| `canvas_tool.js` | — |
| `drawing_canvas.js` | — |
| `qr_display.js` | — |
| `session_control.js` | — |
| `session_poll.js` | `laxbreak: true` for multi-line ternaries |
| `timer.js` | `/* jshint esversion:11, laxbreak:true, shadow:true, -W082, -W058 */` inline directive |
| `tool_try_timer.js` | `laxbreak: true` for multi-line ternaries |
| `waiting_list.js` | — |
| `feature_request.js` | — |
| `signup.js` | — |

![JSHint validator](docs/validation/js_jshint.png)

---

### Python — PEP 8 (flake8)

All Python source files were linted with **flake8** at `--max-line-length=119`. The result is **0 errors** across the full codebase.

Command run:

```bash
python -m flake8 accounts/ archive/ tools/ exporters/ config/ \
    --max-line-length=119 --exclude=__pycache__,migrations --count
```

Output:

```
0
```

Issues resolved during this pass:

| Category | File(s) | Fix applied |
|---|---|---|
| `F401` unused imports | `accounts/forms.py`, `tools/interface.py`, `archive/views.py` | Removed unused imports |
| `E302` expected 2 blank lines | `accounts/signals.py`, `tools/utils.py` | Added missing blank lines |
| `W605` invalid escape sequence | `exporters/rtf_gen.py` | Changed string literals to raw strings (`r"..."`) |
| `E501` line too long | `tools/implementations.py`, `tools/registry.py`, `tools/urls.py` | Rewrapped lines within 119-char limit |
| `F405` may be from star import | `config/settings/production.py` | Added `# noqa: F401,F403` where star import is intentional |

---

## Lighthouse Audit

All public pages were audited with **Google Lighthouse 12** run locally via the Lighthouse CLI against the live development server on **6 June 2026**. Each audit was run twice — once in desktop mode (simulated) and once in default mobile mode (Lighthouse's 4× CPU throttle + slow 4G emulation). Scores run from 0–100:

| Range | Rating |
|---|---|
| 90–100 | 🟢 Good |
| 50–89 | 🟠 Needs improvement |
| 0–49 | 🔴 Poor |

### Scores

| Page | Device | Performance | Accessibility | Best Practices | SEO |
|---|---|:---:|:---:|:---:|:---:|
| Landing (`/`) | Desktop | 🟢 99 | 🟢 95 | 🟢 96 | 🟢 90 |
| Landing (`/`) | Mobile | 🟢 94 | 🟢 100 | 🟢 96 | 🟢 90 |
| About (`/about/`) | Desktop | 🟢 100 | 🟢 100 | 🟢 96 | 🟢 90 |
| About (`/about/`) | Mobile | 🟢 99 | 🟢 100 | 🟢 96 | 🟢 90 |
| Login (`/accounts/login/`) | Desktop | 🟢 100 | 🟢 100 | 🟢 96 | 🟢 90 |
| Login (`/accounts/login/`) | Mobile | 🟢 99 | 🟢 100 | 🟢 96 | 🟢 90 |

Every page scores in the **Good (90+)** band across all four categories.

### Flagged opportunities

The following items were raised by Lighthouse on one or more pages. All are either development-environment artefacts or straightforward improvements deferred from the initial scope.

| Flag | Pages affected | Explanation |
|---|---|---|
| Enable text compression | All | Django's `runserver` does not compress HTTP responses. WhiteNoise, which is active in production, serves Gzip- and Brotli-compressed static files automatically. |
| Serve static assets with efficient cache policy | All | The development server sends no `Cache-Control` headers. WhiteNoise sets long-lived `immutable` headers on versioned static files in production. |
| No meta description | All | Informational pages do not include a `<meta name="description">` tag. This is the sole reason all pages score 90 rather than 100 on SEO. Adding descriptions is a low-effort improvement for a public release. |
| Browser console errors logged | All | One non-fatal console error is produced by the QR-code library during initialisation in the dev environment. No errors occur on pages without a live session, and the error is absent in production. |
| Landing (desktop) — contrast ratio | Landing only | Lighthouse flagged one foreground/background colour pair on the landing page hero, reducing desktop Accessibility from 100 to 95. The colour combination (purple `#5D3A9B` on white) passes WCAG AA for large text (≥ 18 pt) but not for body text — the element in question uses 16 px. This is the only contrast gap found across the full audit. |
| Landing (mobile) — main-thread work | Landing (mobile) | Under Lighthouse's 4× CPU throttle the QR-code generation script and inline CSS account for ~1.5 s of simulated main-thread time, contributing to the 94 mobile Performance score. On real mid-range devices no perceptible delay occurs; the QR code loads before the participant would attempt to scan it. |

---

## Testing

### Principles of automated and manual testing

Software testing can be divided into two broad approaches — automated and manual — that complement each other. Neither is superior in every situation; the choice depends on what is being tested, how often it needs to be run, and how stable the feature under test is.

---

#### Automated testing

Automated tests are scripts that exercise code directly, without human interaction, and assert that the output matches an expectation. They run in milliseconds, can be executed on every commit by a CI pipeline, and give immediate, reproducible feedback.

**Core principles**

| Principle | What it means in practice |
|---|---|
| **Fast feedback** | Tests run on every save or push, catching regressions the moment they are introduced rather than at the end of a release cycle. |
| **Repeatability** | The same test produces the same result every time, removing human variation from the check. |
| **Regression safety** | A suite of tests that passes today continues to pass after a refactor — any new failure points directly at the change that broke something. |
| **Pyramid hierarchy** | Unit tests (smallest, fastest, most numerous) sit at the base; integration tests in the middle; end-to-end tests (slowest, fewest) at the top. Running cheaper tests first maximises speed. |
| **Isolation** | Each test sets up its own data, makes no assumptions about state left by another test, and cleans up after itself. |

**When automated testing is the right choice**

- Pure logic with clear inputs and outputs — calculations, validators, exporters, data-transformation utilities.
- Code that will be refactored or extended repeatedly, where regressions are easy to introduce silently.
- Security-critical invariants (e.g. "a user cannot access another user's archive record") that must hold under every future change.
- API contracts — checking that a view returns the correct status code, redirects to the correct URL, or renders the correct template given a known database state.
- Anything that would be slow or difficult to exercise by hand on every change — for example, edge-case form validation, file-generation output, or timezone-dependent behaviour.

In a Django project, automated tests are written with `unittest.TestCase` or `django.test.TestCase` and run with `python manage.py test`. The Django test runner creates an isolated test database, runs every `test_*` method, and tears the database down at the end.

---

#### Manual testing

Manual testing is a human tester interacting with the running application exactly as a real user would — navigating pages, filling in forms, observing visual feedback, and checking that nothing looks or behaves unexpectedly.

**Core principles**

| Principle | What it means in practice |
|---|---|
| **Exploratory freedom** | A human can notice that something *feels* wrong — an awkward layout, a confusing label, a missing error message — that no predefined assertion would ever catch. |
| **Real-environment fidelity** | Testing against the actual running server with `DEBUG=False` and real browser rendering reveals issues (CORS, static-file handling, CSRF, cookie behaviour) that can be invisible in a test database. |
| **End-to-end realism** | Walking through a complete user journey (sign up → create session → invite guest → close session → download export) validates the integration of every layer at once. |
| **Accessibility and UX** | Screen-reader behaviour, keyboard navigation, focus order, and visual contrast cannot be fully verified by an automated script — they require a human (or an assistive-technology tool operated by a human) to assess. |
| **Structured records** | Writing each check into a test table before running it — listing the steps, the expected result, and the actual result — turns ad hoc clicking into a repeatable audit trail that can be reviewed by an assessor or colleague. |

**When manual testing is the right choice**

- First-time or low-frequency features where writing an automated test would take longer than running the check by hand.
- Anything involving visual presentation, responsive layout, or browser-specific rendering.
- Accessibility checks — verifying skip links, screen-reader announcements, focus indicators, and ARIA attributes in a real browser with a real assistive technology.
- Usability or content review — checking that labels, headings, and error messages are clear and unambiguous.
- Exploratory testing of a new feature before its behaviour is stable enough to encode as assertions.
- Acceptance testing by a non-technical stakeholder who needs to sign off on a user journey without reading code.

---

#### Approach taken in this project

This project is at Milestone 3 of a Level 5 Diploma, where the primary assessment criterion is the correctness and completeness of the working application rather than the breadth of an automated test suite. Accordingly, all verification was performed as **structured manual testing** against the running application with `DEBUG=False`, replicating production behaviour as closely as possible in the development environment. Tests were carried out in Chrome (desktop) and Firefox (desktop).

Automated testing would be the natural next step for production hardening. The highest-value targets would be:

1. **Authorization invariants** — unit tests asserting that every archive, download, and session-state endpoint returns 403 when accessed by a non-owning authenticated user.
2. **Export / file-generation logic** in `tools/utils.py` and the `exporters/` module — pure functions with clear inputs and outputs, ideal for unit testing.
3. **Form validation** on registration, waiting-list, and feature-request forms — checking both valid and invalid input paths.
4. **Session state transitions** — integration tests confirming that a session moves correctly from `open` → `closed` and that the combined export is generated exactly once.

The structured manual test tables that follow cover the same ground and serve as the specification that automated tests would be written against.

---

All user-facing flows were tested manually against the running application with `DEBUG=False` to replicate production behaviour. Tests were carried out in Chrome (desktop) and Firefox (desktop). The tables below are grouped by feature area.

### 1 — Public pages

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Landing page loads | Navigate to `/` | Page renders with hero section, tool previews, and nav links for About, Login, Sign up | As expected | Pass |
| About page loads | Navigate to `/about/` | About page renders with product description and call-to-action links | As expected | Pass |
| Waiting list signup — valid | Navigate to `/waiting-list/`; enter valid email; submit | Success message shown; entry recorded in database | As expected | Pass |
| Waiting list signup — duplicate email | Submit the same email a second time | Form rejects the duplicate with a validation error | As expected | Pass |
| Waiting list signup — blank email | Submit form with empty email field | Form validation error; no submission | As expected | Pass |
| Feature request — valid | Navigate to `/request-a-feature/`; fill in subject and body; submit | Success message shown; request recorded | As expected | Pass |
| Feature request — blank subject | Submit form with empty subject | Form validation error; no submission | As expected | Pass |
| Free try-it — Min Specs | Navigate to `/tools/min-specs/try/`; fill in the prompt fields; submit | Results displayed on page without requiring login | As expected | Pass |
| Free try-it — 15% Solutions | Navigate to `/tools/15-solutions/try/`; fill in the prompt fields; submit | Results displayed on page without requiring login | As expected | Pass |
| Nav links resolve (public) | Click KwaCart logo, About, Login, Sign up in top nav | Each link navigates to the correct page without a 404 | As expected | Pass |

---

### 2 — Registration

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Successful registration | Navigate to `/accounts/signup/`; enter a new email and matching passwords; submit | Account created; user redirected to the tool catalog | As expected | Pass |
| Duplicate email | Attempt signup with an email that already exists | Form shows a validation error; no second account created | As expected | Pass |
| Passwords do not match | Enter two different passwords; submit | Form shows a validation error | As expected | Pass |
| Password too short | Enter a password shorter than 8 characters; submit | Django's built-in validators reject it with an explanation | As expected | Pass |
| Invalid email format | Enter a string without `@`; submit | Form validation error | As expected | Pass |

---

### 3 — Login and logout

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Successful login | Navigate to `/accounts/login/`; enter valid credentials; submit | User redirected to tool catalog; nav shows email and Logout button | As expected | Pass |
| Wrong password | Submit with a correct email but wrong password | Error message shown; user not authenticated | As expected | Pass |
| Unknown email | Submit with an email that has no account | Error message shown; user not authenticated | As expected | Pass |
| Logout | Click the Logout button in the nav | User session cleared; redirected to login page; nav reverts to public state | As expected | Pass |
| Access protected page while logged out | Navigate to `/tools/` without a session | Redirected to `/accounts/login/?next=/tools/` | As expected | Pass |
| Login redirect | Follow redirect from a protected page; log in | After login, user returned to the originally requested URL | As expected | Pass |

---

### 4 — Solo tool — draft creation and autosave

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Tool catalog loads | Log in; navigate to `/tools/` | Catalog page lists all available facilitation tools | As expected | Pass |
| Open draft editor | Click a tool; click "Start solo" | Draft editor page loads with the tool's prompt fields | As expected | Pass |
| Autosave on input | Begin typing in a prompt field; wait 2–3 seconds | Status indicator changes to "Saved" without a manual save action | As expected | Pass |
| Autosave persists on reload | Reload the draft editor after autosave | Previously entered text is pre-populated in the fields | As expected | Pass |
| Manual save button | Click the Save button explicitly | "Draft saved." success message appears | As expected | Pass |
| Resume existing draft | Navigate away; return to the tool's draft URL | Draft content is restored from the last save | As expected | Pass |

---

### 5 — Solo tool — submit and archive

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Submit completed draft | Fill in all required fields; click Submit | "Tool execution successful. Files generated." message shown; redirected to archive detail | As expected | Pass |
| Submit incomplete draft | Clear a required field; click Submit | Validation error shown; no archive entry created | As expected | Pass |
| Archive entry created | After successful submission, view `/archive/dashboard/` | New entry appears in the archive list with timestamp and tool name | As expected | Pass |
| Cannot submit another user's draft | Attempt to load a draft URL belonging to a different account | 403 response returned | As expected | Pass |

---

### 6 — Collaborative session — host flow

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Create session | From a tool page, click "Start a live session" | Session created; host sees the session room with a QR code and shareable guest link | As expected | Pass |
| QR code displayed | On the session page, view the QR code panel | QR code is visible and encodes the guest join URL | As expected | Pass |
| Copy guest link | Click the copy-link button next to the guest URL | URL copied to clipboard (button changes state to confirm) | As expected | Pass |
| Timer start | Click the Start timer button in the session room | Countdown begins and is visible to the host | As expected | Pass |
| Timer reset | Click Reset timer | Timer returns to the configured duration | As expected | Pass |
| Pause reminder | Timer reaches zero | Pause reminder notification displayed | As expected | Pass |
| Close session | Click "Close session" | "Session closed. Combined results are now visible." message; session status updated; combined export available in archive | As expected | Pass |
| Cannot close another user's session | Attempt to POST to `/tools/session/<id>/close/` with a different logged-in account | 403 returned; session not closed | As expected | Pass |

---

### 7 — Collaborative session — participant and guest flow

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Authenticated participant joins | Log in as a second account; open the session detail URL | Session room loads; participant's prompt fields are displayed | As expected | Pass |
| Participant submits response | Fill in the prompt fields; click Submit | "Your response was saved." message shown | As expected | Pass |
| Guest joins via QR / link (no account) | Open the guest join URL in a browser with no session | Guest join page loads; guest prompted to enter name/email and fill in prompts | As expected | Pass |
| Guest response saved | Guest fills in prompts and submits | "Your response was saved." confirmation; no account required | As expected | Pass |
| Guest cannot join a closed session | Attempt to open guest URL after host has closed the session | Page informs guest the session is no longer accepting responses | As expected | Pass |
| Session status polling | Participant page auto-polls session status | Host-initiated close is detected and participant's view updates without a manual reload | As expected | Pass |

---

### 8 — Archive dashboard and detail

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Archive dashboard loads | Log in; navigate to `/archive/dashboard/` | Lists all solo and session archive entries belonging to the logged-in user only | As expected | Pass |
| Solo entry detail | Click a solo archive entry | Detail page shows the submission content and download links | As expected | Pass |
| Session entry detail | Click a session archive entry | Detail page shows combined responses from host, participants, and guests | As expected | Pass |
| Cross-user isolation | Log in as a second account; navigate to `/archive/detail/<id>/` using an ID owned by account one | 403 returned; content not visible | As expected | Pass |
| Unauthenticated access | Navigate to `/archive/dashboard/` without a session | Redirected to login page | As expected | Pass |

---

### 9 — Archive delete

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Delete own record | From archive detail, click Delete; confirm | "Record deleted successfully." message; entry removed from dashboard | As expected | Pass |
| Delete another user's record | POST to `/archive/delete/<id>/` with an ID owned by a different account | 403 returned; record not deleted | As expected | Pass |

---

### 10 — Downloads

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Solo Markdown download | From archive detail, click the Markdown download link | `.md` file downloads with the tool output formatted in Markdown | As expected | Pass |
| Solo RTF download | Click the RTF download link | `.rtf` file downloads and opens correctly in a word processor | As expected | Pass |
| Solo HTML download | Click the HTML download link | `.html` file downloads with styled output | As expected | Pass |
| Session combined Markdown download | From a closed session's detail page, click the combined Markdown download | Single `.md` file containing all participant responses downloads | As expected | Pass |
| Session combined RTF download | Click the combined RTF download | Combined `.rtf` file downloads | As expected | Pass |
| Download another user's file | Attempt to access `/archive/download/<id>/md/` using an ID owned by another account | 403 returned; no file served | As expected | Pass |
| Download from closed session — other user | Attempt to access `/archive/session-download/<uuid>/md/` for a session not hosted by the current user | 403 returned | As expected | Pass |

---

### 11 — Access control and redirects

| Feature | Test steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 404 custom page | Navigate to a URL that does not exist (e.g. `/does-not-exist/`) with `DEBUG=False` | Custom 404 template renders with "Page not found" and navigation buttons | As expected | Pass |
| 403 custom page | Trigger a permission-denied response (e.g. accessing another user's archive record) | Custom 403 template renders with "Access denied" | As expected | Pass |
| Admin restricted to staff | Navigate to `/admin/` as a non-staff authenticated user | Redirected to admin login; access not granted | As expected | Pass |
| Admin accessible to superuser | Log in as a superuser; navigate to `/admin/` | Django admin interface loads | As expected | Pass |
| Draft editor requires login | Navigate to `/tools/<slug>/draft/` without a session | Redirected to `/accounts/login/?next=…` | As expected | Pass |
| Session detail requires login | Navigate to `/tools/session/<uuid>/` without a session | Redirected to login page | As expected | Pass |
| Autosave endpoint rejects unauthenticated POST | POST to `/tools/<slug>/autosave/` without a session | 302 redirect to login returned; draft not saved | As expected | Pass |

---

## Credits

### Project

Built as Milestone Project 3 for the Level 5 Diploma in Web Software Engineering.

### Facilitation methodology

Liberating Structures — created by Henri Lipmanowicz and Keith McCandless — a collection of microstructures that support including and unleashing everyone in a group. See [liberatingstructures.com](https://www.liberatingstructures.com). Tool names, descriptions, phases, and facilitation guidance throughout the platform are drawn from this methodology.

### Python / Django ecosystem (installed via `requirements.txt`)

| Package | Licence | Purpose |
|---|---|---|
| [Django](https://www.djangoproject.com) | BSD-3-Clause | Web framework — ORM, views, forms, auth, admin |
| [WhiteNoise](https://whitenoise.readthedocs.io) | MIT | Static file serving in production |
| [Gunicorn](https://gunicorn.org) | MIT | WSGI HTTP server |
| [django-environ](https://django-environ.readthedocs.io) | MIT | Environment-variable configuration |
| [dj-database-url](https://github.com/jazzband/dj-database-url) | BSD-2-Clause | Database URL parsing |
| [psycopg2-binary](https://www.psycopg.org) | LGPL-3.0 | PostgreSQL adapter (production database) |
| [cloudinary](https://pypi.org/project/cloudinary/) | MIT | Cloudinary Python SDK — uploads raw assets (MD/RTF exports) to Cloudinary |
| [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) | BSD-3-Clause | Django `DEFAULT_FILE_STORAGE` backend backed by Cloudinary |
| [Playwright](https://playwright.dev/python/) | Apache-2.0 | Browser automation used in the test suite |
| [pytest-django](https://pytest-django.readthedocs.io) | BSD-3-Clause | Django integration for pytest |
| [pytest-playwright](https://github.com/microsoft/playwright-pytest) | Apache-2.0 | Playwright integration for pytest |

### JavaScript libraries (vendored — not installed via a package manager)

Both files below are included verbatim from their upstream releases and have not been modified. An attribution comment has been added at the top of each file.

| Library | Licence | File | Purpose |
|---|---|---|---|
| [qrcode.js](https://github.com/davidshimjs/qrcodejs) by davidshimjs | MIT | `static/js/libraries/qrcode.min.js` | Client-side QR code generation for the guest-join link on the session page |
| [marked.js](https://github.com/markedjs/marked) by Christopher Jeffrey | MIT | `static/js/libraries/marked.min.js` | Markdown parsing and HTML rendering used by the inline archive preview modal |

### Learner-written code

All code **not** listed in the sections above was written by the project author. This includes all Python source files in `accounts/`, `archive/`, `tools/`, `exporters/`, and `config/`; all CSS files in `static/css/`; all HTML templates in `templates/`; all migration files; and all JavaScript files in `static/js/` except the two vendored libraries above.

Within the author-written JavaScript, a small number of well-established patterns were adapted from canonical external sources. Each is attributed with an inline comment directly above the relevant code:

| File | Pattern | Source |
|---|---|---|
| `static/js/draft_init.js` | `getCookie()` — reads a named cookie by string-splitting `document.cookie` | [Django CSRF documentation](https://docs.djangoproject.com/en/stable/howto/csrf/) |
| `static/js/timer.js` | `getCsrf()` — same cookie-reading technique, inlined for the timer's fetch calls | [Django CSRF documentation](https://docs.djangoproject.com/en/stable/howto/csrf/) |
| `static/js/autosave.js` | `debounce()` — standard clearTimeout/setTimeout debounce wrapper | [MDN — Debounce](https://developer.mozilla.org/en-US/docs/Glossary/Debounce) |
| `static/js/pathway_finder.js` | `shuffle()` — Fisher-Yates (Durstenfeld) in-place array shuffle | [Wikipedia — Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) |
| `static/js/archive_md_preview.js` | `getFocusable()` / `trapFocus()` — Tab/Shift+Tab focus containment inside a dialog | [WAI-ARIA APG — Dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) |
