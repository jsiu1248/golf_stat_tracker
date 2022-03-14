**Purpose**
	The purpose of the app is to link my personal golf stats to statistics of tour players. As I set goals for myself and progress, I hope that this can be a good improvement tool. Afterwards, I will be sorting the data in various ways and I will be comparing the results.

**What should the app able to do?**
- Use CLI to enter data into “Personal Statistics 9/18 hole” table
- Use CLI to enter data into “Personal Practice” table
- Pull and save API data from Sportradar’s API into table
- Select player to compare myself to
- Average different tours/players stats to compare myself
- A few ways to sort the data and compare the sort times

**Stakeholder and Audience**
- For now, the application will be for personal use.

**Data Sources**
- Sportradar’s Golf API
-	Personal 9/18 hole statistics
-	Personal practice statistics
**Tables Used**
-	Players: Get info about all players
-	Have to figure out what to pull from the Player Profiles table
-	Player Profiles: Stat for a single player (decide how important this info is)
-	Birthplace
-	Birthday
-	First Name
-	Id
-	Last Name
-	Rank
-	Prior Rank
-	Year Turned Pro
-	Residence
-	College
-	Player Statistics: Stats for all players
-	Average Driving Distance
-	Drive Accuracy Percentage
-	Greens in Regulation
-	Strokes Gained Putting
-	Strokes Gained Tee to Green
-	Strokes Gained Total
-	Birdies Per Round
-	Proximity to Hole Average
-	Putting Average
-	Sand Save Percentage
-	Scoring Average
-	Personal Statistics 9/18 hole
-	Average Scores
	- Par 3
	- Par 4
	- Par 5
-	Handicap
-	Score on every hole
-	Putts on every hole
-	Greens in Regulation on every hole
-	If fairway was Hit of every hole
-	Location
-	Date
-	Total Score
-	Numbers of Sand Save/Miss on Hole
-	Number of Hazards Save/Miss on Hole
-	Proximity to Hole for Every Hole
-	Scrambling for Every Hole
-	Notes
-	Goals
-	Personal Practice
-	Location
-	Date
-	Total Score
-	Number of Fairways Hit
-	Notes
-	Greens in Regulation
-	Scrambling
-	Putts
-	Sand Save Percentage
-	Hazards
-	Proximity to Hole
-	Missed By Direction
	- Left
	- Right
	- Long
	- Short
- Goals

**Dependencies**
-	Sportradar’s Golf API
-	MySQL Database
-	Python

**Considerations/Difficulties/Decisions (Ongoing)**
-	Layout of “Personal Statistics 9/18 hole” table
- How do I make it not as cumbersome?
- How do I account for multiple hazards and sand?
-	Layout of “Personal Practice” table
-	How do I calculate proximity to hole?

**Exit Report** 3/13/2022
**What I was able to get done**
I have been able to complete most of the project.
- I have CLI interactive prompts to input round and practice data.
- I pulled data and saved it into a MYSQL Database.
- I created multiple graphs through plotly that I can compare myself to the pro and also track my progress for various stats.
**What did I learn?**
- I learned to use association tables.
- Although I use SQL on a daily basis, I learned CREATE tables, ALTER tables,
**What I wasn't about to do**
Some statistics were no longer needed or would be very hard to calculate, so I chose to disregard them. The items are the following
- Strokes Gained Putting
- Strokes Gained Tee to Green
- Strokes Gained Total
- Handicap
- Missed By Direction
- Sand Save Percentage and Hazard Save Percentage
	- Trying out how to calculate was difficult. I was debating if I should have used the practice table or the round table. Most likely it needed to be the round table. And, I could have had two columns: sand_success and sand_total.


"Proximity to Hole Average" was in text from the API. In further iterations, I may be able to do some conversion in order to utilize that data.
"Birdies Per Round" can also be included after the "Holes" Table is make in a further iteration.
"Sand Save Percentage" will be included soon.
With "Scoring Average," I'll have to double check if I actually pulled the data for it. I'll have to include it soon
"Average Scores" with Pars 3,4,5 wasn't able to made because there are a design flaw. A table that has all of the pars for each hole needs to be made. After that table is
made then I will need to calculate the averages. It was a good lesson to go back to the requirements to double check if I missed anything.
"Score on every hole" "Putt on Every hole"- I can have it for a further iteration. However, how it is built right now it feels cumbersome to extract the data.
Such a graph would be easier when using Dash or Flask
- Check if the API has fairway hit data
- Currently, I can't select certain players to compare myself to. I plan to utilize Dash for this feature later.
- I'm still figuring out how I can improve by tracking my goals

- I didn't have time to do compare various sorting times using different algorithms.
- As of this moment, I'm setting goals, however, I'm not tracking if I have succeeded in those goals. I can pull the goal each week and then input if I have succeeded in those goals.

**What went wrong**

- add the graphs here?
