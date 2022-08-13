-- list all genres in `hbtn_0d_tvshows` and display number of shows linked to it
-- each record should display `TV Show genre` `Number of shows linked to this genre`
-- first column must be called `genre`, second column must be called `number_of_shows`
-- don't display a genre that doesn't have any shows linked
-- results must be sorted in descending order of number of shows linked
-- you can use only one SELECT statement
SELECT `name` AS 'genre', count(`genre_id`) AS 'number_of_shows'
FROM `tv_show_genres` INNER JOIN `tv_genres` ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows` DESC;
