**Purpose**
	The purpose of the app is to link my personal golf stats to statistics of tour players. As I set goals for myself and progress, I hope that this can be a good improvement tool. Afterwards, I will be sorting the data in various ways and I will be comparing the results.

**What should the app able to do?**
- Use CLI to enter data into “Personal Statistics 9/18 hole” table
- Use CLI to enter data into “Personal Practice” table
- Pull and save API data from Sportradar’s API into table
- Select player to compare myself to
- Average different tours/players stats to compare myself
- A few ways to sort the data and compare the sort times

**How to Run**
- Create a clone of the repo.
- Set up a MySQL database. I used MySQL Workbench.
- Create an account with Sportradar's Golf API and get a key for their golf API.
Create an env file within your repo. Include your your api_key in a variable called "golf_demo." And, your mysql password should be stored in a variable named "mysql_pass."
- I will include a requirements.txt soon. In the meantime, you can pip install the packages utilized in the top section of Run_App.py.
- Run the create_queries.sql file from the sql_queries folder. This will create all of the tables needed for your database.
- Url.py in python_files currently provide the 2021 data and so does the json files. - If you wish to update the data to 2022, which I'm not sure if it is out yet then change the year to 2022.
- Within the Run_App.py file, you can run uncomment pull=Api() and pull.api() if you wish to run the Api.py file. This will allow you to pull data from Sportradar's Golf API. If you run the API's, it may rewrite the JSON files in the "data" folder.
- Regardless of if you pull from the API, you will have to run the File_Reader.py file through the Run_App.py. This reads the JSON files.
- You will also need to run data_cleaner.py through the Run_App.py. This cleans the data and picks the columns that we want that will later be comparable to our own data.
- Open insert_queries_v2.sql. There is an insert that inserts data to pga_player. Change my data into the data that you want for yourself. You can add more personal players in the future, but for right now it is easiest for one player. Run the insert_queries_v2.sql file in your MySQL database. This will set up all of the procedures needed to insert data.
- Use Run_App.py to run Database.py. There is a method called insert_file() that will be called over and over again. But, that is alright because there is the logic won't kick back an error. The first go around should insert all of the data from the JSON files.
- Now, we should be all ready to run the Run_App.py file as a whole if everything else runs properly. Choose 1 to add data to a round/practice. Choose 2 to see graphs, but it needs data first.
- Once you have created a couple of rounds of data for both practice and 9/18 holes. - Then, you can run the view.sql file in MySQL Database. It may kick an error if there is no data.
- So, a little background of how to use Run_App.py to run the Cli.py file. It provides the logic for either if you have a practice round or a 9/18 hole round. Also, it asks if you have been to that golf course before. The inital inputting of data maybe a little fidgety because it is fairly case and space sensitive right now.
If you chose to access your graphs, you can continue to follow the prompt to choose what type of graph that you would want.

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
- Sand Save Percentage and Hazard Save Percentage
- Trying out how to calculate was difficult. I was debating if I should have used the practice table or the round table. Most likely it needed to be the round table. And, I could have had two columns: sand_success and sand_total.
- I put tracking for different items such as drive_avg, gir_pct, sand_saves_pct, scrambling, putt_avg, and scoring_avg

**What did I learn?**
- I spend most of my initial time designing how the database schema. There were a lot of design choices to be made in terms of efficiency and data validation.
- I used https://app.dbdesigner.net/.
- I learned to use association tables which allowed later inputs to be joined with their id and it forces the users to input proper values.
- Although I use SQL on a daily basis, I learned CREATE tables, ALTER tables, INSERT data, creating PROCEDURES and VIEWS
- I used git more consistently and used merge and branch for the first time.
- Originally it was one single file, but I learned to break it up into multiple files and classes.
- Instead of calling my SQL scripts through python, I learned that it was safer and more of a best practice to have sql files that I run directly in MYSQL Workbench.
- I learned to clean my data in a more programmatic way through indexes and lists.
- Instead of calling the SQL directly. I stored them into procedures in Workbench and then I called them from Python. This prevents against SQL injection easier.
- I became more comfortable with try and except statements and making sure that the proper errors are shown and easier to debug.
- I learned query maximum values from tables and then piping it back in python for calculations.
- I tried using Pandas to converting data into long instead of wide. But, for the amount of data I have currently, wide data is fine.
- I highlighted myself on graphs using a different color. I can do it in a more customizable way in Dash.
- I learned to subtract an old average and the new to get a comparison. But, there maybe a simpler way of doing it.

**What I wasn't about to do**
Some statistics were no longer needed or would be very hard to calculate, so I chose to disregard them. The items are the following
- Strokes Gained Putting
- Strokes Gained Tee to Green
- Strokes Gained Total
- Handicap
- Missed By Direction



- "Proximity to Hole Average" was in text from the API. In further iterations, I may be able to do some conversion in order to utilize that data.
- "Birdies Per Round" can also be included after the "Holes" Table is make in a further iteration.
- "Sand Save Percentage" will be included soon.
- With "Scoring Average," I'll have to double check if I actually pulled the data for it. I'll have to include it soon.
- "Score on every hole" "Putt on Every hole"- I can have it for a further iteration. However, how it is built right now it feels cumbersome to extract the data. Such a graph would be easier when using Dash or Flask
- Check if the API has fairway hit data
- Currently, I can't select certain players to compare myself to. I plan to utilize Dash for this feature later.
- I'm still figuring out how I can improve by tracking my goals

- I didn't have time to do compare various sorting times using different algorithms.
- As of this moment, I'm setting goals, however, I'm not tracking if I have succeeded in those goals. I can pull the goal each week and then input if I have succeeded in those goals.

**What went wrong**
- I didn't design my code as much as I designed the database. The different classes was an afterthought. So, reserve engineering was harder, took more time, and is less tidy.
- figuring out SQL syntax took a long time especially when I was trying to read the SQL files through Python. It was much easier to do as much SQL in the Workbench
- Similarly, I needed to design my folder structure more in the beginning. Also, I was trying to clear up the directories later on. Github was not as clear as it could have been if I took a bit more time planning folder structure.
- "Average Scores" with Pars 3,4,5 wasn't able to made because there are a design flaw. A table that has all of the pars for each hole needs to be made. After that table is made then I will need to calculate the averages. It was a good lesson to go back to the requirements to double check if I missed anything.


- add the graphs here?
