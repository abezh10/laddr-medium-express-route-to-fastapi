# Express Route to FastAPI

- Category: Migrate / Framework Migration
- Difficulty: Medium

## Contains
- `legacy-node/routes/reports.ts`
- `new-python/app/routers/reports.py`
- `new-python/app/services/reports_service.py`
- `new-python/app/schemas/reports.py`
- `package.json`

## Prompt
A reporting endpoint exists in the old Express service but not the new FastAPI stack. Recreate it with equivalent behavior and clean separation between validation and service logic.

## Likely Change Dirs
- `new-python/app/routers`
- `new-python/app/services`
- `new-python/app/schemas`
