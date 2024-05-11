# -*- coding: utf-8 -*-
# server_version.py - retrieve and display database server version

import MySQLdb
import time, codecs
from reportlab.pdfgen import canvas
from jToolkit.widgets import widgets
from jToolkit.widgets import table
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, LETTER, landscape, portrait 
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm
from mod_python import apache

def recortar(texto,sizeline):
	
	if(texto.find("a href") > 0):
		inia = texto.find("<a href=")
		
		ini1 = texto.find("'>")
		ini2 = texto.find("\">")
		
		if ini1 > ini2:
			ini = ini1
		else:
			ini = ini2
			
		fini = texto.find("</a>")
		bueno = texto[ini+2:fini]
		texto = texto[:inia]+ bueno + texto[fini+4:]
		
	#j = sizeline
	aux9 = texto
	a = 0
	last = 0
	old = 0
	num_chars = len(texto)
	for i in range(num_chars):
		if texto[i] == " ":
			last = i
		if a == sizeline:
			aux9 = aux9[0:last] + '\n' + aux9[last+1:]
		i = last
		a = a + 1
	return aux9
	



def index(req):
  # Our container for 'Flowable' objects
	elements = []

	# A large collection of style sheets pre-made for us
	styles = getSampleStyleSheet()

	# A basic document for us to write to 'rl_hello_table.pdf'
	doc = SimpleDocTemplate('/var/www/htdocs/tcs/robust/files/programme.pdf', title="Robust Programme")
	doc.pagesize = portrait(A4)

	portrait((595.275590551, 841.88976378))

	date  = time.asctime(time.localtime())
	elements.append(Paragraph("Emergence and design of Robustness Programme", styles['Title']))
	elements.append(Paragraph("General principles and applications to biological, social and industrial networks", styles['Normal']))
	elements.append(Paragraph("IFISC, Palma de Mallorca, September 21-25, 2010\n\n\n\n", styles['Normal']))
	elements.append(Paragraph(" ", styles['Normal']))


	#Funcion que pinta una tabla con los datos de los speakers
	conn = MySQLdb.connect (host = "ifisc.uib-csic.es",
														user = "congresos",
														passwd = "0r0tana",
														db = "robust")
	cursor = conn.cursor ()
	cursor.execute ("SELECT * FROM program ORDER BY columna")

	rows = cursor.fetchall ()
	data = []
	#id 0 , hora 1, titulo 2, columna 3, tipo 4

	i = 1

	normal = [
			('ALIGN', (0,0), (-1,-1), 'LEFT'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			#('BACKGROUND', (0,0), (-1,0), colors.orange),
			('FONT', (0,0), (-1,0), 'Helvetica'),
		('GRID', (0,0), (-1,-1), 0.2, colors.black),
			##('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),
	## The bottom row has one line above, and three lines below of
	## various colors and spacing.
			#('LINEABOVE', (0,-1), (-1,-1), 1, colors.purple),
			#('LINEBELOW', (0,-1), (-1,-1), 0.5, colors.purple,
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]

	day = [
			('ALIGN', (0,0), (-1,-1), 'LEFT'),
			('FONTSIZE', (0,0), (-1,-1), 10),
			#('BACKGROUND', (0,0), (-1,0), colors.orange),
			('FONT', (0,0), (-1,0), 'Helvetica'),
			##('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),
	## The bottom row has one line above, and three lines below of
	## various colors and spacing.
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]
			
	event = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			#('FONTSIZE', (7,0), (9,0), 8),
			('FONTSIZE', (0,0), (-1,-1), 8),
			#('FONTSIZE', (3,1), (3,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#CD9AFF"),
			('FONT', (0,0), (-1,0), 'Helvetica'),
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),


	## The bottom row has one line above, and three lines below of
	## various colors and spacing.
			#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]
			
	normal = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#FFFFFF"),
			('FONT', (0,0), (-1,0), 'Helvetica'),
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]
			
	invited = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#FFFFD4"),
			('FONT', (0,0), (-1,0), 'Helvetica'),
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]
			
	breaki = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#E6E6E6"),
			('FONT', (0,0), (-1,0), 'Helvetica'),
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),
			]
			
	session = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#9DCD00"),
			('FONT', (0,0), (-1,0), 'Helvetica')
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),


	## The bottom row has one line above, and three lines below of
	## various colors and spacing.
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]

	special = [
			('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
			('FONTSIZE', (0,0), (-1,-1), 8),
			('GRID', (0,0), (-1,-1), 0.2, colors.black),
			('BACKGROUND', (0,0), (-1,0), "#FFA088"),
			('FONT', (0,0), (-1,0), 'Helvetica')
			#('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
			#('BOX', (0,0), (-1,-1), 0.10, colors.grey),


	## The bottom row has one line above, and three lines below of
	## various colors and spacing.
				#1, None, None, 4,1),
			#('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
			#('FONT', (0,-1), (-1,-1), 'Helvetica')
			]

	for row in rows:
		if row[4] == "day":
			if row[2] == "Saturday 25":
				fila = [ "\n \n "+row[2] , "" ]
			else:
				fila = [ "\n"+row[2] , "" ]
			
			data.append(fila)
			table = Table(data, style=day, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "event":
			fila = [ row[1], recortar(row[2], 100).decode("iso-8859-15") ]
			data.append(fila)
			table = Table(data, style=event, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "":
			if row[5] > 0:
				cursor2 = conn.cursor ()
				cursor2.execute ("SELECT * FROM T_ASISTENTES2 WHERE id_asistente=%d" % row[5])
				rows2 = cursor2.fetchall()
				nombre = rows2[0][4]
				apellidos = rows2[0][3]
				talk_title = rows2[0][27]
				todo = "<b>%s %s</b><br/><i>%s</i>" % (nombre, apellidos, talk_title)
			else:
				todo = row[2]
			try:
				fila = [ row[1], Paragraph("<font name=Helvetica color=black size=8>"+recortar(todo, 100)+"</font>", styles['Normal']) ]
			except:
				continue
			data.append(fila)
			table = Table(data, style=normal, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "invited":
			if row[5] > 0:
				cursor2 = conn.cursor ()
				cursor2.execute ("SELECT * FROM T_ASISTENTES2 WHERE id_asistente=%d" % row[5])
				rows2 = cursor2.fetchall()
				nombre = rows2[0][4]
				apellidos = rows2[0][3]
				talk_title = rows2[0][27]
				todo = "<b>%s %s</b><br/><i>%s</i>" % (nombre, apellidos, talk_title)
			else:
				todo = row[2]
			try:
				fila = [ row[1], Paragraph("<font name=Helvetica color=black size=8>"+recortar(todo, 100)+"</font>", styles['Normal']) ]
			except:
				continue
			data.append(fila)
			table = Table(data, style=invited, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "break":
			fila = [ row[1], recortar(row[2], 100).decode("iso-8859-15") ]
			data.append(fila)
			table = Table(data, style=breaki, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "session":
			fila = [ row[1], recortar(row[2], 100).decode("iso-8859-15") ]
			data.append(fila)
			table = Table(data, style=session, colWidths=[60, 380])
			elements.append(table)
			data = []
		elif row[4] == "special":
			fila = [ row[1], recortar(row[2], 100).decode("iso-8859-15") ]
			data.append(fila)
			table = Table(data, style=special, colWidths=[60, 380])
			elements.append(table)
			data = []		
	#elements.append(Paragraph(date, styles['Normal']))

	cursor.close ()
	conn.close ()
	
	# Write the document to disk
	doc.build(elements)

#Pintamos por browser
#print file(r"/tmp/speakers.pdf", "rb").read()

	#return file(r"/tmp/speakers.pdf", "rb").read();

	req.headers_out.add("Location", 'http://ifisc.uib-csic.es/robust/files/programme.pdf')
	raise apache.SERVER_RETURN, apache.HTTP_SEE_OTHER
