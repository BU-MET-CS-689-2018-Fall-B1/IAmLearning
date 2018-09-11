# Using PyCharm

Our final alternative for Python programming is PyCharm.  Find your PyCharm application and launch it.

PyCharm may (or may not) prompt you to update.  This only takes a few moments, but it is not important now.

## Getting Started

You will get a "Welcome" window.  Select "Create a new project".

It gives you a stack of prefab types of projects, but all we want now is "Pure Python."

## Does it have the right Python available?

Under "Interpreter:" it should have found your Anaconda Python installation.  If there is an interpreter and it says "anaconda," or if its name starts with 3.6, you're good.  If not, see if the dropdown has one of those in the list.

If there are no 3.6 interpreters, click the cog wheel button at right and select "Add Local" to add your Anaconda python.  It will pop up a (funny-looking) navigator window.  Find the `python.exe` file in Windows.  If you're on a Mac, you probably have `/Applications/anaconda/bin/python.app` that you should use.

Once you have a Python 3.6 available, continue.

## Go to your local Git directory for "Location:"

Choose the "A. Installations" subdirectory and continue.

<img src="pix/set up new project.png" height=300 />

Then hit "Create" and it will ask you to create from existing sources.  Do this.

## Configure Git

You will get a browser-like window and it will notice you are using Git.  Good!  Hit 'Add root'.

<img src="pix/add vcs root.png" />

Finally, get it fully registered by selecting PyCharm's VCS menu, and select "Enable Git Integration.

It will set everything up, except one thing.

Double-click on your `hello_cs689.py` file.  It will ask "Do you want to add the following file to Git?"

<img src="pix/do not add to git and do not ask again.png" height=130 />

## Save the file under a new name

Use the File menu "Save As..." to give it a name that includes PyCharm and your name.  Still must end with `.py`!

## Familiarize your self with some hacking around

Note that this is syntax colored, has popup help, etc.  If you like this, please feel free to use this for our Python assignments.

## Add the "random" import and more messages

As we did in Jupyter, import `random` again.  Generate a new message using your name and a random number as before, using any numbers you like for the range.

## Run the script!

How?  PyCharm has a "Run" menu.  For this first time, it doesn't know what you're doing, so select the one that says `Run...`

<img src="pix/Run dialog.png" height=200 /> 

It will pop up a tiny dialog with a prefab "Configuration".  Just click the one selected.

<img src="pix/Run config dialog.png" />

Your results will show up in a new panel below.

When you have the results you like, move along!



## *You may now proceed to <a href="Assign2PartA.8.md"> part A.8</a>*
