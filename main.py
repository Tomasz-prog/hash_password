from classes import Password, File

input_file = File('passwords.txt', 'r')
output_file = File('safe_passwords.txt', 'w')

passwords = Password()
passwords.pass_normal_list = input_file.getting_passwords()
passwords.prepare_hash_password_list()
passwords.get_qty_pass_from_api()
passwords.checking_and_prepare_pass_list(1)
output_file.save_password(passwords)

print(passwords)




