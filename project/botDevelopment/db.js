const Pool = require('pg').Pool

const pool = new Pool({
  user: 'chatbot',
  host: '3.228.127.116',
  database: 'chatbot',
  password: '1234!@#$',
  port: '5432'
});

module.exports = pool;