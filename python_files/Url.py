
"""
Dictionary of keys with the links.
You can try changing the year  to 2022, but the data may not be out yet. 
stat contains the statistics of the tour players. 
pga_player has the demogrpahics information for pga players. 
lpga_player has the demopgrahics information for lpga players. It is currently not used because, their statistics are currently not avaliable. 
lpga_tournament is currently not used. It contains tournament information for lpga players.  

"""

year=2021
url= {#'ranking':f'https://api.sportradar.us/golf/trial/v3/en/players/wgr/{year}/rankings.json?',
'stat':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/statistics.json?',
'pga_player':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/profiles.json?',
'lpga_player':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/players/profiles.json?',
# 'pga_tournament':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/tournaments/schedule.json?',
'lpga_tournament':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/tournaments/schedule.json?'

    } #have to edit id

