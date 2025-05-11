# TokensRevokedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **List[str]** |  | 

## Example

```python
from currency_exchange_fapi_client.models.tokens_revoked_response import TokensRevokedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokensRevokedResponse from a JSON string
tokens_revoked_response_instance = TokensRevokedResponse.from_json(json)
# print the JSON string representation of the object
print(TokensRevokedResponse.to_json())

# convert the object into a dict
tokens_revoked_response_dict = tokens_revoked_response_instance.to_dict()
# create an instance of TokensRevokedResponse from a dict
tokens_revoked_response_from_dict = TokensRevokedResponse.from_dict(tokens_revoked_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


