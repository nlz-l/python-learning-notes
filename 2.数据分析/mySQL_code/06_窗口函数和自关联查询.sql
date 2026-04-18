#----------------------------------------------窗口函数---------------------------------------------------
# 主要用于分组排名
/*
 窗口函数 over([partition by 分组字段 order by 排序字段 asc | desc] rows between ... and ...)
 常用的窗口函数
 row_number(): 执行标记的:1,2,3,4
 rank():       稀疏排名的:1,2,2,4
 dense_rank    密集排名的:1,2,2,3
不写partition by 统计的是全表数据 写了是组内数据
不写order by     统计组内所有数据 写了是组内从第一行,截至到当前行的数据
 */
drop database day03;
create database day03;
use day03;
show tables;


create table employee (
    id int,                 # 员工id
    ename varchar(20),      # 员工名
    deptid int,             # 部门id
    salary decimal(10,2)    # 工资
);
insert into employee values(1,'刘备',10,5500.00);
insert into employee values(2,'赵云',10,4500.00);
insert into employee values(2,'张飞',10,3500.00);
insert into employee values(2,'关羽',10,4500.00);

insert into employee values(3,'曹操',20,1900.00);
insert into employee values(4,'许褚',20,4800.00);
insert into employee values(5,'张辽',20,6500.00);
insert into employee values(6,'徐晃',20,14500.00);

insert into employee values(7,'孙权',30,44500.00);
insert into employee values(8,'周瑜',30,6500.00);
insert into employee values(9,'陆逊',30,7500.00);

select *,'666' from employee;
select *,10/3 from employee;

select
    *,
    sum(salary) over (partition by deptid order by salary desc ) as total_sum

from
    employee;

select
    *,
    row_number() over (partition by deptid order by salary desc ) as rn,
    rank() over (partition by deptid order by salary desc ) as ra,
    dense_rank() over (partition by deptid order by salary desc ) as der
from
    employee;


select * from (
    select
    *,
    rank() over (partition by deptid order by salary desc) rk
from
    employee
) t1
where
    rk <=2;

with t1 as (select *, rank() over (partition by deptid order by salary desc) rk from employee)
select * from t1 where rk <=2;
# ------------------------------------------ 多表查询 自关联查询 ------------------------------------------

# ---------------------- 案例6: 多表查询 自关联查询 ----------------------
/*
解释:
    表自己和自己做关联查询, 称之为: 自关联(自连接)查询.
写法:
    可以是交叉查询, 内连接, 外连接...
经典案例:
    行政区域表 -> 省市区.

例如: 记录省市区的信息,
    复杂的写法: 搞三张表, 分别记录省, 市, 区的关系.
    简单的写法: 用1张表存储, 然后用的时候, 通过 自关联查询 实现即可.
        字段: 自身id    自身名字    父级id
            410000     河南省      0

            410100     郑州市      410000
            410200     开封市      410000
            410300     洛阳市      410000
            410700     新乡市      410000

            410101     二七区      410100
            410102     经开区      410100
            410701     红旗区      410700
            410702     卫滨区      410700
            410721     新乡县      410700
*/
show tables;
select * from areas;
select * from areas where title='吉林省';
select * from areas where pid = '220000';
select * from areas where pid = '220500';
select * from areas where id = '220524';

select
    province.id, province.title,    # 省的id, 名字
    city.id, city.title,            # 市的id, 名字
    county.id, county.title         # 县区的id, 名字
from
    areas as county   #县区表
join
    areas as city on county.pid = city.id     #市区表
join
    areas as province on city.pid = province.id;  #省级表

select
    province.id, province.title,    # 省的id, 名字
    city.id, city.title,            # 市的id, 名字
    county.id, county.title         # 县区的id, 名字
from
    areas as county     # 县区
join
    areas as city on county.pid = city.id    # 市
join
    areas as province on city.pid = province.id    # 省
where
    county.id='220524';