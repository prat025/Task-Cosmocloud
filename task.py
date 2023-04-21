list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    list_3=[]
    res={}
    for info in list_1:
        list_3.append(info)
        res[info['id']]=len(list_3)-1
    for info in list_2:
        idx=res[info['id']]
        list_3[idx].update(info)
    return list_3

list_3 = merge_lists(list_1, list_2)
print(list_3)