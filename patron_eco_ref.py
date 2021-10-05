import re


def links():
    txt = open('C:/Users/ivan9/Desktop/anclas.txt', 'r', encoding="utf8")
    filedata = txt.read()
    txt.close()
    auxfile=filedata

    regex = r"[\w,]+\s[\w.,]+\s[\w,.]*\s*[\w,.&]*\s*[\w,.]*\s*[\w,.]*\s*[\w,.]*\s*[(][0-9]{4}[)]"
    url = re.findall(regex, auxfile)
    print(url)
    a=""
    for i in url:
        """ i = str(i) """
        break
        a=str(i[0])
        filedata = filedata.replace(a, '<a target="_blank" href="'+a+'">' +  a + '</a>')
    f = open('C:/Users/ivan9/Desktop/anclasO.txt', 'w', encoding="utf8")
    f.write(filedata)
    f.close()


links()
