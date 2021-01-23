import boto3
import os
import os.path
import re
import yaml

CONFIG_ACCESS_KEY_ID = os.getenv("CONFIG_ACCESS_KEY_ID")
CONFIG_SECRET_ACCESS_KEY = os.getenv("CONFIG_SECRET_ACCESS_KEY")
CONFIG_REGION = os.getenv("CONFIG_REGION")
ENV = os.getenv("ENV")
MM_DIR = os.getenv("MM_DIR")


def load_from_param_store(name):
    session = boto3.session.Session(
        aws_access_key_id=CONFIG_ACCESS_KEY_ID,
        aws_secret_access_key=CONFIG_SECRET_ACCESS_KEY,
        region_name=CONFIG_REGION
    )
    client = session.client('ssm')
    parameter = client.get_parameter(Name=name)
    value = yaml.safe_load(parameter['Parameter']['Value'])
    return value


def config_path_to_name(configPath):
    """
    for backward compatibility, converts a local yaml file path reference
    to a parameter name that can be used to retrieve an AWS SSM Parameter
    Store value

    assumes that configPath refers to a file in a directory named either
    "configs" or "keys"
    """
    patt = r"(?:(?<=^)|(?<=\/))(?:configs|keys)\/.+(?=\.yml)"
    m = re.search(patt, configPath)
    if m:
        name = m.group().replace("/", "_")
        return name

    return ""


def is_in_path(child, parent):
    """
    returns true if the child path is in the parent path
    """
    relpath = os.path.relpath(child, start=parent)
    return not relpath.startswith("..")


def load_from_local_file(configPath):
    f = open(configPath)
    config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return config


def load_config(configPath="./configs/config.yml", name=None):
    """
    Load configuration information.

    For backward-compatibility reasons, this is a big mess. In its original
    incarnation, this function simply loaded the YAML file at "configPath"

    It has been used for four purposes:
        - load configuration info from files that are checked into a
          source repository

        - load environment-blind configuration info from files that were
          written during host configuration by the Chef configuration
          management system

        - load environment-specific configuration info from files that were
          written by Chef

        - load secrets from files that were written by Chef

    Going forward, configuration info and secrets will be loaded from a
    centralized store rather than local YAML files.

    In order to handle all those options in a backward-compatible manner,
    this function does the following.

    - if "name" is not None, load the parameter of that name from the AWS
      SSM Parameter Store

    - else if configPath is in the path of os.dirname(__file__), load it
      as a YAML file.

    - else if configPath ends in "env.yml", get environment from the "ENV"
      environment variable if possible, otherwise load configPath as a yaml
      file

    - else if the "MM_DIR" environment variable is defined and configPath
      is in the MM_DIR path, convert configPath to a parameter store name
      and load the parameter of that name from the AWS SSM Parameter Store

    - else if CONFIG_KEYS_SECRET_ID environment variable is not set, load
      configPath as a yaml file

    - else convert configPath to a parameter store name and load the
      parameter of that name from the AWS SSM Parameter Store
    """
    if name:
        return load_from_param_store(name)

    if configPath.endswith("env.yml") and ENV:
        return dict(env=ENV)

    if configPath.endswith("env.yml"):
        return load_from_local_file(configPath)

    if MM_DIR and is_in_path(configPath, MM_DIR):
        return load_from_param_store(config_path_to_name(configPath))

    if is_in_path(configPath, os.path.dirname(__file__)):
        return load_from_local_file(configPath)

    if CONFIG_ACCESS_KEY_ID is None:
        return load_from_local_file(configPath)

    return load_from_param_store(config_path_to_name(configPath))
