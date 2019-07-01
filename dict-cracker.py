import optparse
import crypt
import threading
import os


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0;47m'  # white
B = '\033[94m' #blue
BOLD = '\033[1m' 
ENDC = '\033[0m'
M='\033[35m' #magenta 


screenlock=threading.Semaphore(value=1)

p=['!','@','#','$','&','*','%','!!']
version='1.0'
def testpass(tdict,hash,user):
   salt='$'+hash.split('$')[1]+'$'+hash.split('$')[2]
   f=open(tdict,'r')
   for x in f.readlines():
       x=x.strip('\n')
       if crypt.crypt(x,salt)==hash:
           screenlock.acquire()
           print G+'[+] '+C+user+' : '+BOLD+M+x+ENDC
           screenlock.release()
           return
   f.close()
   screenlock.acquire()
   print B+'[-] '+R+'passwd not found for user '+user.upper()
   screenlock.release()
   return
   
def convert(tfile,tdict):
   f=open(tfile,'r')
   for x in f.readlines():
       if ':' in x:
           user=x.split(':')[0]
           hash=x.split(':')[1]
           screenlock.acquire()
           if (hash not in p) and (user not in p):
               t=threading.Thread(target=testpass,args=(tdict,hash,user))
               t.start()
           else:
               print R+'[-] string in passwd file for '+R+user+R+' in wrong format'
           screenlock.release()    
   f.close()
def banner():
   
   os.system('clear')
       
   #print W+'''
   print '###################################################################################  '
   print '#  __ __      __ __ __ ___ __   __ __   __     __ __    __ __         __ __  __    # '
   print '# |     \ |  /          |      /       |   \  /     \  /       |   / |      |   \  # '
   print '# |     | | |           |     |        |   | |       ||        |  /  |      |    | # '
   print '# |     | | |           |     |        |__ / |__ __ _||        | /   |__ __ |__ /  # '
   print '# |     | | |           |     |        |\    |       ||        | \   |      | \    # '
   print '# |__ __/ |  \__ __     |      \__ __  | \   |       | \__ __  |  \  |__ __ |  \   # '
   print '#                                                                                  # '
   print '###################################################################################  '
    #'''
   print
   #print 
   
   print ('\n' + G + '[>]' + C + ' Created By : ' + BOLD+ 'raghuvaran_guptha'+ENDC)
   print (G + '[>]' + C + ' Version    : ' + BOLD+ version +ENDC+ '\n')
   print G
def main():
   
   banner()
   parser=optparse.OptionParser(usage='Usage : %prog [options] -f <passwd file> -d <dictionary file>',version='Version: dictcracker 1.0')
   parser.add_option('-f','--file',dest='tfile',help='specify the file name;')
   parser.add_option('-d','--dict',dest='tdict',help='specify the dict file')
   (values,keys)=parser.parse_args()
   tfile=values.tfile
   tdict=values.tdict
   if (tfile==None) | (tdict==None):
       print parser.usage
       quit()
   print
   print BOLD+'[*] OUTPUT FORMAT :)'
   print '[*] USERNAME : PASSWORD'+ENDC
   print
   convert(tfile,tdict) 

if __name__=='__main__':
   main()
       