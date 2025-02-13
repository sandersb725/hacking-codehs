# hacking-codehs
A *VERY* simple guide on how to exploit CodeHS terminal with Python 

Today, we will be tricking the codehs.com code editor into giving us access to the kernel and running graphical programs. This process only takes a very miniscule understanding of Python, a decent understanding of Linux and Bash prgrams (like wget and tar), a CodeHS account, and the willingness to go against the EXTREMELY low FPS rate.

#### Note: Make your programs in codehs.com/sandbox/{user}/{program}, save them, and run them in codehs.com/sandbox/{user}/{program}/run so you don't into storage problems

## Getting started
You will start by making a simple program that gives you access to the kernel using Bash. Type this into your code editor.

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
