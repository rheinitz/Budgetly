# Installation

[Docs home](../README.md) · Next: [User guide](user-guide.md)

Budgie needs Python 3.12 and Git. It uses SQLite, so there is no database server to install. Bootstrap and Google Fonts load from their CDNs, so the pages need internet access to look right.

## 1. Clone and install

**Linux / macOS**

```bash
git clone https://github.com/rheinitz/Budgie.git
cd Budgie
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/rheinitz/Budgie.git
cd Budgie
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Environment variables (optional)

The app runs without a `.env` file. Every setting has a safe local default. To change one, copy the example file and edit it:

```bash
cp .env.example .env        # Windows: copy .env.example .env
```

| Variable | Purpose | Default |
| --- | --- | --- |
| `SECRET_KEY` | Django signing key | A development key in `config/settings.py` |
| `DEBUG` | Debug mode. `true`, `1` or `yes` turn it on | `True` |
| `ALLOWED_HOSTS` | Comma-separated host names the server answers to | `localhost,127.0.0.1` |

Keep the quotes around `SECRET_KEY` in `.env`. An unquoted `#` or `$` breaks the value. `.env` is git-ignored and must never be committed.

## 3. Create the database and run

```bash
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The database starts empty on purpose: everything is created through the UI. Continue with the [user guide](user-guide.md).

The Django admin is registered for all three models, but the app never needs it. To use it anyway, run `python manage.py createsuperuser` and open `/admin/`.

## Viewing the custom 404 page

Django shows its own debug page while `DEBUG` is on. To see Budgie's 404 page:

1. Set `DEBUG=False` in `.env`.
2. Start the server with `python manage.py runserver --insecure`. Without `--insecure`, Django stops serving the CSS files when debug is off.
3. Open an unknown URL such as `/nowhere/`, or a missing record such as `/types/999/`.

Set `DEBUG=True` again afterwards.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `DisallowedHost` / "Bad Request (400)" | The host is not in `ALLOWED_HOSTS`. Add it to `.env`, comma-separated. |
| Pages have no styling with `DEBUG=False` | Run `runserver --insecure`, as described above. |
| `no such table` errors | `migrate` has not been run in this folder. |
| Fonts look plain | The Google Fonts CDN is unreachable. The layout still works with fallback fonts. |
