# currency_exchange_fapi_client.CurrencyExchangeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_exchange_add_currency**](CurrencyExchangeApi.md#currency_exchange_add_currency) | **POST** /currencies | Add Currency
[**currency_exchange_add_exchange_rate**](CurrencyExchangeApi.md#currency_exchange_add_exchange_rate) | **POST** /exchangerates | Add Exchange Rate
[**currency_exchange_convert_currencies**](CurrencyExchangeApi.md#currency_exchange_convert_currencies) | **GET** /exchange | Convert Currencies
[**currency_exchange_delete_currency**](CurrencyExchangeApi.md#currency_exchange_delete_currency) | **DELETE** /currency/{currency_code} | Delete Currency
[**currency_exchange_delete_exchange_rate**](CurrencyExchangeApi.md#currency_exchange_delete_exchange_rate) | **DELETE** /exchangerate/{code_pair} | Delete Exchange Rate
[**currency_exchange_get_all_currencies**](CurrencyExchangeApi.md#currency_exchange_get_all_currencies) | **GET** /currencies | Get All Currencies
[**currency_exchange_get_all_exchange_rates**](CurrencyExchangeApi.md#currency_exchange_get_all_exchange_rates) | **GET** /exchangerates | Get All Exchange Rates
[**currency_exchange_get_currency**](CurrencyExchangeApi.md#currency_exchange_get_currency) | **GET** /currency/{currency_code} | Get Currency
[**currency_exchange_get_exchange_rate**](CurrencyExchangeApi.md#currency_exchange_get_exchange_rate) | **GET** /exchangerate/{code_pair} | Get Exchange Rate
[**currency_exchange_update_currency**](CurrencyExchangeApi.md#currency_exchange_update_currency) | **PATCH** /currency/{currency_code} | Update Currency
[**currency_exchange_update_exchange_rate**](CurrencyExchangeApi.md#currency_exchange_update_exchange_rate) | **PATCH** /exchangerate/{code_pair} | Update Exchange Rate


# **currency_exchange_add_currency**
> CurrencyOutSchema currency_exchange_add_currency(name, code, sign)

Add Currency

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.currency_out_schema import CurrencyOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    name = 'name_example' # str | 
    code = 'code_example' # str | 
    sign = 'sign_example' # str | 

    try:
        # Add Currency
        api_response = await api_instance.currency_exchange_add_currency(name, code, sign)
        print("The response of CurrencyExchangeApi->currency_exchange_add_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_add_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **code** | **str**|  | 
 **sign** | **str**|  | 

### Return type

[**CurrencyOutSchema**](CurrencyOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Not enough fields provided |  -  |
**409** | Currency with such code already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_add_exchange_rate**
> ExchangeRateOutSchema currency_exchange_add_exchange_rate(base_currency_code, target_currency_code, rate)

Add Exchange Rate

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.exchange_rate_out_schema import ExchangeRateOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    base_currency_code = 'base_currency_code_example' # str | 
    target_currency_code = 'target_currency_code_example' # str | 
    rate = 3.4 # float | 

    try:
        # Add Exchange Rate
        api_response = await api_instance.currency_exchange_add_exchange_rate(base_currency_code, target_currency_code, rate)
        print("The response of CurrencyExchangeApi->currency_exchange_add_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_add_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_currency_code** | **str**|  | 
 **target_currency_code** | **str**|  | 
 **rate** | **float**|  | 

### Return type

[**ExchangeRateOutSchema**](ExchangeRateOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**409** | Exchange rate already exists |  -  |
**404** | Currency(ies) not found |  -  |
**400** | Bad data in request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_convert_currencies**
> ConvertedCurrencySchema currency_exchange_convert_currencies(from_, to, amount)

Convert Currencies

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.converted_currency_schema import ConvertedCurrencySchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    from_ = 'from__example' # str | 
    to = 'to_example' # str | 
    amount = 3.4 # float | 

    try:
        # Convert Currencies
        api_response = await api_instance.currency_exchange_convert_currencies(from_, to, amount)
        print("The response of CurrencyExchangeApi->currency_exchange_convert_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_convert_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_** | **str**|  | 
 **to** | **str**|  | 
 **amount** | **float**|  | 

### Return type

[**ConvertedCurrencySchema**](ConvertedCurrencySchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Exchange rate not found |  -  |
**400** | Bad request data |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_delete_currency**
> object currency_exchange_delete_currency(currency_code)

Delete Currency

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    currency_code = 'currency_code_example' # str | 

    try:
        # Delete Currency
        api_response = await api_instance.currency_exchange_delete_currency(currency_code)
        print("The response of CurrencyExchangeApi->currency_exchange_delete_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_delete_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad request data |  -  |
**404** | Currency not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_delete_exchange_rate**
> object currency_exchange_delete_exchange_rate(code_pair)

Delete Exchange Rate

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    code_pair = 'code_pair_example' # str | 

    try:
        # Delete Exchange Rate
        api_response = await api_instance.currency_exchange_delete_exchange_rate(code_pair)
        print("The response of CurrencyExchangeApi->currency_exchange_delete_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_delete_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_pair** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Currency(ies) not found |  -  |
**400** | Bad request data |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_get_all_currencies**
> List[CurrencyOutSchema] currency_exchange_get_all_currencies()

Get All Currencies

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.currency_out_schema import CurrencyOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)

    try:
        # Get All Currencies
        api_response = await api_instance.currency_exchange_get_all_currencies()
        print("The response of CurrencyExchangeApi->currency_exchange_get_all_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_get_all_currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CurrencyOutSchema]**](CurrencyOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_get_all_exchange_rates**
> List[ExchangeRateOutSchema] currency_exchange_get_all_exchange_rates()

Get All Exchange Rates

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.exchange_rate_out_schema import ExchangeRateOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)

    try:
        # Get All Exchange Rates
        api_response = await api_instance.currency_exchange_get_all_exchange_rates()
        print("The response of CurrencyExchangeApi->currency_exchange_get_all_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_get_all_exchange_rates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ExchangeRateOutSchema]**](ExchangeRateOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_get_currency**
> CurrencyOutSchema currency_exchange_get_currency(currency_code)

Get Currency

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.currency_out_schema import CurrencyOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    currency_code = 'currency_code_example' # str | 

    try:
        # Get Currency
        api_response = await api_instance.currency_exchange_get_currency(currency_code)
        print("The response of CurrencyExchangeApi->currency_exchange_get_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_get_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**|  | 

### Return type

[**CurrencyOutSchema**](CurrencyOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Currency not found |  -  |
**400** | Currency code not provided |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_get_exchange_rate**
> ExchangeRateOutSchema currency_exchange_get_exchange_rate(code_pair)

Get Exchange Rate

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.exchange_rate_out_schema import ExchangeRateOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    code_pair = 'code_pair_example' # str | 

    try:
        # Get Exchange Rate
        api_response = await api_instance.currency_exchange_get_exchange_rate(code_pair)
        print("The response of CurrencyExchangeApi->currency_exchange_get_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_get_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_pair** | **str**|  | 

### Return type

[**ExchangeRateOutSchema**](ExchangeRateOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad data in request |  -  |
**404** | Rate not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_update_currency**
> CurrencyOutSchema currency_exchange_update_currency(currency_code, name, sign)

Update Currency

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.currency_out_schema import CurrencyOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    currency_code = 'currency_code_example' # str | 
    name = 'name_example' # str | 
    sign = 'sign_example' # str | 

    try:
        # Update Currency
        api_response = await api_instance.currency_exchange_update_currency(currency_code, name, sign)
        print("The response of CurrencyExchangeApi->currency_exchange_update_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_update_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**|  | 
 **name** | **str**|  | 
 **sign** | **str**|  | 

### Return type

[**CurrencyOutSchema**](CurrencyOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad request data |  -  |
**404** | Currency not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_exchange_update_exchange_rate**
> ExchangeRateOutSchema currency_exchange_update_exchange_rate(code_pair, rate)

Update Exchange Rate

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.exchange_rate_out_schema import ExchangeRateOutSchema
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.CurrencyExchangeApi(api_client)
    code_pair = 'code_pair_example' # str | 
    rate = 3.4 # float | 

    try:
        # Update Exchange Rate
        api_response = await api_instance.currency_exchange_update_exchange_rate(code_pair, rate)
        print("The response of CurrencyExchangeApi->currency_exchange_update_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeApi->currency_exchange_update_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_pair** | **str**|  | 
 **rate** | **float**|  | 

### Return type

[**ExchangeRateOutSchema**](ExchangeRateOutSchema.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Currency(ies) not found |  -  |
**400** | Bad data in request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

