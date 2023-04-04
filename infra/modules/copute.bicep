/// Parameters ///

@description('Location of all resources')
param location string

@description('Name of the App Service Plan')
param plan_name string

@description('SKU name of the App Service Plan')
param plan_sku_name string

@description('SKU tier of the App Service Plan')
param plan_sku_tier string

@description('Kind of the App Service Plan')
param plan_kind string

@description('Specifies whether the App Service Plan will be Linux (true) or Windows (false)')
param plan_reserved bool

@description('Name of the Webapp')
param webapp_name string

@description('Linux App Framework and version')
param webapp_linux_fx_version string

@description('Specifies whether always on is enabled')
param webapp_always_on bool

/// Resources ///

resource app_svc_plan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: plan_name
  location: location
  kind: plan_kind
  sku: {
    tier: plan_sku_tier
    name: plan_sku_name
  }
  properties: {
    reserved: plan_reserved
  }
}

resource webapp 'Microsoft.Web/sites@2022-03-01' = {
  name: webapp_name
  location: location
  properties: {
    siteConfig: {
      linuxFxVersion: webapp_linux_fx_version
      alwaysOn: webapp_always_on
    }
    httpsOnly: true
    serverFarmId: app_svc_plan.id
    publicNetworkAccess: 'Enabled'
  }
}
