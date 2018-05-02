![Header](images/README_Header.png)  

A wrapper for the Fortnite Tracker API written in Python3. 
[A Fortnite Tracker API scraper exists](https://github.com/mgp25/Fortnite-API), 
but this library plays by the Fortnite Tracker rules. 

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Documentation](#documentation)  
- [Examples](#examples)  
- [Notes](#notes)
- [License](#license)  

## Requirements  
- An Epic Games account linked to your PC, PSN, or Xbox Live account.  
- A Fortnite Tracker account and API key. [Register your Fortnite Tracker API key here](https://fortnitetracker.com/site-api)  
  
- Python 3 (It probably works on Python2, but I'm too lazy to test that)
  
  
## Installation  
Clone the repo and drag the FortniteAPI folder into your project.  
  
## Documentation  
When creating your API object you'll need to suppy it with a platform.  
There are only 3 valid platform values.      
  
| Platform  | Value |
| --------- | ----- |
| PC        | `pc`   |
| Playstation | `psn`|
| Xbox One    | `xbn`|  
  
Every API call, aside from lifetime stats, requires a playlist value to be supplied.  
Here is the list of valid Enum's for the Fortnite Playlists:  
  
| Playlist  | Value |
| --------- | ----- |
| Solo                 | `FortnitePlaylist.SOLO`          |
| Duo                  | `FortnitePlaylist.DUO`           |
| Squads               | `FortnitePlaylist.SQUAD`         |  
| Current Season Solo  | `FortnitePlaylist.CURRENT_SOLO`  |
| Current Season Duo   | `FortnitePlaylist.CURRENT_DUO`   |
| Current Season Squad | `FortnitePlaylist.CURRENT_SQUAD` |
  
And, finally, here are all the currently available API calls.  
  
| Method         | Description   | Parameters | Return Value |
| -------------- | ------------- | ---------- | ------------ |
| `__init__(self, platform, user)`       | Initialized the FortniteAPI object            | `platform` - The gaming platform. Valid values are listed above. `user` - an Epic Games user account | `FortniteAPI`          |
| `set_api_key(self, key)`               | Sets the API key for the FortniteAPI object   | `key` - your Fortnite Tracker API Key                                                                | `void`                 |
| `set_user(self, user)`                 | Changes the user.                             | `user` - an Epic Games user account                                                                  | `void`                 |
| `set_platform(self, platform)`         | Changes the platform.                         | `platform` - The gaming platform                                                                     | `void`                 |
| `get_score(self, playlist)`            | Gets the users score                          | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
| `get_top_one(self, playlist)`          | Retuns number of wins                         | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
| `get_top_three(self, playlist)`        | Returns number of top 3's                     | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_top_five(self, playlist)`        | Returns number of top 5's                     | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_top_six(self, playlist)`         | Returns number of top 6's                     | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_top_ten(self, playlist)`         | Returns number of top 10's                    | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_top_twelve(self, playlist)`      | Returns number of to 12's                     | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_top_twenty_five(self, playlist)` | Returns the number of to 25's                 | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_kd(self, playlist)`              | Returns the user's kill death ratio           | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_matches(self, playlist)`         | Returns the number of matches played          | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_kills(self, playlist)`           | Returns the number of kills for a user        | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
|  `get_kpg(self, playlist)`             | Returns the average number of kills per game  | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
| `get_score_per_match(self, playlist)`  | Returns the users score                       | `playlist` - A FortnitePlaylist enum value                                                           | `String`               | 
| `get_lifetime_score(self)`             | Returns the overall score of the user         | None                                                                                                 | `String`               | 
| `get_lifetime_matches_played(self)`    | Returns total number of matches played        | None                                                                                                 | `String`               | 
| `get_lifetime_wins(self)`              | Returns total number of wins for the user     | None                                                                                                 | `String`               | 
| `get_lifetime_win_percentage(self)`    | Returns the lifetime win percentage           | None                                                                                                 | `String`               | 
| `get_lifetime_kills(self)`             | Returns a users total amount of kills         | None                                                                                                 | `String`               | 
| `get_lifetime_kd(self)`                | Returns a users total kill death ratio        | None                                                                                                 | `String`               | 
| `get_score_per_match(self)`            | Returns a users total average kills per match | None                                                                                                 | `String`               | 


## Examples  
Import the FortniteAPI files  
`from FortniteAPI import FortnitePlaylist, FortniteAPI`  
  
Create the FortniteAPI object supplying the constructor with the platform, and your Epic Games account name:  

`api = FortniteAPI('xbl', 'tylerw330')`  
    
Now you need to give the API your api key:    
`api.set_api_key('YOUR-API-KEY')`  
  
From here you're ready to start making some API calls. Most methods in the API take a `FortnitePlaylist` enum value as a parameter.  
`kill_death_ratio = api.get_kd(FortnitePlaylist.SOLO)`  
  
If you'd like to change what user you get your data for call the `set_user(self, user)` method:  
`api.set_user('different_user')`  
  
This method assumes the user is on the same platform.  
If you want to change the platform call the `set_platform(self, platform)` method, then reset the user with `set_user(self, user)`  
  
`api.set_platform('pc')`  
`api.set_user('user_name')`  

  
## Notes  
Fortnite tracker also provides recent games, and additional lifetime stats, such as top 3, 5, 6, etc.  
This data didn't seem very reliable to me so I didn't include it, but it can be accessed from the json data.   
  
There is also no error handling in this because I'm lazy. If a user hasn't played in the current season, an exception will happen 
claiming an invalid key, so make sure you properly handle error when using this code. As a result of no error handling, 
I'm sure random errors will occur. If it bothers you enough, open a pull request. I'll look over it and accept it.  
If you do send a pull request, make sure you follow the [PEP-8 style guide](https://www.python.org/dev/peps/pep-0008/).  
  
## License  
  
Copyright (c) 2018 Tyler Williamson Licensed under the WTFPL license.