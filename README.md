# Argument labelling tool:
automates the inference of 5 semantics in an abstract argument framework,
visualises arguments and their attack relations graphically, and shows the set of arguments that fit
the different semantics by colour.

# Prerequisites:
The application is written using the latest version of python 3.9 currently available,
please ensure that you have python 3.9 installed on your computer.

# Run:
The application is run from View.py

Make sure you are using Python 3 to run it：
 - Launch Terminal
 - Type "cd" (with spaces) and drag and drop the application folder.
 - Type
```
sh
python3 View.py
```

# User manual：

## Add or remove arguments and attack relations：
Add an argument to the "Attacker" box to indicate the attacker in this relationship
(the attacked can be empty or the attacker itself).

Add an argument to the "Attacked" box to indicate the attacked in this relationship
(separate the different arguments of the attack with commas, all spaces are disregarded).

Press the Add or Remove button on the right to add or remove the argument or attack relationship.

## Inferring semantics：
Press the button on the Calculate Semantics label to display the extension results in the
Argumentation Labelling Window. Arguments labeled as 'in' are shown in green, arguments labeled as 'out'
are shown in red and arguments labeled as 'undec' are shown in grey.

## Open and save files：
You can click the Open button and select the argument framework .json file to open from
your computer. Several examples of argument framework .json files are prepared in the
application and saved in the 'data/file' folder for reference and debugging.

You can click the Save button to save the argument framework you have created as a .json
file to your computer.

You can modify the argument or attack relationship at any time and update the semantics again
with the Calculate Semantics button.

If at any time you want to start again, press the Clear button.