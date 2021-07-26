# **Pipenv** — Cheat Sheet

## **Create** — Environment
* `python -m pipenv install <package> --dev` Install to -> **Development**
* `python -m pipenv install <package>` Install to -> **Production**
---

## **Check** — Environment
* `python -m pipenv check` Check security vulnerabilities.
* `python -m pipenv graph` Check dependency graph.
---

## **Lock** — Environment (before: **Deployment**)
```sh
python -m pipenv lock
```
---

## **Recreate** — Environment
* `python -m pipenv install --dev` Install for -> **Developers**
* `python -m pipenv install --ignore-pipfile` Install for -> **Production**
---