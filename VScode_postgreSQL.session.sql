--SELECT * FROM user_behavior;

SELECT
    --music_recc_rating,
    music_recc_rating AS rating, 
    premium_sub_willingness AS willingness, 
    COUNT(*) AS population
FROM
    user_behavior
GROUP BY
    music_recc_rating, premium_sub_willingness
ORDER BY
    music_recc_rating DESC;


--SELECT willing_population_size FROM will_to_subscribe;
