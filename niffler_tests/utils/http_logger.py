import json
import logging
import allure
import curlify
from allure_commons.types import AttachmentType


def log(response):
    curl = curlify.to_curl(response.request)
    logging.basicConfig(level=logging.INFO)
    logging.info(curl)  # I don't get why it doesn't work
    print(curl)
    allure.attach(
        body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt"
    )
    allure.attach(
        body=response.request.method + " " + response.request.url,
        name="Request",
        attachment_type=AttachmentType.TEXT,
        extension="txt",
    )
    if response.text:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
