import json
from pathlib import Path

from .factory import FieldFactory

# from data.obj import user_obj
# from data.singles import *


def get_single_item(content: dict) -> dict:
    """create a new object depending on type of a field"""
    obj = FieldFactory.create(content=content)
    return obj


def convert_json_schema_to_py(json_schema: dict) -> dict:
    """
    reads json schema in json format and return dict of fields objects
    """
    final_result = {"components": []}
    properties = json_schema.get("properties", {})
    for key in properties.keys():
        type_flag = json_schema["properties"][key]["type"]
        content = properties[key]
        content.update({"key": key})
        if type_flag != "object":
            if key in json_schema.get("required"):
                content.update({"required": True})
            single_field = get_single_item(content=properties[key])
        else:
            single_field = get_single_item(content=properties[key])
            result = convert_json_schema_to_py(json_schema=content)
            # single_field.components .append(result)
            single_field.components = result["components"]
        elem = json.dumps(single_field.dict_repr)
        final_result["components"].append(json.loads(elem))

    return final_result


# result = convert_json_schema_to_py(user_obj)
#
# with open(Path("fake/may.json"), "w") as fh:
#     json_str = json.dumps(result, indent=2)
#     fh.write(json_str)
#
# with open(Path("../tests/formio_examples/user.json"), "w") as fh:
#     json_str = json.dumps(result, indent=2)
#     fh.write(json_str)
if __name__ == "__main__":
    pass
