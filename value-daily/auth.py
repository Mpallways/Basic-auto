from growwapi import GrowwAPI
import os
from dotenv import load_dotenv

load_dotenv()


def get_client():

    api_key = os.getenv(
        "GROWW_API_KEY"
    )

    api_secret = os.getenv(
        "GROWW_API_SECRET"
    )

    access_token = GrowwAPI.get_access_token(
        api_key=api_key,
        secret=api_secret
    )

    client = GrowwAPI(
        access_token
    )

    return client