-- CASTING 
ALTER TABLE user_behavior
ALTER COLUMN music_recc_rating TYPE INTEGER
USING music_recc_rating::integer

-- age distribution pie chart data
SELECT age, COUNT(age)
FROM user_behavior
GROUP BY age
ORDER BY age ASC

-- age distribution under different usage length
SELECT age, COUNT(age)
FROM user_behavior
GROUP BY age
ORDER BY age ASC

-- more than 2 year's user's age distribution
SELECT age, spotify_usage_period, COUNT(gender)
FROM user_behavior
WHERE spotify_usage_period = 'More than 2 years'
GROUP BY age, spotify_usage_period

-- age distribution and the devices they use
-- age distribution and the preffered_premium_plan 
-- those whose plan is premium, what's their preferred_listening_content (distribution)
-- those who prefered premium plan's current plan and age
-- those who likes podcast and the distribution of their prefered pod format
-- those who like well known people as their pod_host, what format do they prefered (podcast and also what genere, what's the frequency they listened to podcast, and their satisfaction to podcast)

-- those music_expl_mthod and theaverage music_Recc_Rating
-- those music_listening frequency ad recc_Rating
-- music time slot and the influencial mood (What's the top genered listening in different time slot)
-- time slot and listening devices
-- age and their fav_music_genre
