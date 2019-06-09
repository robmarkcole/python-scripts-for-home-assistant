"""
Capture a timestamped camera image using the service camera.snapshot.
"""
now = datetime.datetime.now()
time_str = "{}_{}_{}_{}_{}_{}_{}".format(
    now.year, now.month, now.day, now.hour,
    now.minute, now.second, now.microsecond)

folder = '/config/www/front_door_'
filename = folder + time_str + '.jpg'

hass.services.call(
    'camera', 'snapshot',
    {'entity_id': 'camera.front_door_dericam',
     'filename': filename})

## We need to wait for this file to be created before sending to notify
time.sleep(3)

hass.services.call(
    'notify', 'pushbullet_robin', {
        "message": "File saved : " + filename,
        "title": "front door notification",
        "data": {"file": filename}
    })
