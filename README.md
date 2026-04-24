# Gradey Dick Fan Club

---

## Tech Stack

- Frontend: React 19 + Vite + TypeScript
- Backend: Python + FastAPI
- Styling: Tailwind CSS
- Deployment: Vercel

---

## Prerequisites

- Node.js v18+
- npm
- Git
- Python 3.10+

---

## Getting Started

### 1. Clone the repo

```bash
git clone <HTML link>
cd gdfc
```

### 2. Install frontend dependencies

```bash
cd frontend
npm install
```

### 3. Start dev server

```bash
npm run dev
```

You can find the app at http://localhost:5173 by default.

---

## Commands

Make sure to run these from inside the `frontend` directory.

| Command             | Description                            |
|---------------------|----------------------------------------|
| `npm run dev`       | Start local dev server                 |
| `npm run build`     | Build app for production               |
| `npm run preview`   | Preview the production build locally   |
| `npm run lint`      | Run ESLint across the codebase         |

---

## Environment Variables

Create a `.env.local` file inside `frontend` for any local environment variables. NEVER commit this to Git.

```env
# Example: changing the localhost
VITE_API_URL=http://localhost:8000
```

Variables have to be prefixed with `VITE_` to be accessible in frontend code:

```ts
const apiUrl = import.meta.env.VITE_API_URL;
```

---

## Deployment

We will deploy this via Vercel.

How it works (NOT SET UP YET):
- Vercel is connected to this repo.
- Every push to main triggers automatic deployment.
- All pull requests ge ttheir own preview deployment URL automatically.

---

## Backend (Planned)

Data management and API layer will be built using Python and FastAPI.
This lives in the `backend` directory and will be deployed separately via either Railway or Render.
The frontend will communicate with it via the VITE_API_URL `env` variable.

---

## Contributing

1. Make your own new branch: `git checkout -b feature/your-feature name`
2. Make your changes and commit (this is just what my dad taught me to always do):
```bash
git status
git add .
git status
git commit -m "your meassage"
```
3. Push in one of two ways. First is if the branch already exists both locally and on our shared repo. Second is if it doesn't yet exist on our shared repo.
```bash
git push
git push origin feature/your-feature=name
```
4. Open a pull request on GitHub (ONLY IF WE ARE READY TO PUSH TO DEV/CLOSE FEATURE BRANCH)


