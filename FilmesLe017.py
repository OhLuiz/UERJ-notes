filmes={
"drama": ["Cidadão Kane","O Poderoso Chefão"],
"comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
"policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
"guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]
}


pagina = open("filmes.html",'w',encoding='utf-8')
pagina.write("<!DOCTYPE html>\n")
pagina.write("<html lang='pt-BR'>\n")
pagina.write("<head>")
pagina.write("<meta charset='utf-8'>\n")
pagina.write("<title>Filmes</title>\n")
pagina.write("<head>\n")
pagina.write("<body>\n")
pagina.write("Olá!")

for c,v in filmes.items():
    pagina.write("<h1>%s</h1>"%c)
    pagina.write("<ul>")
    for e in v:
        pagina.write("<li>%s</li>"%e)
    pagina.write("</ul>")

pagina.write("""
</body>
</html>
""")
pagina.close()
