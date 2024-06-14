# Bash Scripting Basics

## Comments in bash scripting
Comments start with a # in bash scripting. This means that any line that begins with a # is a comment and will be ignored by the interpreter.

Comments are very helpful in documenting the code, and it is a good practice to add them to help others understand the code.


```bash
#this is comment in bash
```


## Variables and data types in Bash


Variables let you store data. You can use variables to read, access, and manipulate data throughout your script.

There are no data types in Bash. In Bash, a variable is capable of storing numeric values, individual characters, or strings of characters.

In Bash, you can use and set the variable values in the following ways


### 1.Assign the value directly:


```bash
name=alireza parvaresh
```


### 2.  Assign the value based on the output

obtained from a program or command, using command substitution. Note that $ is required to access an existing variable's value.


```bash
f_name=$name
```

**note** : To access the variable value, append $ to the variable name.
example :


```bash
➜  ~ name=alireza
➜  ~ echo hello dear $name
hello dear alireza
```

### Variable Naming Conventions in Bash Scripting

In Bash scripting, the following are the variable naming conventions:

1. Variable names should start with a letter or an underscore (`_`).
2. Variable names can contain letters, numbers, and underscores (`_`).
3. Variable names are case-sensitive.
4. Variable names should not contain spaces or special characters.
5. Use descriptive names that reflect the purpose of the variable.
6. Avoid using reserved keywords, such as `if`, `then`, `else`, `fi`, and so on as variable names.

Here are some examples of valid variable names in Bash:

- `name`
- `count`
- `_var`
- `myVar`
- `MY_VAR`

And here are some examples of invalid variable names:

- `2ndvar` (variable name starts with a number)
- `my var` (variable name contains a space)
- `my-var` (variable name contains a hyphen)

Following these naming conventions helps make Bash scripts more readable and easier to maintain.


## Input and output in Bash scripts


Gathering input
In this section, we'll discuss some methods to provide input to our scripts.

### 1.Reading the user input and storing it in a variable


We can read the user input using the read command.

```bash
➜  ~ read name
alireza
➜  ~ echo hello dear $name
hello dear alireza

```


### 2.  Reading from a file

This code reads each line from a file named input.txt and prints it to the terminal. We'll study while loops later in this article