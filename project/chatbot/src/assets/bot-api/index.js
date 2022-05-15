const fetch = require('node-fetch');
const util = require('util');

class ApiHelper {
  constructor(word, number) {
    this.keyword = word
    this.questionNumber = number
  }

  async responseBack() {
    var query = this.getQuery()
    console.log('query:', query)
    if (query === 404) {
      return undefined
    }
    var query = this.getQuery()
    const host = 'http://localhost:4000/api/v1'
    const url = host + query
    try {
      var res = await fetch(url)
    } catch (error) {
      console.error(error)
    }
    if (!res.ok) {
      throw res
    }
    var responseBody = await res.json()
    return responseBody
  }

  getQuery() {
    switch (this.questionNumber) {
      case 1:
        return util.format('/ad/company=%s&title=%s', this.keyword[0].trim().replace(' ', '%20'), this.keyword[1].trim().replace(' ', '%20'))
        break
      case 2:
        return util.format('/ad/comp=%s', this.keyword.trim().replace(' ', '%20'))
        break
      case 3:
        return util.format('/ad/types=%s&title=%s', this.keyword[0].trim().replace(' ', '%20'), this.keyword[1].trim().replace(' ', '%20'))
        break
      case 4:
        return util.format('/ad/salary=%s&title=%s', this.keyword[0].trim().replace(' ', '%20'), this.keyword[1].trim().replace(' ', '%20'))
      case 404:
        return 404
        break
    }
  }
}
module.exports.ApiHelper = ApiHelper;
