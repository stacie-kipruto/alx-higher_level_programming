-- list all comedy shows in the `hbtn_0d_tvshows` database
-- each record should display `tv_shows.title`
-- results must be sorted in ascending order of show title
-- only one SELECT statement allowed
SELECT `title` FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
LEFT JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
WHERE `tv_genres`.`name` = "Comedy"
GROUP BY `title`
ORDER BY `title`;
