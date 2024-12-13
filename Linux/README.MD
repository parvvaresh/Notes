# 1.pwd

Displays the current working directory.

```bash
➜  ~ pwd
/home/reza
```

# 2.ls
Lists the contents of the current directory.

## ls : 
```bash
➜  ~ ls   
 2021_J_Applied_Clin_Med_Phys_Review_The_application_of_metal_artifact.pdf
 Application
 csv
 data
 Desktop
 dev
 Documents
 Downloads
 duckdns
 hamedan_area
 handle_csv
 Music
 package-lock.json
 Pictures
 Public
 Templates
 Videos
'حلقه و شرط.pdf'
```


## ls -l: 
long listing format

```bash
➜  ~ ls -l
total 2412
-rw-r--r--. 1 reza reza 2143515 Nov 15 18:13  2021_J_Applied_Clin_Med_Phys_Review_The_application_of_metal_artifact.pdf
drwxr-xr-x. 1 reza reza      14 Nov  1 18:37  Application
drwxr-xr-x. 1 reza reza     138 Nov  9 09:13  csv
drwxr-xr-x. 1 reza reza       8 Nov 13 17:53  data
drwxr-xr-x. 1 reza reza     350 Nov 13 23:30  Desktop
drwxr-xr-x. 1 reza reza     328 Nov 16 11:43  dev
drwxr-xr-x. 1 reza reza      78 Nov 10 21:00  Documents
drwxr-xr-x. 1 reza reza    3234 Nov 18 23:46  Downloads
drwxr-xr-x. 1 reza reza      56 Nov  1 21:34  duckdns
drwxr-xr-x. 1 reza reza  166556 Nov 16 11:36  hamedan_area
drwxr-xr-x. 1 reza reza       0 Nov 11 15:45  handle_csv
drwxr-xr-x. 1 reza reza       0 Nov  1 17:50  Music
-rw-r--r--. 1 reza reza      83 Nov  7 22:34  package-lock.json
drwxr-xr-x. 1 reza reza      34 Nov  2 23:16  Pictures
drwxr-xr-x. 1 reza reza       0 Nov  1 17:50  Public
drwxr-xr-x. 1 reza reza       0 Nov  1 17:50  Templates
drwxr-xr-x. 1 reza reza      26 Nov  5 15:31  Videos
-rw-r--r--. 1 reza reza  318115 Nov 13 11:40 'حلقه و شرط.pdf'
```


## ls -a:
shows hidden files

```bash
➜  ~ ls -a
 .
 ..
 2021_J_Applied_Clin_Med_Phys_Review_The_application_of_metal_artifact.pdf
 .anydesk
 Application
 .bash_history
 .bash_logout
 .bash_profile
 .bashrc
 .cache
 .config
 csv
 data
 Desktop
 dev
 Documents
 Downloads
 duckdns
 .gitconfig
 hamedan_area
 handle_csv
 .ipython
 .local
 .mozilla
 Music
 .npm
 .oh-my-zsh
 package-lock.json
 Pictures
 .pki
 Public
 .shell.pre-oh-my-zsh
 .ssh
 Templates
 .var
 Videos
 .vscode
 .zcompdump-alirezas-parvaresh-5.9
 .zcompdump-alirezas-parvaresh-5.9.zwc
 .zsh_history
 .zshrc
'حلقه و شرط.pdf'
```

# 3.cd 
Changes the current working directory.

## cd : 
```bash
➜  ~ cd Desktop
➜  Desktop 
```

## cd .. :
moves up one directory
```bash
➜  NLP git:(main) ✗ pwd   
/home/reza/dev/NLP
➜  NLP git:(main) ✗ cd .. 
➜  dev pwd
/home/reza/dev
```

## cd ~ :
move frist directory
```bash
➜  NLP git:(main) ✗ pwd
/home/reza/dev/NLP
➜  NLP git:(main) ✗ cd ~  
➜  ~ pwd
/home/reza
```

# 4.mkdir :
Creates a new directory.

```bash
➜  Pictures ls
Camera  Screenshots
➜  Pictures mkdir test 
➜  Pictures ls
Camera  Screenshots  test

```

# 5.rm :
Deletes files or directories.

## rm : 
deletes a file

```bash
➜  Pictures ls
Camera  Screenshots  test  test.py
➜  Pictures rm test.py   
➜  Pictures ls
Camera  Screenshots  test
```

## rm -r : 
deletes a directory recursively

```bash
➜  Pictures ls
Camera  Screenshots  test
➜  Pictures rm -r test
➜  Pictures ls
Camera  Screenshots
```


# 6.cp :

##