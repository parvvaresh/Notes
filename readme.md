# Basic command Linux


# Content




# File and Directory Management

## 1.  cd 
Changes current directory

``` bash
cd /directory
```
for example : 

```bash
cd Desktop
```
Changes current directory to Desktop


## 2. cd ..

Changes to the parent directory 

```bash
cd ..
```
example : 

```bash

 reza@parvaresh  ~   main ±✚  cd Desktop
 reza@parvaresh  ~/Desktop/main ±✚  cd projects 
 reza@parvaresh  ~/Desktop/projects/main ±✚  cd ..      
 reza@parvaresh  ~/Desktop / main ±✚ 

```

## 3.  cd ~

Changes to the previous directory


```bash
cd ~
```
example : 

```bash
 reza@parvaresh  ~   main ±✚  cd Desktop
 reza@parvaresh  ~/Desktop   main ±✚  cd projects
 reza@parvaresh  ~/Desktop/projects   main ±✚  cd eval-targoman
 reza@parvaresh  ~/Desktop/projects/eval-targoman   master ±✚  cd metric       
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric   master ±✚  pwd
/home/reza/Desktop/projects/eval-targoman/metric
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric   master ±✚  cd ~          
 reza@parvaresh  ~  main ±✚  pwd
/home/reza

```
## 4. cd -

Changes to the previous directory

```bash
cd -
```

example:




## 5. pwd

Prints the current working directory
```bash
pwd
```
example : 

```bash
reza@parvaresh  ~/Desktop  main  pwd
/home/reza/Desktop
```
## 6. ls
Lists contents of the current directory
```bash
ls
```
example : 

```bash
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric ls
bleu_score.py  chrf_score.py  gleu_score.py  meteor_score.py  nist_score.py  __pycache__  tool  wer_score.py
```

## 7. ls -l
Lists the files and directories in the
current working directory in long format
```bash
ls -l
```
example :

```bash
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric  ls -l 
total 40
-rwxrwxrwx 1 reza reza 1752 دسامبر  12 11:07 bleu_score.py
-rwxrwxrwx 1 reza reza 4257 دسامبر   6 15:05 chrf_score.py
-rwxrwxrwx 1 reza reza 1277 دسامبر   5 20:45 gleu_score.py
-rwxrwxrwx 1 reza reza 4772 دسامبر   5 20:45 meteor_score.py
-rwxrwxrwx 1 reza reza 2359 دسامبر  12 16:45 nist_score.py
drwxrwxrwx 2 reza reza 4096 دسامبر  16 12:11 __pycache__
drwxrwxrwx 3 reza reza 4096 نوامبر   3 14:51 tool
```

## 8. ls -a
Lists all files and directories including the
hidden ones
```bash
ls -a
```

exmaple : 
```bash
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric  ls -a
.  ..  bleu_score.py  chrf_score.py  gleu_score.py  meteor_score.py  nist_score.py  __pycache__  tool  wer_score.py

```

## 9. ls -r

Lists files/directories in reverse

```bash 
ls -r
```

exmaple : 

```bash
 reza@parvaresh  ~/Desktop/projects/eval-targoman/metric  ls -r
wer_score.py  tool  __pycache__  nist_score.py  meteor_score.py  gleu_score.py  chrf_score.py  bleu_score.py

```

