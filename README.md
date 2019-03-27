# Test-Data-Generator
A small python script that automatically generates test data


## How to use
* To start editing the layout of data go to entry function

* You can change the amount of entries for the script to generate by changing the number when constructing a **DataFormat**

* The format is freely configurable, all you need to do is call the **add_command** function and pass a **Field** 
object (Different fields take different paramaters if any)

* Once your desired format is created call **gen_to_files()** with directory path for output and number of files

## Fields
* String field (**StrField**) doesn't take in any parameters and generates a random name

* Number field (**NumField**) takes in the minimum and maximum value of the generated number, as well as the type of number 
(int or float)

* Date field (**DateField**) doesn't take in any parameters and generates a random date with format YYYY-MM-DD

* Time field (**TimeField**) doesn't take in any parameters and generates a random time with format HH-MM-SS

* Text field (**TextField**) takes in a text value, this field doesn't generate anything, it just adds the text

## Commands
* **add_comand()** adds a field to the format line, takes in two parameters second one being optional which specifies what char
is added to the end of the field value

* **gen_to_files()** prints the output of the format into a directory, takes in the directory for files, the amount of files and
an optional parameter of the file name (**NOTE:** if there are more than one file the file name will increment 
e.g file0, file1, file...))
