"""
Capture a timestamped camera image using the service camera.snapshot.
"""
now = datetime.datetime.now()
time_str = "{}_{}_{}_{}_{}_{}_{}".format(
    now.year, now.month, now.day, now.hour,
    now.minute, now.second, now.microsecond)

# Trigger a capture now
hass.services.call(
    'blink', 'trigger_camera',
    {'name': 'Kitchen'})
time.sleep(3)

# Update representation in HA
hass.services.call(
    'blink', 'blink_update')

# Save using snapshot
folder = '/config/www/blink_kitchen_'
filename = folder + time_str + '.jpg'

hass.services.call(
    'camera', 'snapshot',
    {'entity_id': 'camera.blink_kitchen',
     'filename': filename})

## We need to wait for this file to be created before sending to notify
time.sleep(3)

hass.services.call(
    'notify', 'pushbullet_robin', {
        "message": "File saved : " + filename,
        "title": "blink_kitchen notification",
        "data": {"file": filename}
    })
