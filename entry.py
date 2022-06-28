import json

from pathlib import Path

from .factory import FieldFactory

# from data.obj import user_obj
# from data.singles import myobj


def convert_json_schema_to_py(json_schema: dict) -> dict:
    """
    reads json schema in json format and return dict of fields objects
    """
    final_result = {"components": []}
    properties = json_schema.get("properties", {})
    for key, content in properties.items():
        type_flag = content["type"]
        if type_flag != "object":
            required = key in json_schema.get("required")
            single_field = FieldFactory.create(key, required=required, content=content)
        else:
            single_field = FieldFactory.create(key, content=content)
        elem = json.dumps(single_field.dict_repr)
        final_result["components"].append(json.loads(elem))

    return final_result


# result = convert_json_schema_to_py(myobj)
# result = convert_json_schema_to_py(number_schema)
#
# with open(Path("one.json"), "w") as fh:
#     json_str = json.dumps(result, indent=2)
#     fh.write(json_str)
#
# with open(Path("../tests/formio_examples/user.json"), "w") as fh:
#     json_str = json.dumps(result, indent=2)
#     fh.write(json_str)
if __name__ == "__main__":
    pass
