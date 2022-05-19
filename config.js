require('dotenv').config();

const ip = require('underscore').chain(require('os').networkInterfaces()).values().flatten().filter((val) => {
    return (val.family == 'IPv4' && val.internal == false)
}).pluck('address').first().value();
console.log(ip)

module.exports.DEVELOPMENT = {
    PORT: 3001,
    URL: `http://localhost`,
};

module.exports.PRODUCTION = {
    PORT: 3001,
    URL: `http://${ip}`,
};