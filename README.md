# Let’s Go — Hook Study Operating Review

A no-build GitHub Pages dashboard for the Phase 1 five-variant hook-isolation study. It is designed to function as an ongoing biweekly operating review while still being clean enough to surface selectively in a Board discussion.

## Study workflow

1. One source video is held constant.
2. Five hook variants are posted as trial reels: Credential, Numbered / Specific, POV / Direct-address, Contrarian / Pattern-break, and Cold Open / Visual-only.
3. Metrics are pulled at 24 hours and 48 hours.
4. The 48-hour winner is selected primarily on 3-second retention, with watch depth and engagement as supporting signals.
5. Exactly one winner is promoted to the main feed at 48 hours.
6. Seven-day metrics are pulled for all variants, with `7d Distribution Context` distinguishing the promoted winner from trial-only continuation.

## Updating the dashboard

The page reads `data/variants_log.csv` directly. To add a completed round:

1. Copy the five starter rows from `data/variants_template.csv`.
2. Keep the five hook categories unchanged.
3. Give all five rows the same `Round ID`, `Review Cycle`, source metadata, post date/time, and video length.
4. Mark exactly one row `Predicted Best Performing Hook = Y`.
5. Enter 24h and 48h metrics for all five rows.
6. Mark exactly one row `Winner of Round (Y/N) = Y`, and that same row `Promoted to Feed (Y/N) = Y`.
7. Enter `Date Promoted` for the winner.
8. Enter the 7d pull and the correct `7d Distribution Context` for every row.
9. Append the five rows to `data/variants_log.csv` and push.

The dashboard automatically treats the last encountered `Review Cycle` as the current biweekly cycle. No HTML edits are needed for a normal data update.

## Validation

Run:

```bash
python scripts/validate_data.py data/variants_log.csv
```

The included GitHub Action runs the same validation on relevant pushes and pull requests.

## GitHub Pages

Put the contents of this folder at the repository root and enable GitHub Pages for the branch you publish. There is no build step, framework, API key, or environment variable.

For local preview:

```bash
python -m http.server
```

Then open the local server URL. Opening `index.html` directly may block CSV fetching in some browsers; the page also includes a **Load CSV** button for that case.

## Repository structure

```text
/
├── index.html
├── .nojekyll
├── data/
│   ├── variants_log.csv
│   ├── variants_template.csv
│   └── round_summary.csv
├── scripts/
│   └── validate_data.py
└── .github/workflows/
    └── validate-data.yml
```
