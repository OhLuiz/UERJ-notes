pagina = open('pagina.html','w',encoding = 'utf-8')
pagina.write("<!DOCTYPE html>\n")
pagina.write("<html lang='pt-BR'>\n")
pagina.write("<head>")
pagina.write("<meta charset='utf-8'>\n")
pagina.write("<title>Titulo da pagina</title>\n")
pagina.write("<head>\n")
pagina.write("<body>\n")
pagina.write("Olá!")

for i in range(10):
    pagina.write('<p>%d<\p>\n'%i)

pagina.write("</body>\n")
pagina.write("</html>\n")
pagina.close()
