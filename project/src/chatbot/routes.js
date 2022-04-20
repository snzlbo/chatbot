const { Router } = require('express')
const controller = require('./controller')

const router = Router()

router.get('/', controller.getCategories)
router.post('/', controller.addCategory)
router.get('/:id', controller.getCategoryById)

module.exports = router 