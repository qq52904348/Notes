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

$to='xxx@xxx.xxx';
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

​	columns是列名，table_name是表名，当想看那个表中的全部数据时可以用*代替columns。select语句也可以设置条件，比如：

```mysql
select * from aliens_abduction where fang_spotted='yes'
```

### 2-4.PHP中使用mysql语句

​	PHP与数据库通信

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
<?php				
	$dbc = mysqli_connect('localhost', 'root', '******', 'aliendatabase')
    or die('Error connecting to MySQL server.');
	$query = "INSERT INTO aliens_abduction (first_name, last_name,when_it_happened, how_long, " ."how_many, alien_description, what_they_did, fang_spotted, other, email) " .
    "VALUES ('$first_name', '$last_name', '$when_it_happened', '$how_long', '$how_many', " .
    "'$alien_description', '$what_they_did', '$fang_spotted', '$other', '$email')";

  $result = mysqli_query($dbc, $query)
    or die('Error querying database.');

  mysqli_close($dbc);
?>
```

​	**die()**函数会终止一个PHP脚本，并提供失败代码的反馈。如果mysqli_connect()的4个连接变量之一有问题，或者如果无法找到数据库服务器，die()函数就会终止其余PHP脚本的运行，并显示挂号的错误消息。

### 2-5.完整的PHP代码

```php
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Aliens Abducted Me - Report an Abduction</title>
</head>
<body>
  <h2>Aliens Abducted Me - Report an Abduction</h2>

<?php
  $first_name = $_POST['firstname'];
  $last_name = $_POST['lastname'];
  $when_it_happened = $_POST['whenithappened'];
  $how_long = $_POST['howlong'];
  $how_many = $_POST['howmany'];
  $alien_description = $_POST['aliendescription'];
  $what_they_did = $_POST['whattheydid'];
  $fang_spotted = $_POST['fangspotted'];
  $email = $_POST['email'];
  $other = $_POST['other'];

  $dbc = mysqli_connect('localhost', 'root', '******', 'aliendatabase')
    or die('Error connecting to MySQL server.');

  $query = "INSERT INTO aliens_abduction (first_name, last_name, when_it_happened, how_long, " .
    "how_many, alien_description, what_they_did, fang_spotted, other, email) " .
    "VALUES ('$first_name', '$last_name', '$when_it_happened', '$how_long', '$how_many', " .
    "'$alien_description', '$what_they_did', '$fang_spotted', '$other', '$email')";

  $result = mysqli_query($dbc, $query)
    or die('Error querying database.');

  mysqli_close($dbc);

  echo 'Thanks for submitting the form.<br />';
  echo 'You were abducted ' . $when_it_happened;
  echo ' and were gone for ' . $how_long . '<br />';
  echo 'Number of aliens: ' . $how_many . '<br />';
  echo 'Describe them: ' . $alien_description . '<br />';
  echo 'The aliens did this: ' . $what_they_did . '<br />';
  echo 'Was Fang there? ' . $fang_spotted . '<br />';
  echo 'Other comments: ' . $other . '<br />';
  echo 'Your email address is ' . $email;
?>

</body>
</html>
```



##3.《Head First PHP &MySQL》（三）

### 3-1. MySQL数据类型

- VARCHAR：VARiable CHARacter（可变字符）的简写，能够存储文本数据。可以适应你的数据长度，只存储你需要的数据而不用额外的空格填充。

- CHAR或CHARACTER：很严格，数据是定长的。如果文本总是相同的长度使用。

- DATETIME或TIMESTAMP：可以跟踪日期和时间。

- DATE跟踪日期不跟踪时间；TIME跟踪时间不跟踪日期。

- INT或INTERGER：存储整数。

- BLOB：二进制数据。

- TEXT：存储大量文本，比CHAR或VARCHAR多得多的文本。

###3-2.DESCRIBE展示表的结构

​	使用DESCRIBE可以查看表的结构：

```mysql
DESCRIBE table_name
```

​	这个结构只会显示Type、Null、Key、Default、Extra，不会显示数据的值。

### 3-3.DROP TABLE删除表

```mysql
DROP TABLE table_name
```

 	这个语句会把整个表都删除。

### 3-4.PHP中获取mysql中的数据

​	使用上节中的函数 **mysqli_query()** 在PHP中执行mysql命令，然后用函数 **mysqli_fetch_array()**结合**while循环**来获取表的数据。比如：

```php
$query="SELECT * FROM email_list";
$result=mysqli_query($dbc,$query);
/'
email_list是表名，$dbc是连接mysql数据库的变量，然而上面的$result并不会包含数据，如果试图显示$result的值，会显示： Resource id #3
$result变量只是存储了一个MySQL资源的ID号，而不是查询所返回的具体数据，这样就需要用到mysqli_fetch_array()函数了：
'/
  while ($row=mysqli_fetch_array($result)){
    echo $row['first_name'].' '.$row['last_name'].':'.$row['email'].'<br />';
  }
```

​	**mysqli_fetch_array()**可以得到表中的一行，下一次调用就会得到下一行。

### 3-5.用DELETE删除数据

```MYSQL
DELETE FROM table_name
```

​	上面这样的形式会删除这个表中的所有数据（表还在）。如果想要删除特定的行，需要添加where子句:

```mysql
DELETE FROM table_name WHERE list_name ='内容'
```

### 3-6.这章代码

#### addemail.html :

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Add Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <img src="blankface.jpg" width="161" height="350" alt="" style="float:right" />
  <img name="elvislogo" src="elvislogo.gif" width="229" height="32" border="0" alt="Make Me Elvis" />
  <p>Enter your first name, last name, and email to be added to the <strong>Make Me Elvis</strong> mailing list.</p>
  <form method="post" action="addemail.php">
    <label for="firstname">First name:</label>
    <input type="text" id="firstname" name="firstname" /><br />
    <label for="lastname">Last name:</label>
    <input type="text" id="lastname" name="lastname" /><br />
    <label for="email">Email:</label>
    <input type="text" id="email" name="email" /><br />
    <input type="submit" name="Submit" value="Submit" />
  </form>
</body>
</html>
```



#### addemail.php :

```php
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Add Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>

<?php
  $dbc = mysqli_connect('localhost', 'root', '******', 'elvis_store')
    or die('Error connecting to MySQL server.');

  $first_name = $_POST['firstname'];
  $last_name = $_POST['lastname'];
  $email = $_POST['email'];

  $query = "INSERT INTO email_list (first_name, last_name, email)  VALUES ('$first_name', '$last_name', '$email')";
  mysqli_query($dbc, $query)
    or die('Error querying database.');

  echo 'Customer added.';

  mysqli_close($dbc);
?>
</body>
</html>
```



#### sendemail.html :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Send Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <img src="blankface.jpg" width="161" height="350" alt="" style="float:right" />
  <img name="elvislogo" src="elvislogo.gif" width="229" height="32" border="0" alt="Make Me Elvis" />
  <p><strong>Private:</strong> For Elmer's use ONLY<br />
  Write and send an email to mailing list members.</p>
  <form method="post" action="sendemail.php">
    <label for="subject">Subject of email:</label><br />
    <input id="subject" name="subject" type="text" size="30" /><br />
    <label for="elvismail">Body of email:</label><br />
    <textarea id="elvismail" name="elvismail" rows="8" cols="40"></textarea><br />
    <input type="submit" name="Submit" value="Submit" />
  </form>
</body>
</html>
```



#### sendemail.php

```php
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Send Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>

<?php
  $from = 'xxx@xxx.xxx';
  $subject = $_POST['subject'];
  $text = $_POST['elvismail'];

  $dbc = mysqli_connect('localhost', 'root', '******', 'elvis_store')
    or die('Error connecting to MySQL server.');

  $query = "SELECT * FROM email_list";
  $result = mysqli_query($dbc, $query)
    or die('Error querying database.');

  while ($row = mysqli_fetch_array($result)){
    $to = $row['email'];
    $first_name = $row['first_name'];
    $last_name = $row['last_name'];
    $msg = "Dear $first_name $last_name,\n$text";
    mail($to, $subject, $msg, 'From:' . $from);
    echo 'Email sent to: ' . $to . '<br />';
  } 

  mysqli_close($dbc);
?>

</body>
</html>
```



#### removeemail.html :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Remove Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <img src="blankface.jpg" width="161" height="350" alt="" style="float:right" />
  <img name="elvislogo" src="elvislogo.gif" width="229" height="32" border="0" alt="Make Me Elvis" />
  <p>Enter an email address to remove.</p>
  <form method="post" action="removeemail.php">
    <label for="email">Email address:</label><br />
    <input id="email" name="email" type="text" size="30" /><br />
    <input type="submit" name="Remove" value="Remove" />
  </form>
</body>
</html>
```



####removeemail.php :

```php
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Make Me Elvis - Remove Email</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>

<?php
  $dbc = mysqli_connect('localhost', 'root', '******', 'elvis_store')
    or die('Error connecting to MySQL server.');

  $email = $_POST['email'];

  $query = "DELETE FROM email_list WHERE email = '$email'";
  mysqli_query($dbc, $query)
    or die('Error querying database.');

  echo 'Customer removed: ' . $email;

  mysqli_close($dbc);
?>

</body>
</html>
```

