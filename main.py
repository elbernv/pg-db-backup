from dotenv import load_dotenv
import json
import datetime
from pytz import timezone
import os
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

config = cloudinary.config(secure=True) 

def uploadBackup():
  backup_name = str(datetime.datetime.now(timezone('America/Santiago'))).replace(' ', '_')[:-13]
  os.system(f'pg_dump -U {os.getenv("DB_USER")} {os.getenv("DB_NAME")} > ~/db-backup-script/backups/{backup_name}')
  cloudinary.uploader.upload(
    f"backups/{backup_name}", 
    public_id=f"partners-copias-de-seguridad/{backup_name}", 
    unique_filename = False, 
    overwrite=True, 
    resource_type="auto"
  )

uploadBackup()

# * * * * * /root/.pyenv/versions/db-backup-script/bin/python /root/db-backup-script/main.py