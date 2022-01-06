console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (d) => {
  if (d.toString().trim() !== '') {
    process.stdout.write(`Your name is: ${d.toString()}`);
  } else {
    process.exit();
  }
});
process.stdin.on('end', () => {
  console.log('This important software is now closing');
  process.exit();
});
