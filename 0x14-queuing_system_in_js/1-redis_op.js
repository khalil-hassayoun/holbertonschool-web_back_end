import redis from 'redis';
const client = redis.createClient();

client.on("error", (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        redis.print(`Reply: ${reply}`);
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
