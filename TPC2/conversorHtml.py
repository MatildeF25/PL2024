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

code_exp = re.compile("^`[^`].*[^`]`$")

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
        if H1_exp.match(line):
            html += "\t<h1>" + line[2:-1] + "</h1>\n"
        elif H2_exp.match(line):
            html += "\t<h2>" + line[3:-1] + "</h2>\n"
        elif H3_exp.match(line):
            html += "\t<h3>" + line[4:-1] + "</h3>\n"
        elif Bold_exp.match(line):
            html += "\t<b>" + line[2:-3] + "</b>\n"
        elif Ita_exp.match(line):
            html += "\t<i>" + line[1:-2] + "</i>\n"
        elif listP_exp.match(line):
            if(html[-7:] == "\t</ol>\n"):
                html = html[:-7]
                html += "\t\t<li>" + line[2:-1] + "</li>\n"
                html += "\t</ol>\n"
            else:
                html += "\t<ol>\n"
                html += "\t\t<li>" + line[2:-1] + "</li>\n"
                html += "\t</ol>\n"
        elif listT_exp.match(line):
            if(html[-7:] == "\t</ul>\n"):
                html = html[:-7]
                html += "\t\t<li>" + line[2:-1] + "</li>\n"
                html += "\t</ul>\n"
            else:
                html += "\t<ul>\n"
                html += "\t\t<li>" + line[2:-1] + "</li>\n"
                html += "\t</ul>\n"
        elif code_exp.match(line):
            html += "\t<code>" + line[1:-2] + "</code>\n"
        elif url_exp.match(line):
            n_var, url = url_vars(line)
            html += "\t<a href=" + url + ">" + n_var + "</a>\n"
        elif foto_exp.match(line):
            link, alt = foto_var(line)
            html += "\t<img src=" + link + " alt= " + alt + "/>\n"
    return html


def url_vars (line):
    n_var = ""
    url = ""
    for i in range(len(line)):
        if line[i] == "]":
            n_var = line[1:i]
        elif line[i] == "(":
            url = line[i+1:-1]
    return n_var, url

def foto_var (line):
    link = ""
    alt = ""
    for i in range(len(line)):
        if line[i] == "(":
            link = line[i+1:-1]
        elif line[i] == "]":
            alt = line[2:i]
    return link, alt

            




html += parse_md()

html+= """
</html>
"""


# criar um ficheiro html
f = open("index.html", "w")
f.write(html)
f.close()

