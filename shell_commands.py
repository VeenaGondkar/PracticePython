from shell_scripting import shell, run, shell_list

run("date | sed s/2018/2019/ > test.out")

print(shell("env | grep USER").stdout.split("\n"))

print(shell("cat /root/file"))

r = shell("cat /root/file")
print(r)
for x in shell_list("env"):
    print(x)