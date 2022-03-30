USE GOLF;




 CREATE OR REPLACE VIEW practice_data AS 
SELECT DISTINCT PRACTICE.PLAYER_ID, PRACTICE.SESSION_ID, PRACTICE.SHOT_TYPE_ID, PRACTICE.SUCCESS, PRACTICE.TOTAL, PRACTICE.DISTANCE, PRACTICE.CLUB_ID, 
SELF_SESSION.NOTES, SELF_SESSION.DATE, SELF_SESSION.GOALS, SESSION_TYPE.NAME SESSION_NAME, GOLF_COURSE.COURSE_NAME, CLUB.NAME CLUB_NAME, SHOT_TYPE.NAME SHOT_TYPE_NAME
FROM GOLF.PRACTICE
LEFT JOIN GOLF.SELF_SESSION ON PRACTICE.SESSION_ID=SELF_SESSION.SESSION_ID
LEFT JOIN GOLF.SESSION_TYPE ON SELF_SESSION.SESSION_TYPE_ID=SESSION_TYPE.SESSION_TYPE_ID
LEFT JOIN GOLF.CLUB ON CLUB.CLUB_ID=PRACTICE.CLUB_ID
LEFt JOIN GOLF.SHOT_TYPE ON SHOT_TYPE.SHOT_ID=PRACTICE.SHOT_TYPE_ID
LEFT JOIN GOLF.GOLF_COURSE ON SELF_SESSION.COURSE_ID=GOLF_COURSE.ID;


 CREATE OR REPLACE VIEW round_data AS
SELECT DISTINCT ROUND.PLAYER_ID, ROUND.SESSION_ID, ROUND.HOLE, ROUND.GREEN_REG, ROUND.SCORE, ROUND.PUTT, ROUND.FAIRWAY, ROUND.PROXIMITY_TO_HOLE, ROUND.SCRAMBLE, ROUND.SCORE_AVG,
SELF_SESSION.NOTES, SELF_SESSION.DATE, SELF_SESSION.GOALS, SESSION_TYPE.NAME SESSION_NAME, GOLF_COURSE.COURSE_NAME
FROM GOLF.ROUND
LEFT JOIN GOLF.SELF_SESSION ON ROUND.SESSION_ID=SELF_SESSION.SESSION_ID
LEFT JOIN GOLF.SESSION_TYPE ON SELF_SESSION.SESSION_TYPE_ID=SESSION_TYPE.SESSION_TYPE_ID
LEFT JOIN GOLF.GOLF_COURSE ON SELF_SESSION.COURSE_ID=GOLF_COURSE.ID;


 CREATE OR REPLACE VIEW round_data_summary AS 
SELECT player_id, session_id, ROUND(AVG(green_reg),2)*100  green_reg_avg, ROUND(AVG(score),1) score_avg, ROUND(AVG(putt),1) putt_avg,
 ROUND(AVG(fairway),1) fairway_avg, ROUND(AVG(proximity_to_hole),1) proximity_to_hole_avg, ROUND(AVG(scramble),2)*100 scramble_avg, SUM(SCORE) total_score FROM golf.round group by session_id;


 CREATE OR REPLACE VIEW round_data_dim AS
 SELECT player_id, ROUND(AVG(green_reg),2)*100  green_reg_avg, ROUND(AVG(score),1) score_avg, ROUND(AVG(putt),1) putt_avg,
 ROUND(AVG(fairway),1) fairway_avg, ROUND(AVG(proximity_to_hole),1) proximity_to_hole_avg, ROUND(AVG(scramble),2)*100 scramble_avg FROM golf.round;


 CREATE OR REPLACE VIEW practice_data_summary AS 
SELECT player_id, session_id, shot_type_id, ROUND(SUM(success)/SUM(total),2) succes_rate, club_id FROM GOLF.PRACTICE GROUP BY SESSION_ID, SHOT_TYPE_ID;


 CREATE OR REPLACE VIEW practice_data_dim AS 
SELECT player_id, shot_type_id, ROUND(SUM(success)/SUM(total),2) succes_rate FROM GOLF.PRACTICE GROUP BY SESSION_ID, SHOT_TYPE_ID;

-- this table has both the pga summary data and my data
 CREATE OR REPLACE VIEW player_pga_data AS 
SELECT stat.id, stat.earnings, stat.drive_avg, stat.gir_pct, stat.putt_avg, stat.sand_saves_pct, stat.birdies_per_round, stat.hole_proximity_avg, stat.scrambling_pct, stat.world_rank, 
player.first_name, player.last_name, player.height, player.birthday, player.country, player.residence, player.birth_place, player.college FROM GOLF.STAT stat
LEFT JOIN  golf.pga_player player ON stat.id=player.id
LEFT JOIN golf.round_data_dim round_data_dim ON stat.id=round_data_dim.player_id


-- a side note is that I am failing to update a mysql view. Strange. So, I'm updating the actual table
-- maybe this need to been a trigger
UPDATE golf.stat
SET gir_pct=(SELECT green_reg_avg FROM GOLF.round_data_dim), 
putt_avg=(SELECT putt_avg FROM GOLF.round_data_dim), 
drive_avg=(SELECT AVG(DISTANCE) AVG_DRIVE FROM golf.practice_data WHERE SHOT_TYPE_NAME='drive'),
scrambling_pct=(SELECT scramble_avg FROM GOLF.round_data_dim), 
scoring_avg=(SELECT AVG(TOTAL_SCORE) FROM GOLF.round_data_summary)
-- I need to add average_score

WHERE ID='00000000-0000-0000-0000-000000000001'





 CREATE OR REPLACE VIEW pga_stat_summary AS
SELECT ROUND(AVG(EARNINGS),1) EARNINGS_AVG, ROUND(AVG(DRIVE_AVG),1) DRIVE_AVG, ROUND(AVG(GIR_PCT),1) GIR_PCT_AVG, ROUND(AVG(PUTT_AVG),1) PUTT_AVG, 
ROUND(AVG(SAND_SAVES_PCT),1) SAND_SAVES_PCT_AVG, ROUND(AVG(BIRDIES_PER_ROUND),1) BIRDIES_PER_ROUND_AVG, ROUND(AVG(SCRAMBLING_PCT),1) SCRAMBLING_PCT_AVG FROM golf.player_pga_data;