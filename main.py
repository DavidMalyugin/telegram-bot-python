import telebot
import requests

TOKEN = "7817991056:AAFs6zeYvpu3HzaFosbHCeq_xlwgPe59R7o"
bot = telebot.TeleBot(TOKEN)

COIN_MAPPING = {
    "bitcoin": "bitcoin", "ethereum": "ethereum", "dogecoin": "dogecoin", "cardano": "cardano", "ripple": "ripple",
    "polkadot": "polkadot", "binance coin": "binancecoin", "litecoin": "litecoin", "chainlink": "chainlink", "stellar": "stellar",
    "monero": "monero", "tron": "tron", "uniswap": "uniswap", "solana": "solana", "avalanche": "avalanche",
    "polygon": "polygon", "cosmos": "cosmos", "algorand": "algorand", "vechain": "vechain", "filecoin": "filecoin",
    "aave": "aave", "tezos": "tezos", "theta": "theta", "elrond": "elrond", "fantom": "fantom",
    "hedera": "hedera", "decentraland": "decentraland", "the sandbox": "thesandbox", "axie infinity": "axieinfinity",
    "gala": "gala", "maker": "maker", "compound": "compound", "enjin coin": "enjincoin", "zcash": "zcash",
    "quant": "quant", "iota": "iota", "thorchain": "thorchain", "kusama": "kusama", "nexo": "nexo",
    "chiliz": "chiliz", "arweave": "arweave", "curve dao": "curve", "waves": "waves", "dash": "dash",
    "yearn finance": "yearnfinance", "harmony": "harmony", "loopring": "loopring", "basic attention token": "basicattentiontoken",
    "helium": "helium", "ontology": "ontology", "ocean protocol": "oceanprotocol", "siacoin": "siacoin",
    "storj": "storj", "livepeer": "livepeer", "ankr": "ankr", "fetch.ai": "fetch", "dydx": "dydx",
    "reef": "reef", "cartesi": "cartesi", "sushiswap": "sushiswap", "celo": "celo", "iotex": "iotex",
    "tomo chain": "tomochain", "serum": "serum", "hive": "hive", "nervos network": "nervosnetwork", "api3": "api3"
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send /crypto bitcoin, then you can know bitcoin price.")

@bot.message_handler(commands=['crypto', 'price'])
def get_crypto_price(message):
    try:
        coin_name = message.text.split()[1].lower()
        coin = COIN_MAPPING.get(coin_name, coin_name)
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(url).json()

        print(f"API response for {coin}: {response}")  # Логируем ответ API

        if coin in response:
            price = response[coin]['usd']
            bot.reply_to(message, f'💰Price of {coin_name.capitalize()}: ${price}')
        else:
            bot.reply_to(message, '⚠ Error! Wrong coin name.')
    except IndexError:
        bot.reply_to(message, '⚠ Input valid crypto name! Example: /crypto bitcoin')
    except Exception as e:
        bot.reply_to(message, f'⚠ Error: {e}')

bot.polling()
