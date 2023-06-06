# Ejercicio 1: De la base de datos dada. Extraer agentes cuyo nombre empieza por M o termina en O.

SELECT * FROM agents WHERE `name` LIKE "M%" OR `name` LIKE "%O"; # 2 agentes

 # ---------------------------------------------------------------------------------------------------------- #
 
 # Ejercicio 2: De la base de datos dada. Escribir una consulta que produzca una lista, en orden alfabético, de todas las distintas ocupaciones en la tabla Customer que contengan la palabra "Engineer".
 
 SELECT DISTINCT occupation FROM customers WHERE occupation LIKE "%Engineer%" ORDER BY occupation ASC; # 361 registros

# ---------------------------------------------------------------------------------------------------------- #

# Ejercicio 3: De la base de datos dada. Escribir una consulta que devuelva el ID del cliente, su nombre y una columna nueva llamada “Mayor30” que contenga "Sí" si el cliente tiene más de 30 años y "No" en caso contrario.

SELECT customerid, `name`, IF(age > 30, "Si", "No") AS Mayor30 FROM customers;

# ---------------------------------------------------------------------------------------------------------- #

# Ejercicio 4: De la base de datos dada. Escribir una consulta que devuelva todas las llamadas realizadas a clientes de la profesión de ingeniería y muestre si son mayores o menores de 30, así como si terminaron comprando el producto de esa llamada.

SELECT 
	calls.callid, 
	calls.customerid, 
	c.occupation, 
	IF(c.age > 30, "Si", "No") AS Mayor30,
	calls.productsold as `ProductId`,
	IF(calls.productsold > 0, "Si", "No") AS `Compra Realizada`
FROM calls 
inner join customers c ON c.customerid = calls.customerid
WHERE c.occupation LIKE "%Engineer%";


# ---------------------------------------------------------------------------------------------------------- #

# Ejercicio 4: De la base de datos dada. Escribir dos consultas: 

# 1. Una que calcule las ventas totales y las llamadas totales realizadas a los clientes de la profesión de ingeniería.
SELECT 
	c.name AS `Cliente`, 
	COUNT(*) AS `Ventas Realizadas` 
FROM calls
INNER JOIN customers c ON c.customerid = calls.customerid
WHERE calls.productsold > 0
AND c.occupation LIKE "%Engineer%"
GROUP BY calls.customerid;

# 2. Otra que calcule las mismas métricas para toda la base de clientes.
SELECT 
	COUNT(*) AS `Ventas Totales Realizadas` 
FROM calls
INNER JOIN customers c ON c.customerid = calls.customerid
WHERE calls.productsold > 0;

# ---------------------------------------------------------------------------------------------------------- #

# Ejercicio 5: De la base de datos dada. Escribir una consulta que devuelva 
# Para cada agente: el nombre del agente, la cantidad de llamadas, las llamadas más largas y más cortas,
# la  duración promedio de las llamadas y la cantidad total de productos vendidos. 
# Nombra las columnas: AgentName, NCalls, Shortest, Longest, AvgDuration y TotalSales
# Luego ordenar la tabla por: AgentName en orden alfabético.

# Consejo: Asegurarse de incluir la cláusula WHERE PickedUp = 1 para calcular solo el promedio de todas las llamadas que fueron atendidas (de lo contrario ¡todas las duraciones mínimas serán 0!)

SELECT * FROM calls;
SELECT 
	a.`name` AS `AgentName`,
	COUNT(c.agentid) AS `NCalls`,
	MIN(c.duration) AS `Shortest`,
	MAX(c.duration) AS `Longest`,
	SUM(c.duration)/COUNT(c.agentid) AS `AvgDuration`,
	COUNT(c.productsold) AS `TotalSales`
FROM agents AS a
INNER JOIN calls c ON c.agentid = a.agentid
WHERE c.pickedup = 1
GROUP BY a.agentid
ORDER BY a.`name` ASC;

# ---------------------------------------------------------------------------------------------------------- #

# Ejercicio 7: De la base de datos dada. Escribir una consulta que extraiga dos métricas del desempeño de los agentes de ventas que le interesan a su empresa: 

# 1. Para cada agente, cuántos segundos en promedio les toma vender un producto cuando tienen éxito.
SELECT 
	agents.`name`,
	AVG(c.duration)
FROM agents
INNER JOIN calls c ON c.agentid = agents.agentid
WHERE pickedup = 1 AND productsold > 0
GROUP BY agents.agentid;

# 2. Para cada agente, cuántos segundos en promedio permanecen en el teléfono antes de darse por vencidos cuando no tienen éxito.
SELECT 
	agents.`name`,
	AVG(c.duration)
FROM agents
INNER JOIN calls c ON c.agentid = agents.agentid
WHERE pickedup = 1 AND productsold = 0
GROUP BY agents.agentid;
