# Express Route to FastAPI

- Category: Migrate
- Topic: Framework Migration
- Difficulty: Medium

## Overview
This sample repository is set up for a medium migrate exercise in the framework migration track. The starter code is intentionally lightweight: it gives Sandpack something meaningful to render or inspect, but it still leaves the real evaluation work in place so a candidate has to move the implementation to the target framework or version while preserving behavior.

## Exercise Summary
A reporting endpoint exists in the old Express service but not the new FastAPI stack. Recreate it with equivalent behavior and clean separation between validation and service logic.

## Starter State
The current scaffold keeps the requested folder layout intact and includes small task-adjacent starter implementations. Frontend files render simple placeholder UI, while routes, services, hooks, utilities, and data files expose minimal sample data or placeholder behavior without solving the exercise for the learner.

## Repo Files
- `legacy-node/routes/reports.ts`
- `new-python/app/routers/reports.py`
- `new-python/app/schemas/reports.py`
- `new-python/app/services/reports_service.py`
- `package.json`

## Likely Change Areas
- `legacy-node/routes`
- `new-python/app/routers`
- `new-python/app/schemas`
- `new-python/app/services`

## Sandbox Notes
These files are intentionally small and preview-friendly. They should render a lightweight surface where that makes sense, while still leaving the real build, debug, refactor, security, or migration work undone.
