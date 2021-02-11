def postage(x):
  if (x<1):
    return 6.85
  if(x>=1):
    if(x<2):
     return 7.32
  if(x>=2):
    if(x<3):
     return 7.51
  if (x>=3):
    if(x<4):
     return 7.61
  if (x>=4):
    if(x<5):
     return(7.71)
  if (x>=5):
    return 8.5   

def grade(x):
  if(x<=100):
    if(x>=90):
      return("A")
  if(x<90):
    if(x>=80):
      return("B")
  if(x<80):
    if(x>=70):
      return("C")
  if(x<70):
    if(x>=60):
      return("D")
  if(x>=0):
    if(x<60):
      return("F")    

def feedback(a,b,c,d):
  result = "You are "
  if(a is True):
    result = result + "the "
  if(a is False):
    if(b==0):
      result = result +"a "
    if(b==2):
      result = result +"a "
    if(b==4):
      result = result +"a "
    if(b==1):
      result = result +"an "
    if(b==3):
      result = result +"an "
    if(b==5):
      result = result +"an "
  if(b==0):
    result = result + "very "
  if(b==1):
    result = result + "extremely "
  if(b==2):
    result = result + "least "
  if(b==3):
    result = result + "absolutely "
  if(b==4):
    result = result + "most "
  if(b==5):
    result = result+ "absurdly "
  if(c==0):
    result = result+"solid "
  if(c==1):
    result = result+"good "
  if(c==2):
    result = result+"proficient "
  if(c==3):
    result = result+"colorful "
  if(c==4):
    result = result+"bland "
  if(c==5):
    result = result+"renowned "      
  if(d=="m"):
    result = result+"mathematician"
  if(d=="r"):
    result = result+"runner"
  if(d=="p"):
    result = result+"physicist"
  if(d=="s"):
    result = result+"sloth"
  if(d=="P"):
    result = result+"politician"
  if(d=="b"):
    result = result+"biologist"
  if(d=="o"):
    result = result+"ornithologist"
  if(d=="h"):
    result = result+"herpetologist"  
  if(d=="z"):
    result = result+"zoologist"
  return result



