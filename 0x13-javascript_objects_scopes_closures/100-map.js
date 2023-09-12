#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((el, index) => el * index);
console.log(newList);
