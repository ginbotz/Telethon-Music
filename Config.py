import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16051908"))
    API_HASH = os.environ.get("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5746008573:AAHk9t2qr5qwP_gk41hCDfIRxTIgixyORFI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJYBu2b7eEuusbz5bHFngg5RP95HIz-9xL52-tkxNCaUEodk0eMWjjCw8sk-HSjOkCaz7cNoH2mpryQTn0dJ3yS3kuV2A5huaT40MclSgNlVk2bjcySfdNzjt5NxvrO8KPR9bsSHosZf-ngv1VJTE6W_Ju8IdVRARXeN3PPJVNKmcxNBO9Eqwzbq9cF08zmU_EyGISGxGcWl8rsPjEvWSwNOGOg8iri3euZ5fLKeU4S4NRUdsAsoUjCJoOFelR8hKhExT3KB2uT3Cj7ibR8vX1nK8c1QcP_SfOIQEWcV7iFDhsWU5dcmx3SgfQ698wUouAd3qjNN-Fpj8MCaMCGyKr3vHBE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "starxaarubot")
    SUPPORT = os.environ.get("SUPPORT", "FRIENDS_MASTI_CLUB_FMC") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "SAIKOSTAR_XD") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/ead6fd17a560203a28f0c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/ead6fd17a560203a28f0c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5581544044")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
