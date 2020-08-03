import requests, hashlib, sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code},check the api and try again')
    return res


# def read_res(response):
#     print(response.text)
def get_pwd_leaks_count(hashes, tail_to_check):
    hashes = (line.split(':') for line in hashes.text.split())
    for h, count in hashes:
        if h == tail_to_check:
            return count
    return 0


def pwnd_api_check(password):
    hashedpwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = hashedpwd[:5], hashedpwd[5:]
    response = request_api_data(first5char)
    # print(first5char, tail)
    # print(response)
    # return read_res(response)
    return get_pwd_leaks_count(response, tail)


# pwnd_api_check('123')
def main(pwds):
    for pwd in pwds:
        count = pwnd_api_check(pwd)
        if count:
            print(f'{pwd} was found {count} no of time..you should probably change your pasword.')
        else:
            print(f'{pwd} never hacked, you are good.')
    return 'done..!'


lis = ['hello', 'bye', 'skjdhfkjfhd']

if __name__ == '__main__':
    sys.exit(main(lis))
