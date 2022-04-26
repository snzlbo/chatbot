const fetch = require('node-fetch');
const util = require('util');

class ApiHelper {
  constructor(word, number) {
    this.keyword = word
    this.questionNumber = number
  }

  async responseBack() {
    var query = this.getQuery()
    const host = 'http://localhost:4000/api/v1'
    const url = host + query
    var res = await fetch(url)
    if (!res.ok) {
      throw res
    }
    var responseBody = await res.json()
    console.log(responseBody)
    return responseBody
  }

  getQuery() {
    if (this.questionNumber == 1) {
      return util.format('/ad/company=%s&title=%s', this.keyword[0].trim().replace(' ', '%20'), this.keyword[1].trim().replace(' ', '%20'))
    }
  }
}
module.exports.ApiHelper = ApiHelper;
