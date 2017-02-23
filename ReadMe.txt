Faurecia eSMED v061

The propose of this app is to act like a stopwatch for SMED at injection lines featuring troax systems 

Features:
	- Visual interface with last and best times
	- Polish and Portuguese language
	- Adjustable objective times
	- Data export to Excel file
	- Info related to current line and time

Files:
	- cleardb.py - Script to restart database values
	- country.txt - Keeps track of current language. Updated automaticaly
	- db1_9 - Version 1.9 of database scripts - Queries and inserts data to database
	- eSmed.png - Printscreen of working app
	- eSMED_settings - Settings for app and tranlation lines
	- fau.png - Faurecia small logo 
	- faurecia.png - Faurecia big logo
	- faurecia_V061.py - Python main app script
	- novaDBb.sql - Database parameters
	- ParagensInsert.xml.sql - Database parameters
	- UI10.py - Python interface file
	- UI10.ui - PyQt designer interface file
	- Fonts Folder - Fonts Folder
	- Imagens - Images folder - Contains app images
	- mysql-connector-python - library for mysql connection

Dependencies:
	Software:
	-PyQt4
	-mysql
	-openpyxl
	-mysql connector
	-RPi.GPIO 
	-Other dependencies depending on raspberry firmware version 

	Hardware
	- Raspberry 3 (optimized for RPi3)
	- 24v->5v Relay
	- Troax system

Luís Soares
2017
	