# fucking-great-advice-ru-bot
Simple telegram bot with fucking great advice from website [fucking-great-advice.ru](http://fucking-great-advice.ru)

#### Pre-Installation

1. First of all, you need create new telegram bot and get API key for your bot from BotFather. More details about [BotFather](https://core.telegram.org/bots)
2. After you got API key for your bot you must insert key at function `main` at file fucking-great-advice.py.

#### Installation

1. Clone repo [fucking-great-advice](https://github.com/unixzen/fucking-great-advice-ru-bot.git)
```
git clone https://github.com/unixzen/fucking-great-advice-ru-bot
cd ./fucking-great-advice-ru-bot
```

2. For run your personal telegram bot you can just run direct script
```
python3 ./fucking-great-advice.py
```

3. or use prepared Dockerfile
Build image for container
```
docker build -t fucking-great-advice .
```
Run docker container
```
docker run --rm -d fucking-great-advice
```

#### Usage

You can test bot if search by name at Telegram @FuckingGreatAdviceRubot.

Allowed commands:

`/start` - Start working with bot
`/help` - Short help by usage bot
`/advice` - Get random fucking great advice


#### Limitations

At present time all advices you can get only at Russian language.

