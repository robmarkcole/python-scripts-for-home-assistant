"""
Capture a timestamped camera image using the service camera.snapshot.
"""
BLINK_SLEEP_TIME = 7  # seconds to wait for Blink
HA_SLEEP_TIME = 3 # seconds to wait for HA
CAMERA_ENTITY_ID = 'camera.blink_living_room'
CAMERA_NAME = 'Living_room'

now = datetime.datetime.now()
time_str = "{}_{}_{}_{}_{}_{}_{}".format(
    now.year, now.month, now.day, now.hour,
    now.minute, now.second, now.microsecond)

# Trigger a capture now
hass.services.call(
    'blink', 'trigger_camera',
    {'name': CAMERA_NAME})
time.sleep(BLINK_SLEEP_TIME)

# Update representation in HA
hass.services.call(
    'blink', 'blink_update')
time.sleep(HA_SLEEP_TIME)

# Save using snapshot
folder = '/config/www/blink_{}_'.format(CAMERA_NAME)
filename = folder + time_str + '.jpg'

hass.services.call(
    'camera', 'snapshot',
    {'entity_id': CAMERA_ENTITY_ID,
     'filename': filename})

## We need to wait for this file to be created before sending to notify
time.sleep(HA_SLEEP_TIME)

hass.services.call(
    'telegram_bot', 'send_photo', {
        "caption": "New blink capture at {}:{}:{}".format(now.hour,
                                                          now.minute, now.second),
        "file": filename
    })
