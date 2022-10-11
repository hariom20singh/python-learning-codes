from string import Template

nam = "Rishabh yadav"
t = Template('hello ! $w ')

print(t.substitute(w = nam))