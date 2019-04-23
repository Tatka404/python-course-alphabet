from typing import List, Dict, Union, Generator
import random
import string
import math

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:

    #for student in data:
    #    if 'name' in student:
    #       student["name"] = student["name"].capitalize()
    #return data

    #2
    #[k.update({'name': k.get('name').title() if type(k.get('name')) == str else k.get('name')}) for k in data]
    #return data

    #3
    #[k.update({'name': k.get('name').title() if isinstance(k.get('name'),str) else k.get('name')}) for k in data]
    #return data

    #4
    [k.update({'name': k.get('name').title()}) if isinstance(k.get('name'), str) else None for k in data]
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:


    #for student in data:
     #   for key in redundant_keys:
     #       student.pop(key)
    #return data

    #2:
    #for r in range (len(redundant_keys)):
    #    for item in data:
    #        item.pop(redundant_keys[r])
    #return data

    #3
    return [{key: value for key, value in student.items() if key not in redundant_keys} for student in data]


def task_3_find_item_via_value(data: DT, value) -> DT:

    return [({key:value for key,value in student.items()}) for student in data if value in student.values()]


def task_4_min_value_integers(data: List[int]) -> int:

    if data:
        return min(data)

    #2: return min(data, default = None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:

    if data:
        return min([str(r) for r in data], key = len)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:

    return dict(*[r for r in data if r.get(key)==(min([r.get(key) for r in data if r.get(key)]))])


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:

    return max([item for sublist in data for item in sublist])


def task_8_sum_of_ints(data: List[int]) -> int:

    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:

    return sum(r for r in bytearray(text, 'ascii'))


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:

    for num in range(2, 201):
        if all(num%i !=0 for i in range (2, int(math.sqrt(num))+1)):
            yield num


def task_11_create_list_of_random_characters() -> List[str]:

    return random.sample(string.ascii_lowercase, 20)

