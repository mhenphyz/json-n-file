from jsonFile import JSN

j = JSN

j._set_file('config.json')
conf = j.read()
print(j.read())
conf.update({'meunome': 'mhenphyz'})
conf.update({'realname': 'matheus'})
j.write(conf)
print(j.read())