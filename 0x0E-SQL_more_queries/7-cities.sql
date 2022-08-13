-- create database `hbtn_0d_usa` and table `cities` with columns `id` INT unique auto-generated non-null and primary key, `state_id` INT non-null and foreign key that references `id` of `states`, and `name` VARCHAR(256) non-null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
	);
