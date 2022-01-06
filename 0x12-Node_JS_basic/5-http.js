const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((data) => {
        let num = 0;
        let response = '';
        for (const [key, value] of Object.entries(data)) {
          num += value.length;
          response += `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}\n`;
        }
        response = `This is the list of our students\nNumber of students: ${num}\n${response.slice(0, -1)}`;
        res.end(response);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
  // res.end(`This is the list of our students ${dict}`);
  }
});
app.listen(1245);
module.exports = app;
