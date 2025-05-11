# ConvertedCurrencySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | [**CurrencyOutSchema**](CurrencyOutSchema.md) |  | 
**target_currency** | [**CurrencyOutSchema**](CurrencyOutSchema.md) |  | 
**rate** | **float** |  | 
**amount** | **float** |  | 
**converted_amount** | **float** |  | 

## Example

```python
from currency_exchange_fapi_client.models.converted_currency_schema import ConvertedCurrencySchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertedCurrencySchema from a JSON string
converted_currency_schema_instance = ConvertedCurrencySchema.from_json(json)
# print the JSON string representation of the object
print(ConvertedCurrencySchema.to_json())

# convert the object into a dict
converted_currency_schema_dict = converted_currency_schema_instance.to_dict()
# create an instance of ConvertedCurrencySchema from a dict
converted_currency_schema_from_dict = ConvertedCurrencySchema.from_dict(converted_currency_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


