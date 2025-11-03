import json
import logging
import allure
import curlify
from allure_commons.types import AttachmentType



def log(response):
    curl = curlify.to_curl(response.request)
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    logger.info(curl)
    allure.attach(
        body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt"
    )
    allure.attach(
        body=f'{response.status_code}', name="status_code", attachment_type=AttachmentType.TEXT, extension="txt"
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
