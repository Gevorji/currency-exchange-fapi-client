# CurrencyOutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**code** | **str** |  | 
**sign** | **str** |  | 

## Example

```python
from currency_exchange_fapi_client.models.currency_out_schema import CurrencyOutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyOutSchema from a JSON string
currency_out_schema_instance = CurrencyOutSchema.from_json(json)
# print the JSON string representation of the object
print(CurrencyOutSchema.to_json())

# convert the object into a dict
currency_out_schema_dict = currency_out_schema_instance.to_dict()
# create an instance of CurrencyOutSchema from a dict
currency_out_schema_from_dict = CurrencyOutSchema.from_dict(currency_out_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


