"""api call on slack app
    """
import logging

import requests

import json


class InvalidURLError(Exception):
    """Custom exception for invalid URLs."""
    pass


class Slack:
    """slack class 
    """
    def __init__(self):
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

       
          
    def list_conversation(self,url:str):
        """method to list the coversation
        """
        try:
            response=requests.get(url,headers=self.headers)
            # response.raise_for_status()
            if response.ok:
                data=response.json()
                res=json.dumps(data,indent=4)
                self.logger.info(res)
                self.logger.info(response.status_code)
                return response
            else:
                self.logger.exception(f"error found :{response.content}") 
                return response   
           
       
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured :{e}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.exception(f"exception occured here:{e}")
            raise
        
        except Exception as e:
            self.logger.exception(f"error-occured :{e}")
            raise
    
    def list_user(self,url1):
        """method to list the users
        """
        try:
            response=requests.get(url1,headers=self.headers)
            response.raise_for_status()
            if response.ok:
                data=response.json()
                res=json.dumps(data,indent=4)
                self.logger.info(res)
                self.logger.info(response.status_code)
                return response
            else:
                self.logger.exception(f"error found :{response.content}") 
                return response   
           
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured :{e}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.exception(f"exception occured: {e}")
            raise
        
        except Exception as e:
            self.logger.exception(f"error-occured :{e}")
            raise
    

# create an object for class slack
# params={"limit":2,
        
#         }
user_1=Slack()

url='https://slack.com/api/conversations.list'
#call list_conversation method from user_1 object
user_1.list_conversation(url)

url1='https://slack.com/api/users.list'
#call list_user method from user_1 object
# user_1.list_user(url1)


#to logg token to logger
# token=user_1.headers['Authorization']
# user_1.logger.info(token)    



















































