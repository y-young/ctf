DROP DATABASE IF EXISTS `ctf`;

CREATE DATABASE `ctf` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `ctf`;

CREATE TABLE `flag` (`flagx` VARCHAR(64) NOT NULL);

INSERT INTO `flag` (`flagx`) VALUES ("0ops{test}");

CREATE USER IF NOT EXISTS 'user1'@'%' IDENTIFIED BY 'user1passwd';
GRANT SELECT ON ctf.flag TO 'user1'@'%';
