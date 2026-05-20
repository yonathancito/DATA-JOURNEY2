select * from ventas;

select region, vendedor, ventas
from ventas
where ventas > 1000
order by ventas desc;

select producto, ventas
from ventas
order by ventas desc
limit 5;


