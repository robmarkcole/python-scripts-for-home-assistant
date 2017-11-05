"""
Capture a timestamped camera image using the service camera.snapshot.
"""
now = datetime.datetime.now()
time = "{}_{}_{}_{}_{}_{}_{}".format(
    now.year, now.month, now.day, now.hour,
    now.minute, now.second, now.microsecond)

folder = '/home/pi/.homeassistant/camera_captures/'
filename = folder + time + '.jpg'

hass.services.call(
    'camera', 'snapshot',
    {'entity_id': 'camera.raspberry_pi_camera',
     'filename': filename})
