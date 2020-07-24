import json
import logging
from typing import Any, MutableMapping, Optional
from random import choice
from string import ascii_lowercase

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
)

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Miltons::Red::Stapler"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    ssm_client = session.client('ssm')
    model.TPSCode = ''.join([choice(ascii_lowercase) for _ in range(8)])
    ssm_client.put_parameter(Name=model.TPSCode, Value=json.dumps([model.__dict__]), Type='String')
    progress.status = OperationStatus.SUCCESS
    return progress


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    ssm_client = session.client('ssm')
    ssm_client.delete_parameter(Name=model.TPSCode)
    progress.status = OperationStatus.SUCCESS
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    ssm_client = session.client('ssm')
    response = ssm_client.get_parameter(Name=model.TPSCode)
    model.PrintableMemo = f"This is an IniTech Memo coversheet, compliant with v1.9 standards and A4 printable on " \
                          f"HPLaserJet printers. JSON encoded memo follows. \n\n" \
                          f"--------------------------------------------------------------------------------------" \
                          f"{response['Value']}"
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )
