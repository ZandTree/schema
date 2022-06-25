import pytest
from src.entry import convert_json_schema_to_py
from data.example_object import  user_obj


@pytest.mark.parametrize(
    "schema,expected_output",
    [
        (user_obj, "fieldset"),

    ],
)
def test_simple(schema, expected_output):
    print(convert_json_schema_to_py(schema))
    assert convert_json_schema_to_py(schema)["components"][0]["type"] == expected_output


