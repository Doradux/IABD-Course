import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import importlib
from decimal import Decimal
from venv import logger
import json
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr