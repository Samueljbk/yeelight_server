# Deployment methods, Zero to Cloud

* SSH, git, nohup (1 programs)
    * New Machine:
        * `ssh rpi`
        * `git clone https://github.com/Samueljbk/yeelight_server.git`
        * `cd yeelight_server`
        * `python3 -m venv venv`
        * `source ./venv/bin/activate`
        * `pip install -r requirements.txt`
        * `nohup uvicorn --host 0.0.0.0 src.be.app:app &`
        * ctrl+c and `exit`
    * Existing installation:
        * `ssh rpi`
        * `cd yeelight_server`
        * `source ./venv/bin/activate`
        * `nohup uvicorn --host 0.0.0.0 src.be.app:app &`
        * ctrl+c and `exit`
    * Killing server:
        * `ssh rpi`
        * `ps aux | grep yeelight_server`
        * `kill {process id}`
* SSH, sftp, nohup (1 programs)
* SSH, git, tmux (1 programs)
* SSH, docker (1 programs)
* SSH, docker-compose (1-4 programs)

-- Operations teritory

* Kubernetes, (1-1000 programs)
* Cloud based stuff (1-1000 programs)
