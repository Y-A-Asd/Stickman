# with open("point.csv", "r") as input_file:
#     inputs = input_file.readlines()
#     output_dict = {}
#     for item in inputs:
#         key_value = item.split(',')
#         output_dict[key_value[0]] = float(key_value[1].strip())

    # print(output_dict)
# with open("point.csv", "r") as input_file: dict(zip(key_value[0],float(key_value[1].strip())) for key_value in item.strip() for item in input_file.readlines())
with open("point.csv", "r") as input_file: inputs_dict = dict((key_value[0], float(key_value[1].strip())) for key_value in (item.split(',') for item in input_file.readlines()))
print(inputs_dict)
# top = {}
# low = {}
# for k,v in inputs_dict.items():
#     if int(v) > 16 :
#         top.update({k:v})
#     else:
#         low.update({k:v})
top = {k:v for k,v in inputs_dict.items() if int(v) >= 17}
mid = {k:v for k,v in inputs_dict.items() if int(v) >= 17}
low = {k1:v1 for k1,v1 in inputs_dict.items() if int(v1) < 10}
print("\ntops: ",top,"\nlows:",low)
def search(name,top = top,mid = mid, low = low):

    if name in top:print(f"u r graduate : {name}")
    elif name in low:print(f"u r not graduate : {name}")
    else: print(f"{name} not found")
search(name = input("name: "))