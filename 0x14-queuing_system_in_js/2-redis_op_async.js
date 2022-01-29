import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const cGet = promisify(client.get).bind(client);

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
const displaySchoolValue = async (schoolName) => {
    const reply = await cGet(schoolName);
    console.log(reply);
}

(async() => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
