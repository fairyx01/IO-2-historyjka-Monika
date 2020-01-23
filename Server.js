var express = require("express");
var app = express();
const port = 3000;
const fs = require('fs');
const lineReader = require('line-reader');

let importsArray = [];

const readFile = (fileName) => {
  lineReader.eachLine(`./${fileName}`, (line) => {
    if(line.includes('function')) {

      let ObjectWithFileData = {};
      line = line.split(' ');

      ObjectWithFileData.sourceFile = fileName;

      ObjectWithFileData[`${line.length > 4 ? 'importedFunction' : 'importedFile'}`] = line.length > 4 ? line[2] : line[1];

      ObjectWithFileData[`${line[line.length - 1].includes('/') ? 'importedFileSoure' : 'iportedPackage'}`] = line[line.length - 1].includes('/') ? line[line.length - 1].split('/')[1].replace(/'|;/g, '') : line[line.length - 1].replace(/'|;/g, '')
      importsArray.push(ObjectWithFileData)
    }
  },
  // () => getResults()
  );
}

const readDir = () => {
  fs.readdir('./', (err, filenames) => {
    filenames.map(file => {
      if (file.includes('.js') && file !== 'server.js') {
        readFile(file);
      }
    })
  });
}

app.get('/', (req, res) => {
    setTimeout(() => {
      
        res.send(importsArray)
      }, 1000);
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

readDir()