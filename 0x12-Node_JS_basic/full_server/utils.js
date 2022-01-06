const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, datatext) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const datatxt = datatext.split(/\r?\n/);
        const data = [];
        for (const i of datatxt) {
          if (i !== '') {
            data.push(i.split(','));
          }
        }
        const idxFN = data[0].indexOf('firstname');
        const idxFD = data[0].indexOf('field');
        const dict = {};
        for (const line of data) {
          if (data.indexOf(line) !== 0) {
            if (line[idxFD] in dict) {
              dict[line[idxFD]].push(line[idxFN]);
            } else {
              dict[line[idxFD]] = [];
              dict[line[idxFD]].push(line[idxFN]);
            }
          }
        }
        resolve(dict);
      }
    });
  });
}
module.exports = readDatabase;
