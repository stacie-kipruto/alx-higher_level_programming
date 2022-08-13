-- list all genres not linked to the show "Dexter"
-- each record should display `tv_genres.name`
-- results must be sorted in ascending order of genre name
-- maximum 2 SELECT statements allowed
SELECT `name` FROM `tv_genres`
WHERE `name` NOT IN (
	SELECT `name` FROM `tv_shows`
	INNER JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
	INNER JOIN `tv_genres` ON `tv_shows_genre`.`genre_id` = `tv_genres`.`id`
	WHERE `tv_shows`.`title` = "Dexter"
)
ORDER BY `name`;
