import json


def get_title(values_list, value):

    for d in values_list:
        if d['id'] == value:
            return d['title']
    return ''


def try_insert(p_id, value, array):

    for param in array['params']:
        if param['id'] == p_id:

            if param.get('values') is None:
                param['value'] = value
            elif type(value) is str:
                raise
            else:
                param['value'] = get_title(param['values'], value)

        elif param.get('values'):
            for d in param['values']:
                try_insert(p_id, value, d)


try:

    to_fill = json.load(open("TestcaseStructure.json"))
    values = json.load(open("Values.json"))

    for obj in values['values']:
        try_insert(obj['id'], obj['value'], to_fill)

except:
    json.dump({'error': {'message': 'Входные файлы некорректны'}}, open('error.json', 'w'), ensure_ascii=False, indent=4)

else:
    json.dump(to_fill, open("StructureWithValues.json", "w"), ensure_ascii=False, indent=4, sort_keys=True)
