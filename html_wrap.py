import os


def save(rep, fname):
    filen = os.path.expanduser(os.getenv('USERPROFILE')) + '\\Documents\\%s.html'%fname
    with open(filen, 'w') as f:
        f.write(rep)
    print(filen)


def html_wrap(txt, name):
    html = '<html><head></head><body>'
    if isinstance(txt, list):
        html += '<b> %s</b>\n'%name
        html += '<table border="1">'
        for row in txt:
            html += '<tr>'
            for c in row:
                html += '<td>' + str(c) + '</td>'
            html += '</tr>'
        html += '</table>'
    html += '</body></html>'
    return html
