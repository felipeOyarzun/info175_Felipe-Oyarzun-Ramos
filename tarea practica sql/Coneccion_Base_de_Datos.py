#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Debe crear un programa python que se conecte la base de datos pos_empresa y muestre en la shell el resultado de las siguientes consultas:
¿Cantidad total de ventas en el año 2013?
¿Precio promedio de venta por producto?
¿Total de ventas (gross_total) por cliente?
¿Total de ventas por cliente en el año 2014?
¿Cantidad y monto total de ventas por día en noviembre de 2013?
¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad?
"""



import sqlite3

def conectar():
    con = sqlite3.connect('pos_empresa.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_total_venta():
    con = conectar()
    c = con.cursor()
    query = "select count(gross_total) as \"cantidad de ventas \" from sale where date like \"2013%\";"
    resultado= c.execute(query)
    total_venta = resultado.fetchall()
    con.close()
    print total_venta

def promedio():
 	con = conectar()
 	c=con.cursor()
 	query = "SELECT round(avg(gross_total)) as \"precio promedio\",product.name from sale_product join product on sale_product.product_id=product.id group by product_id limit 30;"
 	resultado= c.execute(query)
 	for x in resultado:
 		print x
 	con.close()

def total_ventas_clientes():
 	con = conectar()
 	c=con.cursor()
 	query = "SELECT entity.names, count(sale.gross_total) as \"total de ventas por cliente\"from sale join entity on sale.entity_id=entity.id group by sale.entity_id limit 20;"
 	resultado= c.execute(query)	
 	for x in resultado:
 		print x
 	con.close()

def total_ventas_clientes_ano():
 	con = conectar()
 	c=con.cursor()
 	query = "SELECT entity.names, count(sale.gross_total) as \"total de ventas por cliente\" from sale join entity on sale.entity_id=entity.id where sale.date like \"2014%\" group by sale.entity_id limit 20;"

 	resultado= c.execute(query)	
 	for x in resultado:
 		print x
 	con.close()

def total_ventas_noviembre():
 	con = conectar()
 	c=con.cursor()
 	query ="select  date, count(sale.gross_total), sum(sale.gross_total) from sale where sale.date like \"2013-11%\"group by date; " 
 	resultado= c.execute(query)	
 	for x in resultado:
 		print x
 	con.close()
def exe6():
 	con = conectar()
 	c=con.cursor()
 	query ="select quantity, round(sum(gross_total)),product.name from sale_product join product on product.id=sale_product.product_id group by sale_product.product_id order by sale_product.quantity limit 20;"
 	resultado= c.execute(query)	
 	for x in resultado:
 		print x
 	con.close()

obtener_total_venta()
promedio()
total_ventas_clientes()
total_ventas_clientes_ano()
total_ventas_noviembre()
exe6()





