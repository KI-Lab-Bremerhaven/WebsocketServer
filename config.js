require('dotenv').config();

const ip = require('underscore').chain(require('os').networkInterfaces()).values().flatten().filter((val) => {
    return (val.family == 'IPv4' && val.internal == false)
}).pluck('address').first().value();
console.log(ip)

module.exports.DEVELOPMENT = {
    PORT: 3000,
    URL: `http://localhost:3000`,
};

module.exports.PRODUCTION = {
    PORT: 3000,
    URL: `http://${ip}:3000`,
};