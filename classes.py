from requests import get
import hashlib

class Password:
    def __init__(self):

        self.pass_normal_list = []
        self.pass_hash_list = []
        self.pass_counter_list = []
        self.pass_safe_list = []

    def prepare_hash_password_list(self):
        pass_hash_list = []
        for password in self.pass_normal_list:
            hash_pass_5 = hashlib.sha1(password.split()[0].encode()).hexdigest()[:5]
            pass_hash_list.append(hash_pass_5)
        self.pass_hash_list = pass_hash_list

    def get_qty_pass_from_api(self):
        pass_counter_list = []
        for char_5_hash in self.pass_hash_list:
            response = get(f'https://api.pwnedpasswords.com/range/{char_5_hash}')
            counter = response.text.splitlines()[0].split(':')[1]
            pass_counter_list.append(counter)
        self.pass_counter_list = pass_counter_list

    def checking_and_prepare_pass_list(self, qty):
        safe_pass = []
        for i in range(len(self.pass_hash_list)):
            if int(self.pass_counter_list[i]) > qty:
                safe_pass.append(self.pass_normal_list[i])

        self.pass_safe_list = safe_pass

    def __str__(self):
        return f'{self.pass_normal_list}'

class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def getting_passwords(self):

        with open(self.name, self.mode, encoding='utf-8') as file:
            pass_list = []
            for password in file:
                pass_list.append(password.strip())
            return pass_list



    def save_password(self, Password):

        with open(self.name, self.mode, encoding='utf-8') as file:
            for password in Password.pass_safe_list:
                file.write(f'{password}\n')






