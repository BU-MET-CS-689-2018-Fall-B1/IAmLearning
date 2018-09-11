# Simple Interaction with Jupyter

You probably find IPython a major step up from simple interaction with Python, but Jupyter provides the same features in a superior web-based interface.

## Make sure you are in this directory and launch Jupyter

You want to have your Command Prompt or Terminal window running in this current directory, so that you can directly use the files here.  To verify, issue the command `dir` on Windows, or `ls` on MacOS/Linux.  You should see this file and a bunch of others, including `CS 689 Assignment 2 part A - Python Intro.ipynb`.  If you see these in the file listing, you're good.

You start it with `jupyter notebook`:

<img src="pix/starting jupyter on windows.png" />

All those messages coming out are telling you about the web server that Jupyter is starting.  It also tells you how to shut it down.

## Working via Web Interface

Jupyter will launch your browser automatically, usually before you barely notice the messages above.  What you first see is not python or IPython, but a file browser:

<img src="pix/Jupyter starts with file browser.png" />

## Open the (IPython) Notebook

The file `CS 689 Assignment 2 part A - Python Intro.ipynb` is a "notebook" which records an interactive session with even more detail and options than does IPython.  When you open it, it looks like a sort of structured editor and it has a bunch of commands with their outputs which I have captured for you.

<img src="pix/working with jupyter.png" height=450/>

I suggest that you start by pulling down the internal View menu and select 'Toggle Line Numbers' so that you get line numbers in each entry.

You see that while this looks much like IPython, the presentation has a lot of helpful structure.  It also has a bunch of output from running the commands.

In addition, you still have most of the **%magic** commands.

Each of the In/Out blocks is called a "cell" in Jupyter.

Go into the third line, which just has the command `'hi'`.  If you hit enter at the end, it does not run - instead, you get a new line.  What this means is that you can actually do a sequence of commands, or a whole python block within a single cell.

## Run the 'hi' cell with control-enter or alt-enter

You have a few options for running cells in Jupyter.  "Run Cell and Select Below", which is on the "Cell" menu, will run the current cell and move into the following cell.  The same is accomplished with a toolbar button, or by hitting alt-enter in the cell.

<img src="pix/run and enter next cell.png" />

However you do it, you will see something like the following.

<img src="pix/jupyter run hi.png" />

Note that "In [3]" has now changed to "In [1]" in the cell numbering.  This is because you are in a new session and this is the first command.  Sadly, all the numbers and outputs from the prior session are saved as is, which may be a little confusing.

It's actually a little worse than that.  All of the outputs from prior sessions that have not been re-run or cleared are still there with their original line numbers.  Because of this, the In/Out numbers are not unique!!

I will suggest to you that you clear the outputs.

<img src="pix/clear jupyter output.png" height="270"/>

This will also clear the confusing line numbers.

## Run the History cell

Now, click into the cell with the command `%history -n ~1/`.

You will see all of your commands from your last (non-Jupyter) IPython session!  This makes the multiple-session management of IPython even more useful.

Now the **%magic** commands, as you should now see, do not get the same kind of output.  The In input is numbered as before, but not the output.  Instead, their results are put into a block that is not outlined or numbers.  This block will become scrollable if it gets too long.

## Be Aware of your session

Go into the cell with `print (simple_python)` and run it.  What happens?

<img src="pix/variable simple_python does not exist yet.png" />

This variable does not exist in your session, even though you see the assignment up above.  Go up to the cell that assigns it, and run that line.  Now, when you re-run the print cell you get the correct output.

## Click on the Jupyter Logo to return to the file browser

You now have the file browser again, but your other session is not dead.  It's still running.  More specifically, the *notebook* is still running, as shown by the book icon turning green, and the "Running" label.

<img src="pix/notebook is still running.png" />

We'll end our use of Jupyter by shutting down the notebook from the browser.  Click the checkbox and hit "Shutdown."

<img src="pix/shut down the notebook.png" />

Close your browser, and hit control-C once or twice to shut Jupyter down.

<img src="pix/shut Jupyter down.png" />

## *You may now proceed to <a href="Assign2PartA.6.md"> part A.6</a>*
