# why this regular expersion  is used for
import re
text= "Vishal Attri is learning python. python is programming language. python is easy to learn."
pattern= "python"
result= re.findall(pattern,text)
print("FINDALL RESULT IS :", result)