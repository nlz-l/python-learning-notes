/*
 单表约束:
 主键: primary key  一般结合auto_increment(自动增长,自增)一起使用
 非空: not null     不能为空
 唯一: unique       不能重复
 默认: default      等价 缺省参数
多表约束:
 外键: foreign key
 */

#-----------------------------------------------演示主键约束-------------------------------------------
use day02;
show tables;
#0. 删表
drop table student;
#1.机器学习概述. 建表时添加主键约束
create table student(
    sid int primary key, #学号
    name varchar(10),    #姓名
    age int              #年龄
    #,primary key(sid)
);
desc student;
#2. 添加数据
insert into student values (1,'张三', 18);
#insert into student values (null,'张三', 18);(id不能为空,如果传入自增,是可以传入null的)
select * from student;
#3. 删除主键约束
alter table student drop primary key;
#4. 建表后,添加主键约束,结合自增
alter table student add primary key(sid);
alter table student modify sid int auto_increment; #增加自增
#4. 再次尝试往表中添加数据
insert into student values(2,'李四',20);
insert into student values(null,'李四',20);# sid=2+1.机器学习概述=3
select * from student;
#delete from 不会重置主键id  truncate table 会重置主键id
delete from student;
insert into student values(null,'李四',20); # 3+1.机器学习概述=4
truncate student;
insert into student values(null,'李四',20); # 1.机器学习概述
#----------------------------------------------------------------------------------------------------
show tables;
# 员工表 id 姓名 手机号 性别 住址
truncate employee;
create table employee(
    eid int primary key auto_increment,
    name varchar(10) not null,
    mobile varchar(11) unique,
    address varchar(10) default '北京'
);
desc employee;
#添加数据
insert into employee values(null,'乔峰', '111', '南院');
insert into employee values(null,null, '11', '飘渺峰'); #姓名不能为空 报错
insert into employee values(null,'乔峰', '111', '飘渺峰');#手机号必须唯一 报错
insert into employee values(null,'乔峰', '222', '飘渺峰');
insert into employee values(null,'乔峰', '333'); #值的个数必须与列的个数一致 报错
insert into employee(eid,name,mobile) values(null,'乔峰', '333');
select * from employee;
