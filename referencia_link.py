def direccion(e,archivo,revista,volumen):
    e = e+1
    txt = open('D:/UFPS/Practicas _ Coordinacion de Vicerrectoria/Desarrollo Practicas Empresariales UFPS - Vicerrectoria de Investigacion - 2021-2/NotacionHTML_Vicerrectoria_Investigacion/'+revista+'/'+volumen+'/'+archivo+'.html', 'r', encoding="utf8")
    filedata = txt.read()
    txt.close()
    for i in range(1,e):
        i = str(i)

        filedata = filedata.replace(
            "["+i+"]", '<a href="#r'+i+'">' + '[' + i + ']</a>')
        print("Archivo " + archivo + " LISTO REF" + i)

    f = open('D:/UFPS/Practicas _ Coordinacion de Vicerrectoria/Desarrollo Practicas Empresariales UFPS - Vicerrectoria de Investigacion - 2021-2/NotacionHTML_Vicerrectoria_Investigacion/'+revista+'/'+volumen+'/'+archivo+'.html', 'w', encoding="utf8")
    f.write(filedata)
    f.close()

    idReferencia(e,archivo,revista,volumen)



def idReferencia(e,archivo,revista,volumen):
    txt = open('D:/UFPS/Practicas _ Coordinacion de Vicerrectoria/Desarrollo Practicas Empresariales UFPS - Vicerrectoria de Investigacion - 2021-2/NotacionHTML_Vicerrectoria_Investigacion/'+revista+'/'+volumen+'/'+archivo+'.html', 'r', encoding="utf8")
    filedata = txt.read()
    txt.close()
    for i in range(1,e):
        i = str(i)
        filedata = filedata.replace(
            '<p><a href="#r'+i+'">' + '[' + i + ']</a>', '<p id=r'+i+'>['+i+']')

    f = open('D:/UFPS/Practicas _ Coordinacion de Vicerrectoria/Desarrollo Practicas Empresariales UFPS - Vicerrectoria de Investigacion - 2021-2/NotacionHTML_Vicerrectoria_Investigacion/'+revista+'/'+volumen+'/'+archivo+'.html', 'w', encoding="utf8")
    f.write(filedata)
    f.close()


direccion( 71 , archivo="articulo21",revista="Respuestas",volumen="VOL 25 NUM 2_2020")
