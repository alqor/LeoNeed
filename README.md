Simple telegram bot, which reply with one of phrases from phrases.py. Deployed on Heroku (free)
<br>

* Will tell you something random on command **/speak**
* Or will trigger on words in chart (due to basic logic - if it finds the word in message which is among the words on its pre-defined phrases)

### Module used:

* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* [Flask](https://pypi.org/project/Flask/)

### PATH variables

Make sure to add variables to your local/heroku environment (in Heroku go to Dashboard-Settings):

* Telegram Bot Token (_LEONEED_TOKEN_ in code)
* Heroku

## BotFather

To get token and register your bot, speak first to [BotFather](https://t.me/botfather).

## Deploy on Heroku

1. Create or Login to exsisting [Heroku account](https://signup.heroku.com/dc). It's free and even don't ask for card.
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) (and make sure you have Git installed.)
3. The in your local terminal (in the same directory as your code is):

> heroku login
<br>

> heroku create

It will create the app and give it some random name, it could be changed in Heroku Dashboard-Settings. Make sure to put this name in [parameters.py](parameters.py) **WEBHOOK_HOST** const.

4. Make sure your requirements.txt file is relevant.
5. Create Procfile (without any extension)  - it's needed to explicitly declare what command should be executed to start your app. In this case:
> web: python main_flask.py $PORT
6. Set Heroku remote for this app (YourAppName you could check in Heroku Dashboard-Settings):
> heroku git:remote -a YourAppName
7. Make sure to commit all changes.
8. For actual deploy:
> git push heroku master

<br>
<br>
Drafts folder contains files for local polling and async version with web_hooks (which doesn't work :( )