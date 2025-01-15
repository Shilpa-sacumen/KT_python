"""practice of requests and logging module
    """
import logging

import requests

import json


#created a logger
logger=logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

#create a file handler
file_handler=logging.FileHandler("test.log")

#create a formater for file handler
file_formatter=logging.Formatter('%(process)d %(asctime)s %(name)s %(levelname)s %(message)s')

#set file formatter to handler
file_handler.setFormatter(file_formatter)

#set handler to logger
logger.addHandler(file_handler)

#define custom headers
headers={
    'Authorization':'Token token',
    "Content-type": "application/json",
    "Accept":"application/json",

}

#logg messages to test.log file using get method
response=requests.get('https://api.pagerduty.com/schedules?limit=2&offset=2',headers=headers)
logger.info(response.status_code)
data=response.json()
logger.info(json.dumps(data,indent=4))


#logg response of post method to create a schedule
def create_schedule():
    """to create new schedule
    """
    payload={
             "schedule": {
               "name": "Project9",
               "type": "schedule",
               "time_zone": "Etc/UTC",
               "description": "Rotation schedule for Project6",
               "schedule_layers": [
                 {
                   "name": "Night Shift",
                   "start": "2015-11-06T20:00:00-05:00",
                   "rotation_virtual_start": "2015-11-06T20:00:00-05:00",
                   "rotation_turn_length_seconds": 86400,
                   "users": [
                     {
                       "user": {
                         "id": "PASIKSM",
                         "type": "user_reference"
                       }
                     }
                   ],
                   "restrictions": [
                     {
                       "type": "daily_restriction",
                       "start_time_of_day": "08:00:00",
                       "duration_seconds": 32400
                     }
                   ]
                 }
               ]
             }
         }
            
    response=requests.post('https://api.pagerduty.com/schedules/',headers=headers,data=json.dumps(payload))
    logger.info(response.status_code)
    logger.debug(response.json())

#call the create_schedule function to create new schedule
# create_schedule()


#update the shedule
def update_schedule():
    """update the schedule
    """
    payload={
  "schedule": {
    "name": "kt_logging",
    "type": "schedule",
    "time_zone": "America/New_York",
    "description": "Rotation schedule for engineering",
    "schedule_layers": [
      {
        "name": "Night Shift",
        "start": "2015-11-06T20:00:00-05:00",
        "end": "2016-11-06T20:00:00-05:00",
        "rotation_virtual_start": "2015-11-06T20:00:00-05:00",
        "rotation_turn_length_seconds": 86400,
        "users": [
          {
            "user": {
              "id": "PASIKSM",
              "type": "user_reference"
            }
          }
        ],
        "restrictions": [
          {
            "type": "daily_restriction",
            "start_time_of_day": "08:00:00",
            "duration_seconds": 32400
          }
        ]
      }
    ]
  }
}
    response=requests.put('https://api.pagerduty.com/schedules/P9O8THY',headers=headers,data=json.dumps(payload))
    logger.info(response.status_code)
    logger.debug(response.json())

#call update_schedule fuction to update schedule
# update_schedule()


#delete the schedule
def delete_schedule():
  """delete a schedule
  """
  response=requests.delete('https://api.pagerduty.com/schedules/PCKE7S6',headers=headers)
  logger.info(response.status_code)
  # logger.debug(response.json())

#call delete_schedule to delete the schedule
# delete_schedule()


#patch method
def patch_schedule():
  """patch a schedule
  """
  payload={
    "schedule":{
      "name":"kt_on_requests",
    }
  }
  response=requests.patch('https://api.pagerduty.com/schedules/PXQRXL2',headers=headers,data=json.dumps(payload))
  logger.info(response.status_code)
  logger.debug(response.json())

#call the patch_schedule to patch the schedule details
# patch_schedule()


