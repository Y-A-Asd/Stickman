sent = "This is a sample sentence. This Python a programming  is fun"
count = {}
for i in sent.split():
    if i not in count:
        count.update({i: 1})
    else:
        count.update({i: count[i] + 1})
max = max(count.values())
most_k = []
for k,v in count.items():
    if v == max:
        most_k.append(k)
print(f"most use words: {most_k}")
print(f"uses : {max}")
