"""
python_scripts/set_state.py

Set the state or other attributes for a specified entity.
Enhancements include error handling, data validation, and user feedback.
Source:
https://github.com/selfish/home-assistant-resources/blob/master/config/python_scripts/set_state.py

Adopted based on
https://github.com/rodpayne/home-assistant/blob/main/.homeassistant/python_scripts/set_state.py
"""

inputEntity = data.get("entity_id")
if inputEntity is None:
    logger.error("entity_id is required to set the state.")
else:
    try:
        inputStateObject = hass.states.get(inputEntity)
        inputState = inputStateObject.state if inputStateObject else None
        inputAttributesObject = inputStateObject.attributes.copy() if inputStateObject else {}

        for item, newAttribute in data.items():
            if item in ["entity_id", "allow_create"]:
                continue  # Skip already handled items
            if item == "state":
                inputState = newAttribute
            else:
                inputAttributesObject[item] = newAttribute

        hass.states.set(inputEntity, inputState, inputAttributesObject)
        logger.info(f"Updated state of '{inputEntity}' to '{inputState}' with attributes {inputAttributesObject}.")

    except Exception as e:
        logger.error(f"Error updating state of '{inputEntity}': {e}")