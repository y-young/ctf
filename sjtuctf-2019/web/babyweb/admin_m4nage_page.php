
<?php 
session_start(); 
error_reporting(0);
if($_SESSION['is_login']!== "admin") die("You are not admin.");
?>
<!DOCTYPE html>
<html>
<head>
	<title>Manage page</title>
</head>
<body>
Hello admin, you can upload some pictures here.
<form action="" method="POST" enctype="multipart/form-data">
	<label for="file">Filename:</label>
	<input type="file" name="file"/> 
	<input type="submit" name="submit" value="upload" />
<?php
if(isset($_FILES["file"])){
	if(stristr($_FILES["file"]["name"],"php")){
		die("php is not allowed");
	}
        if(stristr($_FILES["file"]["name"],".ht")){
                die(".ht is not allowed");
        }
	if ($_FILES["file"]["size"] < 20480){
		if($_FILES["file"]["type"] == "image/gif" || $_FILES["file"]["type"] == "image/png" || $_FILES["file"]["type"] == "image/jpeg"){
			if ($_FILES["file"]["error"] > 0){
				echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
			}
			else {
				if (file_exists("admin_up1oad/" . $_FILES["file"]["name"])){
					echo $_FILES["file"]["name"] . " already exists. ";
				}
				else {
					move_uploaded_file($_FILES["file"]["tmp_name"], "admin_up1oad/" . $_FILES["file"]["name"]);
					echo "\n</br>Stored in: " . "admin_up1oad/" . $_FILES["file"]["name"];
				}
			}
		}
		else{
			echo "file type error";
		}
	}
	else {
		echo "file need less than 20kb";
	}
}
?>
</form>
</body>
</html>