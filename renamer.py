import os

movies = []
sub = []

for x in os.listdir():
    if '.mkv' in x:
        movies.append(x)
    elif '.srt' in x:
        s = x.replace('.srt', '')
        sub.append(s)

for n in range(len(movies)):
    os.rename(movies[n], sub[n] + '.mkv')

print(movies)
print(sub)
