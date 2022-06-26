user_obj = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "person",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "object",
                    "properties": {
                        "last_name": {
                            "type": "string",
                            "maxLength": 250,
                        },
                        # "required": ["last_name"],
                    },
                    "required": ["last_name"],
                },
                "email": {"type": "string", "format": "email"},
            },
            "required": ["email"],
        }
    },
}
