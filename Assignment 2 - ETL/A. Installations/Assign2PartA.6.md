# Importing Modules in Python

You may have noticed a command "import" in the `hello_cs689.py` file.  We'll experiment with that a little bit now.

## Reopen Jupyter

At your command prompt, issue the command `jupyter notebook` again.

Create a new notebook, and click the Untitled box at top to rename it with your name.

## Import the cs689_utils.py file

Just use the bare name, without the `.py` suffix.  You shouldn't see anything.  However, there is now a function available for you to use: `log`.  You can use this to put messages into a simple log file.

<img src="pix/import and log.png" height=200/>

## Nothing happened!

Well, not exactly *nothing*...

Let's go back to the Jupyter file browser.  Or you can use Windows Explorer or Finder, they're in the same place.

Open the folder "Put your outputs here!".  You will get a new window, and you should see a file there called "cs689_simple_log.txt".  Click on it, and you will see a few lines 

## Another import

Import is how you make use of modules and classes in Python.  There is a colossal number of these available to you in Python.  We will use "random".

<img src="pix/import random.png" />

Use your birth month and birth day to generate a few random numbers in a range.  Add a few digits to your birthday, e.g. 9/4 would become (9, 4838)

Use the function `random.randrange (lower, higher)` to generate a random number.  You can print it or not.

Now wrap that function call in `str (random.randr...)` to get a string.

Now create a message with your name in it and prefix it to that string by adding the `str (random.randr...)` to the end of it.

Finally, use `cs689_utils.log` to log that message to the log file.

Close your browser and in your command window, close your Jupyter session.

## *You may now proceed to <a href="Assign2PartA.7.md"> part A.7 </a>*
