<?php
error_reporting(0);
if(isset($_POST["username"]) && isset($_POST["password"])){
    if(login($_POST["username"],$_POST["password"])){
        die("Good, can you find out my password?");
    }
    die("username or password error!");
}
else{
    highlight_file(__FILE__);
}


function login($u,$p){
    $manager = new MongoDB\Driver\Manager("mongodb://mongo:27017");
    $q = '{"username": "'.$u.'", "password": "'.$p.'"}';
    $query = new MongoDB\Driver\Query(json_decode($q));
    $cursor = $manager->executeQuery('babyDB.user', $query);

    $data = [];
    foreach($cursor as $doc) {
        $data[] = $doc;
    }
    if (isset($data) && isset($data[0]->password)) {
        return true;
    }
    return false;
}

?>