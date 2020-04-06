
<?php session_start();
 error_reporting(0); ?>
<!DOCTYPE html>
<html>
<head>
	<title>Login page</title>
</head>
<body>
<form action="admin_l0gin_page.php" method="POST">
	<p>username:<input type="text" name="username"></p>
	<p>password:<input type="password" name="password"></p>
	<input type="submit" value="login">
</form>
<?php
require_once 'config.php';

if(isset($_POST['username']) or isset($_POST['password'])){
	$username = filter($_POST['username']);
	$password = $_POST['password'];

	// $db = new mysqli($dbhost,$dbuser,$dbpass,"test");
    // $db = mysqli_connect($dbhost, $dbuser, $dbpass,"babyWeb");
    $db = new mysqli($dbhost,$dbuser,$dbpass,"babyWeb");
    if (!$db) {
        die('Failed to connect to MySQL');
    }
    
	$sql = "SELECT password FROM `user` WHERE username='{$username}'";

    if ($result = $db->query( $sql )) {
        while ($row = $result->fetch_array(MYSQLI_ASSOC)){
            if($row['password'] === $password){
                $_SESSION['is_login'] = "admin";
                die("<script>window.location.href='admin_m4nage_page.php';</script>");
            }
            else
                die("username or password error!");
        }       
        echo "username or password error!";
    	$result->close();
    } else {
        die("db error!");
    }       

	$db->close();

}

?>

</body>
</html>
