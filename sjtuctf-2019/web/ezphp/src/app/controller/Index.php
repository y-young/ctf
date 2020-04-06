<?php
namespace app\controller;

use  app\BaseController;


class Index extends BaseController
{
    public function index()
    {
        $ip = $_SERVER['REMOTE_ADDR'];
        $yourdir = "/var/www/html/public/tmp/".md5($ip."wuwuwu")."/";
        if (!is_dir($yourdir))
        {
            @mkdir($yourdir);
        }
        $filename = $this->request->post("filename");
        if (file_exists($filename)){
            if (filesize($filename)>0){
                    $tmpfile = $yourdir.md5($filename).".temp";
                    copy($filename, $tmpfile);
                    $res = "copy success and your dis is $yourdir";
                }else{
                    $res = "file size is 0";
                }
        }else{
            $res = "file not exist";
        }
        //echo $res;
        return $res;
    }

    public function hello($name = 'ThinkPHP6')
    {
        return 'hello,' . $name;
    }
}
