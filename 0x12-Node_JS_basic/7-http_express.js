const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      let num = 0;
      let response = '';
      for (const [key, value] of Object.entries(data)) {
        num += value.length;
        response += `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}\n`;
      }
      response = `This is the list of our students\nNumber of students: ${num}\n${response.slice(0, -1)}`;
      res.send(response);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});
app.listen(1245);
module.exports = app;
