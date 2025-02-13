# hacking-codehs
A *VERY* simple guide on how to exploit CodeHS terminal with Python 

Today, we will be tricking the codehs.com code editor into giving us access to the kernel and running graphical programs. This process only takes a very miniscule understanding of Python, a decent understanding of Linux and Bash prgrams (like `wget` and `tar`), a CodeHS account, and the willingness to go against the EXTREMELY low FPS rate.

#### NOTE: Make your programs in codehs.com/sandbox/{user}/{program}, save them, and run them in codehs.com/sandbox/{user}/{program}/run so you don't into storage problems

## Getting started
You will start by making a simple program that gives you access to the kernel using Bash. Type this into your code editor:

```
import os

os.system('bash')
```

As you can see it is not at all comlplicated, as it only takes two lines of code without spaces. It'll only get easier from here!

### Play around a bit

Do some simple Bash programs to get used to the enviorment. For example:

#### df -H
![df -h](resources/dfh.png)
#### ls
![ls](resources/ls.png)
#### dd if=/dev/urandom of=...
![dd if=/dev/urandom of=...](resources/dd.png)
## Graphical Programs
Lets learn how to run graphical programs, using Firefox as an example

#### NOTE: from now on, you must have the "Display Server Graphics Screen" (in the Other section of setting) option ON. I reccomend making a "PyGame" project instead of a regular "Python" project and erasing all the text in the code editor, since "PyGame" has the Graphics Screen on by Default
[df -h](resources/dsgs.png)

Put the following code into the code editor (or download the resources/firefox.py file and uploading it to the code editor):
```
import os 

os.system('''wget https://ftp.mozilla.org/pub/firefox/releases/131.0b9/linux-x86_64/en-US/firefox-131.0b9.tar.bz2
tar -xvf firefox-131.0b9.tar.bz2
cd firefox
./firefox
''')
```
Run the program, wait about ~30 seconds, and you should see a Firefox window pop up. 
[Firefox](resources/firefox.png)
(By the way, if you were trying to use this to bypass some type of YouTube or Reddit block, don't, there is no sound and YouTube doesn't work since the OS is so unstable)
