# AirBnB clone


[![hbnb-Air-Bn-B.png](https://i.postimg.cc/pdxsYQhs/hbnb-Air-Bn-B.png)](https://postimg.cc/TK7jTDcb)

## DESCRIPTION :smile:

hbhb This is the first step to build our first full web application: the AirBnB clone.
This project currently only implements back-end.

## CONTENT :closed_book:

The files include in our repository that make our function work are:

+ **models**
  + ***engine***
    + file_storage.py
    + \_\_init__.py
  + \_\_init__.py
  + amenity.py
  + base_model.py
  + city.py
  + place.py
  + review.py
  + state.py
  + user.py
+ **tests**
  + ***test_engine***
    + test_file_storage.py
  + test_amenity.py
  + test_base_model.py
  + test_city.py
  + test_place.py
  + test_review.py
  + test_state.py
  + test_user.py
+ **console.py**

## Console :computer:

The console is the command line interpreter that allows us to manage the hbnb backend (AirBnB clone). It can be used to manage and manipulate all the classes used by the application.

## How to use the console :cd:

The hbnb console can be run in interactive mode and non-interactive mode. To run the console in non-interactive mode, direct any of the run commands to the console.py file on the command line.

[![non-interactive-mode.jpg](https://i.postimg.cc/nLsbzQj0/non-interactive-mode.jpg)](https://postimg.cc/cKN5kCcn)

```
root@751e4fd4b311:~/AirBnB_clone# $ echo "help" | .console.py
```
While running in interactive mode, the console displays a prompt for input

[![prompt-for-input.jpg](https://i.postimg.cc/NFD69D5X/prompt-for-input.jpg)](https://postimg.cc/T5yLBrj2)
```
root@751e4fd4b311:~/AirBnB_clone# ./console.py
(hbnb)
```
To exit the console, enter the quit command, or enter an EOF signal (ctrl-D).

[![quit.jpg](https://i.postimg.cc/YCrpz3j9/quit.jpg)](https://postimg.cc/56rdx8Bd)
```
root@751e4fd4b311:~/AirBnB_clone# ./console.py
(hbnb)  quit
```
[![EOF.jpg](https://i.postimg.cc/xCyx5KXf/EOF.jpg)](https://postimg.cc/1nXr5V02)
```
root@751e4fd4b311:~/AirBnB_clone# ./console.py
(hbnb) EOF
```

## Console commands

The hbnb console has the following commands:

+ **create**
The new instance of the new class given is created. The class ID is printed and the instance is saved in the `file.json` file.

+ **Show**
Prints the string representation of a class instance based on a given id.

+ **destroy**
Removes a class instance based on a given id. The `file.json` storage file is updated accordingly.

+ **all**
Prints the string representations of all instances of the given class. If the class name is not given, the command will print all instances of each class.

+ **count**.
Retrieves the number of instances of a given class.

+ **update**.
Updates a class instance based on a given id with a given key/value attribute pair or a dictionary of attribute pairs. If `update` is called with a single key/value attribute pair, only "simple" attributes can be updated.
key/value attributes, only `single` attributes can be updated in addition, any attribute can be updated by supplying a dictionary.



##  Authors :raising_hand: :raising_hand:

+ **Paula Carbajal** [paulacarvani](https://github.com/paulacarvani)
+ **Andrea Angola** [122-63](https://github.com/122-63)