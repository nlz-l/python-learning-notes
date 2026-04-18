/*
单表查询, 完整查询格式如下:
 select
        [distinct] 列名1 as 别名, 列名2 as 别名, ...
    from
        数据表名
    where
        组前筛选
    group by
        分组字段
    having
        组后筛选
    order by
        排序字段列1[asc | desc],列2[asc | desc]...
    limit
        起始索引, 数据条数;
 */
#准备数据
use day02;
# 1. 创建商品表.
create table product
(
    pid         int primary key auto_increment, # 商品id, 主键
    pname       varchar(20),    # 商品名
    price       double,         # 商品单价
    category_id varchar(32)     # 商品的分类id
);
# 2. 添加表数据.
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'联想',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海尔',3000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'雷神',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'杰克琼斯',800,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'真维斯',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'花花公子',440,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'劲霸',2000,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香奈儿',800,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'相宜本草',200, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'面霸',5,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'好想你枣',56,'c004');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'香飘飘奶茶',1,'c005');
INSERT INTO product(pid,pname,price,category_id) VALUES(null,'海澜之家',1,'c002');
desc product;
#----------------------------------------------简单查询---------------------------------------------
#1. 查询表中所有数据
#格式:select 列名1, 列名2... from 数据表名;
select pid, pname, price, category_id from product;
#同 select * from product;
#2. 查询指定列的数据
select pname,price from product;
#3. 别名查询   列名 as 别名    表名 as 别名
select pname as 商品名, price as 价格 from product as p;  #临时修改
#select pname 商品名, price 价格 from product;  as可以省略不写
#4. 修改某列值
select pname,price+10 as price from product;

#----------------------------------------------条件查询---------------------------------------------

/*like 模糊查询 _代表一个字符
              %任意多个字符,至少0个
  between 值1 and 值2  包左 包右
  in (值1 值2 值3)      满足一个值即可
  is null 或 is not null
 */
#1. 演示比较运算符
select * from product where price>500;
select * from product where category_id != 'c001';
select * from product where category_id <> 'c001'; #同上
select pname,price from product where price>=800 and price<=3000;
select pname,price from product where price between 800 and 3000; #同上
select * from product where pname like '_霸';
select * from product where pname like '%斯%';
select * from product where price in(200,800,5000);
select * from product where price=200 or price=800 or price=5000; #同上
select * from product where price not in(200,800,5000);
select * from product where price!=800 and price!=5000; #同上
select * from product where  category_id is null;

#----------------------------------------------排序查询----------------------------------------------------
#order by 排序字段 [asc | desc]
select * from product;
select * from product order by price;
select * from product order by price asc; #可不写
select * from product order by price desc;
select * from product order by price desc,category_id desc;

#----------------------------------------------聚合查询----------------------------------------------------
/*
聚合查询(多进一出)介绍:
    概述:
        聚合查询是对表中的某列数据做操作.
    常用的聚合函数:
        count()     统计某列值的个数, 只统计非空值. 一般用于统计 表中数据的总条数.
        sum()       求和
        max()       求最大值
        min()       求最小值
        avg()       求平均值
面试题: count(*), count(1), count(列)的区别是什么?
    区别1: 是否统计空值
        count(列): 只统计该列的非空值.
        count(1), count(*): 统计所有数据, 包括空值.
    区别2: 效率问题.
        count(主键列) > count(1) > count(*) > count(普通列)
*/
select * from product;
select count(*) from product; #13
select count(pid) from product; #13
select count(category_id) from product; #11
select
    sum(price) as sum,
    max(price) as max,
    min(price) as min,
    avg(price) as avg_price,
    round(avg(price),2) as avg_price   #四舍五入保留两位小数
from
    product;

#----------------------------------------------分组查询----------------------------------------------------
/*
分组查询介绍:
    概述:
        简单理解为, 根据分组字段, 把表数据 化整为零, 然后基于每个分组后的每个部分, 进行对应的聚合运算.
    格式:
        select 列1, 列2... from 数据表名 where 组前筛选 group by 分组字段 having 组后筛选;
    细节:
        1. 分组查询 一般要结合 聚合函数一起使用, 且根据谁分组, 就根据谁查询.
        2. 组前筛选用where, 组后筛选用having.
        3. 面试题: where 和 having的区别是什么?
            where: 组前筛选, 后边不能跟聚合函数.
            having: 组后筛选, 后边可以跟聚合函数.
        4. 分组查询的查询列 只能出现 分组字段, 聚合函数.
        5. 如果只分组, 没有写聚合, 可以理解为是: 基于分组字段, 进行去重查询
 */
select * from product;
select category_id, count(pid) as total_cnt from product group by category_id;
select category_id, count(pid) as total_cnt from product group by category_id having total_cnt > 2;
#----------------------------------------------去重查询----------------------------------------------------

select * from product;

select distinct category_id from product;
select distinct category_id,price from product; #两项完全一样才会去重
#分组去重
select category_id from product group by category_id;
select category_id,price from product group by category_id,price;
#----------------------------------------------分页查询----------------------------------------------------
/*
分页查询介绍:
    概述:
        分页查询 = 每次从数据表中查询出固定条数的数据, 一方面可以降低服务器的压力, 另一方面可以降低浏览器端的压力, 且可以提高用户体验.
        实际开发中非常常用.
    格式:
        limit 起始索引, 数据条数;
    细节:
        1. 表中每条数据都有自己的索引, 且索引是从0开始的.
        2. 如果是从索引0开始获取数据的, 则索引0可以省略不写.
    要学好分页, 掌握如下的几个参数计算规则即可:
        数据总条数:      count() 函数
        每页的数据条数:   产品经理, 项目经理, 你...
        每页的起始索引:   (当前的页数 - 1) * 每页的数据条数
        总页数:          (数据总条数 + 每页的数据条数 - 1) // 每页的数据条数
                        (13 + 5 - 1) // 5 = 17 // 5 = 3页
                        (14 + 5 - 1) // 5 = 18 // 5 = 3页
                        (15 + 5 - 1) // 5 = 19 // 5 = 3页
                        (16 + 5 - 1) // 5 = 20 // 5 = 4页
*/
select * from product;
select * from product limit 0,3; #第一页
select * from product limit 3,3; #第二页
select * from product limit 6,3; #第三页
select * from product limit 9,3; #第四页
select * from product limit 12,3; #第五页

select * from product limit 0,5; #第一页
select * from product limit 5,5; #第二页
select * from product limit 10,5; #第三页

select * from product order by price desc limit 1,1;  #价格次高