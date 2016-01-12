#Creates the HTML File
import os,datetime

def createFile(filepath):
    
    fileName = os.path.basename(filepath)
    
    htmlPath = filepath + ".html"
    html = open(htmlPath,'w')
    
    struct = """<!doctype html>\n<html>\n<head>\n<style type="text/css">\nbody { background-color:#E0E0E0; font-family:Arial; font-size: 80%; }\n#toplink { right:0; position:fixed; bottom:0px; }\ntd { text-align: center }\n</style>\n"""
    title = """<title>Static Malware Analysis - %s</title>\n</head>\n<body>\n"""%fileName
                
    links = """<ul>\n<li><a href = '#globals'>File Informations</a></li>\n<li><a href = '#version'>File Version Info</a></li>\n<li><a href = '#checksums'>File Checksums</a></li>\n<li><a href = '#sections'>Sections</a></li>\n<li><a href = '#strings'>Strings</a></li>\n<li><a href = '#imports'>Imports</a></li>\n<li><a href = '#suspicious'>Suspicious APIs</a></li>\n<li><a href = '#exports'>Exports</a></li>\n<li><a href = '#resources'>Resources</a></li>\n<li><a href = '#virus'>VirusTotal</a></li>\n</ul>\n"""
              
    time = datetime.datetime.now()
    
    top = """<div id='toplink'><b><a href="#">TOP</a></b> created %s </div>"""%time.strftime("%Y-%m-%d %H:%M")
    
    html.write("%s %s %s %s" %(struct,title,links,top))
    html.write("<b><a id='globals'>File Informations:</a></b><br>File Name: %s<br>" %fileName)
    
    return html

def closeFile(html):
    
    end = """</body>
             </html>"""
                
    html.write(end)

def insertSeperator(html):
    
    sep = """<hr style="float:left; width:100%; height:1px; border:1px solid; border-color:#2c2c2c;">"""
    
    html.write(sep)