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
cd dict-cracker.py
```
Now you can Execute Dict-Cracker by typing <br/>
```
python dict-cracker.py -f <password file> -d <dictionary file>
```
# Note
The strings in the password file should be like the same the string in the UNIX shadow file<br/>
```
bob:$1$9691cSVC$zN/LWa6NNAYADAZXUMGIV0:15582:0:99999:7:::
```
