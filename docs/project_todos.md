# Todos

* Git basics
  * ~~Solo dev workflows (add, commit, push)~~
  * ~~Team workflows (branch, add, commit, push, merge request, review)~~
* Python basics
  * ~~Syntax~~
  * Best practices
    * Project structure
    * Linting, formatting, testing (maybe CI)
  * Environment setup (venv, pip, poetry)
* General Learning
  * ~~SSH Tutorials~~
  * ~~SFTP Tutorials~~
  * Tmux Tutorials
  * Ubuntu Command line Tutorials
  * HTTP APIs
    * General learning of the networking (OSI model)
    * [FastAPI](https://fastapi.tiangolo.com/#example)
    * Try make a few silly APIs
        * ~~Runescape skill picker~~
* Start leveraging those tools
  * ~~HTTP API for controlling lights~~
  * ~~Simple web frontend~~
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