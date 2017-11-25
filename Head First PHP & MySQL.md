# 《Head First PHP &MySQL》     学习笔记

## 1.《Head First PHP &MySQL》（一）

​	HTML作用于客户端，而PHP工作于服务器端。PHP脚本的名字扩展名是**.php**。

​	在HTML的表单元素 form里填写action属性与一个PHP脚本连接，可以在用户提交表单时导致这个PHP脚本运行。代码如下：

```HTML
<form action = "report.php" method = "post">
```

​	report.php是返回的PHP脚本的名字。

### 1-1.编码遵循的一些PHP规则

- PHP代码总是用 **<?php** 和 **?>** 包围。（结束标 ?> 可以不写。）
- 每个PHP语句都必须以一个分号( **;** )结束。
- 如果Web页面中有PHP代码，这个文件的扩展名最好是 **.php** 而不是 **.html**。
- **PHP变量名**必须以一个美元符号 (**$**) 开头。

### 1-2.PHP变量

​	设置变量时可以这样写：

```php
$how_long = $_POST['howlong'];
```

​	$how_long为PHP变量，等号右边的 howlong 对应于HTML中表单中的变量名字。

​	$_POST是一个特殊的变量，称为超级全局变量，因为这是PHP内置的，而且在整个脚本中都可用。当脚本一运行的时候，\$\_POST就已经存在了，不必像创建其他PHP变量那样创建\$\_POST。

​	$_POST超级全局变量直接绑定到HTML表单使用的表单提交方法，如果方法设置为post，那么所有表单数据都会打包到\$\_POST中，可以根据需要从中抽取和使用各部分数据。

### 1-3.利用PHP发送email消息

​	使用PHP内置函数**mail()**可以设置发送消息到你设定的邮箱。

```PHP
mail($to,$subject,$msg,['From:'.$email]);
```

​	设置好PHP变量 **$to** , **$subject** , **$msg** 就可以了。From是可选参数，会将发送者email追加到email地址前。

### 1-4.HTML代码

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Aliens Abducted Me - Report an Abduction</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h2>Aliens Abducted Me - Report an Abduction</h2>
  <p>Share your story of alien abduction:</p>
  <form method="post" action="report.php">
    <label for="firstname">First name:</label>
    <input type="text" id="firstname" name="firstname" /><br />
    <label for="lastname">Last name:</label>
    <input type="text" id="lastname" name="lastname" /><br />
    <label for="email">What is your email address?</label>
    <input type="text" id="email" name="email" /><br />
    <label for="whenithappened">When did it happen?</label>
    <input type="text" id="whenithappened" name="whenithappened" /><br />
    <label for="howlong">How long were you gone?</label>
    <input type="text" id="howlong" name="howlong" /><br />
    <label for="howmany">How many did you see?</label>
    <input type="text" id="howmany" name="howmany" /><br />
    <label for="aliendescription">Describe them:</label>
    <input type="text" id="aliendescription" name="aliendescription" size="32" /><br />
    <label for="whattheydid">What did they do to you?</label>
    <input type="text" id="whattheydid" name="whattheydid" size="32" /><br />
    <label for="fangspotted">Have you seen my dog Fang?</label>
    Yes <input id="fangspotted" name="fangspotted" type="radio" value="yes" />
    No <input id="fangspotted" name="fangspotted" type="radio" value="no" /><br />
    <img src="fang.jpg" width="100" height="175"
      alt="My abducted dog Fang." /><br />
    <label for="other">Anything else you want to add?</label>
    <textarea id="other" name="other"></textarea><br />
    <input type="submit" value="Report Abduction" name="submit" />
  </form>
</body>
</html>
```

### 1-5.PHP代码

```php
<html>
<head>
    <title>Aliens Abducted Me - Report an Abduction</title>
</head>
<body>
<h2>Aliens Abducted Me - Report an Abduction</h2>
<?php
$when_it_happened=$_POST['whenithappened'];
$how_long=$_POST['howlong'];
$alien_description=$_POST['aliendescription'];
$fang_spotted=$_POST['fangspotted'];
$email=$_POST['email'];
$name=$_POST['firstname'].''.$_POST['lastname'];
$how_many=$_POST['howmany'];
$what_they_did=$_POST['whattheydid'];
$other=$_POST['other'];

$to='52904348@qq.com';
$subject='Aliens Abducted Me - Abduction Report';
$msg="$name was abducted @when_it_happened and was gone for @how_long.\n".
	"Number of aliens: $how_many\n".
	"Alien description: $alien_description\n".
	"What they did: $what_they_did\n".
	"Fang spotted:$fang_spotted\n".
	"Other comments:$other";
	mail($to,$subject,$msg,'From:'.$email);

echo 'Thanks for'.$name. 'submit the form.<br />';
echo 'You were abducted ' . $when_it_happened;
echo ' and were gone for ' . $how_long . '<br />';
echo 'Number of aliens: ' . $how_many.'<br />';
echo 'Describe them: ' . $alien_description . '<br />';
echo 'The aliens did this: ' . $what_they_did . '<br />';
echo 'Was Fang there? ' . $fang_spotted . '<br />';
echo 'Other comments: ' . $other.'<br />';
echo 'Your email address is ' . $email;
?>
</body>
</html>
```

​	PHP代码是包含在\<html>里的，echo是打印当前的内容，PHP中连接两个字符串用一个点 **.** 就行。

​	比如上面的   **echo 'Your email address is ' . $email;**

在python3里就是 **print('Your email address is ' , $email)**

##2.《Head First PHP &MySQL》（二）

​	当表单很多时，email会被塞满，需要用到MySQL来存储数据。

### 2-1.创建MySQL数据库和表

​	在终端中输入 **mysql -u root -p** 进入mysql程序。

​	创建数据库：

```mysql
CREATE DATABASE aliendatabase;
```

​	SQL语句每句后面都要写分号 **;**	。

​	在数据库中创建表之前，需要确保已经选择了这个数据库：

```mysql
USE aliendatabase;
```

​	创建新表：

```mysql
CREATE TABLE aliens_abduction(
	first_name varchar(30),
  	last_name varchar(30),
  	when_it_happened varchar(30),
  	how_long varchar(30),
  	how_many varchar(30),
  	alien_description varchar(30),
  	what_they_did varchar(100),
   	fang_spotted varchar(10),
  	other varchar(100),
  	email varchar(50)
  );
```

​	varchar指这个变量是字符类型，后面挂号的数字是变量能存储多少字符。

### 2-2.INSERT语句的使用

​	INSERT用来在表中存储数据，一般格式为：

```mysql
INSERT INTO table_name (column_name1,column_name2,...)
	VALUES ('value1','value2',...)
```

​	INSERT INTO是存储语句，table_name是表的名字，挂号中的column_name1之类的是数据库列名，VALUES语句指示后面对应列的值。

- **顺序很重要，要插入的值必须以与列名完全相同的顺序排列。**

  如下：


```mysql
INSERT INTO aliens_abduction(first_name,last_name,when_it_happened,how_long,how_many,alien_description,what_they_did,fang_spotted,other,email)
values('Sally','Jones','3 days ago','1 day','four','green with six tentacles','We just taliked and played with a dog','yes','I may have seen your dog.Contact me.','sally@gregs-list.net');
```

### 2-3.使用select得到表数据

```mysql
SELECT columns from table_name	
```

​	columns是列名，table_name是表名，当想看那个表中的全部数据时可以用*代替columns。

### 2-4.PHP中使用mysql语句

- PHP与数据库通信

​	使用**mysqli_connect()**函数可以用于建立php脚本与数据库的连接，需要设置4个参数，分别为：

1. mysql服务器位置（IP地址或主机名）

2. 数据库用户名

3. 数据库密码

4. 数据库名

   需要把这个函数赋值给一个变量。

   使用**mysqli_query()**函数向数据库的表中增加数据。有两个参数，第一个是连接变量名，第二个是记录的mysql语句。

   使用**mysql-close()**关闭连接

   整个的代码如下：

```PHP
<?php				$dbc=mysqli_connect('127.0.0.1','gzp','201330220360','aliendatabsae') or die('Error connection to MySQL server.');
$query="INSERT INTO aliens_abduction(first_name,last_name,when_it_happened,how_long,how_many,alien_description,what_they_did,fang_spotted,other,email)
values('Sally','Jones','3 days ago','1 day','four','green with six tentacles','We just taliked and played with a dog','yes','I may have seen your dog.Contact me.','sally@gregs-list.net')";
$result=mysqli_query($dbc,$query) or die('Error querying database.');
mysqli_close($dbc);
?>
```

