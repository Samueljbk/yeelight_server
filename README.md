# yeelight_server
Home automation server for yeelight

## Contributing

Example workflow for stages of uploading changes to server

```sh
git status
git add .
git commit
git push
``` 

Or you can make a branch

```sh
git checkout -b feature/feature-description
git push --upstream origin feature/feature-description
# make some changes
git add .
git commit -m "implemented feature XYZ"
git push
```

This will prompt you to make a "Pull Request" in stdout, click on it, make PR.

# Demo app

## Setup

Make and activate a venv

```sh
python -m venv venv
. venv/bin/activate
# . venv/Scripts/activate # for windows
```

Install deps

```sh
pip install -r requirements.txt
```

Run the app

```sh
uvicorn --reload src.be.app:app --port 8000
```

Go to [localhost:8000/](localhost:8000/)!