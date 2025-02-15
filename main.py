# pip install azure-iot-device
from azure.iot.device import ProvisioningDeviceClient

# Your device credentials
id_scope = ""
device_id = ""
primary_key = ""

# Create DPS client to register device
provisioning_client = ProvisioningDeviceClient.create_from_symmetric_key(
    provisioning_host="global.azure-devices-provisioning.net",
    registration_id=device_id,
    id_scope=id_scope,
    symmetric_key=primary_key
)

# Register and get assigned IoT Hub
registration_result = provisioning_client.register()

# Extract IoT Hub hostname
iot_hub_hostname = registration_result.registration_state.assigned_hub
print(f"Device registered to: {iot_hub_hostname}")

# Generate connection string in required format
connection_string = f"HostName={iot_hub_hostname};DeviceId={device_id};SharedAccessKey={primary_key}"
print(f"Connection String: {connection_string}")
