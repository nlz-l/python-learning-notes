/*
 全称:Structured query language 结构化查询语言
 DDL 数据定义语言 增删改查  数据库 数据表 字段
                create drop alter show
 DML 数据操作语言 增删改 (CDU) 表数据
                insert delete update
 DQL 数据查询语言 查(R)       表数据
                select from where
 DCL 数据控制语言 创建用户 设置权限 隔离级别

 分号结尾
 不区分大小写  ctrl+shift+U 快捷更换大小写
 */
#----------------------------------数据库(database)--------------------------------------------
# 创建数据库

#1.机器学习概述. 查看已创建的所有数据库
show databases;

#2. 创建数据库
create database day01;                     #默认utf8
create database day02 character set 'gbk'; #以gbk创建
create database if not exists day01;
# 完整建库格式
create database if not exists day03 charset 'utf8';

#3. 修改数据库 -> 码表 gbk -> utf8
alter database day02 charset 'utf8';

#4. 删除数据库
drop database day01;

#5. 查看当前用的哪个数据库888
select database();

#6. 切换数据库
use day01;


#7. 查看指定某个数据库的数据库码表
show create database day01;
show create database day02;

#------------------------------------数据表(table)------------------------------------
#1.机器学习概述. 切库
use day01;

#2. 查当前数据库中的所有数据表

show tables;

#3. 创建数据表 学生表 字段为 sid 学生id name 学生姓名 age 学生年龄
#格式:
/*
    create table [if not exists] 数据表名(
        字段名 数据类型 [约束],
        字段名 数据类型 [约束],
        字段名 数据类型 [约束],
        .......
    );
 */

create table if not exists student(
  sid int,              #学生姓名
  name varchar(20),     #学生姓名   #varchar 不定长  char 定长(不够空格补齐)
  age int               #学生年龄
);

#4. 修改数据表名 student -> stu
#格式: rename table 旧表名 to 新表名;
rename table student to stu;

#5. 删除数据表
#格式: drop table [if exists] 数据表名;
drop table if exists stu;

#6. 如何查看表结构
# show create table student;
desc student;

#--------------------------------表字段操作(了解)------------------------------------
#实际开发时,建表时都会一般都会多预留2~7个字段当做扩展字段,将来业务扩展变更等,可以启用新的字段
#1.机器学习概述. 切库 查表
use day01;
show tables;
#2. 查看表结构
desc student;
#3. 给student表 添加字段 address varchar(20);
#格式: alter table 表名 add 新列名 数据类型 [约束];
alter table student add address varchar(20) not null;

#4. 修改字段
#1.机器学习概述.只修改数据类型 和 约束
#格式: alter table 表名 modify 旧列名 新的数据类型 [新的约束];
alter table student modify address int;  #约束覆盖
#2.既修改数据类型 和 约束 还修改 字段名
#格式: alter table 表名 change 旧列名 新列名 新的数据类型 [新的约束];
alter table student change address addr varchar(10) not null;
#5. 删除字段
#格式: alter table 表名 drop 旧列名;
alter table student drop addr;



#------------------------------------------常见数据类型-------------------------------------------

# 整型: tinyint smallint int bigint
# 小数类型 : decimal double float
# 字符类型 : varchar(长度) 不定长  char(长度) 定长(不够空格补齐)
# 日期 datetime date time

#-------------------------------------------约束(常用)----------------------------------------------------
/*
单表约束:
 主键: primary key  一般结合auto_increment(自动增长,自增)一起使用
 非空: not null     不能为空
 唯一: unique       不能重复
 默认: default      等价 缺省参数
多表约束:
 外键: foreign key
 */