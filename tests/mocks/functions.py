from requests import Response
from typing import Any,List,Dict
import json

def mock_list_conversation(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """mock for converstion list api success

    Returns:
        Response: _description_
    """
    result={
        "ok": "true",
        "channels": [
        {
            "id": "C086YFZ9DDL",
            "name": "all-shilpa",
            "is_channel": "true",
            "is_group": "false",
            "is_im": "false",
            "updated": 1735880230018,
            "shared_team_ids": [
                "T0877KXMYAY"
            ],
            "properties": {
                "canvas": {
                    "file_id": "F086YFZAKSA",
                    "is_empty": "false",
                    "quip_thread_id": "DOF9AA4MjtB"
                },
                "use_case": "welcome"
            },
            "previous_names": [
                "all-slack"
            ],
            "num_members": 4
        },
        ]
    }
    url='https://slack.com/api/conversations.list'
    response=Response()
    response.url=url
    response.status_code=200
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response

def mock_list_conversation_fail(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """_summary_

    Returns:
        Response: _description_
    """
    result={
        'error':"Invalid authorization"
    }
    url='https://slack.com/api/conversations.list'
    response=Response()
    response.url=url
    response.status_code=404
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response
