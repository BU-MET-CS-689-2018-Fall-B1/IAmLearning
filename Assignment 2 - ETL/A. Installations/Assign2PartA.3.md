# Experimenting with Python

Finally!  We're ready to hack Python!  You should have your Explorer or Finder open to your ("cloned") copy of the class files.  Double-click on "Assignment 2 - ETL" and then "A. Installations".

## Get (a bit) Used to the Command Line

You will need to be issuing commands several times in the course.  We are trying to minimize this, but let's get real: you'll need it.

The main problem is to get your command prompt (or "shell") window to the directory you want.  Luckily, this is pretty easy.

### Windows: Open *Anaconda Prompt* from Start Menu (or taskbar...)

### Mac: Open *Terminal* from the Utilities Folder

You can get to Utilities (/Applications/Utilities) from the Finder, Pull down the Go menu and select it.  Then double-click *Terminal*.

<img src="pix/Mac Utilities in Finder Go Menu.png" height=140/>

### Type "cd" and space in your command window

### Drag the folder from Explorer/Finder onto your command window
This will paste the path into the window

### Hit \<enter> and you're there!

You can confirm by entering the command "dir" in Windows, or "ls" in Mac.  You will see the files.

## Run a Python File
We'll start by just running a Python file.

<pre> $> python hello_cs689.py </pre>

You should get something like this:

<pre>
Welcome, CS 689 Students!
Got a message for you: Welcome, CS 689 Students!
</pre>

## Running in 'straight' Python

First, clear your screen.  "cls" in Windows, "clear" in Mac.

Enter the command `python`

Python will prompt you with three greater-thans:

<pre> >>> </pre>

Try printing a message with your name (that is, instead of "Waldo"):

<pre> >>> print ("Hi, this is Waldo") </pre>

Create a string variable

<pre> >>> myString = "A variable by Waldo" </pre>

## Edit the hello_cs689.py file

Now we will edit the Python file.  You can use Notepad or TextEdit or Atom or anything you like.  For now we are doing only a few simple edits, so don't double-click the file to open PyCharm or anything like that.

<img src="pix/Edit the Hello file.png" />

And in Windows Notepad, it looks like this:

<img src="pix/Hello file in Notepad.png" height="270" />

Change the contents of the `msg` string to put your name in.

At the bottom of the file, use `print` to send another message or two, and include the instructor's name.

Save the changed file and exit.

## Run the changed python script as before

<pre>
python hello_cs689.py
</pre>

Verify that the program runs correctly and that you see the changes that you put in.

## Running a File with "Indirection"

You can run our "hello" script in a slightly different way, too:

<pre> python < hello_cs689.py </pre>

Do you see that the output is different from what it is when you run it as `python hello_cs689.py`?  **Why do you think that is?**

## *You may now proceed to <a href="Assign2PartA.4.md"> part A.4 </a>*
