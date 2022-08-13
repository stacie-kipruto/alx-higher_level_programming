-- creates database `hbtn_0d_usa` and table `states` with columns `id` INT unique auto-generated non-null primary-key, and `name` VARCHAR non-null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT AUTO_INCREMENT UNIQUE NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
	);
