import re

txt = "> "

H1_exp = re.search("^\#[^#].*$", txt)
H2_exp = re.search("^\#{2}[^#].*$", txt)
H3_exp = re.search("^\#{3}[^#].*$", txt)

Bold_exp = re.search("^\*{2}[^\*].*\*{2}$",txt)
Ita_exp = re.search("^\*[^\*].*\*$",txt)

Bquote_exp = re.search("^>.*$", txt)




if Bquote_exp:
  print("YES! We have a match!")
else:
  print("No match")