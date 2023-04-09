Misc todo:
    * ~~SSH~~
    * FastAPI Tutorials
    * Tmux Tutorials
        * Attach and Detach
    * Ubuntu Command line basics
    * Docker (In the future)
    

Current dir = ./
Parent dir = cd ..
Home dir = ~
touch = make file
mkdir = make folder / directory
* See all previously typed terminal commands:
    * `history`
* Printing content of file to stdout:
    * `cat {file_name}`
* Help commands:
    * `--help`
    * `-h` (Short Version and TLDR)
    * `man {command}`
        * e.g. `man git` or `man git-clone`
* Removing a dir:
    * `rm -rf {dir_name}`
* Removing a file:
    * `rm {file_name}`
* Moving a file:
    * `mv {file_name} {destination}`
* Renaming a file:
    * `mv {file_name} {new_filename}`
* Starting static server:
    * `python3 -m http.server [port]`
* Tmux commands:
    * Create new session:
        * `tmux`
    * Attaching:
        * `tmux a`
    * Detaching:
        * ctrl + b -> d
    * List all tmux sessions:
        * `tmux ls`
    * Attach to a session
        * `tmux a -t {session}`
* Watch:
    * Repeats command infinitely
        * e.g. `watch docker ps`
* Docker Commands:
    * docker ps
        * displays current docker processes
    * docker image ls
        * displays all images
    * docker run
        * Runs image if installed - downloads and runs image if not installed
            e.g. `docker run --name mc -it -p 25565:25565 -e EULA=TRUE itzg/minecraft-server`
    * Rename docker image: 
        * `docker --name`
    * Run image in background:
        * Put -d in command
            * e.g. `docker run -d -it -p 25565:25565 -e EULA=TRUE itzg/minecraft-server`
    * Kill image (Stopping or closing):
        * `docker kill {image_name}`
            * e.g. `docker kill confident_solomon`
    * Stop and remove a docker container:
        * `docker rm -f {CONTAINER}`
    
    
    







/ at front of path means it starts at root 