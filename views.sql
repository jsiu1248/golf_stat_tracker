CREATE VIEW pga_data AS 
SELECT stat.id, stat.earnings, stat.drive_avg, stat.gir_pct, stat.putt_avg, stat.sand_saves_pct, stat.birdies_per_round, stat.hole_proximity_avg, stat.scrambling_pct, stat.world_rank, 
player.first_name, player.last_name, player.height, player.birthday, player.country, player.residence, player.birth_place, player.college FROM GOLF.STAT stat
LEFT JOIN  golf.pga_player player ON stat.id=player.id;
CREATE VIEW practice_data AS 
SELECT DISTINCT PRACTICE.SESSION_ID, PRACTICE.SHOT_TYPE_ID, PRACTICE.SUCCESS, PRACTICE.TOTAL, PRACTICE.DISTANCE, PRACTICE.CLUB_ID, 
SELF_SESSION.NOTES, SELF_SESSION.DATE, SELF_SESSION.GOALS, SESSION_TYPE.NAME SESSION_NAME, GOLF_COURSE.COURSE_NAME
FROM GOLF.PRACTICE
LEFT JOIN GOLF.SELF_SESSION ON PRACTICE.SESSION_ID=SELF_SESSION.SESSION_ID
LEFT JOIN GOLF.SESSION_TYPE ON SELF_SESSION.SESSION_TYPE_ID=SESSION_TYPE.SESSION_TYPE_ID
LEFT JOIN GOLF.GOLF_COURSE ON SELF_SESSION.COURSE_ID=GOLF_COURSE.ID;
CREATE VIEW round_data AS
SELECT DISTINCT ROUND.SESSION_ID, ROUND.HOLE, ROUND.GREEN_REG, ROUND.SCORE, ROUND.PUTT, ROUND.FAIRWAY, ROUND.PROXIMITY_TO_HOLE, ROUND.SCRAMBLE, 
SELF_SESSION.NOTES, SELF_SESSION.DATE, SELF_SESSION.GOALS, SESSION_TYPE.NAME SESSION_NAME, GOLF_COURSE.COURSE_NAME
FROM GOLF.ROUND
LEFT JOIN GOLF.SELF_SESSION ON ROUND.SESSION_ID=SELF_SESSION.SESSION_ID
LEFT JOIN GOLF.SESSION_TYPE ON SELF_SESSION.SESSION_TYPE_ID=SESSION_TYPE.SESSION_TYPE_ID
LEFT JOIN GOLF.GOLF_COURSE ON SELF_SESSION.COURSE_ID=GOLF_COURSE.ID
CREATE VIEW round_data_summary AS 
SELECT session_id, ROUND(AVG(green_reg),1)  green_reg_avg, ROUND(AVG(score),1) score_avg, ROUND(AVG(putt),1) putt_avg,
 ROUND(AVG(fairway),1) fairway_avg, ROUND(AVG(proximity_to_hole),1) proximity_to_hole_avg, ROUND(AVG(scramble),1) scramble_avg FROM golf.round group by session_id;
 CREARE VIEW round_data_dim AS
 SELECT ROUND(AVG(green_reg),1)  green_reg_avg, ROUND(AVG(score),1) score_avg, ROUND(AVG(putt),1) putt_avg,
 ROUND(AVG(fairway),1) fairway_avg, ROUND(AVG(proximity_to_hole),1) proximity_to_hole_avg, ROUND(AVG(scramble),1) scramble_avg FROM golf.round;