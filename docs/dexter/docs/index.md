## **Create** — Environment
* `python -m pipenv install <package> --dev` Install to -> **Developers**
* `python -m pipenv install <package>` Install to -> **Production**
---

## **Check** — Environment
* `python -m pipenv check` Install for -> **Developers**
* `python -m pipenv graph` Install for -> **Production**
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