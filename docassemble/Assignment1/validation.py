import re
from docassemble.base.util import *

def check_nric (string):
  string = string.upper()
  
  ## Checking NRIC Format
  regex_pattern = r'[STFG][0-9]{7}[A-Z]'
  if not re.match(regex_pattern, string):    
    validation_error('Invalid Format. Follow the format: "S1234567A".')
  
  ## Checking NRIC Validity
  else:
    ans = int(string[1])*2
    for i in range (0,6):
      ans += int(string[i+2])*(7-i)
  if string[0] == "T" or string[0] == "G":
    ans+=4
      
  x = ans % 11 
      
  d = {0: 'J', 1: 'Z', 2: 'I', 3: 'H', 4: 'G', 5: 'F', 6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'}
  d2 = {0: 'X', 1: 'W', 2: 'U', 3: 'T', 4: 'R', 5: 'Q', 6: 'P', 7: 'N', 8: 'M', 9: 'L', 10: 'K'}

  if (string[0] == "S" or string[0] == "T") and d.get(x) == string[8]:
    return True
  elif (string[0] == "F" or string[0] == "G") and d2.get(x) == string[8]:
    return True
  else: 
    validation_error('The NRIC provided is not valid.')