# UserCreationErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** |  | 

## Example

```python
from currency_exchange_fapi_client.models.user_creation_error_response import UserCreationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreationErrorResponse from a JSON string
user_creation_error_response_instance = UserCreationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(UserCreationErrorResponse.to_json())

# convert the object into a dict
user_creation_error_response_dict = user_creation_error_response_instance.to_dict()
# create an instance of UserCreationErrorResponse from a dict
user_creation_error_response_from_dict = UserCreationErrorResponse.from_dict(user_creation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


