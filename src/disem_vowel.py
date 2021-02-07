import re
def disemvowel(string):
    return re.sub(r'[aieouAIEOU]','',string)

print(disemvowel('This website is for losers LOL!'))