// Require AWS IoT Device SDK
const awsIoT = require('aws-iot-device-sdk');
const sensor = require("node-dht-sensor").promises;
// Load the endpoint from file
const endpointFile = require('/home/pi/environment/endpoint.json');

// Fetch the deviceName from the folder name
const deviceName = "Hydroponic Sensor";

// Create the thingShadow object with argument data
const device = awsIoT.device({
   keyPath: 'private.pem.key',
  certPath: 'certificate.pem.crt',
    caPath: '/home/pi/environment/root-CA.crt',
  clientId: deviceName,
      host: endpointFile.endpointAddress
});


function convertUTCDateToLocalDate(date) {
  var newDate = new Date(date);
  newDate.setMinutes(date.getMinutes() - date.getTimezoneOffset());
  return newDate;
}

async function getSensorData() {
  try {
    const res = await sensor.read(11, 4);
    const dateTime = await convertUTCDateToLocalDate(new Date);
    const message = {
      'sensor_type': 'hydroponic sensor',
      'temperature': `${res.temperature.toFixed(1)}`,
      'humidity': `${res.humidity.toFixed(1)}`,
      'datetime': dateTime.toISOString().replace(/\..+/, '')
    };
    return JSON.stringify(message);
  } catch (err) {
    console.error("Failed to read sensor data:", err);
  }
}

// Function that gets executed when the connection to IoT is established
device.on('connect', function() {
    console.log('Connected to AWS IoT');
    infiniteLoopPublish();
});

// Publish to AWS IoT every 1 minute.
const infiniteLoopPublish = async () => {
  console.log("Sending data to IoT Cloud!");
  const message = await getSensorData();
  console.log(message);
  await new Promise((resolve) => device.publish('hydroponic/sensor', message, resolve))
    .then(result => console.log(result))
    .catch(err => console.log(err));
  setTimeout(infiniteLoopPublish, 60000);
}

