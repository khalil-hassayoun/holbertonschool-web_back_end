const app = require('../server');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

app.get('/', (req, res) => {
  AppController.getHomepage(req, res);
});
app.get('/students', (req, res) => {
  StudentsController.getAllStudents(req, res, process.argv[2]);
});

app.get('/students/:major', (req, res) => {
  StudentsController.getAllStudentsByMajor(req, res, process.argv[2]);
});
