# python_scripts/set_state.py
# Create, update, or modify state and attributes in HA
# Source: https://github.com/selfish/home-assistant-resources/blob/master/config/python_scripts/set_state.py
# Adopted from https://github.com/rodpayne/home-assistant/blob/main/.homeassistant/python_scripts/set_state.py

inputEntity = data.get("entity_id")
inputState = data.get("state", "unknown")
allowCreate = data.get("allow_create", False)

if inputEntity is None:
    logger.warning("===== entity_id is required if you want to set something.")
else:
    inputStateObject = hass.states.get(inputEntity)
    if inputStateObject is None and not allowCreate:
        logger.warning("===== unknown entity_id: %s", inputEntity)
    else:
        inputAttributesObject = {}
        if inputStateObject is not None:
            inputAttributesObject = inputStateObject.attributes.copy()

        for item in data:
            if item not in ["entity_id", "allow_create", "state"]:
                inputAttributesObject[item] = data.get(item)

        hass.states.set(inputEntity, inputState, inputAttributesObject)
