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

# Todos

* Git basics
  * ~~Solo dev workflows (add, commit, push)~~
  * Team workflows (branch, add, commit, push, merge request, review)
* Python basics
  * Syntax
  * Best practices
    * Project structure
    * Linting, formatting, testing (maybe CI)
  * Environment setup (venv, pip, poetry)
* General Learning
  * HTTP APIs
    * General learning of the networking (OSI model)
    * [FastAPI](https://fastapi.tiangolo.com/#example)
    * Try make a few silly APIs
* Basic tooling for controlling yeelight led strip
  * python package with nice functions
* Start leveraging those tools
  * HTTP API for controlling lights
  * Simple web frontend
  * Implement apps
* Yeelight App Ideas
  * GitHub activity indicator
  * Change colour of other users lights
  * "Self-Control"
  * WiFi scan arriving home detection
  * Runelite idle notification
  * Phone notification (or other pc stuff)
* Plan out the app
  * What sort of server/client structure should it have?
    * Happy to donate my RPi's to the cause (Jerome)
  * What tech stack?
    * Assume python for the language
    * HTTP api server if needed (FastAPI, flask)
    * Client side app?
      * If yes, what GUI framework?
    * Web frontend?
      * If yes, what web FE GUI framework?
    * Do we need a database?
      * Probably not, but if we wanted some extra complexity we could.
  * Thinking about things like:
    * Deployment/Installation
      * Windows vs Linux versions
    * Updates
    * Monitoring
* Deployment
  * Rasperry Pi via ssh+tmux
  * Docker (this is a bit advanced)
    * Kubernetes (even more advanced)
  * Deploy to a few users
    * Sam
    * Jerome
    * Jerome has additional yeelight strip for misc other user
* Books
  * Pragmatic Programmer

# Tutorials

* [learn python](https://www.learnpython.org/)
  * Basics
      * ~~Hello, World!~~
      * ~~Variables and Types~~
      * ~~Lists~~
      * ~~Basic Operators~~
      * ~~String Formatting~~
      * ~~Basic String Operations~~
      * ~~Conditions~~
      * ~~Loops~~
      * ~~Functions~~
      * ~~Classes and Objects~~
      * ~~Dictionaries~~
      * ~~Modules and Packages~~
  * Advanced Tutorials
      * ~~Code Introspection~~
      * ~~Generators~~
      * List Comprehensions
      * Lambda functions
      * Multiple Function Arguments
      * Regular Expressions
      * Exception Handling
      * Sets
      * Serialization
      * Partial Functions
      * Closures
      * Decorators
      * Map, Filter, Reduce
  * Data Science Tutorials
      * Numpy Arrays
      * Pandas Basics

