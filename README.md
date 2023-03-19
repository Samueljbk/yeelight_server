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
* Basic tooling for controlling yeelight led strip
  * python package with nice functions
* Deployment
  * Rasperry Pi via ssh+tmux
  * Docker (this is a bit advanced)
    * Kubernetes (even more advanced)
  * Mess with Jurgen's lights
* Start leveraging those tools
  * HTTP API for controlling lights
  * Simple web frontend
  * Implement apps
* Yeelight App Ideas
  * "Self-Control"
  * WiFi scan arriving home detection
  * Runelite idle notification
  * Phone notification (or other pc stuff)

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
      * ~~List Comprehensions~~
      * ~~Lambda functions~~
      * ~~Multiple Function Arguments~~
      * ~~Exception Handling~~
      * ~~Sets~~
      * ~~Serialization~~
      * ~~Partial Functions~~
      * ~~Closures~~
      * ~~Decorators~~
      * ~~Map, Filter, Reduce~~
      * Regular Expressions - Semi done but difficulty understanding
  * Data Science Tutorials
      * ~~Numpy Arrays~~
      * ~~Pandas Basics~~

