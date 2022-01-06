const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response, path) {
    readDatabase(path).then((data) => {
      response.status = 200;
      let res = '';
      for (const [key, value] of Object.entries(data)) {
        res += `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}\n`;
      }
      res = `This is the list of our students\n${res.slice(0, -1)}`;
      response.send(res);
    }).catch((err) => {
      response.status(500);
      response.send(err.message);
    });
  }

  static getAllStudentsByMajor(request, response, path) {
    readDatabase(path).then((data) => {
      if (request.path === '/CS') {
        response.send(`List: ${data.CS}`);
      } else if (request.path === '/SWE') {
        response.send(`List: ${data.SWE}`);
      } else {
        response.status(500);
        response.send('Major parameter must be CS or SWE');
      }
    }).catch((err) => {
      response.status(500);
      response.send(err.message);
    });
  }
}

module.exports = StudentsController;
