# potatoCookieBruteforcer
A naab python script to bruteforce cookies. 

----------------------------------------------------------------

The script requires four arguments which are the following:

  -u URL of the host
  
  -c Name of the cookie to bruteforce
  
  -w Wordlist to use
  
  -n A string from HTTP response which indicates a negative try
  
  
 ----------------------------------------------------------------
 
Example usage:

python gimmiThatCookie.py -u http://192.168.1.2 -w myWordlist.txt -c secretCookie -n "Cookie incorrect"
