import datetime
import json
import os
import pytz
import socket
import sys


def up(event, context):
  tzInfo = pytz.timezone('America/Los_Angeles')
  mac_address = os.environ['MAC_ADDRESS']
  public_ip = os.environ['PUBLIC_IP']
  now = datetime.datetime.now(tz=tzInfo).strftime("%Y/%m/%d %I:%M:%S %p")
  
  body = {
    "message": f'Waking computer with mac_address - {mac_address}, public_ip - {public_ip} @ {now}!',
  }

  data = ''.join(['FF' * 6, mac_address.replace(':', '') * 16])
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  sock.sendto(bytes.fromhex(data), (public_ip, 9))

  return {
      "statusCode": 200,
      "body": json.dumps(body)
  }
