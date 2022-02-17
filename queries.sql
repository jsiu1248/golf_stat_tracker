CREATE DATABASE IF NOT EXISTS golf;

USE GOLF;

CREATE TABLE IF NOT EXISTS world_rank 
        (
        id VARCHAR(255),
        world_rank INT(10), 
        PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS stat 
        (
        id VARCHAR(255),
        earnings FLOAT(13),
        drive_avg FLOAT(6), 
        gir_pct FLOAT(4),
        putt_avg FLOAT(4),
        sand_saves_pct FLOAT(4),
        birdies_per_round FLOAT(4), 
        hole_proximity_avg VARCHAR(255),
        scrambling_pct FLOAT(4), 
        world_rank INT(4),
        PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS pga_player 
        (
        id VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255), 
        height INT (3),
        birthday DATETIME,
        country VARCHAR(255),
        residence VARCHAR(255), 
        birth_place VARCHAR(255),
        college VARCHAR(255), 
        PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS lpga_player 
        (
        id VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255), 
        height VARCHAR (255),
        birthday DATETIME,
        country VARCHAR(255),
        residence VARCHAR(255), 
        birth_place VARCHAR(255),
        college VARCHAR(255), 
        PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS round 
        (
        session_id INT(10),
        hole INT(2),
        green_reg INT(1),
        score INT(3),
        putt INT(1), 
        fairway INT(1),
        proximity_to_hole FLOAT(5), 
        scramble INT(1),
        PRIMARY KEY(session_id));

CREATE TABLE IF NOT EXISTS practice 
        (
        session_id INT(10),
        shot_type VARCHAR(255), 
        success INT(3),
        total INT(3),
        distance FLOAT(5),
        club VARCHAR(255),
        PRIMARY KEY(session_id));

CREATE TABLE IF NOT EXISTS golf_course 
        (
        id INT(5) AUTO_INCREMENT,
        course_name VARCHAR(255),
        hole INT(2), 
        PRIMARY KEY(id));


CREATE TABLE IF NOT EXISTS self_session
        (
            session_id INT(10), 
            session_type_id INT(2), 
            course_id INT(10), 
            date DATETIME, 
            notes LONGTEXT, 
            goals LONGTEXT, 
            PRIMARY KEY(session_id));

CREATE TABLE IF NOT EXISTS session_type 
        (
        session_type_id INT(2) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(session_type_id));

CREATE TABLE IF NOT EXISTS stat_type 
        (
        stat_id INT(4) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(stat_id));

CREATE TABLE IF NOT EXISTS swing_type 
        (
        swing_id INT(3) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(swing_id));

CREATE TABLE IF NOT EXISTS distance_tracking
        (
        id INT(7) AUTO_INCREMENT,
        date DATETIME,
        club VARCHAR(255),
        distance FLOAT(5),

        PRIMARY KEY(id));