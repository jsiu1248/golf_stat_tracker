USE GOLF;

CREATE PROCEDURE insert_stat
(
    IN id CHAR(255),
    IN earnings FLOAT(13),
    IN drive_avg FLOAT(6), 
    IN gir_pct FLOAT(4),
    IN putt_avg FLOAT(4),
    IN sand_saves_pct FLOAT(4),
    IN birdies_per_round FLOAT(4), 
    IN hole_proximity_avg VARCHAR(255),
    IN scrambling_pct FLOAT(4), 
    IN world_rank INT(4)

)

INSERT IGNORE INTO stat
    (id,earnings, driving_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank)
VALUES
    (id,earnings, driving_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank);



