import logging

import algokit_utils


logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy() -> None:
    from smart_contracts.artifacts.hello_world.hello_world_client import (
        BoxMapSetArgs,
        BoxMapGetArgs,
        BoxMapDeleteArgs,       
        HelloWorldFactory,
    )
    
    algorand = algokit_utils.AlgorandClient.from_environment()
    deployer_ = algorand.account.from_environment("DEPLOYER")

    factory = algorand.client.get_typed_app_factory(
        HelloWorldFactory, default_sender=deployer_.address
    )

    app_client, result = factory.deploy(
        on_update=algokit_utils.OnUpdate.AppendApp,
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
    )

    if result.operation_performed in [
        algokit_utils.OperationPerformed.Create,
        algokit_utils.OperationPerformed.Replace,
    ]:
        algorand.send.payment(
            algokit_utils.PaymentParams(
                amount=algokit_utils.AlgoAmount(algo=1),
                sender=deployer_.address,
                receiver=app_client.app_address,
            )
        )


    # Set the box map with custom struct

    key = 1
    user_struct = {
        "name" : "sanyam",
        "id" : 111,
        "asset" : 111
    }

    # Sets the first index of Box map with user struct
    set_boxmap_response = app_client.send.box_map_set(args=BoxMapSetArgs(
        key=key,
        value=user_struct
    ))

    logger.info(
        f"Box map set response :- {set_boxmap_response.abi_return}"
    )


    # Get box map value at specific index

    get_boxmap_response = app_client.send.box_map_get(args=BoxMapGetArgs(
        key=key
    ))

    logger.info(
        f"Box map get value :- {get_boxmap_response.abi_return}\n"
        f"Name :- {get_boxmap_response.abi_return.name}\n"
        f"Asset :- {get_boxmap_response.abi_return.asset}\n"
        f"ID :- {get_boxmap_response.abi_return.id}\n"
    )


    # Delete box map 

    delete_boxmap_response = app_client.send.box_map_delete(args=BoxMapDeleteArgs(
        key=key
    ))

    logger.info(
        f"Is Box Map key deleted ? :- {delete_boxmap_response.abi_return}"
    )
