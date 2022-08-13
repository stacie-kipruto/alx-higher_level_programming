-- lists all cities in `hbtn_0d_usa` database
-- each record should display `cities.id` - `cities.name` - `states.name` and sorted in ascending order of `cities.id`
-- you can use only one SELECT statement
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities`, `states` WHERE `cities`.`state_id` = `states`.`id` ORDER BY `cities`.`id`;
