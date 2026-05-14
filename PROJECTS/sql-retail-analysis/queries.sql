-- ver data sets
select * from ventas;
-- top ventas
select * from ventas order by ventas desc;
-- region mas fuerte
select * from ventas where region = 'Lima';
-- ventas grandes
select * from ventas where ventas > 1000 order by ventas desc;
-- top 3 ventas
select * from ventas order by ventas desc limit 3;