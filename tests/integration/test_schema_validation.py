import logging

import pytest
from pydantic import BaseModel, Extra

from genai import Credentials
from genai.schemas.generate_params import GenerateParams
from genai.services import RequestHandler

logger = logging.getLogger(__name__)


@pytest.mark.integration
class TestBAMAPICompatibility:
    @staticmethod
    def _get_schema(credentials: Credentials):
        logger.info("Starting up API Compatibility Tests")
        schema_url = f"{credentials.api_endpoint}/models/full"
        logger.info(f"Downloading Schema from {schema_url}")
        schema_doc = RequestHandler.get(schema_url, key=credentials.api_key)
        assert schema_doc.status_code == 200
        return schema_doc.json()["results"]

    @staticmethod
    def _check_param_key(
        parameter: str,
        key: str,
        schema_param: dict,
        model_param: dict,
        severe: bool = False,
    ):
        if key in schema_param and key in model_param:
            sp_val = schema_param[key]
            mp_val = model_param[key]
            if sp_val != model_param[key]:
                logger.warning(f"Inconsistent {key} for [{parameter}]: API: {sp_val} / genai: {mp_val}")
            if severe is True:
                assert sp_val == mp_val, f"Field {key} in {parameter} should be consistent."

    @staticmethod
    def _check_param(parameter: str, schema_param: dict, model_param: dict):
        keys = [
            ("title", False),
            ("description", False),
            ("type", True),
            ("minimum", False),
            ("maximum", False),
            ("nullable", False),
        ]
        for key, severe in keys:
            TestBAMAPICompatibility._check_param_key(parameter, key, schema_param, model_param, severe=severe)

    @staticmethod
    def _check_schema_compatibility(schema_doc: dict, model_type: BaseModel):
        logger.info(f"Processing schema {schema_doc['id']} with model: [{model_type.__name__}]")
        schema_v = schema_doc["value"]
        prop_keys = list(schema_v["properties"].keys())
        logger.info(f"Available fields: {prop_keys}, Required: {schema_v['required']}")
        parameters = schema_v["properties"]["parameters"]["properties"]

        model_param_schema = model_type.schema(by_alias=True)["properties"]
        model_param_keys = model_param_schema.keys()

        for param in parameters.keys():
            if isinstance(parameters[param], dict):
                if "deprecated" not in parameters[param] or parameters[param]["deprecated"] is False:
                    if param not in model_param_keys:
                        # Check that we have the param registered
                        assert param in model_param_keys, f"Parameter {param} should be in {model_type.__name__}"
                    else:
                        # Check the param is defined correctly
                        schema_doc_param = parameters[param]
                        model_param = model_param_schema[param]
                        TestBAMAPICompatibility._check_param(param, schema_doc_param, model_param)
                else:
                    logger.info(f"Not checking deprecated parameter: {param}")
            elif param == "additionalProperties":
                logger.info(f"Checking additionalProperties ({parameters[param]})")
                if "extra" in dir(model_type.Config):
                    logger.info(f"Found extra on model: {model_type.Config.extra}")
                    if parameters[param] is False:
                        assert model_type.Config.extra in [
                            Extra.forbid,
                            Extra.ignore,
                        ], "Extra parameter must not be allowed"
                    else:
                        assert model_type.Config.extra is Extra.allow, "Extra parameters must be allowed"

    def test_generate_params(self, credentials: Credentials):
        logger.info("Testing generate params compatibility")
        schema_doc = self._get_schema(credentials)
        generate_schema = schema_doc["schemas_generate"]
        for schema in generate_schema:
            self._check_schema_compatibility(schema, GenerateParams)
