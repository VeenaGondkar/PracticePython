import subprocess

# bashcommand = 'grep -E "EOM-" /home/factom/factomd/fnode05_networkinputs.txt | grep -v Drop | grep -v Embed |  grep -Eo "[0-9]{2}:[0-9]{2}:[0-9]{2} +$" > time.txt'
bashcommand = 'grep -E "EOM-" /home/factom/go/src/github.com/FactomProject/factomd/simTest/fnode02_networkinputs.txt | grep -v Drop | grep -v Embed |  grep -Eo "[0-9]{2}:[0-9]{2}:[0-9]{2} +$" > time.txt'

output = subprocess.check_output(bashcommand, shell=True)



with open('time.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
result = dict((i, content.count(i)) for i in content)
counter = 0
for i in result:
    # if result[i] == 2:
    counter += 1
    print(f"{i} : {result[i]}")

print(f"total number of times the EOM was seen {counter}")

