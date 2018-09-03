![Header](images/README_Header.png)  

A wrapper for the Fortnite Tracker API written in Python3. 
[A Fortnite Tracker API scraper exists](https://github.com/mgp25/Fortnite-API), 
but this library plays by the Fortnite Tracker rules. 

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Examples](#examples)  
- [Notes](#notes)
- [License](#license)  

## Requirements  
- An Epic Games account linked to your PC, PSN, or Xbox Live account.  
- A Fortnite Tracker account and API key. [Register your Fortnite Tracker API key here](https://fortnitetracker.com/site-api)  
- Python 3 
  
  
## Installation  
Clone the repo and drag the FortniteAPI folder into your project, and removed the unneeded files.  
  
## Examples  
When creating your API object you'll need to suppy it with a platform.  
There are only 3 valid platform values.      
  
| Platform  | Value |
| --------- | ----- |
| PC        | `pc`   |
| Playstation | `psn`|
| Xbox One    | `xbl`|  
  
The API object will return a `FortniteStats` object that contains all useful stats given by the Fortnite Tracker API.
Fortnite tracker also provides recent games, and additional lifetime stats, such as top 3, 5, 6, etc but this data 
didn't seem very reliable to me so I didn't include it.   

The `FortniteStats` object has properties for current season, and lifetime stats. All stat properties are in upper case 
with current stats having `CURRENT_` appended to the front and lifetime stats having `LIFETIME_` appended to the 
front. The playlist for the stats is specified next by either `SOLO_`, `DUO_`, or `SQUAD_`.  
  
Examples:  
`stats.CURRENT_SOLO_KPG`  
`stats.LIFETIME_SOLO_KPG`  
`stats.LIFETIME_KPG`  
  
  
A quick look into the `Stats.py` file will give you an idea on all the stats that are available.  
  
    from FortniteAPI import FortniteAPI
  
    FortniteAPI.api_key = 'fortnite_api_key'
    api = FortniteAPI('xbl', 'tylerw330')
  
    print('Solo kills per game: ' + str(api.stats.CURRENT_SOLO_KPG))
    print('Duo kills per game: ' + str(api.stats.CURRENT_DUO_KPG))
    print('Squad kills per game: ' + str(api.stats.CURRENT_SQUAD_KPG))
     
If you'd like to change what user you get your data for call the `set_user(self, user)` method:  
`api.set_user('different_user')`  
  
This method assumes the user is on the same platform.  
If you want to change the platform call the `set_platform(self, platform)` method, then reset the user with `set_user(self, user)`  
  
`api.set_platform('pc')`  
`api.set_user('user_name')`  
      
## License  
  
Copyright (c) 2018 Tyler Williamson Licensed under the WTFPL license.