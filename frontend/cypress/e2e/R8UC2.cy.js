// describe('Testing create, toggle and delete on todo items', () => {
//   let uid // user id
//   let name // name of the user (firstName + ' ' + lastName)
//   let email // email of the user

//   let taskTitle // title of the tested task

//   beforeEach(function () {
//     // enter the main main page
//     cy.visit('http://localhost:3000')

//     // detect a div which contains "Email Address", find the input and type (in a declarative way)
//     cy.contains('div', 'Email Address')
//       .find('input[type=text]')
//       .type(email)

//     // submit the form on this page
//     cy.get('form')
//       .submit()
//   })

//   before(function () {
//     // create a fabricated user from a fixture
//     cy.fixture('user.json')
//       .then((user) => {
//         cy.request({
//           method: 'POST',
//           url: 'http://localhost:5000/users/create',
//           form: true,
//           body: user
//         }).then((response) => {
//           uid = response.body._id.$oid
//           name = user.firstName + ' ' + user.lastName
//           email = user.email
//         })
//       })

//     cy.fixture('task.json')
//       .then((task) => {
//         taskTitle = task.title

//         let taskBody = {
//           "title": task.title,
//           "description": task.description,
//           "userid": uid,
//           "url": task.url,
//           "todos": task.todos
//         }

//         cy.request({
//           method: 'POST',
//           url: 'http://localhost:5000/tasks/create',
//           form: true,
//           body: taskBody
//         })
//       })

//     // Create todo for user
//     cy.fixture('todo.json').then((todo) => {
//       let todoBody = {
//         "description": todo.description,
//         "userid": uid,
//       }

//       cy.request({
//         method: 'POST',
//         url: 'http://localhost:5000/todos/create',
//         form: true,
//         body: todoBody
//       }).then((response) => {
//         cy.log(response.body)
//       })
//     })
//   })

//   it('checkTodo', () => {
//     //find and click on the task that we created on the "before"
//     cy.contains('div', taskTitle).click()

//     // // Make sure Add button is disabled when the field is empty
//     // cy.get('input[value="Add"]').should('be.disabled')

//     // // Make sure Add button is enabled when field contains text, 
//     // // then click it to add a new todo item
//     // cy.get('input[placeholder="Add a new todo item"]')
//     // .click().type('Todo item').get('input[value="Add"]')
//     // .should('be.enabled').click()

//     // // Make sure the todo-list contains the new todo item
//     cy.get('.todo-list').should('contain', 'do this')

//     // // Remove the new todo item
//     // cy.get('.remover').click()
//     // // cy.get('li').contains('Todo item').get('.remover').click()
//   })

//   after(function () {
//     // clean up by deleting the user from the database
//     //Also deletes tasks from this user
//     cy.request({
//       method: 'DELETE',
//       url: `http://localhost:5000/users/${uid}`
//     }).then((response) => {
//       cy.log(response.body)
//     })

//   })
// })