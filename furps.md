## FURPS

_F_
### Functionality
- Collecting data from the surrounding environment
- Processing of the collected data
- The movement of the bot will be facilitated by a gamepad or over SSH/HTTPS
- The data collected needs to be accurate
- The control interface of the bot needs to be secure (SSH/HTTPS)
- A warning system for very high temperatures and humidities

_U_
### Usability
- The user will be able to access the bot and control it remotely over multiple protocols
- The user will be able to command the bot to move to a desired location,\
may it be a dangerous environment or enemy territory
- The user will be able to retrieve collected data from the bot for further analysis
- Interacting with the bot is made simple and straightforward (_KISS_)

_R_
### Reliability
- A connection recovery system in case of the bot losing connection
- The buzzer will start buzzing when Internet connection is lost\
(dropped **ICMP**s to [ongakken.dk](ongakken.dk))
- The bot must be able to withstand stress and high temperatures/humidities

_P_
### Performance
- The bot must respond to user commands within 50ms
- The bot should be able to go for 2 hours on one charge\
(supposed that we have a 10 000mAh powerbank connected)
- The user should be able to add stuff to the bot to expand it
- The bot should use 50% of CPU time at most
- The bot should use a maximum of 50% of available memory

_S_
### Supportability
- The bot should have an interface for localization so that a user can translate the command interfaces
- All of the software components (classes or so) of the bot are configurable
