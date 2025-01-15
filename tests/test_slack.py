import pytest

from requests.exceptions import HTTPError



from typing import Any

from src.slack import user_1,url,url1

from tests.mocks.functions import mock_list_conversation,mock_list_conversation_fail

def test_conversation_list_fail():
    """ to test list_conversation api """
    # params={"limit":2,
        
    #     }
    

    response=user_1.list_conversation(url)
    assert response.status_code==200

def test_list_conversation_error():
    """to test list_conversations 
    """
    url='https://slack.com/apl/conversations.list'
    with pytest.raises(HTTPError):
        user_1.list_conversation(url)

def test_list_conversation_negative():
    """to test 
    """
    url1='https://sliack.com/api/users.list'
    with pytest.raises(HTTPError):
        user_1.list_user(url1)




def test_user_list_fail():
    """ to test list_conversation api """
    # params={"limit":2,
        
    #     }
    

    response=user_1.list_user(url1)
    assert response.status_code==200


def test_conversation_list_unauth():
    """ to test list_conversation api """
    # params={"limit":2,
        
    #     }
    
    url='https://slack.com/apl/conversations.list'
    response=user_1.list_conversation(url)
    assert response.status_code==404


def test_list_converstion_mocker(mocker:Any):
    """_summary_

    Args:
        mocker (Any): _description_
    """
    
    mocker.patch("requests.get",mock_list_conversation)
    response=user_1.list_conversation(url="test_url")
    data=response.json()
    assert response.status_code==200
    assert data['ok']=='true'


def test_list_converstion_mocker(mocker:Any):
    """_summary_

    Args:
        mocker (Any): _description_
    """
    
    mocker.patch("requests.get",mock_list_conversation_fail)
    response=user_1.list_conversation(url="test_url")
    data=response.json()
    assert response.status_code==404
    assert data['error']=="Invalid authorization"

@pytest.mark.vcr()
def test_list_conversation_vcr():
    """_summary_
    """

    response=user_1.list_conversation(url)
    assert response.status_code==200

@pytest.mark.vcr()
def test_list_user_vcr():
    """_summary_
    """

    response=user_1.list_user(url1)
    assert response.status_code==200


    