# Simple Interaction with IPython

There are multiple tools you can use for writing programs in Python.  As you have seen, you can simply start up the `python` program and enter commands and get output directly.  Obviously, you will use the `python` command to run your programs.

But let's also do some work with the `ipython` tool.  The "i" means this is a special version that is intended to run interactively.  You can run the hello program again with `ipython` if you wish; you will see the result is just the same as before.

You can find a full document about ipython at [http://ipython.readthedocs.io/en/stable/]() 

## First start: IPython Shows History

Start IPython with the simple command `ipython`.  Note it displays "In [1]", usually in green.  This is how IPython asks for a command, rather than the `>>>` prompt from regular `python`.  Rather than enter a 'real' command, just type a string in quotes and hit Enter, like this: 

<img src="pix/IPython Launch.png" />

Now you will notice IPython is giving you an "In" prompt with a number, and sending output after an "Out" marker with a matching number.  As you have already guessed, and as is indicated by the markup in the preceding image, these are the history of your inputs and outputs.

Now hit the up-arrow key, and the same input will reappear, just as it should.  Hit return and you get the same thing - command 2 is the same as command 1.  But they are recorded separately.

## Whew!  We can edit the command line!

Let's up-arrow again for command 3, but let's take that string and assign it to a variable.  You can move the cursor to the beginning of the line with left arrows, or just <ctrl>-A.  Then use your first name for the variable name and equals to assign it, hitting return again to make it happen.  Now issue a print command using that variable.

## And run a file

Within IPython, issue the command `run hello_cs689.py` and you will see your same command output again.

This loads the file into your current session, so that "msg" variable you saw (and edited) before, you can use it.  Print that variable now.

## Using IPython history

You will now be up to command number 6 or 7 or more. IPython is keeping a record, not only of your commands, but of the output.  The way to see this is by issuing the command `%history`.  This will show you the history of your session, but it is presented as a python script, not showing which command was which number.  While you could put this into a file, to view the history in a more readable format, you want to use the "-n" option:

<img src="pix/ipython readable history.png" />

## The '%' and '%%' "Magic" Commands

You should know about Python enough to know that "%" is not legitimate as the beginning of an identifier or command.  Obviously, these are specific to IPython and they are called *magic* commands.

These commands provide a substantial amount of functionality to manage not just command history, but all of the python environment being run by IPython.

You can get a list of all these commands by the (magic) command `%lsmagic`

 <img src="pix/lsmagic command and information.png" height="260" /> 
 
 You can also find out about a particular command by preceding it with a question mark, e.g. *logstart*:
 
<img src="pix/getting info on logstart magic command.png" />

Entering '?' on a line by itself starts up a long reference for IPython.

## A little more on History

IPython does not just keep a command history of the current session, but of all your sessions.  If you add the "-g" switch, you will see history for all of your sessions.  This forces the readability switch '-n'.

With all of your numbered history, you can either

|cmd|desc|
|---|---|
|`%rerun 65`|Re-execute command 65 as the next command|
|`%recall 65`|Recall command 65 and put it at the prompt for the next command, leaving the cursor at the end.  Allow user to edit the command before running it.|

If you give a plain number, it refers to the current session.

However, you can also use commands from a prior session.  You can use the exact session humber, which you could see with `%history -g`, or you can refer to how many prior sessions back you want.

You can refer to the current session as `0/`.  The previous session is `~1/`, before that `~2/`, etc.  Don't forget the slash.

You can find the actual session number for the last session with the slightly annoying `%history -n ~1/1`.

When you finish IPython by `exit()` or ctrl-Z or ctrl-D, the session is saved as the next higher number.

## Saving Your Python Session

You can save the entirety of your current python session with the "-f" switch and a file name to the %history command.

<img src="pix/Save history.png" />

Note you don't need to use quotes.  Please save your session to a file with your name and the '.py' suffix.

## *You may now proceed to <a href="Assign2PartA.5.md"> part A.5</a>*
