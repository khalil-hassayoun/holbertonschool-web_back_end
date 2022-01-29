import redis from 'redis';
const client = redis.createClient();

client.on("error", (error) => {
    if (error) console.log(`Redis client not connected to the server: ${error}`)
  }).on('ready', () => {
      console.log('Redis client connected to the server');
  });

client.subscribe("holberton school channel");

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    process.exit(0);
  }
});
