# scheduleBot
This bot is written for use with Discord. It is intended to parse a command and notify users of an upcoming event or reminder. As with all programs written with management based on time/date, timezone is important.

### Commands
Nothing here yet. This will be updated as changes are made.

### Goals of scheduleBot
  - [X] Appears on Discord
  - [X] Responds to a command
    - Initial goal is to use something like !sch \<command\> [OPTIONS]
    - [X] Has 'add' command (!sch add \<eventname\> [OPTIONS])
    - [ ] Has 'del' command
    - [ ] Has 'edit' command
    - [ ] Has 'abp' command (add by parts, bot will prompt user piece by piece)
  - [ ] Will store date information from user commands permanently (even when bot is offline)
  - [ ] Will alert user of event/reminder as date approaches
  - [ ] Has more locale options than PST
    - Timezone will initially be PST since this is being written to help the Discord channel for my class.
  - [ ] Can alert users using a particular role 
    - (e.g "bot should only alert @webdev of 'switch from react.js to vue.js deadline on 5/22/2020' event")
  - [ ] Has notification options 
    - (e.g "I want to be alerted one day and two days before an event occurs")
