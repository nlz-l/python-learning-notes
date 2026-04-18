## 数据库相关概述

* 问题1: 你知道的存储数据的方式有哪些?

  > 变量, 列表, 字典: 只能对数据**临时存储**, 程序执行结束, 数据就丢失了.
  >
  > 文件: 可以对数据**永久存储**, 但是不方便用户进行精细化管理. 
  >
  > **数据库:** 存储数据的仓库, 本质上就是1个文件系统, 可以有规律的对数据进行存储, 方便用户进行精细化管理(CURD).      C -> Create(增),  U -> Update(改), R -> Read(查),  D -> Delete(删)
  >
  > **实际开发中, 数据库才是真正存储数据的地方.**

* 问题2: 数据库的划分?

  > 关系型数据库:     采用**数据表**来存储数据, 表与表之间有关系, 例如: **多对多, 一对多, 一对一.**
  >
  > 非关系型数据库: 一般采用**Key-Value**的形式存储数据.

* 问题3: 常见的数据库有哪些?

  > 关系型数据库:
  >
  > ​	MySQL, Oracle, SQLServer, DB2, SQLite...
  >
  > 非关系型数据库:
  >
  > ​	Redis, HBase, MongoDB(文档型数据库)

## MySQL环境搭建

* 安装MySQL数据库

  * 方式1: 直接使用我给的虚拟机中的MySQL数据库即可, 已经搭建完毕, 无需手动安装.

    > 账号: root
    >
    > 密码: 
    >
    > ​	windows系统, Mac(Intel系列) -> 123456
    >
    > ​	Mac(M系列) -> 1234

  * 方式2: 手动去MySQL官网下载安装包, 手动安装到本机(windows系统, Mac系统即可).

    > 官网: www.mysql.com
    >
    > 直接下载网址: https://downloads.mysql.com/archives/community/

  * 方式3: 使用小皮工具进行安装.

    > 小皮 -> PhpStudy软件, 专门为了部署各种服务级软件而生. 
    >
    > 官网: https://old.xp.cn/
    >
    > #具体的步骤
    >
    > 1. 安装小皮软件, 此处略, 下一步下一步即可, 安装路径要合法, 不要出现中文, 空格等.
    > 2. 通过小皮软件, 安装MySQL8.X 数据库, 网速要好.
    > 3. 启动MySQL8.X数据库 或者 启动MySQL5.X数据库.
    > 4. 修改MySQL的引擎, 从MyIsam(不支持事务, 约束) -> 改为: InnoDB(支持事务, 约束)
    > 5. 修改MySQL的密码, 默认是: root, 可以改为: 123456

    ![1734314298282](assets/1734314298282.png)

    ![1734314427256](assets/1734314427256.png)

    ![1734314561628](assets/1734314561628.png)

    ![1734314669750](assets/1734314669750.png)

## MySQL的登陆和登出

* 登陆

  * 方式1: 明文登陆

    > 格式: mysql -u账号 -p密码

    ![1734315082387](assets/1734315082387.png)

  * 方式2: 暗文登陆

    > mysql -u root -p			# 敲回车
    >
    > 输入密码				# 敲回车

    ![1734315212174](assets/1734315212174.png)

  * 方式3: 远程访问.

    > 格式: mysql --host=主机名 --user=mysql数据库的账号 --password=mysql数据库的密码

    ![1734315310544](assets/1734315310544.png)

* 登出

  > 方式1: exit
  >
  > 方式2: quit
  >
  > 方式3: ctrl + d

* 扩展: 如果你想用本机的小皮, 需要**给小皮配置环境变量**才可以实现: 在任意的路径下都能访问小皮.

  ![1734315763863](assets/1734315763863.png)

  ![1734315808469](assets/1734315808469.png)

## DataGrip连接MySQL

* 安装DataGrip软件

  > 此处略, 详见讲义, 因为它和PyCharm都是属于JetBrains公司的产品, 所以安装, 激活, 常见设置都是一样的操作. 
  >
  > 下载网址: https://www.jetbrains.com/datagrip/download/other.html

* 配置DataGrip连接MySQL

  1. 新建工程

     ![1734317700089](assets/1734317700089.png)

  2. 选择新工程的打开方式.

     ![1734317750109](assets/1734317750109.png)

  3. 选择要连接到的数据库

     ![1734317814762](assets/1734317814762.png)

  4. 配置连接信息即可.

     ![1734318227334](assets/1734318227334.png)

     ![1734318114958](assets/1734318114958.png)

     ![1734318339811](assets/1734318339811.png)

* 扩展

  1. DataGrip连接小皮(windows本地, Mac本地)的MySQL.

     ![1734318521882](assets/1734318521882.png)

     ![1734318729329](assets/1734318729329.png)

  2. PyCharm(必须是专业版)连接 Linux 或者 本机(Windows, Mac)的数据库.

     ![1734318911388](assets/1734318911388.png)

     ![1734319048304](assets/1734319048304.png)

     ![1734319148783](assets/1734319148783.png)

* 图解

  ![1734319403724](assets/1734319403724.png)

## DataGrip的基本设置

* 基本配置

  ![1734320780317](assets/1734320780317.png)

* 常用的插件推荐

  ![1734320833268](assets/1734320833268.png)

## SQL语句介绍

* 图解

  ![1734322225837](assets/1734322225837.png)

* 特点

  1. SQL语句可以写成一行, 也可以写成多行. 

  2. 如果SQL语句写了多行, 为了阅读方便, 可以增加缩进, 空格等, 方便查看格式. 

  3. SQL不区分大小写, 建议关键字大写, 其它小写.

  4. SQL语句中注释的写法.

     > /*
     >
     > ​	多行
     >
     > ​	注释
     >
     > */
     >
     > #单行注释
     >
     > -- 单行注释			# --后边必须跟空格.

     ```sql
     /*
      多行
      注释
     */
     
     # 单行注释, 为了阅读方便, 可以多加1个空格(也可以不加)
     
     -- 单行注释, --后边必须加空格.
     select * from student;
     ```

* 常用的数据类型

  * 数值型: int, float, double, decimal
  * 字符串型: varchar(n): 不定长, char(n): 定长
  * 日期类型: date, datetime

## DDL语句_操作数据库

```sql
# ------------------- 案例1: DDL语句操作 数据库 -------------------
# 1. 查看当前所有的数据库.
show databases ;

# 2. 删除数据库.
drop database day10;

# 3. 创建数据库.
# 方式1: 数据库存在时, 报错.
create database day01 charset 'utf8';
# 方式2: 数据库存在时, 什么都不做.
create database if not exists day01  charset 'utf8';
# 方式3: 创建数据库, 指定码表.
create database if not exists day02  charset 'gbk';

# 4. 查看两个数据库的详细信息(码表信息)
show create database if not exists day01;   # utf8
show create database if not exists day02;   # gbk -> utf8

# 5. 修改数据库的码表.
alter database day02 charset 'utf8';

# 6. 切换数据库.
use day01;

# 7. 查看当前使用的是哪个数据库.
select database();      # day01
```

## DDL语句_操作数据表

```sqlite
# ------------------- 案例2: DDL语句操作 数据表 -------------------
# 0. 务必先切库, 即: 之后的表, 都是在这个库中玩儿的.
use day01;

# 1. 查看(当前数据库中)所有的数据表.
show tables;
# 核心: 查看某张表的结构信息(字段名, 数据类型, 约束等...)
desc users;
# 2. 创建数据表.
/*
格式:
    create table [if not exists] 数据表名(
        字段名 数据类型 [约束],
        字段名 数据类型 [约束],
        ......
        字段名 数据类型 [约束]
    );
细节:
    上述的中括号中的部分, 表示可选项, 写不写都行.
*/
# 需求: 创建用户表users, 字段为: id, username, password
create table if not exists users(
    id int,                 # id列, 整型.
    username varchar(20),   # 账号, 字符串类型
    password varchar(20)    # 密码, 字符串类型
);

# 3. 修改表名.
# 格式1: alter table 旧表名 rename 新表名;
alter table users rename user_tmp;
# 格式2: rename table 旧表名 to 新表名;
rename table user_tmp to users;

# 4. 删除数据表.
drop table users;
```

## DDL语句_操作字段

```sql
# ------------------- 案例3: DDL语句操作 字段 -------------------
# 1. 查看某表的结构信息(字段信息)
desc users;

# 2. 给表新增字段: address, int, 非空(约束)
# 格式: alter table 表名 add 字段名 数据类型 [约束];
alter table users add address int not null;

# 3. 修改表的字段信息.
# 场景1: 只修改 数据类型 和 约束, 例如: address,int,非空 -> address, varchar(10), 非空
# 格式: alter table 表名 modify 字段名 新的数据类型 [新的约束];
alter table users modify address varchar(10);           # 如果没加约束, 则之前的非空约束就没了.
alter table users modify address varchar(10) not null;  # 这个才是符合题设的SQL语句.

# 场景2: 修改列名, 数据类型, 约束.  address,varchar(10),非空 -> addr,varchar(20), 非空
# 格式: alter table 表名 change 旧字段名 新字段名 新的数据类型 [新的约束];
alter table users change address addr varchar(20) not null;

# 4. 删除addr字段.   需求: 删除addr字段.
# 格式: alter table 表名 drop 旧字段名;
alter table users drop addr;
```

## DML语句_增

```sql
# ------------------- 案例1: DML语句操作 表数据 -> 增 -------------------
/*
DML语句主要操作的是: 表数据. 对表数据进行增, 删, 改的操作.

SQL中, 给表添加数据的格式:
    # 格式1: 普通写法.
    insert into 表名(列名1, 列名2...) values(值1, 值2...);      # 列的个数和类型 要和后续 值的个数和类型完全一致.

    # 格式2: 省略列名
    insert into 表名 values(值1, 值2...);       # 如果不写列名, 则默认表示: 全列名.

    # 格式3: 如果有了主键约束, 则添加表数据的动作可以简写为:
    insert into 表名 values(null, 值1, 值2...);

    # 格式4: 如果要同时添加多条数据, 写法如下:
    insert into 表名 values(值1, 值2, 值3), (值4, 值5, 值6).......;
*/
# 1. 切库
use day01;
# 2. 查表
show tables;
# 3. 查看表数据, 目前先了解, 稍后讲.
select * from users;

# 4. 往 用户表中添加数据.
# 格式1: 普通写法.
insert into users(id, username, password) values(1, 'admin01', 'pwd111');
insert into users(username) values('admin01');

# 格式2: 省略列名, 默认 = 全列名
insert into users values(1, 'admin01', 'pwd111');

# 格式3: 同时添加多个用户信息.
insert into users values(2, 'admin01', 'pwd222'), (3, 'admin03', 'pwd333');
```

## 单表约束_入门

```sql
# ------------------- 案例2: 扩展_约束入门 -------------------
/*
回顾: 建表格式
    create table 表名(
        字段1 数据类型 [约束],
        字段2 数据类型 [约束],
        ......
        字段3 数据类型 [约束]
    );
约束介绍:
    概述:
        用来保证数据完整性和一致性的.
    分类:
        单表约束:
            primary key     # 主键约束, 特点: 非空, 唯一, 且一张表中, 只能有1个主键
                            # 一般结合 auto_increment一起使用, 表示: 自动增长.
            not null        # 非空约束, 该列值不能为空.
            unique          # 唯一约束, 该列值不能重复.
            default         # 默认约束, 如果你不给值, 则用默认值.
        多表约束:
            foreign key     # 主外键
*/
# 0. 删除数据表.
drop table if exists stu;
# 1. 创建数据表, 学生表student, 字段: 学号(唯一), 姓名(非空), 手机号(唯一), 性别(默认: 男)
create table stu(
    id int primary key auto_increment,             # 主键约束(非空, 唯一), 自增
    name varchar(10) not null,      # 非空约束
    tel varchar(11) unique ,        # 唯一约束
    gender varchar(1) default '男'   # 默认约束
);

# 2. 查看上述的表数据.
select * from stu;

# 3. 往上述的表中添加数据.
insert into stu values(null, '乔峰', '111', '男');     # 报错, 主键不能为空.
insert into stu values(1, null, '111', '男');         # 报错, name列不能为空.
insert into stu values(1, '乔峰', '111');             # 报错, 传入值的个数 和 列的个数不匹配

insert into stu values(2, '乔峰', '222', '男');        # 成功
insert into stu values(1, '乔峰', '111', '男');        # 成功
insert into stu values(3, '梦姑', '333', '女');        # 成功

# 测试默认约束
insert into stu(id, name, tel) values(5, '阿朱', '555');

# 4. 写到这里, (单表)约束的基础功能就演示完了, 那: 主键在实际开发中如何用呢?
# 答: 配合自增一起使用.
select * from stu;

# 因为主键列是int类型, 且结合自增一起使用, 则: 每次主键都会在最大主键值的基础上 + 1, 重新存.
insert into stu values(null, '乔峰', '111', '男'); # 对的
insert into stu values(null, '乔峰', '222', '男'); # 对的
insert into stu values(null, '阿朱', '333', '女'); # 对的
```

## DML语句_改

```sql
# ------------------- 案例3: DML语句操作 表数据 -> 改 -------------------
# 记忆: 写update 或者 删除语句时, 一定一定一定要加where条件, 一个过来人的含泪忠告.
# 格式: update 表名 set 字段名=值, 字段名=值 where 条件;
# 1. 查看表数据.
select * from stu;

# 2. 修改id为2的学生信息为: 杨过, 男
update stu set name='杨过', gender='男';   # 如果不加where条件, 会一次性更改所有行.

# 3. 修改id为3的学生信息: 小龙女, 777, 女
update stu set name='小龙女', tel='777', gender='女' where id = 3;
```

## DML语句_删

```sql
# ------------------- 案例4: DML语句操作 表数据 -> 删 -------------------
# 删除: delete from 表名 where 条件;
# 0. 删除数据表.
drop table if exists stu;

# 1. 创建数据表, 学生表student, 字段: 学号(唯一), 姓名(非空), 手机号(唯一), 性别(默认: 男)
create table stu(
    id int primary key auto_increment,             # 主键约束(非空, 唯一), 自增
    name varchar(10) not null,      # 非空约束
    tel varchar(11) unique ,        # 唯一约束
    gender varchar(1) default '男'   # 默认约束
);
# 2. 添加表数据.
insert into stu values(null, '乔峰', '111', '男'), (null, '虚竹', '222', '男'), (null, '段誉', '333', '男');
select * from stu;

# 3. 不加where 条件, 一次性删除所有.
delete from stu where id = 2;       # 删除1条

# 4. 面试题: truncate table 和 delete from的区别.
# delete from 属于: DML语句, 可以结合事务一起用, 相同点是: 都会删除所有数据, id不会重置.
# truncate table: 属于DDL语句, 一般不能结合事务一起用, 相同点是: 都会删除所有数据, id会重置.
delete from stu;        # 一次性删除所有数据, id不会重置.

truncate table stu;     # 一次性删除所有数据, id会重置, 因为truncate table相当于把表摧毁了, 然后创建一张和该表一模一样的表.
truncate stu;           # 效果同上, table可以省略不写.
```

