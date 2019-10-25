const parse = require('csv-parse/lib/sync');
const assert = require('assert');

const fs = require('fs');



const read = () => {
    const txt = fs.readFile('./train.csv');
    return parse(txt, {
        skip_empty_lines: true
    });
};

const main = () => {
    const read = read();

    console.log(read);
}

main();