"""api call on slack app
    """
import logging

import requests

import json


class Slack:
    """slack class 
    """
    def __init__(self,params):
        self.logger=logging.getLogger("my_logger")

        self.logger.setLevel(logging.DEBUG)

        self.handler=logging.FileHandler("slack.log",mode='w')

        self.formatter=logging.Formatter('%(process)d %(asctime)s %(name)s  %(levelname)s  %(message)s')

        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)

        self.headers={
             'Authorization':'Bearer token',
             "Content-type": "application/json",
             "Accept":"application/json",
        }

        self.params=params
          
    def list_conversation(self):
        """method to list the coversations
        """
        try:
            response=requests.get('https://slack.com/api/conversations.list',headers=self.headers,timeout=2,params=self.params)
            response.raise_for_status()
            if response.ok:
                data=response.json()
                res=json.dumps(data,indent=4)
                self.logger.info(res)
                self.logger.info(response.status_code)
            else:
                self.logger.info(f"Request got failed with status code {response.status_code}")
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured :{e}")
        except requests.exceptions.RequestException as e:
            self.logger.exception(f"exception occured :{e}")
        except TimeoutError as e:
            self.logger.exception(f"Time out for response :{e}")
    
    def list_user(self):
        """method to list the users
        """
        try:
            response=requests.get('https://slack.com/api/users.list',headers=self.headers,timeout=(2,4))
            response.raise_for_status()
            if response.ok:
                data=response.json()
                res=json.dumps(data,indent=4)
                self.logger.info(res)
                self.logger.info(response.status_code)
            else:
                self.logger.info(f"Request got failed with status code {response.status_code}")
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured :{e}")
        except requests.exceptions.RequestException as e:
            self.logger.exception(f"exception occured :{e}")
        except TimeoutError as e:
            self.logger.exception(f"Time out for response :{e}")
    

# create an object for class slack
params={"limit":2,
        
        }
user_1=Slack(params)


#call list_conversation method from user_1 object
user_1.list_conversation()


#call list_user method from user_1 object
user_1.list_user()


#to logg token to logger
# token=user_1.headers['Authorization']
# user_1.logger.info(token)    



















































