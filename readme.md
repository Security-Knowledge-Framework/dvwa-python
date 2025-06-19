# Secure Coding Knowledge Framework (SKF)

This application helps developers learn and apply secure coding practices through hands-on threat modeling and vulnerability exploration.

## 🚀 Quick Start

You can run this project either in Docker or directly on your local machine.

---

## 🐳 Running with Docker (Recommended)

First, build the Docker image:

```bash
docker build -t skf-app .
```

Then, run the app with your local code mounted, so changes reflect live:

```bash
docker run --rm -it \
  -v $(pwd):/home/app/threat \
  -w /home/app/threat \
  -p 5000:5000 \
  --user 1000:1000 \
  skf-app
```

➡️ Access the app at [http://localhost:5000](http://localhost:5000)

---

## 💻 Running on the Host Machine (Python)

> Requires Python 3.8+ and [`uv`](https://github.com/astral-sh/uv) (a fast Python package manager).

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python3 TM.py
```

➡️ Visit [http://localhost:5000](http://localhost:5000) once the server starts.

---

## 📝 Notes

- Docker run mode mounts your current folder into the container so you can live-edit the code.
- If you're on Windows, use `$(pwd)` or `%cd%` depending on your shell (e.g., PowerShell vs. Git Bash).
- Make sure your app binds to `0.0.0.0` internally if you're using Docker and want to expose it on your network.

Happy Hacking! 🔐
