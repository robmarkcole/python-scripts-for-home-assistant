FILE = "/config/www/apple.jpg"

hass.services.call(
    'telegram_bot', 'send_photo', {
        "caption": "{}".format(FILE),
        "file": FILE}
    )
