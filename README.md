# Dict-Cracker
Dict Cracker is a simple UNIX password cracker written in python.<br/>
<br />It is a Command Line based tool to crack passwords of UNIX OS.<br/>
<br/>It takes a Password file(Shadow file) of UNIX systems and a Dictionary file as inputs.<br />
<br/>You can also Run this in Termux.
# How To Install
To USE this script type the following Commands<br/>
```
git clone https://github.com/vraghuvaran/Dict-Cracker.git
```
```
cd Dict-Cracker
```
# Usage
```
python dict-cracker.py -h

Usage:  dictcracker.py [options] -f <passwd file> -d <dictionary file>

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f TFILE, --file=TFILE
                        specify the file name;
  -d TDICT, --dict=TDICT
                        specify the dict file

```
# Note
The strings in the password file should be like same as the strings in the UNIX shadow file.<br/>
```
bob:$1$9691cSVC$zN/LWa6NNAYADAZXUMGIV0:15582:0:99999:7:::
```
Make sure that you have successfully Installed python2.

# Contact
For any Queries :)
```
Mail : oldmonk.h@gmail.com
```
