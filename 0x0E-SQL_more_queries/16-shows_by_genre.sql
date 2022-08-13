-- list all shows and all genres linked to that show from the `hbtn_0d_tvshows` database
-- if a show doesn't have a genre, display NULL
-- each record should display `tv_shows.title` `tv_genres.name`
-- only one SELECT statement allowed
SELECT `title`, `name` FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
LEFT JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
ORDER BY `title`, `name`;
