import logging.config

import yaml


def setup_logging(config_yaml: str):
    """
    Set up logging configuration from a YAML file.

    This function reads the logging configuration from 'logging_config.yaml`.

    :raises yaml.YAMLError: If there is an error in parsing the YAML file.
    """
    try:
        # Load the logging config
        with open(config_yaml, "r") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
