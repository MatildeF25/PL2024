import re

txt = """
1. List item 1
2. List item 2
3. List item 3
"""

H1_exp = re.compile("^\#[^#].*$")
H2_exp = re.compile("^\#{2}[^#].*$")
H3_exp = re.compile("^\#{3}[^#].*$")

Bold_exp = re.compile("^\*{2}[^\*].*\*{2}$")
Ita_exp = re.compile("^\*[^\*].*\*$")

Bquote_exp = re.compile("^>.*$")

listP_exp = re.compile("^\d\..*$")

listT_exp = re.compile("^-[^-].*$")

code_exp = re.compile("^`{3}[^`].*\n[\s\S]*?\n`{3}$")

bar_exp = re.compile("^--$")

url_exp = re.compile("^\[\w*\]\([\w\:\/.]*\)$")

foto_exp = re.compile("^!\[[^\]]*\]\(\.{2}\/[^\)]*\)$")

html = """
<!DOCTYPE html>
<html>

"""


#parse do ficheiro markdown
def parse_md():
    m = open("Markdown.md", "r")
    lines = m.readlines()
    html = ""
    for line in lines:
        print(line)
        if H1_exp.match(line):
            print("titulo 1")
            html += "<h1>" + line[2:] + "</h1>"
        elif H2_exp.match(line):
            html += "<h2>" + line[3:] + "</h2>"
        elif H3_exp.match(line):
            html += "<h3>" + line[4:] + "</h3>"
        elif Bold_exp.match(line):
            html += "<b>" + line[2:-2] + "</b>"
        elif Ita_exp.match(line):
            html += "<i>" + line[1:-1] + "</i>"
        elif Bquote_exp.match(line):
            html += "<blockquote>" + line[1:] + "</blockquote>"
        elif listP_exp.match(line):
            html += "<p>" + line[2:] + "</p>"
        elif listT_exp.match(line):
            html += "<ul><li>" + line[2:] + "</li></ul>"
        elif code_exp.match(line):
            html += "<code>" + line[3:-3] + "</code>"
        elif bar_exp.match(line):
            html += "<hr>"
        elif url_exp.match(line):
            html += "<a href=" + line[2:-1] + ">" + line[1:-1] + "</a>"
        elif foto_exp.match(line):
            html += "<img src=" + line[2:-1] + ">"
        else:
            html += "<p>" + line + "</p>"
    return html

html += parse_md()

html+= """
</html>
"""


# criar um ficheiro html
f = open("index.html", "w")
f.write(html)
f.close()

