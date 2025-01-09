# main.bicep

## Usage

Here is a basic example of how to use this Bicep module:

```bicep
module reference_name 'path_to_module | container_registry_reference' = {
  name: 'deployment_name'
  params: {
    // Required parameters
    environment:
    location:
    location_abbreviation:
    workload:

    // Optional parameters
    rg_tags: {}
  }
}
```

> Note: In the default values, strings enclosed in square brackets (e.g. '[resourceGroup().location]' or '[__bicep.function_name(args...)']) represent function calls or references.

## Modules

| Symbolic Name | Source | Description |
| --- | --- | --- |
| compute | modules/compute/main.bicep |  |

## Resources

| Symbolic Name | Type | Description |
| --- | --- | --- |
| rg | [Microsoft.Resources/resourceGroups](https://learn.microsoft.com/en-us/azure/templates/microsoft.resources/resourcegroups) |  |

## Parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| environment | string | Name of the workloads environment |  |
| location | string | Azure region used for the deployment of all resources |  |
| location_abbreviation | string | Abbreviation fo the location |  |
| rg_tags | object | Tags to be applied on the resource group | {} |
| workload | string | Name of the workload that will be deployed |  |

## Variables

| Name | Description |
| --- | --- |
| rg_name |  |
| suffix |  |
| tags |  |
| webapp_name |  |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| resource_groups | array |  |
| webapp_name | string |  |
