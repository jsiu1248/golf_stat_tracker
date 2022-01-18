#**Purpose**
	The purpose of the app is to link my personal golf stats to statistics of tour players. As I set goals for myself and progress, I hope that this can be a good improvement tool. Afterwards, I will be sorting the data in various ways and I will be comparing the results. 
#**What should the app able to do?**
    Use CLI to enter data into “Personal Statistics 9/18 hole” table
    Use CLI to enter data into “Personal Practice” table
    Pull and save API data from Sportradar’s API into table
    Select player to compare myself to
    Average different tours/players stats to compare myself
    A few ways to sort the data and compare the sort times
#**Stakeholder and Audience**
-	For now, the application will be for personal use. 
#**Data Sources**
-	Sportradar’s Golf API
-	Personal 9/18 hole statistics
-	Personal practice statistics
#**Tables Used**
-	Players: Get info about all players
o	Have to figure out what to pull from the Player Profiles table
-	Player Profiles: Stat for a single player (decide how important this info is)
o	Birthplace
o	Birthday
o	First Name
o	Id
o	Last Name
o	Rank
o	Prior Rank
o	Year Turned Pro
o	Residence
o	College
-	Player Statistics: Stats for all players
o	Average Driving Distance
o	Drive Accuracy Percentage
o	Greens in Regulation
o	Strokes Gained Putting
o	Strokes Gained Tee to Green
o	Strokes Gained Total
o	Birdies Per Round
o	Proximity to Hole Average
o	Putting Average
o	Sand Save Percentage
o	Scoring Average
-	Personal Statistics 9/18 hole
o	Average Scores
	Par 3
	Par 4
	Par 5
o	Handicap
o	Score on every hole
o	Putts on every hole
o	Greens in Regulation on every hole
o	If fairway was Hit of every hole
o	Location
o	Date
o	Total Score
o	Numbers of Sand Save/Miss on Hole
o	Number of Hazards Save/Miss on Hole
o	Proximity to Hole for Every Hole
o	Scrambling for Every Hole
o	Notes
o	Goals
-	Personal Practice
o	Location
o	Date
o	Total Score
o	Number of Fairways Hit
o	Notes
o	Greens in Regulation
o	Scrambling
o	Putts
o	Sand Save Percentage
o	Hazards
o	Proximity to Hole
o	Missed By Direction
	Left
	Right
	Long
	Short
o	Goals

**Dependencies**
-	Sportradar’s Golf API
-	MySQL Database
-	Python

**Considerations/Difficulties/Decisions (Ongoing)**
-	Layout of “Personal Statistics 9/18 hole” table
o	How do I make it not as cumbersome?
o	How do I account for multiple hazards and sand?
-	Layout of “Personal Practice” table
-	How do I calculate proximity to hole?
