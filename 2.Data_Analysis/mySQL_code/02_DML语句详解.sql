/*
DML 数据操作语言 增删改 (CDU) 表数据
                insert delete update
删改前一定要备份
    添加数据:
        insert into 数据表名(列名1..)(列名2..) value(值1..)(值2..)
        insert into 数据表名 value(值1..)(值2..)
        insert into 数据表名 value(值1..)(值2..), (值1..)(值2..)
 */

#--------------------------------------------表数据 增------------------------------------
#1.机器学习概述. 切表 查表
use day01;
show tables;

#2. 创建分类表  分类id,分类名,描述信息
create table category(
    cid int,
    cname varchar(20),
    info varchar(100)
);
#3. 往表中添加数据

insert into category(cid, cname) values(1,'电脑');
insert into category values(2,'手机', '华为666' );
insert into category values(3,'汽车', '小米'), (4, '平板', '华为');

#4. 查看表中数据
select * from category;

#--------------------------------------------表数据 改----------------------------------------------------
/*格式:
  update 数据表名 set 字段名=值... where 条件;
  truncate table 数据表名;
 */
#1.机器学习概述. 查看表中数据
select * from category;
#2. 修改cname = '空调',info='格力',cid=3
update category set cname='空调',info='格力' where cid=3;
update category set cname='汽车',info=null where cid=1;

#----------------------------------------------表数据 删-----------------------------------------------

# delete from
delete from category where cid=4;
delete from category; #全删,不重置主键id

truncate table category;#全删,重置主键id

#----------------------------------------------备份数据表------------------------------------------------
show tables;

select * from category;
#1.机器学习概述. 备份表不存在
#格式 create table 备份表名 select * from 原表名 where ...;
create table category_tmp select * from category;
select * from category_tmp;
delete from category_tmp;

#2. 备份表存在
#insert into 备份表名 select * from 原表名 where cid<=3;
insert into category_tmp select * from category where cid<=3;