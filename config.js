require('dotenv').config();

const ip = require('underscore').chain(require('os').networkInterfaces()).values().flatten().filter((val) => {
    return (val.family == 'IPv4' && val.internal == false)
}).pluck('address').first().value();

if (typeof ip === 'undefined') console.log('IP not found, use "ifconfig" in SHELL to find local ip of this device.')
else console.log(`IP: ${ip};`)

module.exports.DEVELOPMENT = {
    PORT: 3001,
    URL: `http://localhost`,
};

module.exports.PRODUCTION = {
    PORT: 3001,
    URL: `http://${ip}`,
};