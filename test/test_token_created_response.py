# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from currency_exchange_fapi_client.models.token_created_response import TokenCreatedResponse

class TestTokenCreatedResponse(unittest.TestCase):
    """TokenCreatedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenCreatedResponse:
        """Test TokenCreatedResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenCreatedResponse`
        """
        model = TokenCreatedResponse()
        if include_optional:
            return TokenCreatedResponse(
                access_token = '',
                token_type = '',
                expires_in = None,
                refresh_token = '',
                scope = [
                    ''
                    ]
            )
        else:
            return TokenCreatedResponse(
                access_token = '',
                token_type = '',
                expires_in = None,
        )
        """

    def testTokenCreatedResponse(self):
        """Test TokenCreatedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
