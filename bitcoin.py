# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : Pymmdrza@gmail.com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================

#              ||================================||
#              ||- ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗ -||
#              ||- ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║ -||
#              ||- ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩ -||
#              ||--------------------------------||
#              ||-| WebSite : Mmdrza.Com        -||
#              ||-| Mail : X4@Mmdrza.Com        -||
#              ||-| DEV.to/Mmdrza               -||
#              ||-| Github.Com/PyMmdrza         -||
#              ||================================||
#              ||================================||
#              ||================================||
# -----------------------------------------------------------------------------------------------------------------




import codecs
import hashlib
import threading

import ecdsa
import requests
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from requests_html import HTMLSession
from rich.console import Console
from rich.panel import Panel

console = Console()
console.clear()

filer = input('\n[*] Just Enter the Desired Text File Name [HERE] : ')

mylist = []

filename = str(filer + ".txt")
with open(filename, newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())


class Color():
    Red = '\33[31m'
    Green = '\33[32m'
    Yellow = '\33[33m'
    Cyan = '\33[36m'
    White = '\33[37m'
    Reset = '\033[0m'


# Example easy:

red = Color.Red
green = Color.Green
yellow = Color.Yellow
cyan = Color.Cyan
white = Color.White
reset = Color.Reset


def GetBal(str):
    url_n = f"https://btc2.trezor.io/address/{str}"
    se = HTMLSession()
    nmp = se.get(url_n)
    Master = nmp.html.xpath('/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]')
    return Master[0].text


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


def MmDrza():
    w = 0
    count = 0
    total = 0
    for i in range(0, len(mylist)):
        count += 1
        passphrase = mylist[i]
        wallet = BrainWallet()
        private_key, address = wallet.generate_address_from_passphrase(passphrase)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=private_key)
        # All Address Type Bitcoin Wallet -------------------
        addr1 = hdwallet.p2pkh_address()
        addr2 = hdwallet.p2sh_address()
        addr3 = hdwallet.p2wsh_address()
        addr4 = hdwallet.p2wpkh_address()
        addr5 = hdwallet.p2wsh_in_p2sh_address()
        addr6 = hdwallet.p2wpkh_in_p2sh_address()
        # All Value Check Balance ---------------------------
        bal1 = GetBal(addr1)
        bal2 = GetBal(addr2)
        bal3 = GetBal(addr3)
        bal4 = GetBal(addr4)
        bal5 = GetBal(addr5)
        bal6 = GetBal(addr6)
        total += 6
        ifer = '0 BTC'
        printer = f"[A] P2PKH           : {addr1} # Balance:{bal1}\n" \
                  f"[A] P2SH            : {addr2} # Balance:{bal2}\n" \
                  f"[A] P2WSH           : {addr3} # Balance:{bal3}\n" \
                  f"[A] P2WPKH          : {addr4} # Balance:{bal4}\n" \
                  f"[A] P2WSH COMPRESS  : {addr5} # Balance:{bal5}\n" \
                  f"[A] P2WPKH COMPRESS : {addr6} # Balance:{bal6}\n" \
                  f"[P] PRIVATE KEY : {private_key}\n" \
                  f"{'=' * 26} MMDRZA.COM {'=' * 26}\n"
        if bal1 != ifer or bal2 != ifer or bal3 != ifer or bal4 != ifer or bal5 != ifer or bal6 != ifer:
            w += 1
            with open(f"{filer}.txt", "a", encoding="utf-8", errors="ignore") as pf:
                pf.write(printer).close()

        else:
            print(
                f"{red}SCAN:{count}{reset} - {red}CHECK/REQ:{reset}{yellow}{total}{reset} - {green}Found:{w}{reset} # {cyan}Passphrase:{reset}{white}{passphrase}{reset}\n"
                f"      [P2PKH] {yellow}#{reset} BALANCE:{red}{bal1}{reset} {white}{addr1}{reset}\n"
                f"       [P2SH] {yellow}#{reset} BALANCE:{red}{bal2}{reset} {white}{addr2}{reset}\n"
                f"      [P2WSH] {yellow}#{reset} BALANCE:{red}{bal3}{reset} {white}{addr3}{reset}\n"
                f"     [P2WPKH] {yellow}#{reset} BALANCE:{red}{bal4}{reset} {white}{addr4}{reset}\n"
                f" [P2WSH-COMP] {yellow}#{reset} BALANCE:{red}{bal5}{reset} {white}{addr5}{reset}\n"
                f"[P2WPKH-COMP] {yellow}#{reset} BALANCE:{red}{bal6}{reset} {white}{addr6}{reset}\n"
                f"{'=' * 33}{yellow} MMDRZA.COM{reset} {'=' * 33}")


MmDrza()

if __name__ == "__main__":
    Master = threading.Thread(target=MmDrza)
    Master.start()
    Master.join()







# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : Pymmdrza@gmail.com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================

#              ||================================||
#              ||- ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗ -||
#              ||- ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║ -||
#              ||- ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩ -||
#              ||--------------------------------||
#              ||-| WebSite : Mmdrza.Com        -||
#              ||-| Mail : X4@Mmdrza.Com        -||
#              ||-| DEV.to/Mmdrza               -||
#              ||-| Github.Com/PyMmdrza         -||
#              ||================================||
#              ||================================||
#              ||================================||
# -----------------------------------------------------------------------------------------------------------------

