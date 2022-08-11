-- lists the number of records with the same score in `second_table`
-- result should display the score and the number of records for this score with the label `number`, and sorted in descending order of number of records
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `score` DESC;

