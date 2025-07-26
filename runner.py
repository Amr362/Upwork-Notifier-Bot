#!/usr/bin/env python3
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import sys
import os

python_command = sys.executable
script_to_run = "upwork_job_feed_notifier.py"


# function to invoke the main script
def cron_process():
    print("checking for new notifications...")
    subprocess.Popen([python_command, script_to_run])


logo = """
ooooo     ooo                                                oooo        
`888'     `8'                                                `888        
 888       8  oo.ooooo.  oooo oooo    ooo  .ooooo.  oooo d8b  888  oooo  
 888       8   888' `88b  `88. `88.  .8'  d88' `88b `888""8P  888 .8P'   
 888       8   888   888   `88..]88..8'   888   888  888      888888.    
 `88.    .8'   888   888    `888'`888'    888   888  888      888 `88b.  
   `YbodP'     888bod8P'     `8'  `8'     `Y8bod8P' d888b    o888o o888o 
               888                                                       
              o888o                                                      
                                                            ~ Notifier                             
"""
print(logo, end="\n\n")

if not os.path.exists("config.json"):
    print("Config File Not Found, Please read README.MD")
    exit()

# قراءة القيم من Environment Variables بدلاً من input()
hours = int(os.environ.get("INTERVAL_HOURS", 1))
minutes = int(os.environ.get("INTERVAL_MINUTES", 0))
seconds = int(os.environ.get("INTERVAL_SECONDS", 0))

print(f"Running every {hours}h:{minutes}m:{seconds}s")

# initialize the scheduler
scheduler = BlockingScheduler(timezone="Asia/Kolkata")

# add the job to the scheduler
scheduler.add_job(
    cron_process, "interval", hours=hours, minutes=minutes, seconds=seconds
)

# start the scheduler
scheduler.start()
