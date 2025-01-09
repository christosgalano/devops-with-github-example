# modules/compute/main.bicep

## Usage

Here is a basic example of how to use this Bicep module:

```bicep
module reference_name 'path_to_module | container_registry_reference' = {
  name: 'deployment_name'
  params: {
    // Required parameters
    location:
    plan_kind:
    plan_name:
    plan_reserved:
    plan_sku_capacity:
    plan_sku_name:
    plan_sku_tier:
    webapp_always_on:
    webapp_health_check_path:
    webapp_linux_fx_version:
    webapp_min_tls_version:
    webapp_name:

    // Optional parameters
  }
}
```

> Note: In the default values, strings enclosed in square brackets (e.g. '[resourceGroup().location]' or '[__bicep.function_name(args...)']) represent function calls or references.

## Resources

| Symbolic Name | Type | Description |
| --- | --- | --- |
| app_svc_plan | [Microsoft.Web/serverfarms](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/serverfarms) |  |
| webapp | [Microsoft.Web/sites](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites) |  |

## Parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| location | string | Location of all resources |  |
| plan_kind | string | Kind of the App Service Plan |  |
| plan_name | string | Name of the App Service Plan |  |
| plan_reserved | bool | Specifies whether the App Service Plan will be Linux (true) or Windows (false) |  |
| plan_sku_capacity | int | SKU capacity of the App Service Plan |  |
| plan_sku_name | string | SKU name of the App Service Plan |  |
| plan_sku_tier | string | SKU tier of the App Service Plan |  |
| webapp_always_on | bool | Specifies whether always on is enabled |  |
| webapp_health_check_path | string | Specifies the health check path |  |
| webapp_linux_fx_version | string | Linux App Framework and version |  |
| webapp_min_tls_version | string | Specifies the minimum TLS version |  |
| webapp_name | string | Name of the Webapp |  |
