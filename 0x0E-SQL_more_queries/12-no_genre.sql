-- list all shows contained in `hbtn_0d_tvshows` that don't have a genre
-- each record should display `tv_shows.title` `tv_show_genres.genre_id`
-- results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
-- if a show does not have a genre, display NULL
-- you can use only one SELECT statement
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
WHERE `tv_show_genres`.`genre_id` IS NULL
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;
