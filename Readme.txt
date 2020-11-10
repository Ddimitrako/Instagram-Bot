The purpose of this project is to auto comment in instagram giveaway-competitions an win some extra posibilities to win by 
letting the bot auto comment contuniusly
The bot starts by reading a comments.txt file where we have stored all of our comments
After that it opens Mozilla Firefox an connect to the Instagram with our account pass and name
Then it goes to the aproprate Instagram link we have set in the bot and start commenting.
This bot has also a smart way to stop instagram from blocking the bot comments after they are continiusly.
It uses an increasingly random time algorithm between comments so this way it can extend its operation time

How to use the code:

1.Install geckodriver.exe in a path an then copy the path to the Instagram_bot.py in line 6
geckodriver is used to acess Mozilla Firefox. For Chrome you should download ChromeDriver.
For more info visit this https://www.edureka.co/blog/selenium-chromedriver-and-geckodriver/

2.Select the link of the picture you want to comment then copy and paste it to Instagram_bot.py in line 60
3. To run the program open both .py scripts an run Main
Also remenber to add your credentials in line 19 in Main.py