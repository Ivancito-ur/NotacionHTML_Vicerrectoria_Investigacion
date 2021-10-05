import re


def links():
    txt = open('C:/Users/ivan9/Desktop/anclas.txt', 'r', encoding="utf8")
    filedata = txt.read()
    txt.close()
    auxfile=filedata

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, auxfile)


    a=""
    for i in url:
        """ i = str(i) """
        a=str(i[0])
        filedata = filedata.replace(a, '<a target="_blank" href="'+a+'">' +  a + '</a>')
    f = open('C:/Users/ivan9/Desktop/anclasO.txt', 'w', encoding="utf8")
    f.write(filedata)
    f.close()


links()
